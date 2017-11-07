#!/usr/bin/python
# -*- coding: utf-8 -*-
from pprint import pprint
class department_query_api :

	def __init__(self, db) :##
		self.db = db

	def get_all_departments(self) :##
		cursor = self.db.departments.aggregate([
			{
            	'$match' : {}
        	}
		])
		departments = []
		for department in cursor :
			departments.append(department)
		return True, departments

	def get_department_detail(self,department_id) :##
		cursor = self.db.departments.aggregate([
			{
            	'$match' : 
            		{
            			'department_id' : department_id
            		}
        	}
		])
		for department in cursor :
			department.pop('_id', None)
			return True, department
		return False, "No match profile"

	def get_all_departments_name(self) :
		cursor = self.db.departments.aggregate([
			{
            	'$match' : {}
        	},
        	{
        		'$project' : {
        			'department_id' : '$department_id',
        			'department_name' : '$department_name',
        		}
        	}
		])
		departments = []
		for department in cursor :
			department.pop('_id', None)
			departments.append(department)
		return True, departments

	def update_department_profile(self, department_id, department_name, department_description) :
		self.db.departments.update_one(
			{
        		'department_id': department_id
    		},
    		{
        		'$set': 
        		{
        			'department_name' : department_name,
        			'department_description' : department_description,
        		}
    		}
		)
		return True, 'Successfully Updated'

	def delete_department(self, department_id) :
		self.db.departments.delete_one(
			{
				'department_id' : department_id
			}
		)
		return True, 'Successfully Removed'

	def get_new_department_id(self) :
		cursor = self.db.departments.aggregate([
			{
				'$match' : {}
			},
			{
				'$sort' :
				{
					'department_id' : -1
				}
			},
			{
				'$limit' : 1
			}
		])
		for i in cursor :
			i = i[department_id]
			return i+1
		return 0

	def insert_department(self, department_name, department_description) :
		self.db.departments.insert(
			{
				'department_id' : get_new_department_id(),
				'department_name' : department_name,
				'department_description' : department_description
			}
		)
		return True, 'Successfully Inserted'