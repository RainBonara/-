'''
A - B <= n * C
(A - B) // C <= n

A1 <= B + n1 * C
A2 <= B + n2 * C
A3 <= B + n3 * C
'''
total = 0
N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

for i in range(N):
    if A[i] <= B:
        pass
    elif (A[i] - B) % C == 0:
        total += (A[i] - B) // C
    else:
        total += (A[i] - B) // C + 1

print(total + N)
