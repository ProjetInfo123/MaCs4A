# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 18:30:25 2020

@author: Azeddine ASSAGHIR & Thomas EGUIENTA
"""


#sujet 1
from random import *
import numpy.polynomial.polynomial as nppol

#fonction qui renvoie 1 si le nombre n est premier et 0 sinon
def premier(n):
    x=0
    for i in range(2, n):
        if(n%i==0):
            x=x+1

    if(x>=1):
        return 0
    else :
        return 1


#méthode qui renvoie tout les nombres premiers inférieurs à n
def pluspetitque(n):
    liste = []
    print("Les nombres premiers inférieurs à ",n," sont :")
    for i in range (2,n):
        if(premier(i)==1):
                liste.append(i)
                print(i," ")

    print("\n")
    return liste



#fontion qui va appliquer l'algorithme d'Euclide pour trouver l'inverse modulo d'un nombre représenté par b, la fonction renvoie 0 s'il n'y en pas
def algoEuclide(b,n):
    n2=n
    u=0
    v=1
    q=n2//b
    r=n2-q*b
    while(r>0):
        temp=u-q*v
        if(temp>=0):
            temp=temp%n
        else:
            temp=n-((-temp)%n)
        u=v
        v=temp
        n2=b
        b=r
        q=n2//b
        r=n2-q*b
    if(b!=1):
        return 0#b n'a pas d'inverse de modulo n
    else :
        return v

#méthode qui applique l'algorithme du reste chinois en fonction d'une liste de nombre premiers.
def restechinois(liste):
    M=1
    x=0
    n=len(liste)
    for i in liste:
        M=M*i
    for i in range(1,n):
        m=liste[i]
        N=M/m
        y=algoEuclide(N,m)
        a=randint(1,m-1)
        x=x+(a*N*y)
    x=x%M
    print("Le reste chinois est de la liste : ")
    for i in range(0,len(liste)) :
        print(liste[i])
    print("est :")
    return x

#méthode qui renvoie 1 si le polynome p est irréduction et 0 sinon
def estIrreductible(p):
    if(p.degree()==1):
        return 1
    else :
        if(p.degree()==2 and (p[1]*p[1]-4*p[2]*p[0])<0):
            return 1
        else:
            return 0


print(restechinois(pluspetitque(20)))

#méthode qui crée un polynome
def creerpoly():
    x3=randint(-10,10)
    x2=randint(-10,10)
    x1=randint(-10,10)
    x=randint(-10,10)
    p=nppol(x,x1,x2,x3)
    return p

#méthode qui remplit une liste de polynome irréductible
def listepoly(n):
    liste = []
    for i in range (1,n):
        p=creerpoly()
        if(estIrreductible(p)==1):
            liste.append(p)

    return liste
