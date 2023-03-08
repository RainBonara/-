'''
num = int(input())

arr = list(map)

for i in range(num):
    a = int(input())
    arr = [a]

for j in range(num):
    print(arr[j])
'''

import sys

num = int(input())
arr_list = []

for _ in range(num):
    arr_list.append(int(sys.stdin.readline()))

for i in sorted(arr_list):
    print(i)
