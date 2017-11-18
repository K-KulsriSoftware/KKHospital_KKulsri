#!/usr/bin/python
# -*- coding: utf-8 -*-

class get_doctor_orders_api :

    def __init__(self, db) :
        self.db = db

    def get_doctor_orders_query(self, doctor_username) :
    	return self.db.orders.aggregate([
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
            	'$match' :
            	{
            		'doctor.username' : doctor_username
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
                    'doctor_id' : '$doctor_id',
                    'doctor_username' : '$doctor.username',
            		'patient_id' : '$patient_id',
            		'patient_username' : '$patient.username',
            		'patient_name_titile' : '$patient.patient_name_title',
            		'patient_name' : '$patient.patient_name',
            		'patient_surname' : '$patient.patient_surname',
            		'package_id' : '$package_id',
            		'package_name' : '$package.package_name',
            		'department_id' : '$department._id',
            		'department_name' : '$department.department_name',
            		'building_id' : '$building_id',
            		'building_name' : '$building_name',
            		'cost' : '$cost',
            		'start_time' : '$time.start',
            		'finish_time' : '$time.finish',
            		'bought_time' : '$bought_time',
            		'notice' : '$notice'
            	}
            }
        ])

    def get_doctor_orders(self, doctor_username) :
    	cursor = self.get_doctor_orders_query(doctor_username)
    	orders = []
    	for order in cursor :
    		order.pop('_id', None)
    		orders.append(order)
    	return True, orders