check = False

for i in range(1, 6):
    codeName = input()

    if -1 < codeName.find('FBI'):
        print(i, end = ' ')
        check = True

if check == False:
    print("HE GOT AWAY!")
