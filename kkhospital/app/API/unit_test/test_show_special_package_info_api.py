# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append('../')
sys.path.append('../../..')
from API import API
from pprint import pprint
from datetime import datetime


api = API()

list_result = ['package_name',
'package_cost',
'description',
'conditions',
'package_notice',
'building_name',
'_id']

class TestUM(unittest.TestCase) :

    def setUp(self) :
        pass

    def test_show_special_package_info_exist_package(self) :
        status, result = api.show_special_package_info(package_id='59d8946b7434c9e2a98088ed')
        list_key = []
        for k in result :
            print(k)
            list_key.append(k)
        self.assertEqual( status ,True )
        self.assertEqual( sorted(list_key) , sorted(list_result))
        print ('test_show_special_package_info_exist_use : success')

    def test_show_special_package_info_non_exist_package(self) :
        status, result = api.show_special_package_info(package_id='5555946b7434c9e2a98088ed')
        self.assertEqual( status , False)
        self.assertEqual( result , 'No package')
        print ('test_show_special_package_info_non_exist_use : success')

    def test_show_special_package_info_no_input(self) :
        status, result = api.show_special_package_info()
        self.assertEqual( status ,True )
        self.assertEqual( result , 'Incomplete input : package_id, ')
        print ('test_show_special_package_info_no_input : success')

if __name__ == '__main__' :
    unittest.main()
