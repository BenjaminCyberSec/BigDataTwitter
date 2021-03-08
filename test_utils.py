# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 18:20:37 2021

@author: Benjamin
"""

def print_data_sets(bas_training, bas_target):
    #print(len(bas_training))
    #print(len(bas_target))
    
    for i in range(len(bas_target)):
        print('%s: %s %s %s %s %s %s %s %s %s' % (bas_target[i],bas_training[i][0],bas_training[i][1],bas_training[i][2],bas_training[i][3],bas_training[i][4],bas_training[i][5],bas_training[i][6],bas_training[i][7],bas_training[i][8]))
    

#eval_useful(9, bas_training)
def eval_useful(feature_nb, training):
    eval_table = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    for i in range(len(training)):
        for j in range(feature_nb):
            value = training[i][j]
            eval_table[j][value] = (eval_table[j][value]) +1
    
    
    for j in range(feature_nb):
        ok = True
        if eval_table[j][0] ==0 :
            print("feature "+str(j)+" is never worth 0")
            ok = False
        if eval_table[j][0] == len(training):
            print("feature "+str(j)+" is always worth 0")
            ok = False
            
            
        if eval_table[j][1] == len(training):
            print("feature "+str(j)+" is always worth 1")
            ok = False
        if eval_table[j][1] ==0 :
            print("feature "+str(j)+" is never worth 1")
            ok = False
            
        if ok:
            print("feature "+str(j)+" has "+str(eval_table[j][1])+" values worth 1 and "+str(eval_table[j][0])+" values worth 0")
            
#3898 <= humans value 1
def count_value(bas_target, value):
    count = 0
    for i in bas_target:
        if bas_target[i] == value:
            count = count +1
    print(count)
    
def analyse_result(result):
    count_0 =0
    count_1 =0
    for i in result:
        if i == 0:
            count_0 = count_0 +1
        else:
            count_1 = count_1 +1
    print('The algo predicted %s bots and %s humans' % (count_0,count_1) )
        