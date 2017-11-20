#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime

class get_collection_pattern_api :
	
	def __init__(self, db) :
		self.db = db
		self.name_title_list = ['none', 'นาย', 'นาง', 'นางสาว']
		self.doctor_title_list = ['none', 'นายแพทย์', 'นายแพทย์หญิง']
		self.gender_list = ['none', 'ชาย', 'หญิง']
		self.hour_list = list(range(7, 23))
		self.blood_abo_list = ['none', 'A', 'B', 'O', 'AB']
		self.blood_rh_list = ['none', 'RH+', 'RH-']
		self.status_list = ['none', 'โสด', 'แต่งงาน', 'หย่าร้าง', 'หม้าย', 'แยกกันอยู่']
		self.permissions = {
							'buildings' : {'delete' : True, 'insert' : True, 'update' : True},
							'departments' : {'delete' : True, 'insert' : True, 'update' : True},
							'doctors' : {'delete' : False, 'insert' : False, 'update' : True},
							'patients' : {'delete' : False, 'insert' : False, 'update' : True},
							'packages' : {'delete' : True, 'insert' : True, 'update' : True},
							'orders' : {'delete' : False, 'insert' : False, 'update' : False}
							}
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
				'field_name' : '_id',
				'field_type' : 'objectId'
			},
			{
				'field_name' : 'building_name',
				'field_type' : 'string'
			}
		]
	
	def get_departments_pattern(self) :
		return [
			{
				'field_name' : '_id',
				'field_type' : 'objectId'
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

	def get_doctors_pattern(self) :
		return [
			{
				'field_name' : '_id',
				'field_type' : 'objectId'
			},
			{
				'field_name' : 'username',
				'field_type' : 'string'
			},
			{
				'field_name' : 'doctor_name_title',
				'field_type' : 'string',
				#'note' : self.doctor_title_list
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
				'field_type' : 'bool',
				'note' : self.gender_list
			},
			{
				'field_name' : 'birthday',
				'field_type' : 'date',
				'note' : 'without hour'
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
				'field_type' : 'objectId'
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
								'field_type' : 'int',
								'note' : self.hour_list
							},
							{
								'field_name' : 'finish',
								'field_type' : 'int',
								'note' : self.hour_list
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
								'field_type' : 'int',
								'note' : self.hour_list
							},
							{
								'field_name' : 'finish',
								'field_type' : 'int',
								'note' : self.hour_list
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
								'field_type' : 'int',
								'note' : self.hour_list
							},
							{
								'field_name' : 'finish',
								'field_type' : 'int',
								'note' : self.hour_list
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
								'field_type' : 'int',
								'note' : self.hour_list
							},
							{
								'field_name' : 'finish',
								'field_type' : 'int',
								'note' : self.hour_list
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
								'field_type' : 'int',
								'note' : self.hour_list
							},
							{
								'field_name' : 'finish',
								'field_type' : 'int',
								'note' : self.hour_list
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
								'field_type' : 'int',
								'note' : self.hour_list
							},
							{
								'field_name' : 'finish',
								'field_type' : 'int',
								'note' : self.hour_list
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
								'field_type' : 'int',
								'note' : self.hour_list
							},
							{
								'field_name' : 'finish',
								'field_type' : 'int',
								'note' : self.hour_list
							}
						]
					},
				]
			}
		]

	def get_patients_pattern(self) :
		return [
			{
				'field_name' : '_id',
				'field_type' : 'objectId'
			},
			{
				'field_name' : 'username',
				'field_type' : 'string'
			},
			{
				'field_name' : 'patient_name_title',
				'field_type' : 'string',
				#'note' : self.name_title_list
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
				'field_type' : 'string'
			},
			{
				'field_name' : 'id_card_number',
				'field_type' : 'string'
			},
			{
				'field_name' : 'gender',
				'field_type' : 'bool',
				'note' : self.gender_list
			},
			{
				'field_name' : 'birthday',
				'field_type' : 'date',
				'note' : 'without hour'
			},
			{
				'field_name' : 'blood_group_abo',
				'field_type' : 'int',
				'note' : self.blood_abo_list
			},
			{
				'field_name' : 'blood_group_rh',
				'field_type' : 'int',
				'note' : self.blood_rh_list
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
				'field_name' : 'religion',
				'field_type' : 'string'
			},
			{
				'field_name' : 'status',
				'field_type' : 'int',
				'note' : self.status_list
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
				'field_name' : 'emergency_phone',
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
				'field_name' : '_id',
				'field_type' : 'objectId'
			},
			{
				'field_name' : 'package_id',
				'field_type' : 'objectId'
			},
			{
				'field_name' : 'doctor_id',
				'field_type' : 'objectId'
			},
			{
				'field_name' : 'patient_id',
				'field_type' : 'objectId'
			},
			{
				'field_name' : 'cost',
				'field_type' : 'double'
			},
			{
				'field_name' : 'time',
				'field_type' : 'dict',
				'dict' : 
				[
					{
						'field_name' : 'start',
						'field_type' : 'date',
						'note' : 'with hour'
					},
					{
						'field_name' : 'finish',
						'field_type' : 'date',
						'note' : 'with hour'
					}
				]
			},
			{
				'field_name' : 'bought_time',
				'field_type' : 'date',
				'note' : 'with hour,min'
			},
			{
				'field_name' : 'notice',
				'field_type' : 'string'
			},
			{
				'field_name' : 'note',
				'field_type' : 'string'	
			}
		]

	def get_packages_pattern(self) :
		return [
			{
				'field_name' : '_id',
				'field_type' : 'objectId'
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
				'field_type' : 'objectId'
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
				'field_type' : 'objectId'
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

	def get_collection_permission(self, collection_name, permission_name) :
		if not collection_name in self.permissions :
			return False, f'No collection name, {collection_name}'
		if not permission_name in ['delete', 'insert', 'update'] :
			return False, f'No permission name, {permission_name}'
		return self.permissions[collection_name][permission_name], 'collection and permission found'

	def encode_thai_value(self, domain, thai_word) :
		#if domain == 'patient_name_title' :
		#	return True, self.name_title_list.index(thai_word) + 1
		#elif domain == 'doctor_name_title' :
		#	return True, self.doctor_title_list.index(thai_word) + 1
		if domain == 'gender' :
			if thai_word == 'ชาย' :
				return True, True
			elif thai_word == 'หญิง' :
				return True, False
			else :
				return thai_word 
		elif domain == 'blood_group_abo' :
			return True, self.blood_abo_list.index(thai_word)
		elif domain == 'blood_group_rh' :
			return True, self.blood_rh_list.index(thai_word)
		elif domain == 'status' :
			return True, self.status_list.index(thai_word)
		else :
			return False, thai_word

	def get_value_from_index(self, mylist, index) :
		if type(index) == type(1) and 0 <= index < len(mylist) :
			return True, mylist[index]
		elif type(index) == type(1) :
			return False, str(index)
		return False, index
	def decode_thai_value(self, domain, code) :
		if type(code) == type('') and code.isdigit() :
			code = int(code)

		if code == 0 :
			return True, 'None'
		
		if domain == 'gender' :
				if code == True :
					return True, 'ชาย'
				elif code == False :
					return True, 'หญิง'
				else :
					return False, code
		elif domain == 'blood_group_abo' :
			return self.get_value_from_index(self.blood_abo_list, code)
			# if type(code) == type(1) and 0 <= code < len(self.blood_abo_list) : 
			# 	return True, self.blood_abo_list[code]
			# return False, code
		elif domain == 'blood_group_rh' :
			if type(code) == type(1) and 0 <= code < len(self.blood_rh_list) : 
				return True, self.blood_rh_list[code]
			return False, code
		elif domain == 'status' :
			if type(code) == type(1) and 0 <= code < len(self.status_list) : 
				return True, self.status_list[code]
			return False, code
		else :
			return False, code