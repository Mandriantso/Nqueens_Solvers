# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 17:13:59 2020

@author: MAEVA
"""

#variable globale pour un plateau de taille N*N
N=8

def plateau():
#fonction qui renvoie une liste de N sous-listes contenant chacune N*0.
    L=[]
    for i in range(N):
        L.append([])
        for _ in range(N):
            L[i].append(0)
    return L

    
def enlever(L,c):
#fonction qui prend en argument une liste et une chaîne de caractères,
#et qui renvoie la liste entrée sans la chaîne de caractères.
    reponse=''
    for e in L:
        if e!=c:
            reponse+=e
    return reponse


##Modélisation de l'échiquier:
def Affichage(L):
#fonction qui prend en argument une liste et qui affiche cette liste sans crochets ni virgules
#de telle sorte qu'on puisse modéliser un échiquier avec 0 les cases vides, et 1, les cases contenant une reine.
    if type(L)==list:
        for i in range(N):
            for j in range(N):
                if L[i][j]==2:
                    L[i][j]=0
        L+='\n'
        for a in L:
            L=enlever(str(a), ',')
            L=enlever(str(L), '[')
            L=enlever(str(L), ']')
            
            print(L)

            
##Placement des reines:
def placer_reines(L,i,j):
#fonction qui prend en argument une liste et deux entiers i et j qui sont la position 
#d'un élément dans la liste, et qui renvoie une liste avec une reine (modélisée pas 1) en position (i,j).
    if type(L)==list:
        L[i][j]=1
    return L

        
##Détermination des zones où on ne peut pas placer de reines:
def case_interdite(L,i,j):
#fonction qui prend en argument une liste et des entiers i et j, i et j donant la position d'un élément dans la liste,
#et qui renvoie une liste dans laquelle on aura ajouter des 2 pour indiquer les positions où on ne pouura pas mettre de reine. 
    for e in range(N):
        L[i][e]=2
        L[e][j]=2

        if i+e<N and j+e<N:
            L[i+e][j+e]=2
          
        if i-e>=0 and j-e>=0:
            L[i-e][j-e]=2

        if i-e>=0 and j+e<N:
            L[i-e][j+e]=2
    
        if i+e<N and j-e>=0:
            L[i+e][j-e]=2
      
    L[i][j]=1

    return L
    

    
def copier(L):
#fonction qui prend en argument une liste et qui renvoie une autre liste identique.
    L1=[]
    for i in L:
        L1.append(i[:])
    return L1


##Récursion:   
def reines(n,L):
#fonction récursive qui prend en argument un entier et deux listes, et qui affiche toutes les solutions possibles du problème des N dames
    if n==N:
        Affichage(L)
    elif n<N:
        for e in range(N):
            if L[e][n]==0:
                F=copier(L)
                placer_reines(F,e,n)
                case_interdite(F,e,n)
                reines(n+1,F)
    
Affichage(reines(0,plateau()))          