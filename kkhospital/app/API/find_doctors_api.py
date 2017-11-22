#!/usr/bin/python
# -*- coding: utf-8 -*-
from bson.objectid import ObjectId
class find_doctors_api :

	def __init__(self, db) :
		self.db = db

	def translate_gender(self, gender) :
		if type(gender) == type(True) :
			if gender :
				return 'ชาย'
			else :
				return 'หญิง'
		else :
			if gender == 'ชาย' :
				return True
			else :
				return False

	def get_doctors_query(self, package_id) :
		return self.db.packages.aggregate([
		    {
		        '$match' :
		        {
		            '_id' : ObjectId(package_id)
		        }
		    },
		    {
		        '$lookup' :
		        {
		            'from' : 'doctors',
		            'localField' : 'department_id',
		            'foreignField' : 'department_id',
		            'as' : 'doctor'
		        }
		    },
		    {
		        '$lookup' :
		        {
		            'from' : 'departments',
		            'localField' : 'department_id',
		            'foreignField' : '_id',
		            'as' : 'department'
		        }
		    },
		    {
		        '$unwind' : '$department'
		    },
		    {
		        '$unwind' : '$doctor'
		    },
		    {
		        '$project' :
		        {
					'doctor_id': '$doctor._id',
		            'username' : '$doctor.username',
		            'doctor_name_title' : '$doctor.doctor_name_title',
		            'doctor_name' : '$doctor.doctor_name',
		            'doctor_surname' : '$doctor.doctor_surname',
		            'department_name' : '$department.department_name',
		            'doctor_img' : '$doctor.doctor_img',
		            'working_time' : '$doctor.working_time',
		            'gender' : '$doctor.gender'
		        }
		    }
		])

	def check_correct_conditions(self, doctor, days, time, doctor_firstname, doctor_lastname, gender) :
		if doctor_firstname != None and doctor_firstname != '' :
			if not doctor_firstname in doctor['doctor_name'] :
				return False
		if doctor_lastname != None and doctor_firstname != '' :
			if not doctor_lastname in doctor['doctor_surname'] :
				return False
		if gender != None and gender != '' :
			if self.translate_gender(gender) != doctor['gender'] :
				return False
		if days != None and time != None and days != [] and time != '' :
			check = True
			for day in days :
				if day in doctor['working_time']:
					for working_time in doctor['working_time'][day] :
						for now_check_time in range(int(working_time['start']), int(working_time['finish'])) :
							if (time == 'ช่วงเช้า' and 9 <= now_check_time <= 12) or (time == 'ช่วงบ่าย' and 13 <= now_check_time <= 17) :
								check = False
			if check :
				return False
		elif days != None and days != [] :
			check = True
			for day in days :
				if day in doctor['working_time']:
					if len(doctor['working_time'][day]) > 0 :
						check = False
			if check :
				return False
		elif time != None and time != '' :
			check = True
			for day in doctor['working_time'] :
				for working_time in doctor['working_time'][day] :
					for now_check_time in range(working_time['start'], working_time['stop']) :
						if (time == 'ช่วงเช้า' and 9 <= now_check_time <= 12) or (time == 'ช่วงบ่าย' and 13 <= now_check_time <= 17) :
							check = False
			if check :
				return False
		return True

	def find_doctors(self, package_id, days, time, doctor_firstname, doctor_lastname, gender) :
		doctors = self.get_doctors_query(package_id)
		result_doctors = []
		for doctor in doctors :
			if self.check_correct_conditions(doctor, days, time, doctor_firstname, doctor_lastname, gender) :
				doctor.pop('_id', None)
				doctor.pop('working_time', None)
				doctor.pop('gender', None)
				doctor['doctor_id'] = str(doctor['doctor_id'])
				result_doctors.append(doctor)
		return True, result_doctors

	def auto_get_doctors_query(package_id, username) :
		return self.db.packages.aggregate([
			{
				'$match' :
				{
					'_id' : ObjectId('59d890e99cb6f0707faf7034')
				}
			},
			{
				'$lookup' :
				{
					'from' : 'doctors',
					'localField' : 'department_id',
					'foreignField' : 'department_id',
					'as' : 'doctor'
				}
			},
			{
				'$lookup' :
				{
					'from' : 'departments',
					'localField' : 'department_id',
					'foreignField' : '_id',
					'as' : 'department'
				}
			},
			{
				'$unwind' : '$department'
			},
			{
				'$unwind' : '$doctor'
			},
			{
				'$lookup' :
				{
					'from' : 'orders',
					'localField' : 'doctor._id',
					'foreignField' : 'doctor_id',
					'as' : 'order'
				}
			},
			{
				'$unwind' : '$order'
			},
			{
				'$lookup' :
				{
					'from' : 'patients',
					'localField' : 'order.patient_id',
					'foreignField' : '_id',
					'as' : 'patient'
				}
			},
			{
				'$unwind' : '$patient'
			},
			{
				'$match' : 
				{
					'patient.username' : username
				}
			},
			{
				'$group' :
				{
					'_id' :
					{
						'doctor' : '$doctor'
					},
					'count' :
					{
						'$sum' : 1
					}
				}
			},
			{
				'$project' :
				{
					'doctor' : '$_id.doctor',
					'count' : 1
				}
			},
			{
				'$sort' :
				{
					'count' : -1
				}
			},
			{
				'$project' :
				{
					'doctor_id': '$doctor._id',
					'username' : '$doctor.username',
					'doctor_name_title' : '$doctor.doctor_name_title',
					'doctor_name' : '$doctor.doctor_name',
					'doctor_surname' : '$doctor.doctor_surname',
					'department_name' : '$department.department_name',
					'doctor_img' : '$doctor.doctor_img',
					#'working_time' : '$doctor.working_time',
					#'gender' : '$doctor.gender',
					'patient_username' : '$patient.username'
				}
			}])

	def auto_find_doctors(self, package_id, username) :
		doctors = self.auto_get_doctors_query(package_id, username)
		result_doctors = []
		result_name_doctors = []
		for doctor in doctors :
			doctor.pop('_id', None)
			doctor['doctor_id'] = str(doctor['doctor_id'])
			result_doctors.append(doctor)
			result_name_doctors.append(doctor['username'])
		print(result_name_doctors)
		doctors = self.get_doctors_query(package_id)
		for doctor in doctors :
			if doctor['username'] not in result_name_doctors :
				doctor.pop('_id', None)
				doctor.pop('working_time', None)
				doctor.pop('gender', None)
				doctor['doctor_id'] = str(doctor['doctor_id'])
				result_doctors.append(doctor)
				result_name_doctors.append(doctor['username'])
		return True, result_doctors