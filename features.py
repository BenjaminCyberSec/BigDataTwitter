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

con = sqlite3.connect("db.sqlite")
cur = con.cursor()
cur2 = con.cursor()


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


def feature_A_SATTE_OF_SEARCH(value_feature):
    features = {}
    features['Bot_in_biography']                = bot_in_biography(value_feature)
    features['Friends_to_followers_has_100']    = friends_to_followers_has_100(value_feature)
    features['Has_duplicate_profile_picture']   = has_duplicate_profile_picture(value_feature)
    return features


def feature_A_STRINGHINI(value_feature):
    features = {}
    features['Friends_count']           = friends_count(value_feature)
    features['Tweets_count']            = tweets_count(value_feature)
    features['Friends_to_followers']    = friends_to_followers_2(value_feature)
    return features


def feature_A_SACIALBAKERS(value_feature):
    features = {}
    features['Friends_to_followers_is_more_50'] = friends_to_followers_is_more_50(value_feature)
    features['Has_default_image']               = has_default_image(value_feature)
    features['Has_no_bio']                      = has_no_bio(value_feature)
    features['Has_no_location']                 = has_no_location(value_feature)
    features['Has_more_friends']                = has_more_friends(value_feature)
    features['Has_no_tweets']                   = has_no_tweets(value_feature)
    return features


def feature_A_YANG_AND_AL(value_feature):
    features = {}
    features['Profile_age']     = profile_age(value_feature)
    features['Following_rate']  = following_rate(value_feature)
    return features


# *********************************
# * LIST FEATURES Class B        *
# *********************************

def feature_B_CAMISANI_CALZOLARI(value_feature):
    features = {}
    features['Is_geo_localized']        = is_geo_localized(value_feature)
    features['Is_favorite']             = is_favorite(value_feature)
    features['Uses_punctuation']        = uses_punctuation(value_feature)
    features['Uses_hashtag']            = uses_hashtag(value_feature)
    features['Has_a_iphone']            = find_a_word_in_source(value_feature, "Iphone")
    features['Has_a_android']           = find_a_word_in_source(value_feature, "Android")
    features['Uses_foursquare']         = find_a_word_in_source(value_feature, "foursquare")
    features['Uses_instagram']          = find_a_word_in_source(value_feature, "Instagram")
    features['Uses_twitter_com']        = find_a_word_in_source(value_feature, "web")
    features['User_id_in_tweet']        = find_a_word_in_tweets(value_feature, value_feature[0])
    features['Tweets_with_url']         = find_a_word_in_tweets(value_feature, "http://")
    features['More_retweet']            = more_retweet(value_feature)
    features['Uses_different_clients']  = uses_different_clients(value_feature)
    return features


def feature_B_SATTE_OF_SEARCH(value_feature):
    features = {}
    features['Same_sentences'] = same_sentences(value_feature)
    features['Tweet_from_api'] = find_a_word_in_source(value_feature, "twitter.com")
    return features

def feature_B_STRINGHINI(value_feature):
    features = {}
    features['Tweet_similarity'] = tweet_similarity(value_feature)
    features['Tweet_similarity'] = url_ratio_tweets(value_feature, "http://")
    return features

def feature_B_SACIALBAKERS(value_feature):
    features = {}
    features['Has_name'] = tweet_similarity(value_feature)
    return features

def feature_B_YANG_AND_AL(value_feature):
    features = {}
    features['Has_name'] = tweet_similarity(value_feature)
    return features


# *********************************
# * LIST FEATURES Class C        *
# *********************************

def feature_C_YANG_AND_AL(value_feature):
    features = {}
    features['Has_description'] = has_description(value_feature)
    return features


# *********************************
# * Fonction pour testes les feactures       *
# *********************************


'''
Returns 1 si 'name' est non vide.
'''
def has_name(value_feature):
    if value_feature[1] is not None:
        result = 1
    else:
        result = 0
    return result


'''
Returns 1 si 'profile_use_background_image' est non vide.
'''
def has_background_image(value_feature):
    if value_feature[2] is not None:
        result = 1
    else:
        result = 0
    return result


'''
Returns 1 si 'location' est non vide.
'''
def has_location(value_feature):
    if len(value_feature) >= 4 and value_feature[3] is not None:
        result = 1
    else:
        result = 0
    return result


