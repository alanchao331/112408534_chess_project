# -*- coding: utf-8 -*-
"""P1_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ofItkDsOybZomdyuD68hqK5w_f36pa9z
"""

x1, y1 = input().split()
x2, y2 = input().split()
if (x1, y1) == (x2, y2):
  print('No')
if 0 <= int(x2) <= 7 and 0 <= int(y2) <= 7:
  if abs(int(x1) - int(x2)) <= 1 and abs(int(y1) - int(y2)) <= 1:
    if checkerboard[int(x2)][int(y2)] == 0:
      print('Yes')
    else:
      print('No')
  else:
    print('No')
else:
  print('No')

#if checkerboard[int(x1)][int(y1)] != checkerboard[int(x2)][int(y2)] and checkerboard[int(x2)][int(y2)] != 1 :
#if (int(x1) - int(x2) == 1 or int(x1) - int(x2) == -1 or int(x1) == int(x2)) and (int(y1) - int(y2) == 1 or int(y1) - int(y2) == -1 or int(y1) == int(y2)):