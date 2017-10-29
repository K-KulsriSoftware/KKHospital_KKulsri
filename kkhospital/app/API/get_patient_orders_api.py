#!/usr/bin/python
# -*- coding: utf-8 -*-

class get_patient_orders_api :

    def __init__(self, db) :
        self.db = db

    def get_patient_orders_query(self, patient_username) :
    	return self.db.orders.aggregate([
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
            	'$match' :
            	{
            		'patient.username' : patient_username
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
            		'patient_id' : '$patient_id',
            		'patient_username' : '$patient.username',
            		'doctor_id' : '$doctor_id',
            		'doctor_username' : '$doctor.username',
            		'doctor_name_title' : '$doctor.doctor_name_title',
            		'doctor_name' : '$doctor.doctor_name',
            		'doctor_surname' : '$doctor.doctor_surname',
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

    def get_patient_orders(self, patient_username) :
    	cursor = self.get_patient_orders_query(patient_username)
    	orders = []
    	for order in cursor :
    		order.pop('_id', None)
    		orders.append(order)
    	return True, orders