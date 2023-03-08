n = int(input())

for j in range(n):
    score = 0
    bracket = input()
    
    for i in range(len(bracket)):
        if bracket[i] == '(':
            score += 1
        else:
            score -= 1
            
            if score < 0:
                print("NO")
                break

    if 0 == score:
        print("YES")
    elif 0 < score:
        print("NO") 
