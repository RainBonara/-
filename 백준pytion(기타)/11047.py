import sys
input = sys.stdin.readline

count = 0
n, k = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(int(input()))

for i in range(n-1, -1, -1):
    while(k >= arr[i]):
        k -= arr[i]
        count += 1

print("%d" %(count))
