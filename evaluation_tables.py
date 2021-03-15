# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 00:41:57 2021

@author: benja
"""
from features import check_feature, select_features
from main import gen_training_features
from eval import Eval
from visualisation import save_results

class_and_author = {
    'A': {'CAMISANI_CALZOLARI':['name', 'profile_use_background_image', 'location', 'description', 'url', 'listed_count', 'followers_count', 'statuses_count', 'friends_count'],
          'SATTE_OF_SEARCH' : ['followers_count', 'friends_count', 'profile_image_url', 'description'],
           'STRINGHINI': ['followers_count', 'friends_count'],
          'SACIALBAKERS': ['statuses_count', 'followers_count', 'friends_count', 'location', 'default_profile_image','description'],
          'YANG_AND_AL':['created_at', 'followers_count']
         },

    'B': {
         'CAMISANI_CALZOLARI':['geo_enabled'],
          'SATTE_OF_SEARCH' : ['name'],
          'STRINGHINI':['name']#,


          # 'SACIALBAKERS': ['name'],
          # 'YANG_AND_AL':['name']
         } #,

    }



def evaluating_features_foreach_author(bas_uid, bas_target,cur,algos):
    results_evaluator = {}
    for class_, value in class_and_author.items():
        results_evaluator[class_] = dict()

        for author, specific_feature in value.items():
            results_evaluator[class_][author] = dict()

            results = []
            for uid in bas_uid:
                cur.execute(select_features(specific_feature), (uid,))
                row = cur.fetchone()
                result = []

                for key, value in check_feature(class_, author, row).items():
                    result.append(value)

                results.append(result)

            bas_training = results
            evaluator = Eval(bas_training, bas_target)

            for algo in algos:
                print("| process.. | %3s | %20s | %27s |" % (class_, author, algo))

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
    print('printing results in file: results_evaluator.txt')
    save_results(results_evaluator,path='SaveResult', filename='results_evaluator.txt')