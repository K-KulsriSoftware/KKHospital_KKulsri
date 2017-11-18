#!/usr/bin/python
# -*- coding: utf-8 -*-
from passlib.hash import pbkdf2_sha256

class add_account_api :

	def __init__(self, db) :
		self.db = db

	def already_used(self, username) :
		cursor = self.db.users.aggregate([
			{
				'$match' :
				{
					'username' : username
				}
			}
		])
		for temp in cursor :
			return True
		return False

	def add_account(self, username, password) :
		
		if self.already_used(username) :
			return False, 'this username is used'
		password = pbkdf2_sha256.encrypt(password, rounds=200000, salt_size=16)
		self.db.users.insert(
			{
            	'username' : username,
            	'password' : password
        	}
		)
		return True, 'Successfully Insert'