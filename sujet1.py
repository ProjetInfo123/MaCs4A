# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 18:30:25 2020

@author: Thomas
"""


#sujet 1
from random import *
import numpy.polynomial.polynomial as nppol

def premier(n):
    x=0
    for i in range(2, n):
        if(n%i==0):
            x=x+1

    if(x>=1):
        return 0
    else :
        return 1

print(premier(97))


def pluspetitque(n):
    liste = []
    print("Les nombres premiers inférieurs à ",n," sont ")
    for i in range (1,n):
        if(premier(i)==1):
                liste.append(i)
                print(i)
                print("\n")
    return liste


print(pluspetitque(150))

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
    return x


def estIrreductible(p):
    if(p.degree()==1):
        return 1
    else :
        if(p.degree()==2 and (p[1]*p[1]-4*p[2]*p[0])<0):
            return 1
        else:
            return 0


print(restechinois([7,11,13]))
