# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 19:29:58 2024

@author: ThaiThiDiemKieu
"""

day = int(input("Nhập ngày sinh: "))
month = int(input("Nhập tháng sinh: "))
year = int(input("Nhập năm sinh: "))
print(f"{day}/{month}/{year}")
print(f"{day}/{month}/{str(year)[-2:]}")
print(f"{year}/{month}/{day}")