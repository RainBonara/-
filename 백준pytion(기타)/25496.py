major, n = map(int, input().split())
plus = list(map(int, input().split()))
q = 0

plus = sorted(plus)
for i in range(n):
    if major < 200:
        major += plus[i]
        q += 1
    else:
        break
    
print(q)
