n1, n2, n3 = map(int, input().split())
m3 = max(n1, n2, n3)
m1 = min(n1, n2, n3)
m2 = n1 + n2 + n3 - m1 - m3

ABC = input()
for i in ABC:
    if i == 'A':
        print(m1, end = ' ')
    elif i == 'B':
        print(m2, end = ' ')
    elif i == 'C':
        print(m3, end = ' ')
