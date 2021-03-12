# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 17:45:01 2021

@author: Bergé Benjamin, Wathelet Jolan, Anicet
"""

import sqlite3

from features import select_features, feature_A_CAMISANI_CALZOLARI
from gen_dataset import gen_target_array
from eval import Eval
from visualisation import save_results
from load_db import gen_database
import sys
import test_utils
from evaluation_tables import evaluating_features_foreach_author




"""
Returne a table witch, foreach uid, list the features described in the study in numerical format
    the table matches the index of base_uid and base_target
    format: [[0,1,0][1,1,1]]
"""



def gen_training_features(cur, bas_uid, specific_feature):
    results = []

    for uid in bas_uid:

        cur.execute(select_features(specific_feature), (uid,))
        row = cur.fetchone()
        result = []

        for key, value in feature_A_CAMISANI_CALZOLARI(row).items():
            result.append(value)

        results.append(result)
    return results




def printing_table_16(bas_uid, bas_target, cur):
    features = ['name', 'profile_use_background_image', 'location', 'description', 'url', 'listed_count', 'followers_count', 'statuses_count', 'friends_count']
    bas_training = gen_training_features(cur, bas_uid, features)
    evaluator = Eval(bas_training, bas_target)
    
    print("svm")
    print(evaluator.svm())
    print("tree")
    print(evaluator.tree())
    print("forest")
    print(evaluator.forest())
    print("linear_regression")
    print(evaluator.linear_regression())
    
    """
    c'est cassé pour l'instant
    print("neighbors")
    print(evaluator.neighbors()) 
    """
    print("adaBoost")
    print(evaluator.adaBoost())

if __name__ == "__main__":
    con = sqlite3.connect("db.sqlite")
    cur = con.cursor()
    #/!\ do not remove this line, it builds the db
    #gen_database(con)
    bas_uid, bas_target = gen_target_array()
    
    #evaluating_features_foreach_author(bas_uid, bas_target, cur, ['svm', 'tree', 'forest', 'linear_regression', 'neighbors', 'adaBoost'],'SaveResult','results_evaluator.txt')
    
    printing_table_16(bas_uid, bas_target, cur)
    
    con.close()


