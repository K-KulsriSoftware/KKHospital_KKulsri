#!/usr/bin/python
# -*- coding: utf-8 -*-

class show_confirmation_info_api :

	def __init__(self, db) :
		self.db = db

	def get_packages_query(self, package_id) :
		return self.db.packages.aggregate([
			{
				'$match' : 
				{
            		'package_id' : package_id
            	}
			},
			{
				'$project' : 
				{
            		'package_name' : '$package_name',
					'package_cost' : '$package_cost'
            	}
			}
		])

	def get_doctors_query(self, doctor_id):
		return self.db.doctors.aggregate([
			{
				'$match' : 
				{
            		'username' : doctor_id
            	}
			},
			{
				'$project' : 
				{
					'doctor_name_title' : '$doctor_name_title',
            		'doctor_name' : '$doctor_name',
					'doctor_surname' : '$doctor_surname',
					'office_phone_number' : '$office_phone_number'
            	}
			}
		])

	def get_patients_query(self, username) :
		return self.db.patients.aggregate([
			{
				'$match' : 
				{
            		'username' : username
            	}
			},
			{
				'$project' : 
				{
					'patient_name_title' : '$patient_name_title',
            		'patient_name' : '$patient_name',
					'patient_surname' : '$patient_surname'
            	}
			}
		])

	def show_confirmation_info(self,package_id, doctor_id, username, time) :
		packages = self.get_packages_query(package_id)
		res_package = ''
		for package in packages:
			package.pop('_id',None)
			res_package = package
		doctors = self.get_doctors_query(doctor_id)
		res_doctor = ''
		for doctor in doctors:
			doctor.pop('_id',None)
			res_doctor = doctor
		patients = self.get_patients_query(username)
		res_patient = ''
		for patient in patients:
			patient.pop('_id',None)
			res_patient = patient
		#dateandtime = "time" : {'start':datetime(time['year'],time['month'],time['date'],time['start_hr'],0),'finish':datetime(time['year'],time['month'],time['date'],time['finish_hr'],0)}
		result = {**res_package,**res_doctor,**res_patient,**time}
		return True, result