'''
Returns 1 si 'description' est non vide.
'''
def has_description(value_feature):
    if len(value_feature) >= 5 and value_feature[4] is not None:
        result = 1
    else:
        result = 0
    return result


'''
Returns 1 si 'url' est non vide.
'''
def has_url(value_feature):
    if len(value_feature) >= 6 and value_feature[5] is not None:
        result = 1
    else:
        result = 0
    return result


'''
Returns 1 si 'listed_count' est non vide.
'''
def has_a_list(value_feature):
    if len(value_feature) >= 7 and value_feature[6] is not None:
        result = 1
    else:
        result = 0
    return result


'''
Returns 1 si 'followers_count' est > 30.
'''
def has_more_follower(value_feature, defauld_follower=30):
    if len(value_feature) >= 8 and value_feature[7] >= defauld_follower:
        result = 1
    else:
        result = 0
    return result


'''
Returns 1 si 'statuses_count' est > 50.
'''
def has_more_tweet(value_feature, defauld_tweet=50):
    if len(value_feature) >= 9 and value_feature[8] >= defauld_tweet:
        result = 1
    else:
        result = 0
    return result


'''
Returns 1 si 'friends_count' 
'''
def has_follower_as_friends(value_feature):
    if len(value_feature) >= 10 and value_feature[7] * 2 >= value_feature[9]:
        result = 1
    else:
        result = 0
    return result

'''
Returns 1 si 'description' est non vide
'''
def bot_in_biography(value_feature):
    if value_feature[4] is not None:
        result = 0
    else:
        result = 1
    return result


'''
Returns 1 si 'friends_count'/'followers_count' est comprit enter [90, 100]
'''
def friends_to_followers_has_100(value_feature):
    feature_to_followers = divise_nombre1_par_nombre2(value_feature[2], value_feature[1])
    if 90 <= feature_to_followers <= 110:
        result = 1
    else:
        result = 0
    return result

'''
divise deux nombre . si le denominateur = 0, retourne valeur du numerateur
'''
def divise_nombre1_par_nombre2(nbr1, nbr2):
    if nbr2 != 0:
        resulta = int(nbr1 / nbr2)
    else:
        resulta = nbr1

    return resulta


'''
Returns 1 si la valeur de 'profile_image_url' est la meme pour deux utilisateurs different
'''
def has_duplicate_profile_picture(value_feature):
    result = 0
    cur.execute("SELECT profile_image_url FROM users WHERE id = ?;", (value_feature[0],))
    cur2.execute("SELECT profile_image_url FROM users ;")

    for i in cur:
        for j in cur2:
            if i[0]==j[0]:
                result = 1

    return result


'''
Returns la valeur de 'friends_count'
'''
def friends_count(value_feature):
    return value_feature[2]


'''
compte le nombre de tweets pour un utilisateur . et retourne sa valeur
'''
def tweets_count(value_feature):
    result = 0
    cur.execute("SELECT text FROM tweets WHERE user_id = ?;", (value_feature[0],))
    for tweet in cur:
        result +=1
    return result


'''
retourne la valeur de 'friends_count'/'followers_count'^2
'''
def friends_to_followers_2(value_feature):
    resulta = divise_nombre1_par_nombre2(value_feature[2], value_feature[1])
    return int(resulta)

'''
retourne 1 si la valeur de 'friends_count'/'followers_count' est > 50
'''
def friends_to_followers_is_more_50(value_feature):
    friends_to_followers = divise_nombre1_par_nombre2(value_feature[3], value_feature[2])
    if friends_to_followers >= 50:
        result = 1
    else:
        result = 0
    return result


'''
Returns 1 si 'profile_image_url' est non vide
'''
def has_default_image(value_feature):
    if value_feature[5] is not None:
        result = 1
    else:
        result = 0
    return result

'''
Returns 1 si 'description' est non vide
'''
def has_no_bio(value_feature):
    if value_feature[6] is not None:
        result = 1
    else:
        result = 0
    return result


'''
Returns 1 si 'location' est non vide
'''
def has_no_location(value_feature):
    if value_feature[4] is not None:
        result = 1
    else:
        result = 0
    return result

'''
Returns 1 si 'friends_count' est > 100
'''
def has_more_friends(value_feature, defauld_friends=100):
    if value_feature[3] >= defauld_friends:
        result = 1
    else:
        result = 0
    return result


