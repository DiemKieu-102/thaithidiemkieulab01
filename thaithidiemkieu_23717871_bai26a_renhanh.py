# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:14:15 2024

@author: ThaiThiDiemKieu
"""

a = int(input("Nhập số thứ nhất (a): "))
b = int(input("Nhập số thứ hai (b): "))
c = int(input("Nhập số thứ ba (c): "))
if a > b:
    temp = a
    a = b
    b = temp

if a > c:
    temp = a
    a = c
    c = temp

if b > c:
    temp = b
    b = c
    c = temp
print("Thứ tự tăng dần của ba số là:", a, b, c)