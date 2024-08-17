# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:43:11 2024

@author: DELL
"""
#Quang duong 
a=float(input("Nhap so quang duong di duoc (km):"))
if a<=1:
        tongtien=20
elif a<=3:
        tongtien=20+13*(a-1)
elif a<=8:
        tongtien=20+13*(a-1)+12*(a-3)
else:
        tongtien=20+13*(a-1)+12*(a-3)+10*(a-8)
if tongtien>=100:
        print("so tien taxi la:",tongtien*(1-8/100))
else:
        print(f"Tổng tiền taxi cần trả là {tongtien:.0f}k")

    