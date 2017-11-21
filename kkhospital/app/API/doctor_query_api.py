#!/usr/bin/python
# -*- coding: utf-8 -*-
from pprint import pprint
from datetime import datetime
from bson.objectid import ObjectId
from .common_functions import separate_time, get_time
from .get_collection_pattern_api import get_collection_pattern_api

class doctor_query_api :

	def __init__(self, db) :
		self.db = db
		self.get_collection_pattern_api = get_collection_pattern_api(db)
		self.decode = self.get_collection_pattern_api.decode_thai_value
		self.encode = self.get_collection_pattern_api.encode_thai_value

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
			doctor['gender'] = self.decode('gender', doctor['gender'])[1]
			doctor['birthday'] = separate_time(doctor['birthday'])
			print(doctor)
			return True, doctor
		return False, "No match profile"

	def get_all_doctors_name(self) :
		cursor = self.db.doctors.aggregate([
			{
            	'$match' : {}
        	},
        	{
        		'$project' : {
        			'_id' : 1,
        			'username' : 1,
        			'doctor_name_title' : 1,
        			'doctor_name' : 1,
        			'doctor_surname' : 1
        		}
        	}
		])
		doctors = []
		for doctor in cursor :
			doctors.append(doctor)
		return True, doctors

	def edited_working_time(self, working_time) :
		result = {}
		for i in working_time :
			result[i] = []
			for j in working_time[i] :
				result[i].append({'start' : int(j['start']), 'finish' : int(j['finish'])})
		return result

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
        			'gender' : self.decode('gender', gender)[1],
        			'birthday' : get_time(birthday),
        			'office_phone_number' : office_phone_number,
	               	'email': email,
	               	'department_id' : ObjectId(department_id),
	               	'doctor_img' : doctor_img,
	               	'position' : position,
	               	'expertises' : expertises,
	               	'educations' : educations,
	               	'working_time' : self.edited_working_time(working_time)
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

	def edited_birthday(self, birthday_string) :
		birthday_list = birthday_string.split('-')
		return datetime(int(birthday_list[0]), int(birthday_list[1]), int(birthday_list[2]))

	def insert_doctor(self, username, doctor_name_title, doctor_name, doctor_surname, gender, birthday, 
		office_phone_number, email, department_id, doctor_img, position, expertises, educations, working_time) :
		self.db.doctors.insert_one(
			{
				'username' : username,
    			'doctor_name_title' : doctor_name_title,
    			'doctor_name' : doctor_name,
    			'doctor_surname' : doctor_surname,
    			'gender' : self.decode('gender', gender)[1],
    			'birthday' : get_time(birthday),
    			'office_phone_number' : office_phone_number,
               	'email': email,
               	'department_id' : ObjectId(department_id),
               	'doctor_img' : doctor_img,
               	'position' : position,
               	'expertises' : expertises,
               	'educations' : educations,
               	'working_time' : self.edited_working_time(working_time)
			}
		)
		return True, 'Successfully Inserted'

	def get_doctor_id(self, doctor_username):
		cursor = self.db.doctors.aggregate([
			{
				'$match' : 
				{
					'username' : doctor_username
				}
			},
			{
				'$project' : 
				{
					'doctor_id' : '$_id'
				}
			},
		])
		for temp in cursor:
			return True, str(temp['doctor_id'])
		return False, 'doctor error'