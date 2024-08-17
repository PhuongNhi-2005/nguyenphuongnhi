# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 13:43:28 2024

@author: PhNhi
"""
#Ket qua xep hang hoc luc_GPA
a=float(input("Nhap diem trung binh xep hang hoc luc:"))
if a<3.5:
    print("Hoc luc kem")
elif a>=3.5 and a<5.0:
    print("Hoc luc yeu")
elif a>=5.0 and a<7.0:
    print("Hoc luc trung binh")
elif a>=7.0 and a<8.0:
    print("Hoc luc kha")
elif a>=8.0 and a<9.0:
    print("Hoc sinh gioi")
elif a>=9.0 and a<10:
    print("Hoc sinh xuat sac")
else:
    print("Khong xac dinh")
    