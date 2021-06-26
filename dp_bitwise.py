# -*- coding: utf-8 -*-
"""DP_bitwise.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CZf_4kU6zn9XQV4qAzBv-lUtZDcrxtdp
"""

def decimalToBinary(n):
    return "{0:b}".format(int(n))

def  countSetBits(n):
    count = 0
    while (n):
        count += n & 1
        n >>= 1
    return count

def isKthBitSet(n, k):
    if n & (1 << k):
        return 1
    else:
        return 0

def set_bit(value, bit):
    return value | (1<<bit)

def clear_bit(value, bit):
    return value & ~(1<<bit)

import math

def assign(N,cost):
  dp=[]
  dp.append(0)
  for i in range(1,int(math.pow(2,N))):
    dp.append(math.inf)
  for mask in range(0,int(math.pow(2,N))):
    x=countSetBits(mask)
    for j in range(N):
      ck=isKthBitSet(mask,j)
      if ck==0:
        dp[mask | (1<<j)] = min(dp[mask | (1<<j)], dp[mask]+cost[x][j])
  return dp[-1]

cost=[[3,2,7],[5,1,3],[2,7,2]]
N=3
xi=assign(N,cost)
print(xi)