# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 10:41:15 2020

@author: MAEVA

"""
import copy
import random

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

def resolution(plateau):
    
    if(plateau.conflits == conflits_final):
        plateau.affichage_plateau()
        
    else:
        plateau.update_conflits()
        plateau.verification_diagonales()
        other_plateau = Plateau(N)
        other_plateau.reines = plateau.reines
        resolution(other_plateau)
        
    
resolution(plateau)
