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


class TestUM(unittest.TestCase) :

    def setUp(self) :
        pass

    #### if username already_used this test_case will fail. Be sure that add new_user ##
    def test_add_new_user_with_username_passwd(self) :
        status, result = api.add_account('mindy', 'jirateepy')
        self.assertEqual( status, True)
        print ('test_add_new_user_with_username_passwd : success')

    '''
    def test_add_new_user_with_only_username(self) :
       try :
           status, result = api.add_account('mindddd')
       except TypeError:
           status = False
           result = 'error parameter
    '''
    '''
    def test_strings_a_3(self) :
        self.assertEqual( multiply('a',3), 'aaa')
        print ('test_numbers_a_3 : success')

    def test_json(self) :
        dict_test = {'a':1, 'b':2}
        list_key = []
        for k in dict_test : list_key.append(k)
        self.assertEqual( sorted(list_key) , sorted(['b','a']))
        print ('test_json : success')
    '''

