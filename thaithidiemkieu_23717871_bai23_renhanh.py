# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:00:26 2024

@author: ThaiThiDiemKieu
"""

import math
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
if a == 0:
    if b != 0:
        x = -c / b
        print("Phương trình là bậc nhất với nghiệm x =", x)
    else:
        if c != 0:
            print("Phương trình vô nghiệm.")
        else:
            print("Phương trình có vô số nghiệm.")
else:
    delta = b**2 - 4*a*c  
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("Phương trình có hai nghiệm phân biệt: x1 =", x1, "và x2 =", x2)
    elif delta == 0:
        x = -b / (2 * a)
        print("Phương trình có nghiệm kép: x =", x)
    else:
        print("Phương trình vô nghiệm.")