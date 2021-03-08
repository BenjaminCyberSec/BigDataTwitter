# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 14:46:58 2021

@author: Bergé Benjamin, Wathelet Jolan, Anicet
"""

import csv
import numpy as np
import random
import os

"""
Creates two tables: array_uid, array_target to associate an uid to a target value (shared index)
arg:
    target value: equals 1 if the uid belongs to a human, equals 0 otherwise
"""
def to_target_array(filename, target_value):
    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader((line.replace('\0','') for line in csvfile), delimiter=',')
        array_target = []
        array_uid = []
        for row in reader:
            array_uid.append(row[0])
            array_target.append(target_value)
    return array_uid[1:], array_target[1:] #retire titres

"""
Generates training data sets described in the study.
Creates two tables for each data set: array_uid, array_target to associate an uid to a target value (shared index)

Note: there are 1950 humans and 1950 bots

@returns bas_uid, bas_target: only the base dataset is returned as others were not needed so far
"""
def gen_target_array():
    #Human
    e13_uid, e13_target = to_target_array('E13'+os.sep+'users.csv',1)
    tfp_uid, tfp_target  = to_target_array('TFP'+os.sep+'users.csv',1)
    merged_uid = np.concatenate((e13_uid, tfp_uid))
    merged_target = np.concatenate((e13_target, tfp_target))
    hum_uid = merged_uid #il y en a 1952 dans le set 
    hum_target = merged_target
    #Fake
    fsf_uid, fsf_target = to_target_array('FSF'+os.sep+'users.csv',0)
    int_uid, int_target = to_target_array('INT'+os.sep+'users.csv',0)
    twt_uid, twt_target = to_target_array('TWT'+os.sep+'users.csv',0)
    merged_uid = np.concatenate((fsf_uid, int_uid,twt_uid))
    merged_target = np.concatenate((fsf_target, int_target,twt_target))
    #fak_u = random.sample(list(temp), 1950)
    fak_uid, fak_target = zip(*random.sample(list(zip(merged_uid, merged_target)), 1950))
    #Training sample
    bas_uid = np.concatenate((hum_uid, fak_uid))
    bas_target = np.concatenate((hum_target, fak_target))
    
    return bas_uid, bas_target