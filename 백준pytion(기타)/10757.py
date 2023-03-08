print('몇번 테스트 하시겠습니까?.')
task = int(input())

#print('호텔의 층수와 최대호수 그리고 손님의 수를 차례로 입력하세요.')

for n in range(task):
    print('호텔의 층수와 최대호수 그리고 손님의 수를 차례로 입력하세요.')
    h, w, n = map(int, input('높이 최대호수 손님의 수 ').split())

    #h
    if n%h == 0 :
        y = h
    else:
        y = n%h

    #w
    if n%h == 0:
        x = n//h
    else :
        x = n//h+1

    print(n,"번째 손님의 호실은", 100*y+x,"호 입니다\n")

