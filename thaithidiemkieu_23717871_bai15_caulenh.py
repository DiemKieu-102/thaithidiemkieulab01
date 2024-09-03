# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 19:35:32 2024

@author: ThaiThiDiemKieu
"""

a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
Căn_a = a ** (1 / 3)
Căn_b = b ** (1 / 3)
Căn_ab = (a * b) ** (1 / 3)
TuSo = ((a + b) / (Căn_a + Căn_b)) - Căn_ab
MauSo = (Căn_a - Căn_b) ** 2
result = TuSo / MauSo
print("Giá trị của biểu thức là:", result)