x, y = map(int,input().split())
mini = x * 1000 / y
n = int(input())
for _ in range(n):
    x, y = map(int,input().split())
    if x * 1000 / y < mini:
        mini = x * 1000 / y
print(mini)
