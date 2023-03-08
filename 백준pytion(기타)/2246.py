condos = []

for _ in range(int(input())):
    D, C = map(int, input().split())
    condos.append([D, C])

condos.sort()
