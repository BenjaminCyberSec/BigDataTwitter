# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 17:45:01 2021

@author: Bergé Benjamin, Wathelet Jolan, Anicet
"""

import csv
import numpy as np
import random
import sqlite3
import pandas as pd
from sklearn import tree
import matplotlib.pyplot as plt



#if target value = true then is human = true
def to_target_array(filename, target_value):
    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader((line.replace('\0','') for line in csvfile), delimiter=',')
        array_u = []
        for row in reader:
            array_u.append([row[0],target_value])
    return array_u[1:] #retire titres

def gen_target_array():
    #Human
    e13_u = to_target_array('E13\\users.csv',1)
    tfp_u = to_target_array('TFP\\users.csv',1)
    temp = np.concatenate((e13_u, tfp_u))
    hum_u = temp[:-2] #il y en a 1952 dans le set 
    #Fake
    fsf_u = to_target_array('FSF\\users.csv',0)
    int_u = to_target_array('INT\\users.csv',0)
    twt_u = to_target_array('TWT\\users.csv',0)
    temp = np.concatenate((fsf_u, int_u,twt_u))
    fak_u = random.sample(list(temp), 1950)
    #Training sample
    bas_u = np.concatenate((hum_u, fak_u))
    return bas_u

def dbgen_users(con):
    #users
    e13_u = pd.read_csv('E13\\users.csv')
    tfp_u = pd.read_csv('TFP\\users.csv')
    fsf_u = pd.read_csv('FSF\\users.csv')
    int_u = pd.read_csv('INT\\users.csv')
    twt_u = pd.read_csv('TWT\\users.csv')
    df = pd.concat([e13_u, tfp_u, fsf_u, int_u, twt_u])
    df.to_sql('users', con, if_exists='append', index=False)
def dbgen_friends(con):
    #friends
    e13_f = pd.read_csv('E13\\friends.csv')
    tfp_f = pd.read_csv('TFP\\friends.csv')
    fsf_f = pd.read_csv('FSF\\friends.csv')
    int_f = pd.read_csv('INT\\friends.csv')
    twt_f = pd.read_csv('TWT\\friends.csv')
    df = pd.concat([e13_f, tfp_f, fsf_f, int_f, twt_f])
    df.to_sql('friends', con, if_exists='append', index=False)
def dbgen_tweets(con):
    #tweets
    e13_t = pd.read_csv('E13\\tweets.csv')
    tfp_t = pd.read_csv('TFP\\tweets.csv')
    fsf_t = pd.read_csv('FSF\\tweets.csv')
    int_t = pd.read_csv('INT\\tweets.csv')
    twt_t = pd.read_csv('TWT\\tweets.csv')
    df = pd.concat([e13_t, tfp_t, fsf_t, int_t, twt_t])
    df.to_sql('tweets', con, if_exists='append', index=False)
def dbgen_followers(con):
    #followers
    e13_fo = pd.read_csv('E13\\followers.csv')
    tfp_fo = pd.read_csv('TFP\\followers.csv')
    fsf_fo = pd.read_csv('FSF\\followers.csv')
    int_fo = pd.read_csv('INT\\followers.csv')
    twt_fo = pd.read_csv('TWT\\followers.csv')
    df = pd.concat([e13_fo, tfp_fo, fsf_fo, int_fo, twt_fo])
    df.to_sql('followers', con, if_exists='append', index=False)
def gen_database(con): 
    dbgen_users(con)
    dbgen_friends(con)
    dbgen_followers(con)
    #dbgen_tweets(con)
    
def gen_training(cur, bas_target):
    #has_name, has_image, has_address
    results = []
    for t in bas_target:
        uid= t[0]
        cur.execute("SELECT id,name, profile_use_background_image, location FROM users WHERE id = ?;", (uid,))
        row = cur.fetchone()
        result = []
        #result.append(row[0])
        for i in range(0,3):
            if row[i] != None:
                result.append(1)
            else:
                result.append(0)
        results.append(result)
    return results

if __name__ == "__main__":
    con = sqlite3.connect("data/db.sqlite")
    cur = con.cursor()
    """
    gen_database(con)
    for row in cur.execute('SELECT * FROM tweets LIMIT 1;'):
        print(row)

    """
    
    bas_target = gen_target_array()
    bas_training = gen_training(cur, bas_target)
    
    a = [item[1] for item in bas_target]
    bas_target = a
    
    
    #https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
    
    bas_training = bas_training
    bas_target = bas_target
    clf = tree.DecisionTreeClassifier(criterion='entropy', min_impurity_decrease=0.03)
    clf = clf.fit(bas_training, bas_target)
    #/!\ change to use test values!
    porcent_of_success = clf.score(bas_training, bas_target)
    tree.plot_tree(clf.fit(bas_training,  bas_target)) #build the tree
    
    
    """
    porcent_of_success = clf.score(data.get('test'), data.get('test_target'))
    tree.plot_tree(clf.fit(data.get('training'), data.get('target'))) #build the tree
    
    """
    
   
    
    con.close()
    
    #https://stackoverflow.com/questions/30218963/storing-sql-statements-in-a-properties-file-to-be-used-by-python-scripts/30219756