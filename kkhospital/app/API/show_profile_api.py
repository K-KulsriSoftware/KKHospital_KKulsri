#!/usr/bin/python
# -*- coding: utf-8 -*-

class show_profile_api :

	def __init__(self, db) :
		self.db = db

	def get_patients_profile_query(self, username) :
		return self.db.patients.aggregate([
    		{
        		'$match':
        		{
            		'username' : username
        		}
    		},
    		{
        		'$project':
        		{
            		'username' : '$username',
	    			'patient_name_title' : '$patient_name_title',
	    			'patient_name' : '$patient_name',
	    			'patient_surname' : '$patient_surname',
	    			'patient_img' : '$patient_img',
	    			'id_card_number' : '$id_card_number',
	    			'gender' : '$gender',
					'birthday' : '$birthday',
					'blood_group_abo' : '$blood_group_abo',
					'blood_group_rh' : '$blood_group_rh',
					'race' : '$race',
					'nationallity' : '$nationallity',
					'religion' : '$religion',
					'status' : '$status',
					'patient_address' : '$patient_address',
					'occupy' : '$occupy',
					'telephone_number' : '$telephone_number',
					'father_name' : '$father_name',
					'mother_name' : '$mother_name',
					'emergency_name' : '$emergency_name',
					'emergency_phone' : '$emergency_phone',
					'emergency_address' : '$emergency_address',
					'email' : '$email',
					'congenital_disease' : '$congenital_disease'
        		}
     		}
		])

	def show_profile(self, username) :
		patients = self.get_patients_profile_query(username)
		for patient in patients:
			patient.pop('_id',None)
			return True, patient
		return False, 'No Profile'
