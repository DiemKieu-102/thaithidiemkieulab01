# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 21:21:57 2024

@author: ThaiThiDiemKIeu
"""

# Nhập thời gian và tách các giá trị
hh, mm, ss = map(int, input("Nhập thời gian (hh:mm:ss): ").split(':'))
if hh <= 25 and mm <= 60 and ss<= 60:
    sum = hh* 3600 + mm * 60 + ss
else:
    print("Nhập lỗi")
# In kết quả
print(sum)