# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 00:41:57 2021

@author: benja
"""

from main import gen_training_features
from eval import Eval
from visualisation import save_results

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
    'C': {'YANG_AND_AL': ['name', 'profile_use_background_image', 'location', 'description', 'url', 'listed_count', 'followers_count', 'statuses_count', 'friends_count']}
    }


def evaluating_features_foreach_author(bas_uid, bas_target,cur,algos,features,path,filename):
    results_evaluator = {}
    for class_, value in class_and_author.items():
        results_evaluator[class_] = dict()

        for author, specific_feature in value.items():
            results_evaluator[class_][author] = dict()

            bas_training = gen_training_features(cur, bas_uid, specific_feature)
            evaluator = Eval(bas_training, bas_target)

            for algo in algos:
                print('process..')
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