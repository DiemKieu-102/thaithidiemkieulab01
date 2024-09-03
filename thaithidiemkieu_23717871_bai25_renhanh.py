# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:07:18 2024

@author: ThaiThiDiemKieu
"""

c = input("Nhập vào một chữ cái: ")
if c.islower():
    KyTu_chuyen = c.upper()
    print("Chữ cái đã chuyển đổi:", KyTu_chuyen)
elif c.isupper():
    KyTu_chuyen = c.lower()
    print("Chữ cái đã chuyển đổi:", KyTu_chuyen)
else:
    print("Ký tự không hợp lệ. Vui lòng nhập một chữ cái.")