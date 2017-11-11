# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append('../')
sys.path.append('../../..')
from API import API
from pprint import pprint
from datetime import datetime

api = API()

list_result = ['package_id',
'package_name',
'package_cost',
'description']

class TestUM(unittest.TestCase) :

    def setUp(self) :
        pass

    def test_show_general_list_exist(self) :
        status, result = api.show_general_list()
        list_key0 = []
        list_key1 = []
        list_key2 = []
        for k in result[0] : list_key0.append(k)
        for k in result[1] : list_key1.append(k)
        for k in result[2] : list_key2.append(k)
        self.assertEqual( status ,True )
        self.assertEqual( sorted(list_key0) , sorted(list_result))
        self.assertEqual( sorted(list_key1) , sorted(list_result))
        self.assertEqual( sorted(list_key2) , sorted(list_result))
        print ('test_show_general_list_exist_use : success')

if __name__ == '__main__' :
    unittest.main()
