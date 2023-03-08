cur_milk = 2
drink = 0

n = int(input())
point_milk = list(map(int, input().split()))

for i in range(n):
    if (cur_milk + 1) % 3 == point_milk[i]:
        drink += 1
        cur_milk = (cur_milk + 1) % 3

print(drink)
