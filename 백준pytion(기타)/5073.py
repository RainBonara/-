while True:
    a1, a2, a3 = map(int, input().split())
    b3 = max(a1,a2,a3)
    b1 = min(a1,a2,a3)
    b2 = a1 + a2 + a3 - b1 - b3
    
    if a1 == 0:
        break
    elif b3 >= b2 + b1:
        print("Invalid")
    elif b1 == b2 == b3:
        print("Equilateral")
    elif b1 != b2 and b2 != b3 and b3 != b1:
        print("Scalene")
    else:
        print("Isosceles")
