test = int(input())
arr = []

for i in range(test):

    for w in range(test):
        arr.append(0)
    
    num = int(input())

    for j in range(num):
        if arr[j] == 0:
            arr[j] = 1
        elif arr[j] == 1:
            arr[j] = 0

print(sum(arr))
