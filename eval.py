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



class Eval:
    def __init__(self, bas_training, bas_target, nbr_folds=10):
        self.bas_training = bas_training
        self.bas_target = bas_target
        self.nbr_folds=nbr_folds
    
    def concat_score(self, scores):
        """
        #TODO decide if mean is ok to concat score
        """
        #deviation scores.std() 
        return scores.mean()
    
    
    def kfold_eval(self, classifier):
        """
        TODO add other metrics than score 
        accuracy precision recall F-M. MCC AUC
        
        je sais pas si score est bon
        """
        scores = cross_val_score(classifier, self.bas_training, self.bas_target, cv=self.nbr_folds)
        #accuracy =  metrics.accuracy_score(y_test, y_pred)
        return self.concat_score(scores)
    
    def svm(self):
        return self.kfold_eval(svm.SVC(kernel='linear', C=1, random_state=42))
    
    def tree(self):
        """
        peut construire graph pour choisir les meilleurs params: 
            porcent_of_success = clf.score(bas_training, bas_target)
            tree.plot_tree(clf.fit(bas_training,  bas_target)) #build the tree
        """
        return self.kfold_eval(tree.DecisionTreeClassifier(criterion='entropy', min_impurity_decrease=0.03))
    
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
    