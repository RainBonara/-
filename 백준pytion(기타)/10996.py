N = int(input())

for a in range(2 * N):
    for b in range(N):
        if not (a + b) % 2:
            print(end = '*')
        else:
            print(end = ' ')
    print()
