# -*- coding: utf-8 -*-
"""
@author: Bergé Benjamin, Wathelet Jolan, Anicet
"""
import os

def save_results(dictionary_results, path='SaveResult', filename='results_evaluator.txt'):
    li = 196 #total length 173
    sli = 160 #137

    with open(path + os.sep +filename , 'w') as fichier:
        fichier.write(
            '\n\n' * 3 + ' ' * 8 + 'Table: Performance comparison for 10-fold cross validation. Training set: BAS   \n\n+' + "-" * li + "+\n")

        fichier.write(#84
            "|Class type | Author " + " " * 15 + "|" + " " * 31 + " evaluation  metrics " + " " * 107 + " | \n+" + "-" * li + "+")
        fichier.write("\n|" + " " * 35 + "|" + "%23s %22s %22s %22s %22s %22s %22s" % (
        'algorithm |', 'precision |', 'accuracy |', 'f1_score |', 'recall |', 'mc |', 'auc |') + "\n|" + "*" * li + "|")

        for class_, value in dictionary_results.items():
            fichier.write("\n| CLASS %3s" % (class_))

            for author, algo in value.items():
                fichier.write(" |  %20s " % (author))
                first = True
                for algo_name, performance in algo.items():
                    if not first:
                        fichier.write(" |  %20s " % (''))
                    fichier.write("| %20s " % (algo_name))
                    first = False
                    for performance_name, value in performance.items():
                        fichier.write("| %20s " % (value))
                    fichier.write("|\n|" + " " * 35 + "+" + "-" * sli + "+ \n")
                    #fichier.write("|" + " " * 35)
                    fichier.write("|       %3s" % (' '))
            fichier.write("|\n#" + "#" * li + "#")