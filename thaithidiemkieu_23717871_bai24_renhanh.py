# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:03:51 2024

@author: ThaiThiDiemKieu
"""

h = int(input("Nhập giờ (0-23): "))
m = int(input("Nhập phút (0-59): "))
s = int(input("Nhập giây (0-59): "))
if 0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59:
    print("Thời gian hợp lệ.")
else:
    print("Thời gian không hợp lệ.")