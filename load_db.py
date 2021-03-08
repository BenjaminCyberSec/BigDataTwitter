# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 14:33:30 2021

@author: Bergé Benjamin, Wathelet Jolan, Anicet
"""
import pandas as pd
import os

"""
tweets not working
"""

def dbgen_users(con):
    #users
    e13_u = pd.read_csv('E13'+os.sep+'users.csv')
    tfp_u = pd.read_csv('TFP'+os.sep+'users.csv')
    fsf_u = pd.read_csv('FSF'+os.sep+'users.csv')
    int_u = pd.read_csv('INT'+os.sep+'users.csv')
    twt_u = pd.read_csv('TWT'+os.sep+'users.csv')
    df = pd.concat([e13_u, tfp_u, fsf_u, int_u, twt_u])
    df.to_sql('users', con, if_exists='append', index=False)
    
def dbgen_friends(con):
    #friends
    e13_f = pd.read_csv('E13'+os.sep+'friends.csv')
    tfp_f = pd.read_csv('TFP'+os.sep+'friends.csv')
    fsf_f = pd.read_csv('FSF'+os.sep+'friends.csv')
    int_f = pd.read_csv('INT'+os.sep+'friends.csv')
    twt_f = pd.read_csv('TWT'+os.sep+'friends.csv')
    df = pd.concat([e13_f, tfp_f, fsf_f, int_f, twt_f])
    df.to_sql('friends', con, if_exists='append', index=False)
    
def dbgen_tweets(con):
    #tweets
    e13_t = pd.read_csv('E13'+os.sep+'tweets.csv')
    tfp_t = pd.read_csv('TFP'+os.sep+'tweets.csv')
    fsf_t = pd.read_csv('FSF'+os.sep+'tweets.csv')
    int_t = pd.read_csv('INT'+os.sep+'tweets.csv')
    twt_t = pd.read_csv('TWT'+os.sep+'tweets.csv')
    df = pd.concat([e13_t, tfp_t, fsf_t, int_t, twt_t])
    df.to_sql('tweets', con, if_exists='append', index=False)
    
def dbgen_followers(con):
    #followers
    e13_fo = pd.read_csv('E13'+os.sep+'followers.csv')
    tfp_fo = pd.read_csv('TFP'+os.sep+'followers.csv')
    fsf_fo = pd.read_csv('FSF'+os.sep+'followers.csv')
    int_fo = pd.read_csv('INT'+os.sep+'followers.csv')
    twt_fo = pd.read_csv('TWT'+os.sep+'followers.csv')
    df = pd.concat([e13_fo, tfp_fo, fsf_fo, int_fo, twt_fo])
    df.to_sql('followers', con, if_exists='append', index=False)
    
def gen_database(con): 
    dbgen_users(con)
    dbgen_friends(con)
    dbgen_followers(con)
    #dbgen_tweets(con)