#!/usr/bin/python
# -*- coding: utf-8 -*-

class edit_profile_api :

	def __init__(self, db) :
		self.db = db

	def update_query(self, username, email, telphone_number, emergency_phone) :
		self.db.patients.update_one(
    		{
        		'username': username
    		},
    		{
        		'$set': 
        		{
	               	'email': email,
	               	'telphone_number' : telphone_number,
	               	'emergency_phone' : emergency_phone
        		}
    		}
		)
		
	def edit_profile(self, username, email, telphone_number, emergency_phone, submit) :
		if submit :
			self.update_query(username, email, telphone_number, emergency_phone)
			return True,'Successfully Updated'
		else :
			return False, 'Fail Updated'