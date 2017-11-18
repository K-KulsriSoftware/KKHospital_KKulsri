#!/usr/bin/python
# -*- coding: utf-8 -*-

class show_general_list_api :

	def __init__(self, db) :
		self.db = db

	def get_package_query(self) :
		return self.db.packages.aggregate([
    		{
        		'$lookup' :
        		{
        		    'from' : 'departments',
        		    'localField' : 'department_id',
        	   		'foreignField' : '_id',
            		'as' : 'department'
                }
    		},
    		{
        		'$match' : 
        		{
            		'department.department_name' : 'ศูนย์อายุรกรรม'
            	}
    		},
    		{
        		'$project' : 
        		{
            		'package_id' : '$_id',
            		'package_name' : '$package_name',
            		'package_cost' : '$package_cost',
            		'description' : '$description'
            	}
    		}
		])

	def show_general_list(self) :
		packages = self.get_package_query()
		result = []
		for package in packages:
			package.pop('_id',None)
			result.append(package)
		return True,result