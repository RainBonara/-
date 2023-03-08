V = 0
N = int(input())
arr = list(map(int, input().split()))

for i in range(N):
    arr[i] /= 100
    V = V + arr[i] - V * arr[i]
    print(100 * V)
