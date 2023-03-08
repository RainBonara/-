num = 0
sen = input()

for i in range(len(sen)):
    if sen[i] == 'a' or sen[i] == 'e' or sen[i] == 'i' or sen[i] == 'o' or sen[i] == 'u':
        num += 1

print(num)
