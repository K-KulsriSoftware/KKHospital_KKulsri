#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
   from config import MONGO_PATH
except ImportError:
   pass

import urllib.parse
from pymongo import MongoClient
import json

#for website
from .find_doctors_api import find_doctors_api
from .show_profile_api import show_profile_api
from .show_doctor_detail_api import show_doctor_detail_api
from .edit_profile_api import edit_profile_api
from .register_api import register_api
from .show_general_list_api import show_general_list_api
from .show_departments_api import show_departments_api
from .show_special_package_info_api import show_special_package_info_api
from .create_order_api import create_order_api
from .show_confirmation_info_api import show_confirmation_info_api
from .doctor_query_api import doctor_query_api
from .department_query_api import department_query_api###Watcharachat Tay
from .user_query_api import user_query_api###Watcharachat Tay
from .building_query_api import building_query_api###Watcharachat Tay
from .show_doctor_in_department_api import show_doctor_in_department_api
from .patients_query_api import patients_query_api###Jakapong Mo
from .packages_query_api import packages_query_api###Jakapong Mo
from .orders_query_api import orders_query_api###Jakapong Mo
from .get_collection_pattern_api import get_collection_pattern_api
from .get_patient_orders_api import get_patient_orders_api
from .get_doctor_orders_api import get_doctor_orders_api
from .add_account_api import add_account_api
from .verify_password_api import verify_password_api
'''
#for test api
from find_doctors_api import find_doctors_api
from show_profile_api import show_profile_api
from show_doctor_detail_api import show_doctor_detail_api
from edit_profile_api import edit_profile_api
from register_api import register_api
from show_general_list_api import show_general_list_api
from show_departments_api import show_departments_api
from show_special_package_info_api import show_special_package_info_api
from create_order_api import create_order_api
from show_confirmation_info_api import show_confirmation_info_api
from doctor_query_api import doctor_query_api
from department_query_api import department_query_api
from user_query_api import user_query_api
from building_query_api import building_query_api
from show_doctor_in_department_api import show_doctor_in_department_api
from patients_query_api import patients_query_api
from packages_query_api import packages_query_api
from orders_query_api import orders_query_api
from get_collection_pattern_api import get_collection_pattern_api
from get_patient_orders_api import get_patient_orders_api
from get_doctor_orders_api import get_doctor_orders_api
from add_account_api import add_account_api
from verify_password_api import verify_password_api
'''
class API :

	def __init__(self) :
		#for test api
		# with open('./config.json', 'r') as json_file :
		#for website
		# with open('./app/API/config.json', 'r') as json_file :
		# 	data = json.load(json_file)
		# 	username = urllib.parse.quote_plus(data['username'])
		# 	password = urllib.parse.quote_plus(data['password'])
		# 	db = data['db']
		self.client = MongoClient(MONGO_PATH)
		self.db = self.client.kk_db
		self.find_doctors_api = find_doctors_api(self.db)
		self.show_profile_api = show_profile_api(self.db)
		self.show_doctor_detail_api = show_doctor_detail_api(self.db)
		self.edit_profile_api = edit_profile_api(self.db)
		self.register_api = register_api(self.db)
		self.show_general_list_api = show_general_list_api(self.db)
		self.show_departments_api = show_departments_api(self.db)
		self.show_special_package_info_api = show_special_package_info_api(self.db)
		self.create_order_api = create_order_api(self.db)
		self.show_confirmation_info_api = show_confirmation_info_api(self.db)
		self.doctor_query_api = doctor_query_api(self.db)
		self.department_query_api = department_query_api(self.db)
		self.user_query_api = user_query_api(self.db)
		self.building_query_api = building_query_api(self.db)
		self.show_doctor_in_department_api = show_doctor_in_department_api(self.db)
		self.patients_query_api = patients_query_api(self.db)
		self.packages_query_api = packages_query_api(self.db)
		self.orders_query_api = orders_query_api(self.db)
		self.get_collection_pattern_api = get_collection_pattern_api(self.db)
		self.get_patient_orders_api = get_patient_orders_api(self.db)
		self.get_doctor_orders_api = get_doctor_orders_api(self.db)
		self.add_account_api = add_account_api(self.db)
		self.verify_password_api = verify_password_api(self.db)

	def incomplete_input(self, inputs) :
		check = False
		result = 'Incomplete input : '
		for input in inputs :
			if inputs[input] == None :
				check = True
				result += input + ', '
		if check :
			return check, result
		return check, 'Complete input'

	# time('ช่วงเช้า'  or 'ช่วงบ่าย'), gender('ชาย' or 'หญิง')
	def find_doctors(self, package_id=None, days=None, time=None, doctor_firstname=None, doctor_lastname=None, gender=None) :
		if package_id == None :
			return False, 'Incomplete input: package_id'
		return self.find_doctors_api.find_doctors(package_id,days,time,doctor_firstname,doctor_lastname,gender)

	def auto_find_doctors(self, package_id=None, user_id=None) :
		# use user_id in phase II
		return self.find_doctors(package_id=package_id)

	def show_profile(self, username=None) :
		check, result = self.incomplete_input(locals())
		if check : return True, result
		return self.show_profile_api.show_profile(username)

	def show_doctor_detail(self, doctor_id=None) :
		check, result = self.incomplete_input(locals())
		if check : return True, result
		return self.show_doctor_detail_api.show_doctor_detail(doctor_id)

	def edit_profile(self, username=None, email=None, telphone_number=None, emergency_phone=None, submit=False) :
		check, result = self.incomplete_input(locals())
		if check : return True, result
		return self.edit_profile_api.edit_profile(username,email,telphone_number,emergency_phone,submit)

	def register(self, username=None, patient_name_title=None, patient_name=None, patient_surname=None, 
		         patient_img=None, id_card_number=None, gender=None, birthday_year=None, 
		         birthday_month=None, birthday_day=None, blood_group_abo=None, blood_group_rh=None, race=None, 
		         nationallity=None, religion=None, status=None, patient_address=None, occupy=None, 
		         telephone_number=None, father_name=None, mother_name=None, emergency_name=None, 
		         emergency_phone=None, emergency_address=None, email=None, congenital_disease=None, submit=False) :
		check, result = self.incomplete_input(locals())
		if check : return True, result
		return self.register_api.register(username, patient_name_title, patient_name, patient_surname, patient_img, id_card_number, gender,
					 birthday_year, birthday_month, birthday_day, blood_group_abo, blood_group_rh, race, nationallity,
					 religion, status, patient_address, occupy, telephone_number, father_name, mother_name, emergency_name,
					 emergency_phone, emergency_address, email, congenital_disease, submit)

	def show_general_list(self) :
		return self.show_general_list_api.show_general_list()

	def show_departments(self) :
		return self.show_departments_api.show_departments()

	def show_special_package_info(self, package_id=None) :
		check, result = self.incomplete_input(locals())
		if check : return True, result
		return self.show_special_package_info_api.show_special_package_info(package_id)

	def show_confirmation_info(self,package_id=None, doctor_id=None, username=None, time=None) :
		check, result = self.incomplete_input(locals())
		if check : return True, result
		return self.show_confirmation_info_api.show_confirmation_info(package_id, doctor_id, username, time)

	def create_order(self,package_id=None, doctor_id=None, patient_id=None, notice='', time=None) :
		check, result = self.incomplete_input(locals())
		if check : return True, result
		return self.create_order_api.create_order(package_id, doctor_id, patient_id, notice, time)

