
# -*- coding: utf-8 -*-

from API import API
from pprint import pprint
from datetime import datetime

api = API()

#test find_doctors
#status, result = api.find_doctors(package_id="59d890e99cb6f0707faf7034")
#status, result = api.find_doctors(package_id='p00001',days=['mon'])
#status, result = api.find_doctors(package_id='p00001',days=['mon','tue'],time='ช่วงเช้า')
#status, result = api.find_doctors(package_id='p00001',days=['wed','sat'],time='ช่วงบ่าย',gender='ชาย')
#status, result = api.find_doctors(days=['wed','sat'],time='ช่วงบ่าย',gender='ชาย')
#status, result = api.find_doctors(package_id='p00001',days=['wed','sat'],time='ช่วงบ่าย',gender='ชาย')
#status, result = api.find_doctors(package_id='p00001',days=[],time='',gender='')

#test auto_find_doctors
#status, result = api.auto_find_doctors(package_id='p00001')

#test get_all_doctors
#status, result = api.get_all_doctors()

#test get_all_doctors_name
#status, result = api.get_all_doctors_name()

#test get_doctor_detail
#status, result = api.get_doctor_detail('d001')
#status, result = api.get_doctor_detail('d007')

#test  update_doctor
'''
status, result = api.update_doctor('d001', 'นายแพทย์', 'กนกพล', 'กุลศรี', 'True', datetime(1997,2,8,0,0),
										   '0856789012', 'palmpalm@gmail.com', 1, 'https://scontent.fbkk10-1.fna.fbcdn.net/v/t1.0-9/13907130_10205456063434894_2847443788461698332_n.jpg?oh=913be734de97d590b0db87f3ca219342&oe=5A83D820',
							 			   'แพทย์เชี่ยวชาญทางด้านดวงตาง', ['aaa', 'bbb'], ['กขค'], ['ไทย', 'เกาหลี'],
							  			   {"mon" : [{"start" : 9, "finish" : 10}, {"start" : 14, "finish" : 18}], "tue" : [{"start" : 9, "finish" : 10}]},
							               [])
'''

#test delete_doctor
#status, result = api.delete_doctor('d003')

#test insert_doctor
'''
working_time = {
					"mon" : [{"start" : 9, "finish" : 10}, {"start" : 14, "finish" : 18}],
					"tue" : [{"start" : 9, "finish" : 10}]
				}
birthday = datetime(1997,2,8,0,0)
language = ['ไทย', 'เกาหลี']
status, result = api.insert_doctor('นายแพทย์', 'นิติ', 'นานา', True, birthday, '0856789012', 'palmpalm@gmail.com',
								   2, 'https://scontent.fbkk10-1.fna.fbcdn.net/v/t1.0-9/13907130_10205456063434894_2847443788461698332_n.jpg?oh=913be734de97d590b0db87f3ca219342&oe=5A83D820',
							  	   'แพทย์เชี่ยวชาญทางด้านจิตวิทยา', ['om', 'บลาบลา'], ['กขค'], language,
							  	   working_time)
'''

#test get_all_collections_name
#status, result = api.get_all_collections_name()
#######Jakapong Mo START
#status, result = api.get_all_patients()

#test get_patients_detail
#status, result = api.get_patients_detail('admao')
#status, result = api.get_patients_detail('ukukukkkk')

#test get_all_patients_name
#status, result = api.get_all_patients_name()

#test  update_patients

'''
status, result = api.update_patient("watermelon", "นาง", "สมหญิง", "ชำนาญคอม", "img.html", "1309905889674", True, [], 1996,
							  1, 1, 1, 2, "ไทย", "ไทย", "พุทธ", 1, "37/16 สุขุมวิทย์ กทม", "โปรแกรมเมอร์", "0818453265",
							  "วิศรุต ชำนาญคอม", "วริศรา หล่อเภรี", "มหาอินทร์ การช่างเยี่ยม", "0845263254", "98/14 ทองหล่อ กทม",
							  "st@gmail.com", [])
'''
'''
status, result = api.update_patient("booktay", "นาย", "องเนียล", "คัง", "https://scontent.fbkk10-1.fna.fbcdn.net/v/t1.0-9/15726866_1370353863009540_4965290848458318950_n.jpg?oh=c044e7f534bde74389423b1f508fe367&oe=5A3B122E", "11002233004506", True, 1989,
							  12, 31, 1, 2, "ไทย", "ไทย", "พุทธ", 1, "37/16 สุขุมวิทย์ กทม", "นักศึกษา", "0881020304",
							  "คังแดเชียล", "อง ซองอู", "คิม แจฮวาน", "0845263254", "98/14 ทองหล่อ กทม",
							  "jaehwan@wannaone.th", [])
'''
#test delete_patient
#status, result = api.delete_patient(username='eiei')

#test insert_patient
'''
status, result = api.insert_patient("watermelon22", "นางสาว", "สมหญิง", "ชำนาญคอม", "img.html", "1309905889674", True, [], 1996,
							  1, 1, 1, 2, "ไทย", "ไทย", "พุทธ", 1, "37/16 สุขุมวิทย์ กทม", "โปรแกรมเมอร์", "0818453265",
							  "วิศรุต ชำนาญคอม", "วริศรา หล่อเภรี", "มหาอินทร์ การช่างเยี่ยม", "0845263254", "98/14 ทองหล่อ กทม",
							  "st@gmail.com", [])
'''

#####

#status, result = api.get_all_packages()

#test get_package_detail
#status, result = api.get_package_detail('p00001')
#status, result = api.get_package_detail()

#test get_all_packages_name
#status, result = api.get_all_packages_name()

