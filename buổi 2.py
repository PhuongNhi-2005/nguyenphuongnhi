# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 13:22:05 2024

@author: PhNhi
"""
#Khoang cach
x=float(input("Nhap do dai doan duong den truong (m):"))
if x<300:
    print("Duong den truong qua gan. Thoi! Di bo")
elif x>1200:
    print("Duong den truong qua xa. Thoi! Di xe may")
elif x>=300 and x<=700:
    print("Duong den truong khong xa. Thoi!Di xe dap")
else:
    print("Khong xac dinh")

    
    