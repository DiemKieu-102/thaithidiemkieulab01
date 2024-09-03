# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 19:58:55 2024

@author: ThaiThiDiemKieu
"""

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm.")
    else:
        print("Phương trình vô nghiệm.")
else:
    x = -b / a
    print("Phương trình có nghiệm x =", x)