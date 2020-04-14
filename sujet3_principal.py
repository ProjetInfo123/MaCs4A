# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 17:13:52 2020

@author: Azeddine ASSAGHIR & Thomas EGUIENTA
"""
import numpy as np
from scipy import linalg as LA



#fonction permettant de renvoyer une matrice de taille n*n comportant des nombres entiers aléatoires entre 0 et 100
def vect_alea(n):
    A= 101*np.random.rand(n,n)//1
    return A

#fonction dont le but est de retourner le déterminant de la matrice donnée en paramètre
def deter(mat) :
    det=LA.det(mat)
    return det


#fonction qui va retourner la matrice d'une base orthonormale dont la famille est donnée en paramètre sous forme de matrice
def orthonormaliser(mat):
    m,n=mat.shape
    u=[]
    t=mat[:,0]/(np.vdot(mat[:,0],mat[:,0]))**0.5
    u.append(t)
    for i in range(1,n) :
        vect=mat[:,i]
        e=vect
        for j in range(0,i):
            v=(np.vdot(u[j],vect))
            w=u[j]*v
            e=e-w
        o=e/(np.vdot(e,e))**0.5
        u.append(o)
    return u


dim=input("Entrez la dimension de la matrice souhaitée :")
A=vect_alea(int(dim))
print("\nLa matrice aléatoire est :\n")
print(A)


if(deter(A)) : print("\nLa famille est une base.\n")
else : print("\nLa famille n'est pas une base.\n")



if(deter(A)):
    print("La matrice qui représente la base orthonormée est :\n")
    bon=orthonormaliser(A)
    for i in range(0,len(bon)) :
        print(bon[i])

print("\nLa décompsition QR de la matrice est :")
Q,R=LA.qr(A)
print("\n Q:\n")
print(Q)
print("\nR:\n")
print(R)
