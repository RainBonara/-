import sys
record = []
total = 0
N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    num, ie = map(str, sys.stdin.readline().rstrip().split())

    if num in record and ie == '0':
        record.remove(num)
    elif num not in record and ie == '1':
        record.append(num)
    else:
        total += 1

total += len(record)
print(total)
