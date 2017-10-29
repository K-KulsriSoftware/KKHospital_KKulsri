#!/usr/bin/python
# -*- coding: utf-8 -*-
from pprint import pprint
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
			doctor.pop('_id', None)
			doctors.append(doctor)
		return True, doctors

	def get_doctor_detail(self,doctor_id) :
		cursor = self.db.doctors.aggregate([
			{
            	'$match' : 
            		{
            			'username' : doctor_id
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
        			'doctor_id' : '$username',
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

	def update_doctor(self, doctor_id, doctor_name_title, doctor_name, doctor_surname, gender, birthday, 
		              office_phone_number, email, department_id, doctor_img, position, expertises, 
		              educations, language, working_time, order_ids) :
		self.db.doctors.update_one(
			{
        		'username': doctor_id
    		},
    		{
        		'$set': 
        		{
        			'doctor_name_title' : doctor_name_title,
        			'doctor_name' : doctor_name,
        			'doctor_surname' : doctor_surname,
        			'gender' : gender,
        			'birthday' : birthday,
        			'office_phone_number' : office_phone_number,
	               	'email': email,
	               	'department_id' : department_id,
	               	'doctor_img' : doctor_img,
	               	'position' : position,
	               	'expertises' : expertises,
	               	'educations' : educations,
	               	'language' : language,
	               	'working_time' : working_time,
	               	'order_ids' : order_ids
        		}
    		}
		)
		return True, 'Successfully Updated'

	def delete_doctor(self, doctor_id) :
		self.db.doctors.delete_one(
			{
				"username": doctor_id
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

	def insert_doctor(self, doctor_name_title, doctor_name, doctor_surname, gender, birthday, 
					  office_phone_number, email, department_id, doctor_img, position, expertises, 
		              educations, language, working_time) :
		self.db.doctors.insert(
			{
				'username' : self.get_new_doctor_id(),
				'doctor_name_title' : doctor_name_title, 
				'doctor_name' : doctor_name,
				'doctor_surname' : doctor_surname,
				'gender' : gender, 
				'birthday' : birthday, 
				'office_phone_number' : office_phone_number, 
				'email' : email, 
				'department_id' : department_id, 
				'doctor_img' : doctor_img, 
				'position' : position, 
				'expertises' : expertises, 
		        'educations' : educations, 
		        'language' : language, 
		        'working_time' : working_time,
		        'order_ids' : []
			}
		)
		return True, 'Successfully Inserted'