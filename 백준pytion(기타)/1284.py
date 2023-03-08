while True:
    plus = 1
    n = int(input())
    
    if n == 0:
        break

    while n != 0:
        temp = n % 10
        n //= 10

        if temp == 0:
            plus += 5
        elif temp == 1:
            plus += 3
        else:
            plus += 4

    print(plus)
