#!/usr/bin/python
# -*- coding: utf-8 -*-
from pprint import pprint
class user_query_api :

	def __init__(self, db) :##
		self.db = db

	def get_all_users(self) :##
		cursor = self.db.users.aggregate([
			{
            	'$match' : {}
        	}
		])
		users = []
		for user in cursor :
			user.pop('_id', None)
			users.append(user)
		return True, users

	def get_user_detail(self,username) :##
		cursor = self.db.users.aggregate([
			{
            	'$match' : 
            		{
            			'username' : username
            		}
        	}
		])
		for user in cursor :
			user.pop('_id', None)
			return True, user
		return False, "No match profile"

	def get_all_users_name(self) :
		cursor = self.db.users.aggregate([
			{
            	'$match' : {}
        	},
        	{
        		'$project' : {
        			'username' : '$username',
        			'password' : '$password',
        		}
        	}
		])
		users = []
		for user in cursor :
			user.pop('_id', None)
			users.append(user)
		return True, users

	def update_user_profile(self, username, password) :
		self.db.users.update_one(
			{
        		'username': username
    		},
    		{
        		'$set': 
        		{
        			'password' : password,
        		}
    		}
		)
		return True, 'Successfully Updated'

	def delete_user(self, username) :
		self.db.users.delete_one(
			{
				"username": username
			}
		)
		return True, 'Successfully Removed'