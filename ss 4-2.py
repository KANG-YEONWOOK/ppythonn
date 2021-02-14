a = int(input("시프트할 숫자는?"))          ##시프트할 숫자를 입력받아 a에 저장
b = int(input("시프트할 횟수는?"))          ##시프트할 횟수를 입력받아 b에 저장
result = 0                                  ##result 초기값을 0으로 설정
i = 0                                       ##i의 초기값을 0으로 설정

for i in range(1, b+1) :                    ##i값이 1에서 b까지 변할 때 코드를 반복한다.
    result = a << i                         ##변수 result에 a를 왼쪽으로 i만큼 시프트한 값을 저장한다.
    print("%d << %d = %d" % (a, i, result)) ##출력한다.

for i in range(1, b+1) :                    ##i값이 1에서 b까지 변할 때 코드를 반복한다.
    result = a >> i                         ##변수 result에 a를 오른쪽으로 i만큼 시프트한 값을 저장한다.
    print("%d >> %d = %d" % (a, i, result)) ##출력한다.
