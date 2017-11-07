# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append('../')
sys.path.append('../../..')
from API import API
from pprint import pprint
from datetime import datetime


### error below here ###
api = API()

#test add_account()
status, result = api.add_account('mindy', 'jirateepy')


def multiply (a, b) :
    return a*b

class TestUM(unittest.TestCase) :

    def setUp(self) :
        pass

    def test_numbers_3_4(self) :
        self.assertEqual( multiply(3,4), 12)
        print ('test_numbers_3_4 : success')

    def test_strings_a_3(self) :
        self.assertEqual( multiply('a',3), 'aaa')
        print ('test_numbers_a_3 : success')

    def test_json(self) :
        dict_test = {'a':1, 'b':2}
        list_key = []
        for k in dict_test : list_key.append(k)
        self.assertEqual( sorted(list_key) , sorted(['b','a']))
        print ('test_json : success')

if __name__ == '__main__' :
    unittest.main()

'''
dict_test = {'a':1, 'b':2}
list_key = []
print (dict_test)
for k in dict_test : list_key.append(k)
print (list_key
'''
