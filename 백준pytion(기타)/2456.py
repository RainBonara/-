li = [0,0,0]
cnt = [0,0,0]
n = int(input())

for _ in range(n):
    a,b,c = map(int,input().split())
    li[0] += a
    li[1] += b
    li[2] += c

    if a == 3:
        cnt[0] += 1
    elif b == 3;
        cnt[1] += 1
    else:
        cnt[2] += 1

m = max(li)

if li[0] != li[1] and li[1] != li[2] and li[2] != li[0]:
    if li[0] == m:
        print(1, m)
    elif li[1] == m:
        print(2, m)
    else:
        print(3, m)

n = max(cnt)
temp = 0

if n == cnt[0]:
    temp += 1
elif n == cnt[1]:
    temp += 1
elif n == cnt[2]:
    temp += 1

if temp == 1:
    print(, )
