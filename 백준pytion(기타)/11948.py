science = []
novel = []

for i in range(4):
    n = int(input())
    science.append(n)
science.sort(reverse = True)

for i in range(2):
    n = int(input())
    novel.append(n)
novel.sort(reverse = True)

sum = science[0] + science[1] + science[2] + novel[0]
print(sum)
