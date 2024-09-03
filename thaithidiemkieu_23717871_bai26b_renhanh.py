# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:16:26 2024

@author: ThaiThiDIemKieu
"""

N = int(input("Nhập số nguyên N: "))
str_N = str(N)
chuoi= list(str_N)
for i in range(len(chuoi)):
    for j in range(i + 1, len(chuoi)):
        if chuoi[i] >= chuoi[j]:
            temp = chuoi[i]
            chuoi[i] = chuoi[j]
            chuoi[j] = temp
sorted_str_N = ''.join(chuoi)
sorted_number = int(sorted_str_N)
print("Số có các con số theo thứ tự tăng dần là:", sorted_number)
