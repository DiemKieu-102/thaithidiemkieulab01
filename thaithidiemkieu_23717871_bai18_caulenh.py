# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 19:48:54 2024

@author: ThaiThiDiemKieu
"""

h1 = int(input("Nhập giờ thứ nhất: "))
m1 = int(input("Nhập phút thứ nhất: "))
s1 = int(input("Nhập giây thứ nhất: "))

h2 = int(input("Nhập giờ thứ hai: "))
m2 = int(input("Nhập phút thứ hai: "))
s2 = int(input("Nhập giây thứ hai: "))
tong_giay_1 = h1 * 3600 + m1 * 60 + s1
tong_giay_2 = h2 * 3600 + m2 * 60 + s2
tong_giay = tong_giay_1 + tong_giay_2
hieu_giay = abs(tong_giay_1 - tong_giay_2)
add_h = tong_giay // 3600
add_m = (tong_giay % 3600) // 60
add_s = tong_giay % 60
sub_h = hieu_giay  // 3600
sub_m = (hieu_giay  % 3600) // 60
sub_s = hieu_giay  % 60
print(f"Tổng thời gian: {add_h} giờ {add_m} phút {add_s} giây")
print(f"Hiệu thời gian: {sub_h} giờ {sub_m} phút {sub_s} giây")