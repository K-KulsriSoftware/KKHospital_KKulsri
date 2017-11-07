# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append('../')
sys.path.append('../../..')
from API import API
from pprint import pprint
from datetime import datetime


api = API()

list_result = ['username',
'patient_name_title',
'patient_name',
'patient_surname',
'patient_img',
'id_card_number',
'gender',
'birthday',
'blood_group_abo',
'blood_group_rh',
'race',
'nationallity',
'religion',
'status',
'patient_address',
'occupy',
'telephone_number',
'father_name',
'mother_name',
'emergency_name',
'emergency_phone',
'emergency_address',
'email',
'congenital_disease']

class TestUM(unittest.TestCase) :

    def setUp(self) :
        pass

    def test_show_profile_exist_user(self) :
        status, result = api.show_profile(username='jirateep')
        list_key = []
        for k in result : list_key.append(k)
        self.assertEqual( status ,True )
        self.assertEqual( sorted(list_key) , sorted(list_result))
        print ('test_show_profile_exist_use : success')

    def test_show_profile_non_exist_user(self) :
        status, result = api.show_profile(username='ekeeeekeekee')
        self.assertEqual( status , False)
        self.assertEqual( result , 'No Profile')
        print ('test_show_profile_non_exist_use : success')

    def test_show_profile_no_input(self) :
        status, result = api.show_profile()
        self.assertEqual( status ,True )
        self.assertEqual( result , 'Incomplete input : username, ')

if __name__ == '__main__' :
    unittest.main()
