#!/usr/bin/python
# -*- coding: utf-8 -*-
from bson.objectid import ObjectId
from datetime import datetime

class show_doctor_detail_api :

	def __init__(self, db) :
		self.db = db

	def get_doctor_query(self, doctor_id) :
		return self.db.doctors.aggregate([
    		{
        		'$match' :
        		{
            		'_id' : ObjectId(doctor_id)
        		}
    		},
    		{
        		'$project':
        		{
        			'doctor_id' : '$_id',
					'username' : '$username',
					'doctor_name_title' : '$doctor_name_title',
            		'doctor_name' : '$doctor_name',
            		'doctor_surname' : '$doctor_surname',
            		'doctor_img' : '$doctor_img',
					'doctor_img' : '$doctor_img',
					'position' : '$position',
					'expertises' : '$expertises',
					'educations' : '$educations',
					'language' : '$language',
					'working_time' : '$working_time',
        		}
     		}
		])

	def unavailable(self, doctor_id) :
		now = datetime.now()
		cursor = self.db.orders.aggregate([
    		{
        		'$match' :
        		{
            		'time.finish' : 
            		{
            			'$gt' : now
            		},
            		'doctor_id' : ObjectId(doctor_id)
        		}
    		}
		])
		unavailable_time = {}
		for order in cursor :
			start = order['time']['finish']
			finish = order['time']['finish']
			while start != finish :
				if start in unavailable_time :
					unavailable_time[start] += 1
				else :
					unavailable_time[start] = 1
				start += timedelta(hours=1)
		unavailable_list = []
		today_morning = datetime(int(time.strftime('%Y')),int(time.strftime('%m')),int(time.strftime('%d')),0,0)
		while today_morning <= now :
			unavailable_list.append(today_morning)
			today_morning += timedelta(hours=1)
		unavailable_list.append(today_morning)
		for time in unavailable_time :
			if unavailable_time[time] >= self.max_per_period :
				if time not in unavailable_list :
					unavailable_list.append(time)
		return unavailable_list
	
	def show_doctor_detail(self, doctor_id) :
		doctors = self.get_doctor_query(doctor_id)
		for doctor in doctors :
			doctor.pop('_id',None)
			doctor['reserved'] = unavailable(doctor_id)
			return True, doctor
		return False, 'No Profile'