# -*- coding: utf-8 -*-
"""
@author: Bergé Benjamin, Wathelet Jolan, Anicet
"""

import csv
import numpy as np
import random
import os

"""
requete préparé pour selectionner les donner dans la base avec une liste bien défini de colonnes 
"""
def select_features(lists_features):
    query_list = ""

    for item in lists_features:
        query_list = query_list + item + ","

    query_list = query_list[:-1]
    query_list = query_list + " "
    query_list = "SELECT id," + query_list + "FROM users WHERE id = ?;"

    return query_list


# *********************************
# * LIST FEATURES Class A        *
# *********************************

"""
stocke l'ensemble des résultats de la vérification effectuer sur les feature."""

def check_feature(value_feature):
    features = {}
    features['Has_name']                = has_name(value_feature)
    features['Has_background_image']    = has_background_image(value_feature)
    features['Has_location']            = has_location(value_feature)
    features['Has_description']         = has_description(value_feature)
    features['Has_url']                 = has_url(value_feature)
    features['Has_a_list']              = has_a_list(value_feature)
    features['Has_more_follower']       = has_more_follower(value_feature)
    features['Has_more_tweet']          = has_more_tweet(value_feature)
    features['Has_follower_as_friends'] = has_follower_as_friends(value_feature)

    return features



# *********************************
# * LIST FEATURES Class B        *
# *********************************


# *********************************
# * LIST FEATURES Class c        *
# *********************************


# Has a name
def has_name(value_feature):
    if value_feature[1] is not None:
        result = 1
    else:
        result = 0
    return result

# Has a background_image ?
def has_background_image(value_feature):
    if value_feature[2] is not None:
        result = 1
    else:
        result = 0
    return result

# Has a location
def has_location(value_feature):
    if value_feature[3] is not None:
        result = 1
    else:
        result = 0
    return result

# Has a description (bio)
def has_description(value_feature):
    if value_feature[4] is not None:
        result = 1
    else:
        result = 0
    return result

# Has a url
def has_url(value_feature):
    if value_feature[5] is not None:
        result = 1
    else:
        result = 0
    return result

# Is in a list
def has_a_list(value_feature):
    if value_feature[6] is not None:
        result = 1
    else:
        result = 0
    return result

# Has 30 follower or more
def has_more_follower(value_feature, defauld_follower=30):
    if value_feature[7] >= defauld_follower:
        result = 1
    else:
        result = 0
    return result

# Has 50 tweet or more
def has_more_tweet(value_feature, defauld_tweet=50):
    if value_feature[8] >= defauld_tweet:
        result = 1
    else:
        result = 0
    return result

# Has at least twice the number of follower as friends
def has_follower_as_friends(value_feature):
    if value_feature[1] is not None:
        result = 1
    else:
        result = 0
    return result

