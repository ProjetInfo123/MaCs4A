# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 17:13:52 2020

@author: Azeddine
"""
import numpy as np
from scipy import linalg as LA



def vect_alea(n):
    A= 101*np.random.rand(n,n)
    return A

A=vect_alea(5)
print(A)


def deter(mat) :
    det=LA.det(mat)
    return det

def normaliser(v):



def orthonormaliser(mat):


print(A)

if(deter(A)) : print("La famille est une base")
else : print("la famille n'est pas une base")

Q,R=LA.qr(A)
print(Q)
print(R)




B =  np.array([[2,-2,1], [-2,2,0],[1,1,2]])
print(B)
print(deter(B))
print(orthonormaliser(B))
