# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 19:39:49 2024

@author: ThaiThiDiemKieu
"""

h = int(input("Nhập giờ: "))
m = int(input("Nhập phút: "))
s = int(input("Nhập giây: "))
tong_giay = h * 3600 + m * 60 + s
print("Tổng số giây:", tong_giay)