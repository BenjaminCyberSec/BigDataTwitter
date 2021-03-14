# -*- coding: utf-8 -*-
"""
@author: Bergé Benjamin, Wathelet Jolan, Anicet
"""
import string
from datetime import datetime
import sqlite3

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
    features['Bot_in_biography'] = bot_in_biography(value_feature)
    features['Friends_to_followers_has_100'] = friends_to_followers_has_100(value_feature)
    features['Has_duplicate_profile_picture'] = has_duplicate_profile_picture(value_feature)
    return features


def feature_A_STRINGHINI(value_feature):
    # features = {}
    # features['Friends_count'] = friends_count(value_feature)
    # features['Tweets_count'] = tweets_count(value_feature)
    # features['Friends_to_followers'] = friends_to_followers_2(value_feature)

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
    features['Friends_to_followers_is_more_50'] = friends_to_followers_is_more_50(value_feature)
    features['Has_default_image'] = has_default_image(value_feature)
    features['Has_no_bio'] = has_no_bio(value_feature)
    features['Has_no_location'] = has_no_location(value_feature)
    features['Has_more_friends'] = has_more_friends(value_feature)
    features['Has_no_tweets'] = has_no_tweets(value_feature)

    return features


def feature_A_YANG_AND_AL(value_feature):
    features = {}
    features['Profile_age'] = profile_age(value_feature)
    features['Following_rate'] = following_rate(value_feature)
    return features


# *********************************
# * LIST FEATURES Class B        *
# *********************************

def feature_B_CAMISANI_CALZOLARI(value_feature):
    features = {}

    features['Is_geo_localized'] = is_geo_localized(value_feature)
    features['Is_favorite'] = is_favorite(value_feature)
    features['Uses_punctuation'] = uses_punctuation(value_feature)
    features['Uses_hashtag'] = uses_hashtag(value_feature)
    features['Has_a_iphone'] = has_a_phone_type(value_feature, "Iphone")
    features['Has_a_android'] = has_a_phone_type(value_feature, "Android")

    ## a partir d'ici lesvaleur ne sont plus bonne
    features['Uses_foursquare'] = uses_foursquare(value_feature)
    features['Uses_instagram'] = uses_instagram(value_feature)
    features['Uses_twitter_com'] = uses_twitter_com(value_feature)
    features['User_id_in_tweet'] = user_id_in_tweet(value_feature)
    features['Tweets_with_url'] = tweets_with_url(value_feature)
    features['More_retweet'] = more_retweet(value_feature)
    features['Uses_different_clients'] = uses_different_clients(value_feature)

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
    if len(value_feature) >= 4 and value_feature[3] is not None:
        result = 1
    else:
        result = 0
    return result


# Has a description (bio)
def has_description(value_feature):
    if len(value_feature) >= 5 and value_feature[4] is not None:
        result = 1
    else:
        result = 0
    return result


# Has a url
def has_url(value_feature):
    if len(value_feature) >= 6 and value_feature[5] is not None:
        result = 1
    else:
        result = 0
    return result


# Is in a list
def has_a_list(value_feature):
    if len(value_feature) >= 7 and value_feature[6] is not None:
        result = 1
    else:
        result = 0
    return result


# Has 30 follower or more
def has_more_follower(value_feature, defauld_follower=30):
    if len(value_feature) >= 8 and value_feature[7] >= defauld_follower:
        result = 1
    else:
        result = 0
    return result


# Has 50 tweet or more
def has_more_tweet(value_feature, defauld_tweet=50):
    if len(value_feature) >= 9 and value_feature[8] >= defauld_tweet:
        result = 1
    else:
        result = 0
    return result


# Has at least twice the number of follower as friends
def has_follower_as_friends(value_feature):
    if len(value_feature) >= 10 and value_feature[7] * 2 >= value_feature[9]:
        result = 1
    else:
        result = 0
    return result


######## ####### ####### #######
#  NEW FONCTION
####### ####### ####### #######


# Feature is : description
def bot_in_biography(value_feature):
    if value_feature[4] is not None:
        result = 0
    else:
        result = 1
    return result


# Feature is :
def friends_to_followers_has_100(value_feature):
    feature_to_followers = divise_nombre1_par_nombre2(value_feature[2], value_feature[1])
    if 90 <= feature_to_followers <= 110:
        result = 1
    else:
        result = 0
    return result


def divise_nombre1_par_nombre2(nbr1, nbr2):
    if nbr2 != 0:
        resulta = int(nbr1 / nbr2)
    else:
        resulta = nbr1

    return resulta


