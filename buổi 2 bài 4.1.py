# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 14:55:08 2024

@author: PhNhi
"""
#Bai tap tam giac 
a = float(input("Nhap canh cua a:"))
b = float(input("Nhap canh cua b:"))
c = float(input("Nhap canh cua c:"))

if a + b > c and a + c > b and b + c > a:
    #tam giác deu
    if a == b == c:
        print("la tam giac deu")
        #tam giac cân
    elif a==b or a==c or b==c:
        print("la tam giac can")
        #tam giac vuong
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print(" la tam giac vuong")
    else:
        print("la tam giac thuong")
else:
    print("a,b,c khong phai la canh cua tam giac")
        
        
                