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
import sys
import test_utils




"""
Returne a table witch, foreach uid, list the features described in the study in numerical format
    the table matches the index of base_uid and base_target
    format: [[0,1,0][1,1,1]]
"""
class_and_author = {
    'A': {'CAMISANI_CALZOLARI':['name', 'profile_use_background_image', 'location', 'description', 'url', 'listed_count', 'followers_count', 'statuses_count', 'friends_count'],
          'SATTE_OF_SEARCH' : ['name', 'profile_use_background_image', 'location', 'description', 'url', 'listed_count', 'followers_count', 'statuses_count', 'friends_count'],
          'STRINGHINI':['name', 'profile_use_background_image', 'location', 'description', 'url', 'listed_count', 'followers_count', 'statuses_count', 'friends_count'],
          'SACIALBAKERS': ['name', 'profile_use_background_image', 'location', 'description', 'url', 'listed_count', 'followers_count', 'statuses_count', 'friends_count'],
          'YANG_AND_AL':['name', 'profile_use_background_image', 'location', 'description', 'url', 'listed_count', 'followers_count', 'statuses_count', 'friends_count']
         },
    'B': {'CAMISANI_CALZOLARI':['name', 'profile_use_background_image', 'location', 'description', 'url', 'listed_count', 'followers_count', 'statuses_count', 'friends_count'],
          'SATTE_OF_SEARCH' : ['name', 'profile_use_background_image', 'location', 'description', 'url', 'listed_count', 'followers_count', 'statuses_count', 'friends_count'],
          'STRINGHINI':['name', 'profile_use_background_image', 'location', 'description', 'url', 'listed_count', 'followers_count', 'statuses_count', 'friends_count'],
          'SACIALBAKERS': ['name', 'profile_use_background_image', 'location', 'description', 'url', 'listed_count', 'followers_count', 'statuses_count', 'friends_count'],
          'YANG_AND_AL':['name', 'profile_use_background_image', 'location', 'description', 'url', 'listed_count', 'followers_count', 'statuses_count', 'friends_count']
         },
    'C': {'YANG_AND_AL': ['name', 'profile_use_background_image', 'location', 'description', 'url', 'listed_count', 'followers_count', 'statuses_count', 'friends_count']} }



def gen_training_features(cur, bas_uid, specific_feature):
    ########
    # TODO
    #######

    results = []

    for uid in bas_uid:

        cur.execute(select_features(specific_feature), (uid,))
        row = cur.fetchone()
        result = []

        for key, value in feature_A_CAMISANI_CALZOLARI(row).items():
            result.append(value)

        results.append(result)
    return results




if __name__ == "__main__":
    con = sqlite3.connect("db.sqlite")
    cur = con.cursor()
    bas_uid, bas_target = gen_target_array()
    results_evaluator = {}
    algos = ['svm', 'tree', 'forest', 'linear_regression', 'neighbors', 'adaBoost']

    for class_, value in class_and_author.items():
        results_evaluator[class_] = dict()

        for author, specific_feature in value.items():
            results_evaluator[class_][author] = dict()

            bas_training = gen_training_features(cur, bas_uid, specific_feature)
            evaluator = Eval(bas_training, bas_target)

            for algo in algos:
                print("process...")
                results_evaluator[class_][author][algo] = dict()
                if algo == "svm":
                    results_evaluator[class_][author][algo] = evaluator.svm()
                elif algo == "tree":
                    results_evaluator[class_][author][algo] = evaluator.tree()
                elif algo == "forest":
                    results_evaluator[class_][author][algo] = evaluator.forest()
                elif algo == "linear_regression":
                    results_evaluator[class_][author][algo] = evaluator.linear_regression()
                elif algo == "neighbors":
                    results_evaluator[class_][author][algo] = evaluator.neighbors()
                elif algo == "adaBoost":
                    results_evaluator[class_][author][algo] = evaluator.adaBoost()

    save_results(results_evaluator)



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
