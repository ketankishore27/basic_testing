# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 17:03:27 2020

@author: Ketan Kishore
"""

import unittest
from initial_code import *

class TestCalc(unittest.TestCase):
    
    
    def setUp(self):
        
        """Sets up the environment before each unit test is to be executed. Currently doing nothing.
           But can be used later"""
        pass
    
    def tearDown(self):

        """Sets up the environment before each unit test is to be executed. Currently doing nothing.
           But can be used later"""
        pass
    
    
    def test_validate_data_source(self):
        
        # Check if the file provided is csv or not. Else it would crash the program
        self.assertEqual(validate_data_source(), 'csv')
       
    def test_data_sources(self):
        
        # checks for the expected data type which is present in the data file and matches with the expected
        self.assertEqual(id_check(), 'int64')
        self.assertEqual(name_check(), 'object')
        self.assertEqual(credit_check(), 'int64')
        self.assertEqual(geo_check(), 'object')
        self.assertEqual(gen_check(), 'object')
        self.assertEqual(age_check(), 'int64')
        self.assertEqual(tenure_check(), 'int64')
        self.assertEqual(bal_check(), 'float64')
        self.assertEqual(card_check(), 'int64')
        self.assertEqual(active_check(), 'float64')
        self.assertEqual(salary_check(), 'float64')
        
    def test_data_validity(self):
        
        # Checks for data validity. For Ex: Credit Score can never cross 999, or age can never be less than 0 etc.
        self.assertEqual(invalid_age_check(), 0)
        self.assertEqual(invalid_gender_check(), 2)
        self.assertEqual(check_for_missing_data(), 0)
        self.assertEqual(check_for_invalid_tenure(), 0)
        self.assertEqual(type(expect_calculation_result()), float)
        self.assertEqual(check_scaling(), 0)
        
    def test_datatype_after_computation(self):
        
        # Checks the data of newly computed column to check if it is desirable
        self.assertEqual(computation_check(), 'float64')
        
    def test_check_invalid_calculation(self):
        
        # Specifically checks for invalid division
        
        with self.assertRaises(ValueError):
            check_invalid_calculation()
            
        # self.assertEqual(check_invalid_calculation(), 'float64')
            
if __name__ == '__main__':
    unittest.main()