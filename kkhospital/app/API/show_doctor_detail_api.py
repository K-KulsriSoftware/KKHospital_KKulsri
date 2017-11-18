#!/usr/bin/python
# -*- coding: utf-8 -*-
from bson.objectid import ObjectId

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
	
	def show_doctor_detail(self, doctor_id) :
		doctors = self.get_doctor_query(doctor_id)
		for doctor in doctors :
			doctor.pop('_id',None)
			return True, doctor
		return False, 'No Profile'