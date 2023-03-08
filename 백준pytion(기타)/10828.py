print("본 프로그램을 다루면서 스택에 대해 이해하여 보세요.")
print("사용가능한 명령어는 다음과 같습니다.")
print("push, pop, len, empty, top, stop(종료)")

stack = []

while True:
    command = input()

    if command == "push":
        print("스택에 쌓을 데이터를 입력하세요.")
        data = input()
        stack.append(data)
        
    elif command == "pop":
        print("가장 위에 있는 데이터:", stack[len(stack)-1])
        stack.pop()
        
    elif command == "len":
        print("스택의 높이:", len(stack))
        
    elif command == "empty":
        if len(stack) == 0:
            print("스택은 비어있습니다.")
        else:
            print("스택은 비어있지 않습니다.")
            
    elif command == "top":
        print("가장 위에 있는 데이터:", stack[len(stack)-1])
        
    elif command == "stop":
        break
    
    else:
        print("다시 입력해 주세요.")

print(stack)
print("'스택 갖고 놀기' 프로그램이 종료되었습니다")
