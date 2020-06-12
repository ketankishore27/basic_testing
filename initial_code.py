# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 16:08:07 2020

@author: Ketan
"""

import pandas as pd
import numpy as np

filename = 'Churn_Modelling.csv'

def validate_data_source():
    if filename.split('.')[1] == 'csv':
        return 'csv'
    else:
        return 'Other File format'
    
data = pd.read_csv(filename)

def id_check():
    return data['CustomerId'].dtype

def name_check():
    return data['Surname'].dtype

def credit_check():
    return data['CreditScore'].dtype

def geo_check():
    return data['Geography'].dtype

def gen_check():
    return data['Gender'].dtype

def age_check():
    return data['Age'].dtype

def tenure_check():
    return data['Tenure'].dtype

def bal_check():
    return data['Balance'].dtype

def product_check():
    return data['NumOfProducts'].dtype

def card_check():
    return data['HasCrCard'].dtype

def active_check():
    return data['Balance'].dtype

def salary_check():
    return data['Balance'].dtype

def invalid_credit_score_check():
    return ((data['CreditScore'] <= 0) | (data['CreditScore'] > 999)).sum()

def invalid_age_check():
    return ((data['Age'] <= 0) | (data['Age'] > 100)).sum()

def invalid_gender_check():
    return len(data['Gender'].unique())

def check_for_missing_data():
    return np.sum(data.isna().sum())

def check_for_invalid_tenure():
    return (data['Tenure'] < 0).sum()

def expect_calculation_result():
    
    """ I am just doing a random calculation and doing a sanity check whether the result i get 
        is of the same data type which i expect """
        
    return np.mean(data['CreditScore'])

def check_scaling():
    """ Suppose I do a scaling on one of the columns and want to check if the scaling 
        works as expected """
    
    from sklearn.preprocessing import MinMaxScaler
    scaled_credit_score = pd.Series(MinMaxScaler(feature_range = (1, 5)).fit_transform(np.array(data['CreditScore']).reshape(-1, 1)).squeeze())
    return ((1 >= scaled_credit_score) & (scaled_credit_score >= 5)).sum()

def computation_check():
    
    """Suppose I do some kind of Computation on Columnar level and wants to check if I get desired
       results"""
       
    random_computation = data['EstimatedSalary'] + data['Balance']
    return random_computation.dtype
    

def check_invalid_calculation():
    
    """ Checks for specific division done by 0 """
    
    if (data['Balance'] == 0).sum() > 0:
        raise ValueError(' You are about to divide a number by 0 ')
        
    random_division = data['EstimatedSalary'] / data['Balance']
    
    return random_division.dtype
