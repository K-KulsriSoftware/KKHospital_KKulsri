#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime

class register_api :

	def __init__(self, db) :
		self.db = db

	def insert_query(self, username, patient_name_title, patient_name, patient_surname, patient_img, id_card_number, gender,
				 birthday_year, birthday_month, birthday_day, blood_group_abo, blood_group_rh, race, nationallity,
				 religion, status, patient_address, occupy, telephone_number, father_name, mother_name, emergency_name,
				 emergency_phone, emergency_address, email, congenital_disease) :
		self.db.patients.insert_one(
			{
    			'username' : username,
    			'patient_name_title' : patient_name_title,
    			'patient_name' : patient_name,
    			'patient_surname' : patient_surname,
    			'patient_img' : patient_img,
    			'id_card_number' : id_card_number,
    			'gender' : gender,
				'birthday' : datetime(birthday_year, birthday_month, birthday_day),
				'blood_group_abo' : blood_group_abo,
				'blood_group_rh' : blood_group_rh,
				'race' : race,
				'nationallity' : nationallity,
				'religion' : religion,
				'status' : status,
				'patient_address' : patient_address,
				'occupy' : occupy,
				'telephone_number' : telephone_number,
				'father_name' : father_name,
				'mother_name' : mother_name,
				'emergency_name' : emergency_name,
				'emergency_phone' : emergency_phone,
				'emergency_address' : emergency_address,
				'email' : email,
				'congenital_disease' : congenital_disease
			}
	    )


	def register(self, username, patient_name_title, patient_name, patient_surname, patient_img, id_card_number, gender,
				 birthday_year, birthday_month, birthday_day, blood_group_abo, blood_group_rh, race, nationallity,
				 religion, status, patient_address, occupy, telephone_number, father_name, mother_name, emergency_name,
				 emergency_phone, emergency_address, email, congenital_disease, submit) :
		if submit :
			self.insert_query(username, patient_name_title, patient_name, patient_surname, patient_img, id_card_number, gender,
							  birthday_year, birthday_month, birthday_day, blood_group_abo, blood_group_rh, race, nationallity,
							  religion, status, patient_address, occupy, telephone_number, father_name, mother_name, emergency_name,
							  emergency_phone, emergency_address, email, congenital_disease)
			return True, 'Successfully Added'
		else :
			return False, 'Not submit'