'''
Returns 1 si 'friends_count' est > 100
'''
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
    result = 0
    cur.execute("SELECT favorite_count FROM tweets WHERE user_id = ?;", (value_feature[0],))
    for i in cur:
        if i[0] != 0:
            result = 1

    return result


# checking whether the char is punctuation.
def uses_punctuation(value_feature):
    nbr_of_tweet_with_punctuation = 0
    total_tweets = 0

    cur.execute("SELECT text FROM tweets WHERE user_id = ?;", (value_feature[0],))
    for tweet in cur:
        total_tweets += 1

        for char_ in str(tweet[0]):
            if char_ in string.punctuation:
                nbr_of_tweet_with_punctuation += 1

    pourcentage = divise_nombre1_par_nombre2(nbr_of_tweet_with_punctuation, total_tweets) * 100
    if int(pourcentage) >= 50:
        result = 1
    else:
        result = 0

    return result


# checking whether the char is hashtag.
def uses_hashtag(value_feature):
    nbr_of_tweet_with_hashtag = 0
    total_tweets = 0

    cur.execute("SELECT text FROM tweets WHERE user_id = ?;", (value_feature[0],))
    for tweet in cur:
        total_tweets += 1

        for char_ in str(tweet[0]):
            if char_ == "#":
                nbr_of_tweet_with_hashtag += 1

    pourcentage = divise_nombre1_par_nombre2(nbr_of_tweet_with_hashtag, total_tweets) * 100
    if int(pourcentage) >= 50:
        result = 1
    else:
        result = 0

    return result


# checking whether the char is hashtag.
def find_a_word_in_source(value_feature, substring):
    result = 0
    cur.execute("SELECT source FROM tweets WHERE user_id = ?;", (value_feature[0],))
    for source in cur:
        fullstring = str(source[0])
        if fullstring.find(str(substring)) != -1:
            result = 1
            break

    return result


def find_a_word_in_tweets(value_feature, substring):
    result = 0
    cur.execute("SELECT text FROM tweets WHERE user_id = ?;", (value_feature[0],))
    for tweet in cur:
        fullstring = str(tweet[0])
        if fullstring.find(str(substring)) != -1:
            print(fullstring)
            result = 1
            break

    return result


def more_retweet(value_feature):
    result = 0
    cur.execute("SELECT retweet_count FROM tweets WHERE user_id = ?;", (value_feature[0],))
    for i in cur:
        if i[0] > 1:
            print(i[0])
            result = 1
            break

    return result


def uses_different_clients(value_feature):
    result = 0
    cur.execute("SELECT source FROM tweets WHERE user_id = ?;", (value_feature[0],))
    for i in cur:
        for j in cur:
            if i[0] == j[0]:
                print(i[0])
                result = 1
                break
        break

    return result


def tweet_similarity(value_feature):
    result = 0
    cur.execute("SELECT text FROM tweets WHERE user_id = ?;", (value_feature[0],))
    for i in cur:
        for j in cur:
            if i[0] == j[0]:
                result = 1
                break
        break

    return result


def same_sentences(value_feature):
    result = 0

    cur.execute("SELECT text FROM tweets WHERE user_id = ?;", (value_feature[0],))

    for i in cur:
        s1 = str(i[0])
        set1 = set(s1.split(' '))

        for j in cur:
            s2=str(j[0])
            set2 = set(s2.split(' '))
            same_word = 0
            total_word = 0

            for k in set1:
                total_word += 1

                for l in set2:

                    if k == l:
                        same_word += 1

            pourcentage = divise_nombre1_par_nombre2(same_word, total_word) * 100
            if int(pourcentage) >= 50:
                result = 1

    return result

def url_ratio_tweets(value_feature, substring):

    nbr_of_tweet_with_url = 0
    total_tweets = 0
    cur.execute("SELECT text FROM tweets WHERE user_id = ?;", (value_feature[0],))

    for tweet in cur:
        total_tweets += 1
        fullstring = str(tweet[0])

        if fullstring.find(str(substring)) != -1:
            nbr_of_tweet_with_url +=1

    ratio_value = float(divise_nombre1_par_nombre2(nbr_of_tweet_with_url, total_tweets))
    return ratio_value



