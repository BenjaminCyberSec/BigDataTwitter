# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 17:45:01 2021

@author: Bergé Benjamin, Wathelet Jolan, Anicet
"""


import sqlite3
from load_db import gen_database
from gen_dataset import gen_target_array
from sklearn.model_selection import KFold
import numpy as np
from eval import Eval

from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn import neighbors
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import os
from utils import *
from tsne import *




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
        cur.execute("SELECT statuses_count,followers_count, friends_count, favourites_count FROM users WHERE id = ?;", (uid,))
        row = cur.fetchone()
        result = []
        for i in range(0,3):
            if row[i] != None:
                result.append(row[i])
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

    # evaluator = Eval(bas_training, bas_target)
    # print(evaluator.svm())
    # print(evaluator.tree())
    # print(evaluator.forest())
    # print(evaluator.linear_regression())
    # #print(evaluator.neighbors()) bug
    # print(evaluator.adaBoost())

    #Algorithme KNN
    print(bas_uid.shape)
    xtrain, xtest, ytrain, ytest = train_test_split(bas_training, bas_target, train_size=0.8)



    neigh = KNeighborsClassifier()
    neigh.fit(xtrain, ytrain)

    print(ytest)
    print("######################################################################")
    print(neigh.predict(xtest))

    evaluator = Eval(neigh.predict(xtest), ytrain)
    print(evaluator.svm())







    
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
    