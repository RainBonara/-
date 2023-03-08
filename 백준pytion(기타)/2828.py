space, back = map(int, input("스크린의 길이와 바구니의 길이를 입력하세요: ").split())
num = int(input("떨어뜨릴 사과의 갯수를 입력하세요: "))

front = 1
move_cnt = 0

print("사과를 n번 떨어뜨리세요")

for i in range(num):
    location = int(input())

    if location < front:
        move_cnt += front - location
        back -= front - location
        front = location

        print("front:", front, "back:", back, "move_cnt", move_cnt)
        
    elif back < location:
        move_cnt += location - back
        front += location - back
        back = location

        print("front:", front, "back:", back, "move_cnt", move_cnt)

    else:
        print("front:", front, "back:", back, "move_cnt", move_cnt)
        
print("사과를 모두 담기위해 움직여야하는 최소거리는 ", move_cnt,"칸입니다", sep='')

#front -= front - location
#front = front - front + location
#front = location

#back += location - back
#back = back + location - back
#back = location
