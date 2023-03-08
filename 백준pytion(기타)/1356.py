import sys

n = input()
n_len = len(n)
point = 0

for i in range(n_len - 1):
    left = 1
    right = 1
    point += 1
    
    for j in range(point):
        left *= int(n[j])
    for k in range(point, n_len):
        right *= int(n[k])

    if left == right:
        print("YES")
        sys.exit()

print("NO")
