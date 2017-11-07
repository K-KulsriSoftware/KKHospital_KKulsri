#!/usr/bin/python
# -*- coding: utf-8 -*-
from pprint import pprint
from datetime import datetime
from bson.objectid import ObjectId
class doctor_query_api :

	def __init__(self, db) :
		self.db = db

	def get_all_doctors(self) :
		cursor = self.db.doctors.aggregate([
			{
            	'$match' : {}
        	}
		])
		doctors = []
		for doctor in cursor :
			doctors.append(doctor)
		return True, doctors

	def get_doctor_detail(self,doctor_id) :
		cursor = self.db.doctors.aggregate([
			{
            	'$match' : 
            		{
            			'_id' : ObjectId(doctor_id)
            		}
        	}
		])
		for doctor in cursor :
			doctor.pop('_id', None)
			return True, doctor
		return False, "No match profile"

	def get_all_doctors_name(self) :
		cursor = self.db.doctors.aggregate([
			{
            	'$match' : {}
        	},
        	{
        		'$project' : {
        			'username' : '$username',
        			'doctor_name_title' : '$doctor_name_title',
        			'doctor_first_name' : '$doctor_name',
        			'doctor_surname' : '$doctor_surname'
        		}
        	}
		])
		doctors = []
		for doctor in cursor :
			doctor.pop('_id', None)
			doctors.append(doctor)
		return True, doctors

	def update_doctor(self, doctor_id, username, doctor_name_title, doctor_name, doctor_surname, gender, birthday, 
		office_phone_number, email, department_id, doctor_img, position, expertises, educations, working_time) :
		self.db.doctors.update_one(
			{
        		'_id': ObjectId(doctor_id)
    		},
    		{
        		'$set': 
        		{
        			'username' : username,
        			'doctor_name_title' : doctor_name_title,
        			'doctor_name' : doctor_name,
        			'doctor_surname' : doctor_surname,
        			'gender' : gender,
        			'birthday' : datetime(birthday['year'], birthday['month'], birthday['day']),
        			'office_phone_number' : office_phone_number,
	               	'email': email,
	               	'department_id' : department_id,
	               	'doctor_img' : doctor_img,
	               	'position' : position,
	               	'expertises' : expertises,
	               	'educations' : educations,
	               	'working_time' : working_time,
        		}
    		}
		)
		return True, 'Successfully Updated'

	def delete_doctor(self, doctor_id) :
		self.db.doctors.delete_one(
			{
				"_id": ObjectId(doctor_id)
			}
		)
		return True, 'Successfully Removed'

	def get_new_doctor_id(self) :
		cursor = self.db.doctors.aggregate([
			{
				'$match' : {}
			},
			{
				'$sort' : 
				{
					'username' : -1
				}
			},
			{
				'$limit' : 1
			}
		])
		for i in cursor :
			i = int(i['username'][1:])
			if i < 10 :
				return 'd00' + str(i)
			elif i < 100 :
				return 'd0' + str(i)
			elif i < 1000 :
				return 'd' + str(i)
		return 'd000'

	def insert_doctor(self, username, doctor_name_title, doctor_name, doctor_surname, gender, birthday, 
		office_phone_number, email, department_id, doctor_img, position, expertises, educations, working_time) :
		self.db.doctors.insert(
			{
				'username' : username,
				'doctor_name_title' : doctor_name_title, 
				'doctor_name' : doctor_name,
				'doctor_surname' : doctor_surname,
				'gender' : gender, 
				'birthday' : datetime(birthday['year'], birthday['month'], birthday['day']),
				'office_phone_number' : office_phone_number, 
				'email' : email, 
				'department_id' : department_id, 
				'doctor_img' : doctor_img, 
				'position' : position, 
				'expertises' : expertises, 
		        'educations' : educations, 
		        'working_time' : working_time,
			}
		)
		return True, 'Successfully Inserted'