# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append('../')
sys.path.append('../../..')
from API import API
from pprint import pprint
from datetime import datetime


api = API()

list_result = ['package_list',
'department_name',
'department_id']

class TestUM(unittest.TestCase) :

    def setUp(self) :
        pass

    def test_show_departments(self) :
        status, result = api.show_departments()
        list_key = []
        for k in result :
            list_key.append(k)
        self.assertEqual( status ,True )
        self.assertEqual( sorted(list_key[0]) , sorted(list_result))

if __name__ == '__main__' :
    unittest.main()
