# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append('../')
sys.path.append('../../..')
from API import API
from pprint import pprint
from datetime import datetime


api = API()

list_result = [
    {'package_cost', 'package_name'},
    {'_id','doctor_name','doctor_name_title','doctor_surname','office_phone_number'},
    {'_id','patient_name','patient_name_title','patient_surname'},
    {'date', 'finish_hr', 'month', 'start_hr', 'year'}]

class TestUM(unittest.TestCase) :

    def setUp(self) :
        pass

    def test_show_confirmation_info(self) :
        status, result = api.show_confirmation_info('59d8946b7434c9e2a98088ed','d0001', 'jirateep',
				{
    	    		'year' : 2017,
					'date' : 12,
					'month' : 11,
					'start_hr' : 9,
					'finish_hr' : 10,
    			})
        list_key = []
        for k in result : list_key.append(k)
        self.assertEqual( status ,True )
        self.assertEqual( sorted(list_key[0]) , sorted(list_result[0]))
        print ('test_show_confirmation_info(package) : success')
        self.assertEqual( sorted(list_key[1]) , sorted(list_result[1]))
        print ('test_show_confirmation_info(doctor) : success')
        self.assertEqual( sorted(list_key[2]) , sorted(list_result[2]))
        print ('test_show_confirmation_info(patient) : success')
        self.assertEqual( sorted(list_key[3]) , sorted(list_result[3]))
        print ('test_show_confirmation_info(time) : success')

if __name__ == '__main__' :
    unittest.main()