# Feature is : profile_image_url
def has_duplicate_profile_picture(value_feature):
    con = sqlite3.connect("db.sqlite")
    cur = con.cursor()

    cur.execute("SELECT profile_image_url FROM users ;")

    # for i in cur:
    #     if i == value_feature[3]:
    #         result = 1
    #     else:
    #         result = 0

    result = 1
    return result


# Feature is : friends_count
def friends_count(value_feature):
    return value_feature[3]
    # return 100


# Feature is : statuses_count . remplace le mombre de tweet
def tweets_count(value_feature):
    return value_feature[1]
    # return 20


# Feature is : friends_count/followers_count^2
def friends_to_followers_2(value_feature):
    resulta = divise_nombre1_par_nombre2(value_feature[3], value_feature[2])
    return int(resulta)
    # return (1/900)


# Feature is : friends_count/followers_count^2
def friends_to_followers_is_more_50(value_feature):
    friends_to_followers = divise_nombre1_par_nombre2(value_feature[3], value_feature[2])
    if friends_to_followers >= 50:
        result = 1
    else:
        result = 0
    return result


# Feature is : default_profile_image
def has_default_image(value_feature):
    if value_feature[5] is not None:
        result = 1
    else:
        result = 0
    return result


def has_no_bio(value_feature):
    if value_feature[6] is not None:
        result = 1
    else:
        result = 0
    return result


def has_no_location(value_feature):
    if value_feature[4] is not None:
        result = 1
    else:
        result = 0
    return result


def has_more_friends(value_feature, defauld_friends=100):
    if value_feature[3] >= defauld_friends:
        result = 1
    else:
        result = 0
    return result


def has_no_tweets(value_feature, defauld_tweets=1):
    if value_feature[1] >= defauld_tweets:
        result = 0
    else:
        result = 1
    return result


def profile_age(value_feature):
    profile_creation = datetime.strptime(value_feature[1], '%a %b %d %H:%M:%S %z %Y')
    timezone = profile_creation.tzinfo
    today = datetime.now(timezone)
    return (today - profile_creation).days


def following_rate(value_feature):
    return value_feature[2]


def is_geo_localized(value_feature):
    if value_feature[1] is not None:
        result = 1
    else:
        result = 0
    return result


def is_favorite(value_feature):
    if value_feature[2] != 0:
        result = 1
    else:
        result = 0
    return result


# checking whether the char is punctuation.
def uses_punctuation(value_feature):
    result = 0
    sentence = str(value_feature[3])
    for i in sentence:
        if i in string.punctuation:
            result = 1

    return result


# checking whether the char is hashtag.
def uses_hashtag(value_feature):
    result = 0
    sentence = str(value_feature[3])
    for i in sentence:
        if i == "#":
            result = 1

    return result


# checking whether the char is hashtag.
def has_a_phone_type(value_feature, phone_type):
    fullstring = str(value_feature[3])

    try:
        fullstring.index(str(phone_type))
    except ValueError:
        result = 0
    else:
        result = 1

    return result


# checking whether the char is hashtag.
def uses_foursquare(value_feature):
    fullstring = str(value_feature[3])
    substring = "foursquare"

    try:
        fullstring.index(substring)
    except ValueError:
        result = 0
    else:
        result = 1

    return result

# checking whether the char is hashtag.
def uses_instagram(value_feature):
    fullstring = str(value_feature[3])
    substring = "Instagram"

    try:
        fullstring.index(substring)
    except ValueError:
        result = 0
    else:
        result = 1

    return result


def uses_twitter_com(value_feature):
    fullstring = str(value_feature[3])
    substring = "web"

    try:
        fullstring.index(substring)
    except ValueError:
        result = 0
    else:
        result = 1

    return result

def user_id_in_tweet(value_feature):
    fullstring = str(value_feature[3])
    substring = "web"

    try:
        fullstring.index(substring)
    except ValueError:
        result = 0
    else:
        result = 1

    return result


def tweets_with_url(value_feature):
    fullstring = str(value_feature[3])
    substring = "web"

    try:
        fullstring.index(substring)
    except ValueError:
        result = 0
    else:
        result = 1

    return result

def more_retweet(value_feature):
    fullstring = str(value_feature[3])
    substring = "web"

    try:
        fullstring.index(substring)
    except ValueError:
        result = 0
    else:
        result = 1

    return result

def uses_different_clients(value_feature):
    fullstring = str(value_feature[3])
    substring = "web"

    try:
        fullstring.index(substring)
    except ValueError:
        result = 0
    else:
        result = 1

    return result