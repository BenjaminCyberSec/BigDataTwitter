# -*- coding: utf-8 -*-
"""
@author: Bergé Benjamin, Wathelet Jolan, Anicet
"""

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


def check_feature(class_, author, value_feature):
    if class_ == 'A':
        if author == 'CAMISANI_CALZOLARI':
            return (feature_A_CAMISANI_CALZOLARI(value_feature))
        elif author == 'SATTE_OF_SEARCH':
            return (feature_A_SATTE_OF_SEARCH(value_feature))
        elif author == 'STRINGHINI':
            return (feature_A_STRINGHINI(value_feature))
        elif author == 'SACIALBAKERS':
            return (feature_A_SACIALBAKERS(value_feature))
        elif author == 'YANG_AND_AL':
            return (feature_A_YANG_AND_AL(value_feature))

    elif class_ == 'B':
        if author == 'CAMISANI_CALZOLARI':
            return (feature_B_CAMISANI_CALZOLARI(value_feature))
        elif author == 'SATTE_OF_SEARCH':
            return (feature_B_SATTE_OF_SEARCH(value_feature))
        elif author == 'STRINGHINI':
            return (feature_B_STRINGHINI(value_feature))
        elif author == 'SACIALBAKERS':
            return (feature_B_SACIALBAKERS(value_feature))
        elif author == 'YANG_AND_AL':
            return (feature_B_YANG_AND_AL(value_feature))

    elif class_ == 'C':
        if author == 'YANG_AND_AL':
            return (feature_C_YANG_AND_AL(value_feature))


"""
stocke l'ensemble des résultats de la vérification effectuer sur les feature."""

# *********************************
# * LIST FEATURES Class A        *
# *********************************

def feature_A_CAMISANI_CALZOLARI(value_feature):
    features = {}
    features['Has_name'] = has_name(value_feature)
    features['Has_background_image'] = has_background_image(value_feature)
    features['Has_location'] = has_location(value_feature)
    features['Has_description'] = has_description(value_feature)
    features['Has_url'] = has_url(value_feature)
    features['Has_a_list'] = has_a_list(value_feature)
    features['Has_more_follower'] = has_more_follower(value_feature)
    features['Has_more_tweet'] = has_more_tweet(value_feature)
    features['Has_follower_as_friends'] = has_follower_as_friends(value_feature)
    return features

def feature_A_SATTE_OF_SEARCH(value_feature):
    features = {}

    ########
    # TODO : a completer. pour cet autheur et cette classe,  mettre les bon feature defini dans l'article. remplcer egalement dans celle du dictionnaire "class_and_author{}"
    #######
    features['Has_name'] = has_name(value_feature)
    features['Has_background_image'] = has_background_image(value_feature)
    features['Has_location'] = has_location(value_feature)
    features['Has_description'] = has_description(value_feature)
    features['Has_url'] = has_url(value_feature)
    features['Has_a_list'] = has_a_list(value_feature)
    features['Has_more_follower'] = has_more_follower(value_feature)
    features['Has_more_tweet'] = has_more_tweet(value_feature)
    features['Has_follower_as_friends'] = has_follower_as_friends(value_feature)
    return features

def feature_A_STRINGHINI(value_feature):
    features = {}

    ########
    # TODO : a completer. pour cet autheur et cette classe,  mettre les bon feature defini dans l'article. remplcer egalement dans celle du dictionnaire "class_and_author{}"
    #######
    features['Has_name'] = has_name(value_feature)
    features['Has_background_image'] = has_background_image(value_feature)
    features['Has_location'] = has_location(value_feature)
    features['Has_description'] = has_description(value_feature)
    features['Has_url'] = has_url(value_feature)
    features['Has_a_list'] = has_a_list(value_feature)
    features['Has_more_follower'] = has_more_follower(value_feature)
    features['Has_more_tweet'] = has_more_tweet(value_feature)
    features['Has_follower_as_friends'] = has_follower_as_friends(value_feature)
    return features

def feature_A_SACIALBAKERS(value_feature):
    features = {}

    ########
    # TODO : a completer. pour cet autheur et cette classe,  mettre les bon feature defini dans l'article. remplcer egalement dans celle du dictionnaire "class_and_author{}"
    #######
    features['Has_name'] = has_name(value_feature)
    features['Has_background_image'] = has_background_image(value_feature)
    features['Has_location'] = has_location(value_feature)
    features['Has_description'] = has_description(value_feature)
    features['Has_url'] = has_url(value_feature)
    features['Has_a_list'] = has_a_list(value_feature)
    features['Has_more_follower'] = has_more_follower(value_feature)
    features['Has_more_tweet'] = has_more_tweet(value_feature)
    features['Has_follower_as_friends'] = has_follower_as_friends(value_feature)
    return features

def feature_A_YANG_AND_AL(value_feature):
    features = {}

    ########
    # TODO : a completer. pour cet autheur et cette classe,  mettre les bon feature defini dans l'article. remplcer egalement dans celle du dictionnaire "class_and_author{}"
    #######
    features['Has_name'] = has_name(value_feature)
    features['Has_background_image'] = has_background_image(value_feature)
    features['Has_location'] = has_location(value_feature)
    features['Has_description'] = has_description(value_feature)
    features['Has_url'] = has_url(value_feature)
    features['Has_a_list'] = has_a_list(value_feature)
    features['Has_more_follower'] = has_more_follower(value_feature)
    features['Has_more_tweet'] = has_more_tweet(value_feature)
    features['Has_follower_as_friends'] = has_follower_as_friends(value_feature)
    return features


