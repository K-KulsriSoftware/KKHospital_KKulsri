#!/usr/bin/python
# -*- coding: utf-8 -*-
from pprint import pprint
from bson.objectid import ObjectId
class building_query_api :

	def __init__(self, db) :
		self.db = db

	def get_all_buildings(self) :
		cursor = self.db.buildings.aggregate([
			{
            	'$match' : {}
        	}
		])
		buildings = []
		for building in cursor :
			buildings.append(building)
		return True, buildings

	def get_building_detail(self,building_id) :
		cursor = self.db.buildings.aggregate([
			{
            	'$match' : 
            		{
            			'_id' : ObjectId(building_id)
            		}
        	}
		])
		for building in cursor :
			return True, building
		return False, "No match profile"

	def get_all_buildings_name(self) :
		cursor = self.db.buildings.aggregate([
			{
            	'$match' : {}
        	},
        	{
        		'$project' : {
        			'_id' : 1,
        			'building_name' : 1,
        		}
        	}
		])
		buildings = []
		for building in cursor :
			buildings.append(building)
		return True, buildings

	def update_building_profile(self, building_id, building_name) :
		self.db.buildings.update_one(
			{
        		'_id': ObjectId(building_id)
    		},
    		{
        		'$set': 
        		{
        			'building_name' : building_name,
        		}
    		}
		)
		return True, 'Successfully Updated'

	def delete_building(self, building_id) :
		self.db.buildings.delete_one(
			{
				'_id': ObjectId(building_id)
			}
		)
		return True, 'Successfully Removed'

	def insert_building(self, building_name) :
		self.db.buildings.insert(
			{
				'building_name' : building_name
			}
		)
		return True, 'Successfully Inserted'