#test  update_package

#status, result = api.update_package("p000099", "eiei", 1.1, 9, "-", [],"s", 1)
#status, result = api.update_package(package_id= "p000099", package_name = "eiei",  package_cost = 1.1, department_id = 99, description = "-", conditions = [], package_notice = "s", building_id= 1)
#status, result = api.update_package()
#test delete_package
#status, result = api.delete_package(package_id = "p000099")

#test insert_package
'''
status, result = api.insert_package(package_id= "p000099", package_name = "eiei", package_cost = 1.1,
									department_id = 99, description = "-", conditions = [], package_notice = "s", building_id= 1)
'''

#####

#status, result = api.get_all_orders()

#test get_order_detail
#status, result = api.get_order_detail('o000001')

#test get_all_orders_with_package_and_user
#status, result = api.get_all_orders_with_package_and_user()

#test  update_order
'''
status, result = api.update_order(order_id = "o0000099", package_id = "p0000999", doctor_id = "d0099", username = "99", notice = "9", cost = 9.9,
								time = {
				    	    		"year" : 2018,
									"date" : 13,
									"month" : 11,
									"start_hr" : 9,
									"finish_hr" : 10,
				    			} )
'''
#test delete_order
#status, result = api.delete_order(order_id = "o0000099")

#test insert_order
'''
status, result = api.create_order(order_id = 'o000001', package_id = 'p0000999', doctor_id = 'd0099', username = '99', notice = '9', cost = 9.9,
								time = {
				    	    		'year' : 2018,
									'date' : 13,
									'month' : 11,
									'start_hr' : 9,
									'finish_hr' : 10,
				    			} )
'''
#######Jakapong Mo END

#######Watcharachat Tay START
#test get_all_departments
#status, result = api.get_all_departments()

#test get_all_departments_name
#status, result = api.get_all_departments_name()

#test get_department_detail
#status, result = api.get_department_detail(1.0)
#status, result = api.get_department_detail(2.0)

#test  update_department_profile
#status, result = api.update_department_profile(department_id=None, department_name=None)
#status, result = api.update_department_profile(6.6, 'loltest')


#test delete_department
#status, result = api.delete_department(6.6)

#####

#test get_all_users
#status, result = api.get_all_users()

#test get_all_users_name
#status, result = api.get_all_users_name()

#test get_user_detail
#status, result = api.get_user_detail('ekekjubjub')
#status, result = api.get_user_detail('d001')

#test  update_user_profile
#status, result = api.update_user_profile(username=None, password=None)
#status, result = api.update_user_profile('testuser', 'loltest')


#test delete_user
#status, result = api.delete_user('testuser')

########

#test get_all_buildings
#status, result = api.get_all_buildings()

#test get_all_buildings_name
#status, result = api.get_all_buildings_name()

#test  update_building_profile

#status, result = api.update_building_profile(building_id=None, building_name=None)
#status, result = api.update_building_profile(9.9, 'loltest')

#test delete_building
#status, result = api.delete_building(9.9)

#test insert_building
#status, result = api.insert_building('อาคารออโทปิทิส')
#######Watcharachat Tay END

#test show_profile
#status, result = api.show_profile(username='ekekjubjub')

#test show_detail
#status, result = api.show_detail(doctor_name="จักรพงษ์", doctor_surname='คล้ายหนองสรวง')
#status, result = api.show_detail(doctor_name="Jackapong", doctor_surname='K.')

#test edit_profile
#status, result = api.edit_profile(username='admao',email="eiei@gmail.com", telphone_number="0923485995", emergency_phone="0653251554", submit=True)

#test register
'''
status, result = api.register("watermelon", "นางสาว", "สมหญิง", "ชำนาญคอม", "img.html", "1309905889674", True, [], 1996,
							  1, 1, 1, 2, "ไทย", "ไทย", "พุทธ", 1, "37/16 สุขุมวิทย์ กทม", "โปรแกรมเมอร์", "0818453265",
							  "วิศรุต ชำนาญคอม", "วริศรา หล่อเภรี", "มหาอินทร์ การช่างเยี่ยม", "0845263254", "98/14 ทองหล่อ กทม",
							  "st@gmail.com", [], True)
'''

#test show_general_list
#status,result = api.show_general_list()

#test show_departments
#status,result = api.show_departments()

#test show_special_package_info
#status,result = api.show_special_package_info('p00002')

#test create_order
'''
status,result = api.create_order('59d8bc02612d9a6b5fb41c33', '59d8ca694ddf3286ea4e5f4f', 'ongniel', 'test notice',
				{
    	    		'year' : 2018,
					'date' : 17,
					'month' : 12,
					'start_hr' : 9,
					'finish_hr' : 10,
    			})
'''

#test show_confirmation_info
'''
status,result = api.show_confirmation_info('59d8946b7434c9e2a98088ed','d0001', 'jirateep',
				{
    	    		'year' : 2017,
					'date' : 12,
					'month' : 11,
					'start_hr' : 9,
					'finish_hr' : 10,
    			})
'''

#test get_collection_pattern
#status, result = api.get_collection_pattern('doctors')

#test show_doctor_in_department()
#status, result = api.show_doctor_in_department()

#test get_patient_orders()
#status, result = api.get_patient_orders('ongniel')

#test get_doctor_orders()
#status, result = api.get_doctor_orders('d0006')

#test add_account()
#status, result = api.add_account('mind', 'jirateep')

#test verify_password()
#status, result = api.verify_password('mind', '5555')
#status, result = api.verify_password('mind', 'jirateep')

if status :
	pprint(result)
else :
	print('ERROR: ' + result)
