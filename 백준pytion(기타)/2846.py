highest = 0
temp = 0
n = int(input())
terrain = list(map(int, input().split()))

for i in range(0, n - 1):
    if terrain[i] < terrain[i+1]:
        temp += terrain[i + 1] - terrain[i]
    elif terrain[i] >= terrain[i+1] and highest < temp:
        highest = temp
        temp = 0
    elif terrain[i] >= terrain[i+1] and highest > temp:
        temp = 0

if highest < temp:
    highest = temp

print(highest)