###############

	def show_doctor_in_department(self) :
		return self.show_doctor_in_department_api.show_doctor_in_department()

	def get_all_doctors(self) :
		return self.doctor_query_api.get_all_doctors()

	def get_doctor_detail(self,doctor_id=None) :
		check, result = self.incomplete_input(locals())
		if check : return True, result
		return self.doctor_query_api.get_doctor_detail(doctor_id)

	def get_all_doctors_name(self) :
		return self.doctor_query_api.get_all_doctors_name()

	def update_doctor_profile(self, doctor_id=None, doctor_name_title=None, doctor_name=None,
							  doctor_surname=None, gender=None, birthday=None, office_phone_number=None,
							  email=None, department_id=None, doctor_img=None, position=None,
		                      expertises=None, educations=None, language=None, working_time=None, order_ids=None) :
		check, result = self.incomplete_input(locals())
		if check : return True, result
		return self.doctor_query_api.update_doctor_profile(doctor_id, doctor_name_title, doctor_name,
							  doctor_surname, gender, birthday, office_phone_number, email, department_id,
							  doctor_img, position, expertises, educations, language, working_time, order_ids)

	def delete_doctor(self, doctor_id=None) :
		check, result = self.incomplete_input(locals())
		if check : return True, result
		return self.delete_doctor(self, doctor_id)

	def insert_doctor(self, doctor_name_title=None, doctor_name=None, doctor_surname=None, gender=None,
		   birthday=None, office_phone_number=None, email=None, department_id=None, doctor_img=None,
		   position=None, expertises=None, educations=None, language=None, working_time=None) :
		check, result = self.incomplete_input(locals())
		if check : return True, result
		return self.doctor_query_api.insert_doctor(doctor_name_title, doctor_name, doctor_surname, gender,
		   birthday, office_phone_number, email, department_id, doctor_img,
		   position, expertises, educations, language, working_time)

