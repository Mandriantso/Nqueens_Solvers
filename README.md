# Nqueens_Solvers
Ce TP consistait à résoudre le problèmes des N dames. Il s'agit de placer N dames sur un plateau de taille N * N sans qu'elles ne puissent s'attaquer mutuellement.  

Ce répertoire est composé de 3 fichiers .py qui sont chacun une manière de résoudre le problème.

- **Nqueens_Permutation.py** qui consiste à placer toutes les reines sur le plateau, une reine par ligne et colonne. On calcule ensuite le nombre de conflits par reine, c'est-à-dire le nombre de reines qui peuvent l'attaquer. On fait ensuite une permutation entre la reine qui a le plus de conflits avec une reine choisie au hasard, puis on recalcule le nombre de conflits de toutes les reines. On procède ainsi jusqu'à ce que plus aucune reine ne soit en conflit.  

Cette méthode n'est pas la plus rapide et je n'ai réussi à obtenir qu'une seule solution.

- **Nqueens_SAT.py** qui consiste à réécrire le problème des N dames avec des clauses, de sorte qu'on puisse le résoudre avec un solveur SAT. Cet algorithme ne fait qu'écrire les contraintes dans un fichier **constraints.cnf** qu'on pourra ensuite exécuter avec un solveur SAT. Pour essayer, j'ai recopié les contraintes sur [CryptoMiniSat en ligne](https://msoos.github.io/cryptominisat_web/). Comme pour la méthode précédente je n'obtiens qu'une solution. Il serait intéressant d'écrire un algorithme qui permette ensuite de réécrire la solution avec un plateau constitué de 0 et de 1.

- **Nqueens_Recursion.py** consiste à poser une reine sur le plateau, déterminer toutes les cases interdites, c'est-à-dire les cases où on ne peut plus poser de reines, poser la reine suivante, mettre à jour la liste des cases interdites et ainsi de suite. A chaque fois que l'on pose une reine, on fait une copie du plateau pour tester un autre positionnement de la même reine. De ce fait, on arrive à avoir toutes les solutions possibles.
