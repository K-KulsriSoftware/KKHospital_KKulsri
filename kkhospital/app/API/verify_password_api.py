#!/usr/bin/python
# -*- coding: utf-8 -*-
from passlib.hash import pbkdf2_sha256

class verify_password_api :

	def __init__(self, db) :
		self.db = db

	def get_password(self, username) :
		cursor = self.db.users.aggregate([
			{
				'$match' :
				{
					'username' : username
				}
			}
		])
		for temp in cursor :
			return True, temp['password']
		return False, 'No user'

	def verify_password(self, username, password):
		check, hash_password = self.get_password(username)
		if check :
			if pbkdf2_sha256.verify(password, hash_password) :
				return True, username
			else :
				return False, 'Wrong Password'
		else :
			return False , hash_password
