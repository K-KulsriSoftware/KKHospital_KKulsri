#!/usr/bin/python
# -*- coding: utf-8 -*-
from pprint import pprint
from datetime import datetime
from bson.objectid import ObjectId
class packages_query_api :

	def __init__(self, db) :
		self.db = db

	def get_all_packages(self) :
		cursor = self.db.packages.aggregate([
			{
            	'$match' : {}
        	}
		])
		packages = []
		for package in cursor :
			package.pop('_id', None)
			packages.append(package)
		return True, packages



	def get_package_detail(self,package_id) :
		cursor = self.db.packages.aggregate([
			{
            	'$match' :
            		{
            			'_id' : ObjectId(package_id)
            		}
        	}
		])
		for package in cursor :
			package.pop('_id', None)
			return True, package
		return False, "No match package"


	def get_all_packages_name(self) :
		cursor = self.db.packages.aggregate([
			{
            	'$match' : {}
        	},
        	{
        		'$project' : {
        			'package_id' : '$_id',
        			'package_name' : '$package_name'
        		}
        	}
		])
		packages = []
		for package in cursor :
			package.pop('_id', None)
			packages.append(package)
		return True, packages


	def update_package(self, package_id, package_name, package_cost, department_id, description, conditions, package_notice, building_id) :
		self.db.packages.update_one(
    		{
        		'_id': ObjectId(package_id)
    		},
    		{
        		'$set':
        		{
        			'package_name' : package_name,
        			'package_cost' : package_cost,
        			'department_id' : department_id,
        			'description' : description,
        			'conditions' : conditions,
        			'package_notice' : package_notice,
    				'building_id' : building_id

        		}
    		}
		)
		return True, 'Successfully Updated'

	def delete_package(self, package_id) :
		self.db.packages.delete_one(
            {
                "_id": ObjectId(package_id)
            }
        )
		return True, 'Successfully Removed'


	def insert_package(self, package_name, package_cost, department_id, description, conditions, package_notice, building_id) :
		self.db.packages.insert(
			{
    			'package_name' : package_name,
                'package_cost' : package_cost,
                'department_id' : department_id,
                'description' : description,
                'conditions' : conditions,
                'package_notice' : package_notice,
                'building_id' : building_id
			}
	    )
		return True,'Successfully Added'