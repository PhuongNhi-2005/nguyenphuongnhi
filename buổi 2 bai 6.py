# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 16:16:01 2024

@author: DELL
"""
#Keo bua bao 
import random
print("Chao mung ban den voi tro choi keo bua bao!")
nguoichon=input("Nhap lua chon cua ban:")
if nguoichon=="keo" or nguoichon=="bua" or nguoichon=="bao":
    print("Nguoi choi chon", nguoichon)
else:
    print("Loi! Moi nhap lai ")
maychon=random.choice(["keo", "bua", "bao"])
print("May chon:", maychon)
if nguoichon==maychon: 
    print("Hoa")
elif (nguoichon=="keo" and maychon=="bao") or (nguoichon=="bua" and maychon=="keo") or (nguoichon=="bao" and maychon=="bua"):
    print("Ban thang")
elif (maychon=="keo" and nguoichon=="bao") or (maychon=="bao" and nguoichon=="keo") or (maychon=="bao" and nguoichon=="bua"):
    print("May thang")
else:
    print("Nguoi chon sai. Khong co ket qua ")