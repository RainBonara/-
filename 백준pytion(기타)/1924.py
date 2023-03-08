month, day = map(int, input().split())
DW = {0:'SUN', 1:'MON', 2:'TUE', 3:'WED', 4:'THU', 5:'FRI', 6:'SAT'}

if month == 1 or month == 10:
    print(DW[day % 7])
elif month == 2 or month == 3 or month == 11:
    print(DW[(day + 3) % 7])
elif month == 4 or month == 7:
    print(DW[(day + 6) % 7])
elif month == 5:
    print(DW[(day + 1) % 7])
elif month == 6:
    print(DW[(day + 4)% 7])
elif month == 8:
    print(DW[(day + 2) % 7])
else
    print(DW[(day + 5) % 7])
