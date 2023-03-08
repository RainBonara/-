task = int(input())

for i in range(task):
    sum = 0
    N = int(input())

    for _ in range(N):
        sum += int(input()) % N
        
    if sum % N:
        print("NO")
    else:
        print("YES")
