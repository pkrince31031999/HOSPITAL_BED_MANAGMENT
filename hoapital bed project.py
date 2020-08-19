# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 22:08:29 2020

@author: prince pandey
"""

print("*********************HOSPITAL BED MANAGMENT************************")
N=int(input("ENTER ID:"))
P=int(input("ENTER PASSWORD:"))
if(P==N):
        print("*********WELCOME TO SHARDA HOSPITAL*************")
        print("1.ICU WARD")
        print("2.CCU WARD")
        print("3.GEN.WARD")
        print("4.VIP WARD")
        print("5.ACCOUNT/DETAILS")
        x=int(input("ENTER YOUR CHOICE:"))
else:
        print("YOU ENTERD WRONG PASSWORD")
            
