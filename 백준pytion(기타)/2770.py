n = int(input())

for _ in range(n):
    e = int(input())

    print(e // 25, end = ' ')
    e %= 25

    print(e // 10, end = ' ')
    e %= 10
    
    print(e // 5, end = ' ')
    e %= 5

    print(e)
