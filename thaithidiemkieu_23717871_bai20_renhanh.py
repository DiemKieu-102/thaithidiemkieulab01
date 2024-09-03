# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 19:54:47 2024

@author: ThaiThiDiemKieu
"""

a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))
c = int(input("Nhập số nguyên thứ ba: "))
max_value = a
if b > max_value:
    max_value = b
if c > max_value:
    max_value = c
print("Số lớn nhất trong 3 số đã nhập là:", max_value)