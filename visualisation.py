# -*- coding: utf-8 -*-
"""
@author: Bergé Benjamin, Wathelet Jolan, Anicet
"""
import os

def save_results(dictionary_results, path='SaveResult', filename='results_evaluator.txt'):
    li = 173
    sli = 137

    with open(path + os.sep +filename , 'w') as fichier:
        fichier.write(
            '\n\n' * 3 + ' ' * 8 + 'Table: Performance comparison for 10-fold cross validation. Training set: BAS   \n\n+' + "-" * li + "+\n")

        fichier.write(
            "|Class type | Author " + " " * 15 + "|" + " " * 31 + " evaluation  metrics " + " " * 84 + " | \n+" + "-" * li + "+")
        fichier.write("\n|" + " " * 35 + "|" + "%23s %22s %22s %22s %22s %22s" % (
        'algorithm |', 'precision |', 'accuracy |', 'f1_score |', 'recall |', 'mc |') + "\n|" + "*" * li + "|")

        for class_, value in dictionary_results.items():
            fichier.write("\n| CLASS %3s" % (class_))

            for author, algo in value.items():
                fichier.write(" |  %20s " % (author))

                for algo_name, performance in algo.items():
                    fichier.write("| %20s " % (algo_name))

                    for performance_name, value in performance.items():
                        fichier.write("| %20s " % (value))
                    fichier.write("|\n|" + " " * 35 + "+" + "-" * sli + "+ \n")
                    #fichier.write("|" + " " * 35)
                    fichier.write("|       %3s" % (' '))
            fichier.write("|\n#" + "#" * li + "#")