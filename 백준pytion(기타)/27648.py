a,b,c = map(int, input().split())

if a + b - 1 <= c and 1 < a and 1 < b:
    print("YES")

    for i in range(1, a+1):
        for j in range(0, b):
            print(i + j, end = ' ')
        print()
else:
    print("NO")
