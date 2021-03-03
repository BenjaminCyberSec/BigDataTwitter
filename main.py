# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 17:45:01 2021

@author: Bergé Benjamin, Wathelet Jolan, Anicet
"""


import sqlite3
from sklearn import tree
from load_db import gen_database
from gen_dataset import gen_target_array

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
    