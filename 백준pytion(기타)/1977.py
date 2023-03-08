import math

total = 0
small = int(input())
big = int(input())
small = math.ceil(math.sqrt(small))
big = math.floor(math.sqrt(big))

if big - small <= 0:
    print(-1)
else:
    for i in range(small, big+1):
        total += i**2

    print(total)
    print(small**2)
