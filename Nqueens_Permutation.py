# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 10:41:15 2020

@author: MAEVA

"""
import copy
import random
# TODO : retourner le nombre de solutions et toutes les solutions (jsp si on peut faire toutes les solutions en fait, ça a l'air compliqué)
# TODO : essayer de faire pareil pour la version prépa afin de pouvoir comparer les deux
# TODO : encodage avec SAT pour comparer les 3
# TODO : ajouter temps de résolution
# TODO : RecursionError: maximum recursion depth exceeded in comparison
# TODO : vérifier que la solution n'est pas encore dans la liste solutions avant de l'ajouter

# RSS 1 : https://www.dericbourg.net/2015/08/11/probleme-des-huit-reines/

# RSS 2 : http://www.applis.univ-tours.fr/scd/EPU_DI/2015_PFEDI_Montmirail.Valentin.pdf



class Plateau:
    def __init__(self, N):
        self.N=N
        self.reines = [0]*N
        self.conflits = [0]*N
        self.plateau=self._init_plateau_()
        
        self._init_reines_()
        self.affichage_reines()
        self.verification_diagonales()


    def _init_plateau_(self):
        # fonction qui initialise le plateau (matrice de taille N*N remplie de 0)
        plateau=[]
        for i in range(N):
            plateau.append([])
            for _ in range(N):
                plateau[i].append(0)
        return plateau
    

    def _init_reines_(self):
        # fonction qui initialise la position des reines sur le plateau 
        # la position dans la liste représente la colonne 
        # la valeur représente la ligne
        reines = random.sample(range(0,N), N)  
        self.reines = reines
    
    
    def affichage_reines(self):
        for i in range(len(self.reines)):
            ligne_reine = self.reines[i]
            self.plateau[ligne_reine][i] = 1
            


    def enlever(self,L,c):
    #fonction qui prend en argument une liste et une chaîne de caractères,
    #et qui renvoie la liste entrée sans la chaîne de caractères.
        reponse=''
        for e in L:
            if e!=c:
                reponse+=e
        return reponse
    
    
    def affichage_plateau(self):
        plateau = self.plateau
        print("\n")
        for ligne in plateau:
            ligne=self.enlever(str(ligne), ',')
            ligne=self.enlever(str(ligne), '[')
            ligne=self.enlever(str(ligne), ']')
            print(ligne)
    
    
    def update_conflits(self):
        # on a une liste conflit qui correspond au nombre de conflits pour chaque reine
        # pour la résolution de conflits on peut peut-être échanger la position (colonne) de deux reines (celle qui a le plus de conflits et une choisie aléatoirement ou non) jusqu'à ce qu'il n'y ait plus de conflits
        copy_conflits = copy.copy(self.conflits)
        max_conf = copy_conflits.index(max(copy_conflits))
        
        # permuter aléatoirement maybe
        ind_2 = random.randint(0,N-1)
        while ind_2==max_conf:
            ind_2 = random.randint(0,N-1)
            
        # copy_conflits.remove(copy_conflits[max_conf])
        # second_max = copy_conflits.index(max(copy_conflits))
        self.reines[max_conf], self.reines[ind_2] = self.reines[ind_2], self.reines[max_conf]
        
    
    
    def verification_diagonales(self):
        conflits=[]
        
        for j in range(len(self.reines)):
            i = self.reines[j]
            conf=0
            for c in range(1,N):
                if j+c<N and i+c<N:
                    if self.reines[j+c]==i+c:
                        conf+=1
                    else:
                        conf=conf
                
                if j-c>=0 and i-c>=0:
                    if self.reines[j-c]==i-c:
                        conf+=1
                    else:
                        conf=conf
        
                if j-c>=0 and i+c<N:
                    if self.reines[j-c]==i+c:
                        conf+=1
                    else:
                        conf=conf
            
                if j+c<N and i-c>=0:
                    if self.reines[j+c]==i-c:
                        conf+=1
                    else:
                        conf=conf
            
            conflits.append(conf)
            
                
        self.conflits=conflits
    

# variable globale pour un plateau de taille N*N
N=8

plateau = Plateau(N)
conflits_final = [0]*N
solutions =[]

def resolution(plateau):
    
    if(plateau.conflits == conflits_final):
        plateau.affichage_plateau()
        solutions.append(plateau)
        #print("2")
        
    else:
        plateau.update_conflits()
        plateau.verification_diagonales()
        other_plateau = Plateau(N)
        other_plateau.reines = plateau.reines
        #print("1")
        resolution(other_plateau)
        
    
    # while(plateau.conflits != conflits_final):
    #     plateau.update_conflits()
    #     plateau.verification_diagonales()
    #     other_plateau = Plateau(N)
    #     other_plateau.reines = plateau.reines
    #     resolution(other_plateau)
    #     
    # solutions.append(plateau)
    # plateau.affichage_plateau()



def mainloop():
    
    tours = 0
    solutions = []
    solutions.append(plateau)
    
    print("reines : ", plateau.reines)
    print("conflits : ", plateau.conflits)
    while(plateau.conflits != conflits_final):
        plateau.update_conflits()
        plateau.verification_diagonales()
        other_plateau = copy.deepcopy(plateau)
        solutions.append(other_plateau)
        while(other_plateau.conflits != conflits_final):
            other_plateau.update_conflits()
            other_plateau.verification_diagonales()
            
        tours +=1
        
        other_plateau.affichage_plateau()
    plateau.affichage_plateau()  
    print("\nNb solutions : ", len(solutions))      
    print("\nconflits : ",plateau.conflits)
    print("\nNombre de tours : ", tours)
        

#resolution(plateau)
#print("\nNb solutions : ", len(solutions))

mainloop()