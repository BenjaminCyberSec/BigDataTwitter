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
from sklearn.neighbors import NearestNeighbors, KNeighborsClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import KFold
import numpy as np
from statistics import mean 
import test_utils


def evaluate_all( clf, training, target, nbr_folds):
    training = np.array(training)
    target = np.array(target)
    
    kf = KFold(n_splits=nbr_folds, shuffle=True)
    kf.get_n_splits(training)
    
    recall_t = []
    precision_t = []
    accuracy_t = []
    f1_score_t = []
    mc_t = []
    auc_t = []
    for train_index, test_index in kf.split(training):
        X_train, X_test = training[train_index], training[test_index]
        y_train, y_test = target[train_index], target[test_index]

        X_train = np.array(X_train).tolist()
        X_test = np.array(X_test).tolist()
        y_train = np.array(y_train).tolist()
        y_test = np.array(y_test).tolist()
        
        clf.fit(X_train,y_train )
        result = clf.predict(X_test)
        
        recall = metrics.recall_score(y_test, result)
        precision = metrics.precision_score(y_test, result)
        accuracy = metrics.accuracy_score(y_test, result)
        f1_score = metrics.f1_score(y_test, result)
        matthews_corrcoef = metrics.matthews_corrcoef(y_test, result)
        fpr, tpr, thresholds = metrics.roc_curve(y_test, result)
        auc = metrics.auc(fpr, tpr)
        
        recall_t.append(recall)
        precision_t.append(precision)
        accuracy_t.append(accuracy)
        f1_score_t.append(f1_score)
        mc_t.append(matthews_corrcoef)
        auc_t.append(auc)

    
    return {'precision': precision_t, 'accuracy': accuracy_t, 'f1_score': f1_score_t, 'recall':recall_t, 'mc': mc_t, 'auc':auc_t }


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
        dic = evaluate_all(classifier, self.bas_training, self.bas_target, self.nbr_folds)
        return self.concat_dict(dic)
    
    def svm(self):
        return self.kfold_eval(svm.SVC(kernel='linear', C=10, random_state=69))
    
    def tree(self):
        return self.kfold_eval(tree.DecisionTreeClassifier(criterion='entropy',   min_impurity_decrease=0.02, min_samples_leaf=1))
    
    def forest(self, tree_size=100, max_depth=None, min_samples_split=2, min_impurity_decrease=0.0):
        return self.kfold_eval(RandomForestClassifier(n_estimators=tree_size,max_depth=max_depth, min_samples_split=min_samples_split, min_impurity_decrease=min_impurity_decrease))
   
    def linear_regression(self):
        return self.kfold_eval(linear_model.LogisticRegression())
    
    def neighbors(self):
        return self.kfold_eval(KNeighborsClassifier(n_neighbors=2, algorithm='kd_tree'))
    
    def adaBoost(self):
        return self.kfold_eval(AdaBoostClassifier(n_estimators=100,learning_rate=0.9, random_state=0))
    