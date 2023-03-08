li = []
n = int(input())

for i in range(n):
    word = input()
    li.append(word)

li.append('')
li.sort()
li.sort(key = len)

for i in range(n):
    if li[i] != li[i+1]:
        print(li[i+1])
