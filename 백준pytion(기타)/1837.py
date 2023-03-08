P, K = map(int, input().split())
check = True

for i in range(2, K):
    if P % i == 0:
        print("BAD", i)
        check = False
        break

if check:
    print("GOOD")
