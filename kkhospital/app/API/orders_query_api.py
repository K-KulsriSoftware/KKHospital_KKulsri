#!/usr/bin/python
# -*- coding: utf-8 -*-
from pprint import pprint
from datetime import datetime
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


	def get_order_detail(self,order_id) :
		cursor = self.db.orders.aggregate([
			{
            	'$match' :
            		{
            			'_id' : order_id
            		}
        	}
		])
		for order in cursor :
			return True, order
		return False, "No match order"


	def get_all_orders_name(self) :
		cursor = self.db.orders.aggregate([
            {
                '$match' : {}
            },
            {
                '$project' : {
                    'order_id' : '$_id'
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


	def update_order(self, order_id, package_id, doctor_id, patient_id, cost, time, bought_time, notice) :
		self.db.orders.update_one(
    		{
        		'_id': order_id
    		},
    		{
        		'$set':
        		{
            			'package_id' : package_id,
            			'doctor_id' : doctor_id,
            			'patient_id' : patient_id,
            			'cost' : cost ,
            			'time' :
            			{
            				'start':datetime(time['year'],time['month'],time['date'],time['start_hr'],0),
            				'finish':datetime(time['year'],time['month'],time['date'],time['finish_hr'],0)
            			},
            			'notice' : notice

        		}
    		}
		)
		return True, 'Successfully Updated'


	def delete_order(self, order_id) :
		self.db.orders.delete_one(
            {
                "_id": order_id
            }
        )
		return True, 'Successfully Removed'


	def insert_order(self, package_id, doctor_id, patient_id, cost, time, bought_time, notice) :
		self.db.orders.insert(
			{
                'package_id' : package_id,
                'doctor_id' : doctor_id,
                'patient_id' : patient_id,
                'cost' : cost ,
                'time' :
                {
                    'start':datetime(time['year'],time['month'],time['date'],time['start_hr'],0),
                    'finish':datetime(time['year'],time['month'],time['date'],time['finish_hr'],0)
                },
                'notice' : notice
			}
	    )
		return True,'Successfully Added'