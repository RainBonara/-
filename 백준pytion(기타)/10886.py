n = int(input())
t = 0

for i in range(n):
    s = int(input())
    if s:
        t += 1

if n/2 <= t:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
