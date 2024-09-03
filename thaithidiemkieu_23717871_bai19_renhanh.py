# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 19:52:45 2024

@author: ThaiThiDiemKieu
"""

a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))
c = int(input("Nhập số nguyên thứ ba: "))
d = int(input("Nhập số nguyên thứ tư: "))
min = a
if b < min:
    min = b
if c < min:
    min= c
if d < min:
    min = d
print("Số nhỏ nhất trong 4 số đã nhập là:", min)