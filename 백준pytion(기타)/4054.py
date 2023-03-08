n = int(input())

while 1 :
    i = int(input())
    if i == 0 :
        break;

    if i % n == 0 :
        print(i," is a multiple of ", n,'.', sep = '')
    else :
        print(i," is NOT a multiple of ", n,'.', sep = '')