# *********************************
# * LIST FEATURES Class B        *
# *********************************

def feature_B_CAMISANI_CALZOLARI(value_feature):
    features = {}

    ########
    # TODO : a completer. pour cet autheur et cette classe,  mettre les bon feature defini dans l'article. remplcer egalement dans celle du dictionnaire "class_and_author{}"
    #######
    features['Has_name'] = has_name(value_feature)
    features['Has_background_image'] = has_background_image(value_feature)
    features['Has_location'] = has_location(value_feature)
    features['Has_description'] = has_description(value_feature)
    features['Has_url'] = has_url(value_feature)
    features['Has_a_list'] = has_a_list(value_feature)
    features['Has_more_follower'] = has_more_follower(value_feature)
    features['Has_more_tweet'] = has_more_tweet(value_feature)
    features['Has_follower_as_friends'] = has_follower_as_friends(value_feature)
    return features

def feature_B_SATTE_OF_SEARCH(value_feature):
    features = {}

    ########
    # TODO : a completer. pour cet autheur et cette classe,  mettre les bon feature defini dans l'article. remplcer egalement dans celle du dictionnaire "class_and_author{}"
    #######
    features['Has_name'] = has_name(value_feature)
    features['Has_background_image'] = has_background_image(value_feature)
    features['Has_location'] = has_location(value_feature)
    features['Has_description'] = has_description(value_feature)
    features['Has_url'] = has_url(value_feature)
    features['Has_a_list'] = has_a_list(value_feature)
    features['Has_more_follower'] = has_more_follower(value_feature)
    features['Has_more_tweet'] = has_more_tweet(value_feature)
    features['Has_follower_as_friends'] = has_follower_as_friends(value_feature)
    return features

def feature_B_STRINGHINI(value_feature):
    features = {}

    ########
    # TODO : a completer. pour cet autheur et cette classe,  mettre les bon feature defini dans l'article. remplcer egalement dans celle du dictionnaire "class_and_author{}"
    #######
    features['Has_name'] = has_name(value_feature)
    features['Has_background_image'] = has_background_image(value_feature)
    features['Has_location'] = has_location(value_feature)
    features['Has_description'] = has_description(value_feature)
    features['Has_url'] = has_url(value_feature)
    features['Has_a_list'] = has_a_list(value_feature)
    features['Has_more_follower'] = has_more_follower(value_feature)
    features['Has_more_tweet'] = has_more_tweet(value_feature)
    features['Has_follower_as_friends'] = has_follower_as_friends(value_feature)
    return features

def feature_B_SACIALBAKERS(value_feature):
    features = {}

    ########
    # TODO : a completer. pour cet autheur et cette classe,  mettre les bon feature defini dans l'article. remplcer egalement dans celle du dictionnaire "class_and_author{}"
    #######
    features['Has_name'] = has_name(value_feature)
    features['Has_background_image'] = has_background_image(value_feature)
    features['Has_location'] = has_location(value_feature)
    features['Has_description'] = has_description(value_feature)
    features['Has_url'] = has_url(value_feature)
    features['Has_a_list'] = has_a_list(value_feature)
    features['Has_more_follower'] = has_more_follower(value_feature)
    features['Has_more_tweet'] = has_more_tweet(value_feature)
    features['Has_follower_as_friends'] = has_follower_as_friends(value_feature)
    return features

def feature_B_YANG_AND_AL(value_feature):
    features = {}

    ########
    # TODO : a completer. pour cet autheur et cette classe,  mettre les bon feature defini dans l'article. remplcer egalement dans celle du dictionnaire "class_and_author{}"
    #######
    features['Has_name'] = has_name(value_feature)
    features['Has_background_image'] = has_background_image(value_feature)
    features['Has_location'] = has_location(value_feature)
    features['Has_description'] = has_description(value_feature)
    features['Has_url'] = has_url(value_feature)
    features['Has_a_list'] = has_a_list(value_feature)
    features['Has_more_follower'] = has_more_follower(value_feature)
    features['Has_more_tweet'] = has_more_tweet(value_feature)
    features['Has_follower_as_friends'] = has_follower_as_friends(value_feature)
    return features

# *********************************
# * LIST FEATURES Class C        *
# *********************************


def feature_C_YANG_AND_AL(value_feature):
    features = {}

    ########
    # TODO : a completer. pour cet autheur et cette classe,  mettre les bon feature defini dans l'article. remplcer egalement dans celle du dictionnaire "class_and_author{}"
    #######
    features['Has_name'] = has_name(value_feature)
    features['Has_background_image'] = has_background_image(value_feature)
    features['Has_location'] = has_location(value_feature)
    features['Has_description'] = has_description(value_feature)
    features['Has_url'] = has_url(value_feature)
    features['Has_a_list'] = has_a_list(value_feature)
    features['Has_more_follower'] = has_more_follower(value_feature)
    features['Has_more_tweet'] = has_more_tweet(value_feature)
    features['Has_follower_as_friends'] = has_follower_as_friends(value_feature)
    return features


# *********************************
# * Fonction pour testes les feactures       *
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
