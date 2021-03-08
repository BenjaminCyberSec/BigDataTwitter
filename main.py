# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 17:45:01 2021

@author: Bergé Benjamin, Wathelet Jolan, Anicet
"""


import sqlite3
from load_db import gen_database
from gen_dataset import gen_target_array
from eval import Eval
import sys
import test_utils




"""
Returne a table witch, foreach uid, list the features described in the study in numerical format
    the table matches the index of base_uid and base_target
    format: [[0,1,0][1,1,1]]
"""
def gen_training_features(cur,bas_uid):
    ########
    # TODO
    #######
    
    #has_name, has_image, has_address
    results = []
    for uid in bas_uid:
        cur.execute("SELECT id, name, profile_use_background_image, location, description, url, listed_count, followers_count, statuses_count, friends_count FROM users WHERE id = ?;", (uid,))
        row = cur.fetchone()
        result = []

        #Camisani-Calzolari
        # Has a name ?  
        """ Ils ont tous un nom
        if row[1] != None:
            result.append(1)
        else:
            result.append(0)
        """
        # Has a background_image ?   
        if row[2] != None:
            result.append(1)
        else:
            result.append(0)
        # Has a location
        if row[3] != None:
            result.append(1)
        else:
            result.append(0)
        # Has a description (bio)
        if row[4] != None:
            result.append(1)
        else:
            result.append(0)
        # Has a url
        if row[5] != None:
            result.append(1)
        else:
            result.append(0)
        # Is in a list
        if row[6] != 0:
            result.append(1)
        else:
            result.append(0)
        # Has 30 follower or more
        if row[7] >= 30:
            result.append(1)
        else:
            result.append(0)
        # Has 50 tweet or more
        if row[8] >= 50:
            result.append(1)
        else:
            result.append(0)
        # Has at least twice the number of follower as friends
        if row[7] * 2 >= row[9]:
            result.append(1)
        else:
            result.append(0)
            

        #State of search
        #

        #Socialbakers

        #Stringhini et al.
        #Number of follower
        #result.append(row[7])
        #Number of tweet
        #result.append(row[8])
        #Yang et al.
        #Added features
        
        results.append(result)
    return results
        
    
if __name__ == "__main__":
    con = sqlite3.connect("db.sqlite")
    cur = con.cursor()
    
    #gen database can be commented if the database has already been created, code is in another file
    #gen_database(con)
    
    bas_uid, bas_target = gen_target_array()
    bas_training = gen_training_features(cur, bas_uid)
    

    
    #test_utils.print_data_sets(bas_training,bas_target)
    test_utils.eval_useful(9-1, bas_training)
    
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
    
    """
    Résultat KO (voir featurs, voir algo parameter, voir concatenation & score)
        0.5210394832245732
        0.5002570694087403
        0.5210394832245732
        0.5210394832245732
        0.5210394832245732
    """
    
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
    