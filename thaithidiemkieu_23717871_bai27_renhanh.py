# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:16:50 2024

@author: ThaiThiDiemKieu
"""

import math
loai = input("Nhập loại hình (v: hình vuông, n: hình chữ nhật, t: hình tròn): ")

if loai == 'v':
    canh = float(input("Nhập cạnh của hình vuông: "))
    P = 4 * canh
    S = canh * canh
    print(f"Chu vi của hình vuông là: {P}")
    print(f"Diện tích của hình vuông là: {S}")

elif loai == 'n':
    CR = float(input("Nhập chiều rộng của hình chữ nhật: "))
    CC = float(input("Nhập chiều dài của hình chữ nhật: "))
    P = 2 * (CR + CC)
    S = CR * CC
    print(f"Chu vi của hình chữ nhật là: {P}")
    print(f"Diện tích của hình chữ nhật là: {S}")

elif loai == 't':
    BK = float(input("Nhập bán kính của hình tròn: "))
    P = 2 * math.pi * BK
    S = math.pi * BK * BK
    print(f"Chu vi của hình tròn là: {P:.2f}")
    print(f"Diện tích của hình tròn là: {S:.2f}")

else:
    print("Loại hình không hợp lệ. Vui lòng nhập 'v', 'n' hoặc 't'.")