###############

	def get_all_departments(self) :
		return self.department_query_api.get_all_departments()

	def get_department_detail(self,department_id=None) :
		check, result = self.incomplete_input(locals())
		if check : return True, result
		return self.department_query_api.get_department_detail(department_id)

	def get_all_departments_name(self) :
		return self.department_query_api.get_all_departments()

	def update_department_profile(self, department_id=None, department_name=None, department_description=None) :
		check, result = self.incomplete_input(locals())
		if check : return True, result
		return self.department_query_api.update_department_profile(department_id, department_name, department_description)

	def delete_department(self, department_id=None) :
		check, result = self.incomplete_input(locals())
		if check : return True, result
		return self.department_query_api.delete_department(department_id)

	def insert_department(self, department_name=None, department_description=None) :
		check, result = self.incomplete_input(locals())
		if check : return True, result
		return self.department_query_api.insert_department(department_name,department_description)

###############

	def get_all_users(self) :
		return self.user_query_api.get_all_users()

	def get_user_detail(self,user_id=None) :
		check, result = self.incomplete_input(locals())
		if check : return True, result
		return self.user_query_api.get_user_detail(user_id)

	def get_all_users_name(self) :
		return self.user_query_api.get_all_users()

	def update_user_profile(self, username=None, password=None) :
		check, result = self.incomplete_input(locals())
		if check : return True, result
		return self.user_query_api.update_user_profile(username, password)

	def delete_user(self, username=None) :
		check, result = self.incomplete_input(locals())
		if check : return True, result
		return self.user_query_api.delete_user(username)

#############

	def get_all_buildings(self) :
		return self.building_query_api.get_all_buildings()

	def get_building_detail(self) :
		return self.building_query_api.get_building_detail()

	def get_all_buildings_name(self) :
		return self.building_query_api.get_all_buildings()

	def update_building_profile(self, building_id=None, building_name=None) :
		check, result = self.incomplete_input(locals())
		if check : return True, result
		return self.building_query_api.update_building_profile(building_id, building_name)

	def delete_building(self, building_id=None) :
		check, result = self.incomplete_input(locals())
		if check : return True, result
		return self.building_query_api.delete_building(building_id)

	def insert_building(self, building_name=None) :
		check, result = self.incomplete_input(locals())
		if check : return True, result
		return self.building_query_api.insert_building(building_name)

#############

	def get_all_patients(self) :
		return self.patients_query_api.get_all_patients()

	def get_patients_detail(self,username=None) :
		check, result = self.incomplete_input(locals())
		if check : return True, result
		return self.patients_query_api.get_patients_detail(username)

	def get_all_patients_name(self) :
		return self.patients_query_api.get_all_patients_name()

	def update_patient_profile(self, username=None, patient_name_title=None, patient_name=None, 
		                       patient_surname=None, patient_img=None, id_card_number=None, gender=None,
                 		       birthday_year=None, birthday_month=None, birthday_day=None, 
                 		       blood_group_abo=None, blood_group_rh=None, race=None, nationallity=None,
				 		       religion=None, status=None, patient_address=None, occupy=None, telephone_number=None, 
				 		       father_name=None, mother_name=None, emergency_name=None,
				 		       emergency_phone=None, emergency_address=None, email=None, congenital_disease=None) :
		check, result = self.incomplete_input(locals())
		if check : return True, result
		return self.patients_query_api.update_patient_profile(username, patient_name_title, patient_name, 
			   patient_surname, patient_img, id_card_number, gender, birthday_year, birthday_month, 
			   birthday_day, blood_group_abo, blood_group_rh, race, nationallity, religion, status, 
			   patient_address, occupy, telephone_number, father_name, mother_name, emergency_name, 
			   emergency_phone, emergency_address, email, congenital_disease)

	def delete_patient(self, username=None) :
		check, result = self.incomplete_input(locals())
		if check : return True, result
		return self.patients_query_api.delete_patient(username)

	def insert_patient(self, username=None, patient_name_title=None, patient_name=None, patient_surname=None, 
		               patient_img=None, id_card_number=None, gender=None, order_ids=None, birthday_year=None, 
		               birthday_month=None, birthday_day=None, blood_group_abo=None, blood_group_rh=None, race=None, 
		               nationallity=None, religion=None, status=None, patient_address=None, occupy=None, 
		               telphone_number=None, father_name=None, mother_name=None, emergency_name=None,
				 	   emergency_phone=None, emergency_address=None, email=None, congenital_disease=None) :
		check, result = self.incomplete_input(locals())
		if check : return True, result
		return self.patients_query_api.insert_patient(username, patient_name_title, patient_name, patient_surname, patient_img,
			   id_card_number, gender, order_ids, birthday_year, birthday_month, birthday_day, blood_group_abo,
			   blood_group_rh, race, nationallity, religion, status, patient_address, occupy, telphone_number,
			   father_name, mother_name, emergency_name, emergency_phone, emergency_address, email, congenital_disease)

	def check_already_used_this_username(self, username=None) :
		check, result = self.incomplete_input(locals())
		if check : return True, result
		return self.patients_query_api.check_already_used_this_username(username)
