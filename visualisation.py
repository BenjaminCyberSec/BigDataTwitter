# -*- coding: utf-8 -*-
"""
@author: Bergé Benjamin, Wathelet Jolan, Anicet
"""
import os

"""
"""

def save_results(dictionary_results):
    li = 127
    sli = 91

    with open('SaveResult' + os.sep + 'results_evaluator.txt', 'w') as fichier:
        fichier.write(
            '\n\n' * 3 + ' ' * 8 + 'Tableau_2: estimation du niveau de proximiter entre les pays en fonction des caractiristique   \n\n+' + "-" * li + "+\n")

        fichier.write(
            "|Class type | Author " + " " * 15 + "|" + " " * 31 + " evaluation  metrics " + " " * 38 + " | \n+" + "-" * li + "+")
        fichier.write("\n|" + " " * 35 + "|" + "%23s %22s %22s %22s " % (
        'algorithm |', 'precision |', 'accuracy |', 'f1_score |') + "\n|" + "*" * li + "|")

        for class_, value in dictionary_results.items():
            fichier.write("\n| CLASS %3s" % (class_))

            for author, algo in value.items():
                fichier.write(" |  %20s " % (author))

                for algo_name, performance in algo.items():
                    fichier.write("| %20s " % (algo_name))

                    for performance_name, value in performance.items():
                        fichier.write("| %20s " % (value))
                    fichier.write("|\n|" + " " * 35 + "+" + "-" * sli + "+ \n")
                    fichier.write("|" + " " * 35)
            fichier.write("|\n#" + "#" * li + "#")