#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime
from bson.objectid import ObjectId
class create_order_api :

    def __init__(self, db) :
        self.db = db

    def get_package_cost(self,package_id) :
        cursor = self.db.packages.aggregate([
            {
                '$match' : 
                {
                    '_id' : ObjectId(package_id)
                }
            },
            {
                '$project' : 
                {
                    'package_cost' : '$package_cost'
                }
            },
        ])
        for temp in cursor:
            return True, temp['package_cost']
        return False, 'patient error'

    def find_bought_time(self) :
        time = datetime.now()
        year = int(time.strftime('%Y'))
        month = int(time.strftime('%m'))
        date = int(time.strftime('%d'))
        hr = int(time.strftime('%H'))
        min = int(time.strftime('%M'))
        return {'year' : year, 'month' : month, 'date' : date, 'hr' : hr, 'min' : min}

    def get_patient_id(self, patient_username):
        cursor = self.db.patients.aggregate([
            {
                '$match' : 
                {
                    'username' : patient_username
                }
            },
            {
                '$project' : 
                {
                    'patient_id' : '$_id'
                }
            },
        ])
        for temp in cursor:
            return True, temp['patient_id']
        return False, 'patient error'
    
    def insert_query(self, package_id, doctor_id, patient_id, package_cost, notice, time, bought_time) :
        self.db.orders.insert(
            {
                'package_id' : ObjectId(package_id),
                'doctor_id' : ObjectId(doctor_id),
                'patient_id' : patient_id,
                'cost' : package_cost,
                'time' : 
                {
                    'start' : datetime(time['year'], time['month'], time['date'], time['start_hr'], 0),
                    'finish' : datetime(time['year'], time['month'], time['date'], time['finish_hr'], 0)
                },
                'bought_time' : datetime(bought_time['year'], bought_time['month'], bought_time['date'], bought_time['hr'], bought_time['min']),
                'notice' : notice
            }
        )

    def create_order(self, package_id, doctor_id, patient_username, notice, time) :
        bought_time = self.find_bought_time()
        check_patient, patient_id = self.get_patient_id(patient_username)
        check_package, package_cost = self.get_package_cost(package_id)
        if check_package and check_patient :
            self.insert_query(package_id, doctor_id, patient_id, package_cost, notice, time, bought_time)
            return True, 'Successfully Added'
        else :
            return False, 'No patient or package'