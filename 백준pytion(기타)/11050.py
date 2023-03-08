n, r = map(int,input().split())
u = d1 = d2 = 1

for i in range(2, n+1):
    u *= i

for i in range(2, n-r+1):
    d1 *= i

for i in range(2, r+1):
    d2 *= i

print(u // d1 // d2)
