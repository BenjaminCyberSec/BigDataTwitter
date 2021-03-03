# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 14:33:30 2021

@author: Benjamin
"""
import pandas as pd

"""
tweets not working
"""

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