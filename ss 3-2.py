sel = int(input("입력 진수 결정(16/10/8/2) : "))    ##입력할 수의 진수를 입력받는다.


if sel == 16 :                                  ##변수 sel이 16일 때,
    num = input("값 입력 : ")                   ##변수 num에 값을 입력받고,
    num1 = int(num, 16)                         ##num을 16진수로 나타내고 그 값을 num1에 저장한다.
elif sel == 10 :                                ##변수 sel이 10일 때,
    num = input("값 입력 : ")                   ##변수 num에 값을 입력받고,
    num1 = int(num, 10)                         ##num을 16진수로 나타내고 그 값을 num1에 저장한다.
elif sel == 8 :                                 ##변수 sel이 8일 때,
    num = input("값 입력 : ")                   ##변수 num에 값을 입력받고,
    num1 = int(num, 8)                          ##num을 16진수로 나타내고 그 값을 num1에 저장한다.
elif sel == 2 :                                 ##변수 sel이 2일 때,
    num = input("값 입력 : ")                   ##변수 num에 값을 입력받고,
    num1 = int(num, 2)                          ##num을 16진수로 나타내고 그 값을 num1에 저장한다.

else :                                              ## 변수 sel이 16,10,8,2가 아닐 때,
    print("16,10,8,2 숫자중 하나만 입력하세요!")    ##"16,10,8,2 숫자중 하나만 입력하세요!"라는 안내를 출력한다.
    input()


if sel != 16 or 10 or 8 or 2 :                      ##sel 값이 16,10,8,2일때,
    print("16진수 ==>", hex(num1))                  ##num1을 16진수, 10진수, 8진수, 2진수로 변환한 값을 출력하도록 한다.
    print("10진수 ==>", num1)
    print("8진수 ==>", oct(num1))
    print("2진수 ==>", bin(num1))
    input()                                         ##출력이 끝난뒤 결과를 확인하기위해 사용자가 임의의 키를 입력할때까지 대기한다.
