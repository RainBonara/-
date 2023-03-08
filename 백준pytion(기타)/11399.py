save = 0
total = 0
input()
order = list(map(int, input().split()))

order.sort()

for i in order:
    save += i
    total += save

print(total)
