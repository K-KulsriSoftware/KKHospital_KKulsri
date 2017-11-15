#!/usr/bin/python
# -*- coding: utf-8 -*-
from pprint import pprint
from datetime import datetime
from bson.objectid import ObjectId
class patients_query_api :

	def __init__(self, db) :
		self.db = db

	def get_all_patients(self) :
		cursor = self.db.patients.aggregate([
			{
            	'$match' : {}
        	}
		])
		patients = []
		for patient in cursor :
			patients.append(patient)
		return True, patients

	def get_patient_detail(self,patient_id) :
		cursor = self.db.patients.aggregate([
			{
            	'$match' :
            		{
            			'_id' : ObjectId(patient_id)
            		}
        	}
		])
		for patient in cursor :
			return True, patient
		return False, "No match profile"


	def get_all_patients_name(self) :
		cursor = self.db.patients.aggregate([
			{
            	'$match' : {}
        	},
        	{
        		'$project' : {
        			'_id' : 1,
        			'username' : 1,
        			'patient_name_title' : 1,
        			'patient_first_name' : 1,
        			'patient_surname' : 1
        		}
        	}
		])
		patients = []
		for patient in cursor :
			patients.append(patient)
		return True, patients


	def update_patient(self, patient_id, username, patient_name_title, patient_name, patient_surname, patient_img, 
		id_card_number, gender, birthday, blood_group_abo, blood_group_rh, race, nationallity, religion, status, 
		patient_address, occupy, telphone_number, father_name, mother_name, emergency_name, emergency_phone, 
		emergency_address, email, congenital_disease) :
		self.db.patients.update_one(
    		{
        		'_id': ObjectId(patient_id)
    		},
    		{
        		'$set':
        		{
        			'username' : username,
        			'patient_name_title' : patient_name_title,
        			'patient_name' : patient_name,
        			'patient_surname' : patient_surname,
        			'patient_img' : patient_img,
        			'id_card_number' : id_card_number,
        			'gender' : gender,
    				'birthday' : datetime(int(birthday['year']), int(birthday['month']), int(birthday['day'])),
    				'blood_group_abo' : blood_group_abo,
    				'blood_group_rh' : blood_group_rh,
    				'race' : race,
    				'nationallity' : nationallity,
    				'religion' : religion,
    				'status' : status,
    				'patient_address' : patient_address,
    				'occupy' : occupy,
    				'telephone_number' : telphone_number,
    				'father_name' : father_name,
    				'mother_name' : mother_name,
    				'emergency_name' : emergency_name,
    				'emergency_phone' : emergency_phone,
    				'emergency_address' : emergency_address,
    				'email' : email,
    				'congenital_disease' : congenital_disease
        		}
    		}
		)
		return True, 'Successfully Updated'

	def delete_patient(self, patient_id) :
		self.db.patients.delete_one(
            {
                "_id": ObjectId(patient_id)
            }
        )
		return True, 'Successfully Removed'

	def insert_patient(self, username, patient_name_title, patient_name, patient_surname, patient_img, 
		id_card_number, gender, birthday, blood_group_abo, blood_group_rh, race, nationallity, religion, status, 
		patient_address, occupy, telphone_number, father_name, mother_name, emergency_name, emergency_phone, 
		emergency_address, email, congenital_disease) :
		self.db.patients.insert(
			{
    			'username' : username,
    			'patient_name_title' : patient_name_title,
    			'patient_name' : patient_name,
    			'patient_surname' : patient_surname,
    			'patient_img' : patient_img,
    			'id_card_number' : id_card_number,
    			'gender' : gender,
				'birthday' : datetime(birthday['year'], birthday['month'], birthday['day']),
				'blood_group_abo' : blood_group_abo,
				'blood_group_rh' : blood_group_rh,
				'race' : race,
				'nationallity' : nationallity,
				'religion' : religion,
				'status' : status,
				'patient_address' : patient_address,
				'occupy' : occupy,
				'telphone_number' : telphone_number,
				'father_name' : father_name,
				'mother_name' : mother_name,
				'emergency_name' : emergency_name,
				'emergency_phone' : emergency_phone,
				'emergency_address' : emergency_address,
				'email' : email,
				'congenital_disease' : congenital_disease
			}
	    )
		return True,'Successfully Added'

	def check_already_used_this_username(self, username) :
		cursor = self.db.patients.aggregate([
        	{
        		'$match' :
        		{
        			'username' : username
        		}
        	}
        ])
		for temp in cursor :
			return True, 'User Already Used'
		return False, 'User Inactivate'