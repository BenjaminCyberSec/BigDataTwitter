# -*- coding: utf-8 -*-
"""
@author: Bergé Benjamin, Wathelet Jolan, Anicet
"""

import csv
import numpy as np
import random
import os

"""
"""

def save_results(dictionary_results):
    li = 70

    with open('SaveResult' + os.sep + 'results_evaluator.txt', 'w') as fichier:
        print('Bon')

    with open('SaveResult' + os.sep + 'results_evaluator.txt', 'a') as fichier:
        fichier.write(
            '\n\n' * 3 + ' ' * 8 + 'Tableau : Performance comparison for 10-fold cross validation. Training set: BAS.   \n\n+' + "-" * li + "+\n")

        fichier.write("|" + " " * 35 + "| evaluation  metrics \n+" + "-" * li + "+")
        fichier.write("|\n#" + "#" * li + "#")

        for class_, value in dictionary_results.items():
            fichier.write("\n| CLASS %3s " % (class_))

            for author, algo in value.items():
                fichier.write("|  %24s " % (author))

                for algo_name, performance in algo.items():
                    fichier.write("| %15s " % (algo_name))

                    for performance_name, value in performance.items():
                        fichier.write("|%10s " % (value))
                    fichier.write("|\n+" + " " * 40 + "-" * li + "+ \n")
                    fichier.write(" " * 40)
                fichier.write(" " * 20 + "\n+")