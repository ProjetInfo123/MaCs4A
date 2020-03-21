# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 18:30:25 2020

@author: Thomas
"""


#sujet 1
import random

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


def pluspetitque(n,x,j):
    print("Les nombres premiers inférieurs à ",n," sont ")
    for i in range (1,n):
        if(premier(i)==1):
            if(i>x and j<3):
                x=i
                j=j+1
    print(x)
    print("\n")
    return x


print(pluspetitque(150,0,0))
m1=pluspetitque(100, 0, 0)
m2=pluspetitque(100,m1,1)
m3=pluspetitque(100, m2, 2)




def restechinois(m1,m2,m3):
    M=m1*m2*m3
    M1=M/m1
    M2=M/m2
    M3=M/m3
    y1=(1/M1)%m1
    y2=(1/M2)%m2
    y3=(1/M3)%m3
    a1=random.randint(1,m1-1)
    print("a1 ",a1)
    print("\n")
    a2=random.randint(1,m2-1)
    print("a2",a2)
    print("\n")
    a3=random.randint(1,m3-1)
    print("a3 ",a3)
    print("\n")
    res = (a1*M1*y1)+(a2*M2*y2)+(a3*M3*y3)
    return res

print(restechinois(m1,m2,m3))
