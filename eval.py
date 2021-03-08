# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 18:01:11 2021

@author: Benjamin
"""
from sklearn.model_selection import cross_val_score
from sklearn import svm
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn import linear_model
from sklearn.neighbors import NearestNeighbors
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import KFold
import numpy as np
from statistics import mean 


def evaluate_all( clf, training, target, nbr_folds):
    training = np.array(training)
    target = np.array(target)
    
    kf = KFold(n_splits=nbr_folds)
    kf.get_n_splits(training)
    
    recall_t = []
    precision_t = []
    accuracy_t = []
    f1_score_t = []
    mc_t = []
    for train_index, test_index in kf.split(training):
        X_train, X_test = training[train_index], training[test_index]
        y_train, y_test = target[train_index], target[test_index]

        X_train = np.array(X_train).tolist()
        X_test = np.array(X_test).tolist()
        y_train = np.array(y_train).tolist()
        y_test = np.array(y_test).tolist()
        
        clf.fit(X_train,y_train )
        result = clf.predict(X_test)
        
        #recall = metrics.recall_score(y_test, result)
        precision = metrics.precision_score(y_test, result)
        accuracy = metrics.accuracy_score(y_test, result)
        f1_score = metrics.f1_score(y_test, result)
        #matthews_corrcoef = metrics.matthews_corrcoef(y_test, result)
        
        #recall_t.append(recall)
        precision_t.append(precision)
        accuracy_t.append(accuracy)
        f1_score_t.append(f1_score)
        #mc_t.append(matthews_corrcoef)
        
        #'recall':recall_t, , 'mc': mc_t
    
    return {'precision': precision_t, 'accuracy': accuracy_t, 'f1_score': f1_score_t}


class Eval:
    def __init__(self, bas_training, bas_target, nbr_folds=10):
        self.bas_training = bas_training
        self.bas_target = bas_target
        self.nbr_folds=nbr_folds
    
    def concat_dict(self, dic):
        result = {}
        for key,value in dic.items():
            result[key]= mean(value)
        return result
    
    
    def kfold_eval(self, classifier):
        #scores = cross_val_score(classifier, self.bas_training, self.bas_target, cv=self.nbr_folds)
        #return self.concat_score(scores)
        
        dic = evaluate_all(classifier, self.bas_training, self.bas_target, self.nbr_folds)
        return self.concat_dict(dic)
    
    def svm(self):
        print("svm")
        return self.kfold_eval(svm.SVC(kernel='linear', C=1, random_state=42))
    
    def tree(self):
        """
        peut construire graph pour choisir les meilleurs params: 
            porcent_of_success = clf.score(bas_training, bas_target)
            tree.plot_tree(clf.fit(bas_training,  bas_target)) #build the tree
        """
        return self.kfold_eval(tree.DecisionTreeClassifier(criterion='entropy',  max_depth=50))
    
    def forest(self):
        return self.kfold_eval(RandomForestClassifier(n_estimators=100))
   
    def linear_regression(self):
        return self.kfold_eval(linear_model.LogisticRegression())
    
    def neighbors(self):
        """
        TypeError: If no scoring is specified, the estimator passed should have a 'score' method. The estimator NearestNeighbors(algorithm='ball_tree', n_neighbors=2) does not.
        """
        return self.kfold_eval(NearestNeighbors(n_neighbors=2, algorithm='ball_tree'))
    
    def adaBoost(self):
        return self.kfold_eval(AdaBoostClassifier(n_estimators=100, random_state=0))
    