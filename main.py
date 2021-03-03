# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 17:45:01 2021

@author: Bergé Benjamin, Wathelet Jolan, Anicet
"""

import csv
import numpy as np
import random
import sqlite3
from sklearn import tree
import matplotlib.pyplot as plt
from load_db import gen_database


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

@returns bas_uid, bas_target: only the base dataset is returned as others were not needed so far
"""
def gen_target_array():
    #Human
    e13_uid, e13_target = to_target_array('E13\\users.csv',1)
    tfp_uid, tfp_target  = to_target_array('TFP\\users.csv',1)
    merged_uid = np.concatenate((e13_uid, tfp_uid))
    merged_target = np.concatenate((e13_target, tfp_target))
    hum_uid = merged_uid[:-2] #il y en a 1952 dans le set 
    hum_target = merged_target[:-2]
    #Fake
    fsf_uid, fsf_target = to_target_array('FSF\\users.csv',0)
    int_uid, int_target = to_target_array('INT\\users.csv',0)
    twt_uid, twt_target = to_target_array('TWT\\users.csv',0)
    merged_uid = np.concatenate((fsf_uid, int_uid,twt_uid))
    merged_target = np.concatenate((fsf_target, int_target,twt_target))
    #fak_u = random.sample(list(temp), 1950)
    fak_uid, fak_target = zip(*random.sample(list(zip(merged_uid, merged_target)), 1950))
    #Training sample
    bas_uid = np.concatenate((hum_uid, fak_uid))
    bas_target = np.concatenate((hum_target, fak_target))
    return bas_uid, bas_target

"""
Returne a table witch, foreach uid, list the features described in the study in numerical format
    the table matches the index of base_uid and base_target
    format: [[0,1,0][1,1,1]]
"""
def gen_training_features(cur,bas_uid):
    #has_name, has_image, has_address
    results = []
    for uid in bas_uid:
        cur.execute("SELECT id,name, profile_use_background_image, location FROM users WHERE id = ?;", (uid,))
        row = cur.fetchone()
        result = []
        for i in range(0,3):
            if row[i] != None:
                result.append(1)
            else:
                result.append(0)
        results.append(result)
    return results

if __name__ == "__main__":
    con = sqlite3.connect("db.sqlite")
    cur = con.cursor()
    
    #gen database can be commented if the database has already been created, code is in another file
    gen_database(con)
    
    bas_uid, bas_target = gen_target_array()
    bas_training = gen_training_features(cur, bas_uid)
    
  
    clf = tree.DecisionTreeClassifier(criterion='entropy', min_impurity_decrease=0.03)
    clf = clf.fit(bas_training, bas_target)
    #/!\ il faut changer pour utiliser des valeurs de test, là j'utilise les même data
        # #porcent_of_success = clf.score(data.get('test'), data.get('test_target'))
    porcent_of_success = clf.score(bas_training, bas_target)
    tree.plot_tree(clf.fit(bas_training,  bas_target)) #build the tree   
    
    con.close()
    
"""
Syntaxe:
    pour parcourir deux listes dont l'indexe correspond: for uid, target in zip(bas_uid, bas_target):

Possible amélioration:
    pour gen features, store les queries: 
            https://stackoverflow.com/questions/30218963/storing-sql-statements-in-a-properties-file-to-be-used-by-python-scripts/30219756
            
Doc:
    https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
    
Anaconda:
    To see the plot, look at the square on the top right corner and select "plots" view instead of "help"
"""
    