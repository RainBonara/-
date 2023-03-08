word = input() + ' '
cnt = 0

while True:
    if word[0] == word[cnt]:
        cnt += 1
    else:
        break

print(cnt)
