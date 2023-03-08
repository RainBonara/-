task = int(input())

for _ in range(task):
    input()
    stores = list(map(int, input().split()))
    print(2 * (max(stores) - min(stores)))
