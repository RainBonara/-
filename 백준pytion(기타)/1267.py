N = int (input())
arr = list(map(int, input().split()))
sumY = 0
sumM = 0

for i in range(N):
    Y = (arr[i] // 30 + 1) * 10
    sumY += Y

for i in range(N):
    M = (arr[i] // 60 + 1) * 15
    sumM += M

if sumY > sumM:
    print("M", sumM)
elif sumY < sumM:
    print("Y", sumY)
else:
    print("Y M", sumM)
