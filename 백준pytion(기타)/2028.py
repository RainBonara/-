task = int(input())

for _ in range(task):
    a = int(input())

    if a < 10:
        c = 10
    elif a < 100:
        c = 100
    elif a < 1000:
        c = 1000
    else:
        c = 10000

    if a*a % c == a:
        print("YES")
    else:
        print("NO")
