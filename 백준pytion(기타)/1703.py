while True :
    age = int(input())

    if age == 0 :
        break;

    num = 1

    for i in range(age) :
        splitting_factor = int(input())
        remove = int(input())
        num = num * splitting_factor - remove

    print(num)
