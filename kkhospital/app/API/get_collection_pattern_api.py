#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime

class get_collection_pattern_api :

	def __init__(self, db) :
		self.db = db
	'''
	def str_type_name(self, field_type) :
		#print(field_type)
		if field_type == type(0) :
			return 'int'
		if field_type == type(0.2) :
			return 'double'
		if field_type == type(datetime(1,1,1,1,0)) :
			return 'date'
		if field_type == type(True) :
			return 'bool'
		if field_type == type('') :
			return 'string'
		if field_type == type({}) :
			return 'dict'
		if field_type == type([]) :
			return 'list'

	def read_dict(self, collection_name, record_dict) :
		result = []
		for field in record_dict :
			field_type = self.str_type_name(type(record_dict[field]))
			if field_type == 'dict' :
				print(field)
				result.append({'field_name' : field, 'field_type' : 'dict', 'dict' : self.read_dict(collection_name, record_dict[field])})
			elif field_type == 'list' :
				if collection_name == 'patients' and field == 'congenital_disease':
					result.append({'field_name' : field, 'field_type' : 'string'})
				elif collection_name == 'doctors' and field in ['mon','tue','wed','thu','fri','sat','sun'] :
					result.append('field_name' : field, 'field_type' : 'list', 'value' : dict)
				else :
					result.append({'field_name' : field, 'field_type' : 'list', 'value' : self.str_type_name(type(record_dict[field][0]))})
			else :
				#print(field_type)
				result.append({'field_name' : field, 'field_type' : field_type})
		return result

	def get_collection_pattern(self, collection_name) :
		if collection_name == None :
			return False, 'Incomplete input: collection_name'
		all_collections_name = self.db.collection_names()
		if collection_name not in all_collections_name :
			return False, 'No collection name :' + collection_name
		cursor = self.db[collection_name].aggregate([
			{
				'$match' : {}
			},
			{
				'$limit' : 1
			}
		])
		result = []
		for record in cursor :
			record.pop('_id', None)
			result = self.read_dict(collection_name, record)
		return True, result
	'''

	def get_buildings_pattern(self) :
		return [
			{
				'field_name' : 'building_id',
				'field_type' : 'int'
			},
			{
				'field_name' : 'building_name',
				'field_type' : 'int'
			}
		]
	
	def get_departments_pattern(self) :
		return [
			{
				'field_name' : 'department_id',
				'field_type' : 'int'
			},
			{
				'field_name' : 'department_name',
				'field_type' : 'string'
			},
			{
				'field_name' : 'department_description',
				'field_type' : 'string'
			}
		]

	def get_departments_pattern(self) :
		return [
			{
				'field_name' : 'username',
				'field_type' : 'string'
			},
			{
				'field_name' : 'doctor_name_title',
				'field_type' : 'string'
			},
			{
				'field_name' : 'doctor_name',
				'field_type' : 'string'
			},
			{
				'field_name' : 'doctor_surname',
				'field_type' : 'string'
			},
			{
				'field_name' : 'gender',
				'field_type' : 'bool'
			},
			{
				'field_name' : 'birthday',
				'field_type' : 'date'
			},
			{
				'field_name' : 'office_phone_number',
				'field_type' : 'string'
			},
			{
				'field_name' : 'email',
				'field_type' : 'string'
			},
			{
				'field_name' : 'department_id',
				'field_type' : 'int'
			},
			{
				'field_name' : 'doctor_img',
				'field_type' : 'string'
			},
			{
				'field_name' : 'position',
				'field_type' : 'string'
			},
			{
				'field_name' : 'expertises',
				'field_type' : 'list',
				'value' : 'string'
			},
			{
				'field_name' : 'educations',
				'field_type' : 'list',
				'value' : 'string'
			},
			{
				'field_name' : 'language',
				'field_type' : 'list',
				'value' : 'string'
			},
			{
				'field_name' : 'working_time',
				'field_type' : 'dict',
				'dict' : 
				[
					{
						'field_name' : 'mon',
						'field_type' : 'list',
						'value' : 'dict',
						'dict' :
						[
							{
								'field_name' : 'start',
								'field_type' : 'string'
							},
							{
								'field_name' : 'finish',
								'field_type' : 'string'
							}
						]
					},
					{
						'field_name' : 'tue',
						'field_type' : 'list',
						'value' : 'dict',
						'dict' :
						[
							{
								'field_name' : 'start',
								'field_type' : 'string'
							},
							{
								'field_name' : 'finish',
								'field_type' : 'string'
							}
						]
					},
					{
						'field_name' : 'wed',
						'field_type' : 'list',
						'value' : 'dict',
						'dict' :
						[
							{
								'field_name' : 'start',
								'field_type' : 'string'
							},
							{
								'field_name' : 'finish',
								'field_type' : 'string'
							}
						]
					},
					{
						'field_name' : 'thu',
						'field_type' : 'list',
						'value' : 'dict',
						'dict' :
						[
							{
								'field_name' : 'start',
								'field_type' : 'string'
							},
							{
								'field_name' : 'finish',
								'field_type' : 'string'
							}
						]
					},
					{
						'field_name' : 'fri',
						'field_type' : 'list',
						'value' : 'dict',
						'dict' :
						[
							{
								'field_name' : 'start',
								'field_type' : 'string'
							},
							{
								'field_name' : 'finish',
								'field_type' : 'string'
							}
						]
					},
					{
						'field_name' : 'sat',
						'field_type' : 'list',
						'value' : 'dict',
						'dict' :
						[
							{
								'field_name' : 'start',
								'field_type' : 'string'
							},
							{
								'field_name' : 'finish',
								'field_type' : 'string'
							}
						]
					},
					{
						'field_name' : 'sun',
						'field_type' : 'list',
						'value' : 'dict',
						'dict' :
						[
							{
								'field_name' : 'start',
								'field_type' : 'string'
							},
							{
								'field_name' : 'finish',
								'field_type' : 'string'
							}
						]
					},
				]
			},
			{
				'field_name' : 'order_ids',
				'field_type' : 'list',
				'value' : 'string'
			}
		]

	def get_patients_pattern(self) :
		return [
			{
				'field_name' : 'username',
				'field_type' : 'string'
			},
			{
				'field_name' : 'patient_name_title',
				'field_type' : 'string'
			},
			{
				'field_name' : 'patient_name',
				'field_type' : 'string'
			},
			{
				'field_name' : 'patient_surname',
				'field_type' : 'string'
			},
			{
				'field_name' : 'patient_img',
				'field_type' : 'bool'
			},
			{
				'field_name' : 'id_card_number',
				'field_type' : 'date'
			},
			{
				'field_name' : 'gender',
				'field_type' : 'bool'
			},
			{
				'field_name' : 'order_ids',
				'field_type' : 'list',
				'value' : 'string'
			},
			{
				'field_name' : 'birthday',
				'field_type' : 'date'
			},
			{
				'field_name' : 'blood_group_abo',
				'field_type' : 'int'
			},
			{
				'field_name' : 'blood_group_rh',
				'field_type' : 'int',
			},
			{
				'field_name' : 'race',
				'field_type' : 'string'
			},
			{
				'field_name' : 'nationallity',
				'field_type' : 'string'
			},
			{
				'field_name' : 'Religion',
				'field_type' : 'string'
			},
			{
				'field_name' : 'Status',
				'field_type' : 'int'
			},
			{
				'field_name' : 'patient_address',
				'field_type' : 'string'
			},
			{
				'field_name' : 'occupy',
				'field_type' : 'string'
			},
			{
				'field_name' : 'telphone_number',
				'field_type' : 'string'
			},
			{
				'field_name' : 'father_name',
				'field_type' : 'string'
			},
			{
				'field_name' : 'mother_name',
				'field_type' : 'string'
			},
			{
				'field_name' : 'emergency_name',
				'field_type' : 'string'
			},
			{
				'field_name' : 'emergency_address',
				'field_type' : 'string'
			},
			{
				'field_name' : 'email',
				'field_type' : 'string'
			},
			{
				'field_name' : 'congenital_disease',
				'field_type' : 'list',
				'value' : 'string'
			}
		]

	def get_orders_pattern(self) :
		return [
			{
				'field_name' : 'order_id',
				'field_type' : 'string'
			},
			{
				'field_name' : 'package_id',
				'field_type' : 'string'
			},
			{
				'field_name' : 'doctor_id',
				'field_type' : 'string'
			},
			{
				'field_name' : 'user_id',
				'field_type' : 'string'
			},
			{
				'field_name' : 'cost',
				'field_type' : 'double'
			},
			{
				'field_name' : 'notice',
				'field_type' : 'string'
			},
			{
				'field_name' : 'time',
				'field_type' : 'dict',
				'dict' : 
				[
					{
						'field_name' : 'start',
						'field_type' : 'date'
					},
					{
						'field_name' : 'finish',
						'field_type' : 'date'
					}
				]
			}
		]

	def get_packages_pattern(self) :
		return [
			{
				'field_name' : 'package_id',
				'field_type' : 'string'
			},
			{
				'field_name' : 'package_name',
				'field_type' : 'string'
			},
			{
				'field_name' : 'package_cost',
				'field_type' : 'double'
			},
			{
				'field_name' : 'department_id',
				'field_type' : 'int'
			},
			{
				'field_name' : 'description',
				'field_type' : 'string'
			},
			{
				'field_name' : 'conditions',
				'field_type' : 'list',
				'value' : 'string'
			},
			{
				'field_name' : 'package_notice',
				'field_type' : 'string'
			},
			{
				'field_name' : 'building_id',
				'field_type' : 'int'
			}
		]

	def get_collection_pattern(self, collection_name) :
		if collection_name == 'buildings' :
			return True, self.get_buildings_pattern()
		elif collection_name == 'departments' :
			return True, self.get_departments_pattern()
		elif collection_name == 'doctors' :
			return True, self.get_doctors_pattern()
		elif collection_name == 'patients' :
			return True, self.get_patients_pattern()
		elif collection_name == 'orders' :
			return True, self.get_orders_pattern()
		elif collection_name == 'packages' :
			return True, self.get_packages_pattern()
		else :
			return False, 'No collection name : ' + collection_name