#############

	def get_all_packages(self) :
		return self.packages_query_api.get_all_packages()

	def get_package_detail(self,package_id=None) :
		check, result = self.incomplete_input(locals())
		if check : return True, result
		return self.packages_query_api.get_package_detail(package_id)

	def get_all_packages_name(self) :
		return self.packages_query_api.get_all_packages_name()

	def update_package(self, package_id=None, package_name=None, package_cost=None, department_id=None, 
		               description=None, conditions=None, package_notice=None, building_id=None) :
		check, result = self.incomplete_input(locals())
		if check : return True, result
		return self.packages_query_api.update_package(package_id, package_name, package_cost, department_id, description, conditions, package_notice, building_id)

	def delete_package(self, package_id=None) :
		check, result = self.incomplete_input(locals())
		if check : return True, result
		return self.packages_query_api.delete_package(package_id)

	def insert_package(self,package_id=None, package_name=None,  package_cost=None, department_id=None, 
		               description=None, conditions=None, package_notice=None, building_id=None) :
		check, result = self.incomplete_input(locals())
		if check : return True, result
		return self.packages_query_api.insert_package(package_id, package_name,  package_cost, department_id, description, conditions, package_notice, building_id)

#############

	def get_all_orders(self) :
		return self.orders_query_api.get_all_orders()

	def get_order_detail(self,order_id=None) :
		check, result = self.incomplete_input(locals())
		if check : return True, result
		return self.orders_query_api.get_order_detail(order_id)

	def get_all_orders_with_package_and_user(self) :
		return self.orders_query_api.get_all_orders_with_package_and_user()

	def update_order(self, order_id=None, package_id=None, doctor_id=None, username=None, notice=None, cost=None, 
		             time=None) :
		check, result = self.incomplete_input(locals())
		if check : return True, result
		return self.orders_query_api.update_order(order_id, package_id, doctor_id, username, notice, cost, time)

	def delete_order(self, order_id=None) :
		check, result = self.incomplete_input(locals())
		if check : return True, result
		return self.orders_query_api.delete_order(order_id)

	#input: order_id(str), package_id(str), doctor_id(str), username(str), notice,(str) cost(double), time(object)
	# def create_order(self, order_id = None, package_id = None, doctor_id = None, username = None, notice = None, cost = None, time = None) :
	# 	return self.orders_query_api.create_order(order_id, package_id, doctor_id, username, notice, cost, time)

#############

	def get_all_collections_name(self) :
		return True, self.db.collection_names()

	def get_collection_pattern(self, collection_name=None) :
		check, result = self.incomplete_input(locals())
		if check : return True, result
		return self.get_collection_pattern_api.get_collection_pattern(collection_name)

	def get_patient_orders(self, patient_username) :
		check, result = self.incomplete_input(locals())
		if check : return True, result
		return self.get_patient_orders_api.get_patient_orders(patient_username)

	def get_doctor_orders(self, doctor_username) :
		check, result = self.incomplete_input(locals())
		if check : return True, result
		return self.get_doctor_orders_api.get_doctor_orders(doctor_username)

	def add_account(self, username, password) :
		check, result = self.incomplete_input(locals())
		if check : return True, result
		return self.add_account_api.add_account(username, password)

	def verify_password(self, username, password) :
		check, result = self.incomplete_input(locals())
		if check : return True, result
		return self.verify_password_api.verify_password(username, password)
