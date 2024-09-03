# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 22:42:21 2024

@author: ThaiThiDiemKieu
"""

so_xe = int(input("Nhập số xe có 4 chữ số:"))
so1 = so_xe // 1000
so2 = ( so_xe //100)%10
so3 = ( so_xe //10)%10
so4 = so_xe %10
tong = so1 + so2 + so3 + so4
so_nut = tong %10
print("Số xe của bạn được", so_nut , "nút.")
 