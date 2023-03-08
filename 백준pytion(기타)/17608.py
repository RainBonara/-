arr = []
cnt = 0
n = int(input())

for i in range(n):
    data = int(input())
    arr.append(data)

arr.reverse()
biggest = arr[0]

for i in range(1, n):
    if biggest < arr[i]:
        biggest = arr[i]
        cnt += 1
       
print(cnt+1)
