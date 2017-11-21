#!/usr/bin/python
# -*- coding: utf-8 -*-
from pprint import pprint
from datetime import datetime, timedelta
from bson.objectid import ObjectId
class orders_query_api :

    def __init__(self, db) :
        self.db = db

    def get_all_orders(self) :
        cursor = self.db.orders.aggregate([
            {
                '$match' : {}
            }
        ])
        orders = []
        for order in cursor :
            orders.append(order)
        return True, orders

    def separate_time_hour(self, time) :
        day = str(time.date())
        hour = int(time.strftime('%H'))
        return {'day':day, 'hour':hour}

    def separate_time_hour_minute(self, time) :
        day = str(time.date())
        hour = int(time.strftime('%H'))
        minute = int(time.strftime('%M'))
        return {'day':day, 'hour':hour, 'minute':minute}

    def get_order_detail(self,order_id) :
        cursor = self.db.orders.aggregate([
            {
                '$match' :
                {
                    '_id' : ObjectId(order_id)
                }
            }
        ])
        for order in cursor :
            order['start_time'] = self.separate_time_hour(order['time']['start'])
            order['finish_time'] = self.separate_time_hour(order['time']['finish'])
            order['bought_time'] = self.separate_time_hour_minute(order['bought_time'])
            return True, order
        return False, "No match order"

    def get_all_orders_name(self) :
        cursor = self.db.orders.aggregate([
            {
                '$match' : {}
            },
            {
                '$project' : 
                {
                    '_id' : 1,
                    'package_id' : 1,
                    'doctor_id' : 1,
                    'patient_id' : 1
                }
            }
        ])
        orders = []
        for order in cursor :
            orders.append(order)
        return True, orders

    def get_all_orders_with_package_and_user(self) :
        cursor = self.db.orders.aggregate([
            {
                '$match' : {}
            },
            {
                '$project' : {
                    'order_id' : '$_id',
                    'package_id' : '$package_id',
                    'patient_id' : '$patient_id'
                }
            }
        ])
        orders = []
        for order in cursor :
            order.pop('_id', None)
            orders.append(order)
        return True, orders

    def get_time_from_hour(self, time) :
        time_list = time['day'].split('-')
        return datetime(int(time_list[0]),int(time_list[1]),int(time_list[2]),int(time['hour']),0)

    def get_time_from_hour_minute(self, time) :
        time_list = time['day'].split('-')
        return datetime(int(time_list[0]),int(time_list[1]),int(time_list[2]),int(time['hour']),int(time['minute']))

    def update_order(self, order_id, package_id, doctor_id, patient_id, cost, start_time, finish_time, bought_time, notice, note) :
        print(locals())
        self.db.orders.update_one(
    		{
        		'_id': ObjectId(order_id)
    		},
    		{
        		'$set':
        		{
            			'package_id' : ObjectId(package_id),
            			'doctor_id' : ObjectId(doctor_id),
            			'patient_id' : ObjectId(patient_id),
            			'cost' : float(cost) ,
            			'time' :
            			{
                            'start' : self.get_time_from_hour(start_time),
                            'finish' : self.get_time_from_hour(finish_time)
            			},
                        'bought_time' : self.get_time_from_hour_minute(bought_time),
            			'notice' : notice,
                        'note' : note
        		}
    		}
		)
        return True, 'Successfully Updated'

    def delete_order(self, order_id) :
        self.db.orders.delete_one(
            {
                "_id": ObjectId(order_id)
            }
        )
        return True, 'Successfully Removed'

    def insert_order(self, package_id, doctor_id, patient_id, cost, time, bought_time, notice, note) :
        self.db.orders.insert_one(
            {
                'package_id' : ObjectId(package_id),
                'doctor_id' : ObjectId(doctor_id),
                'patient_id' : ObjectId(patient_id),
                'cost' : float(cost) ,
                'time' :
                {
                    'start' : datetime(time['year'],time['month'],time['date'],time['start_hr'],0),
                    'finish' : datetime(time['year'],time['month'],time['date'],time['finish_hr'],0)
                },
                'bought_time' : bought_time,
                'notice' : notice,
                'note' : note
			}
        )
        return True,'Successfully Added'

    def get_doctor_orders(self, doctor_id) :
        now_time = datetime.now()
        year = int(now_time.strftime('%Y'))
        month = int(now_time.strftime('%m'))
        date = int(now_time.strftime('%d'))
        today_morning = datetime(year, month, date, 0, 0)
        cursor = self.db.orders.aggregate([
            {
                '$match' : 
                {
                    'doctor_id' : ObjectId(doctor_id),
                    'time.start' :  
                    {
                        '$gte' : today_morning
                    }
                }
            },
             {
                '$lookup' :
                {
                    'from' : 'doctors',
                    'localField' : 'doctor_id',
                    'foreignField' : '_id',
                    'as' : 'doctor'
                }
            },
            {
                '$lookup' :
                {
                    'from' : 'patients',
                    'localField' : 'patient_id',
                    'foreignField' : '_id',
                    'as' : 'patient'
                }
            },
            {
                '$lookup' :
                {
                    'from' : 'packages',
                    'localField' : 'package_id',
                    'foreignField' : '_id',
                    'as' : 'package'
                }
            },
            {
                '$unwind' : '$patient'
            },
            {
                '$unwind' : '$doctor'
            },
            {
                '$unwind' : '$package'
            },
            {
                '$lookup' :
                {
                    'from' : 'departments',
                    'localField' : 'package.department_id',
                    'foreignField' : '_id',
                    'as' : 'department'
                }
            },
            {
                '$unwind' : '$department'
            },
            {
                '$lookup' :
                {
                    'from' : 'buildings',
                    'localField' : 'package.building_id',
                    'foreignField' : '_id',
                    'as' : 'building'
                }
            },
            {
                '$unwind' : '$building'
            },
            {
                '$project' :
                {
                    'order_id' : '$_id',
                    'doctor_id' : 1,
                    'doctor_username' : '$doctor.username',
                    'patient_id' : 1,
                    'patient_username' : '$patient.username',
                    'patient_name_titile' : '$patient.patient_name_title',
                    'patient_name' : '$patient.patient_name',
                    'patient_surname' : '$patient.patient_surname',
                    'package_id' : 1,
                    'package_name' : '$package.package_name',
                    'department_id' : '$department._id',
                    'department_name' : '$department.department_name',
                    'building_id' : 1,
                    'building_name' : 1,
                    'cost' : 1,
                    'start_time' : '$time.start',
                    'finish_time' : '$time.finish',
                    'bought_time' : 1,
                    'notice' : 1,
                    'note' : 1
                }
            }
        ])
        orders = []
        for order in cursor :
            order.pop('_id', None)
            orders.append(order)
        return True, orders

    def insert_note(self, order_id, note) :
        self.db.orders.update_one(
            {
                '_id' : ObjectId(order_id)
            },
            {
                '$set' :
                {
                    'note' : note
                }
            }
        )
        return True, 'Successfully Updated'