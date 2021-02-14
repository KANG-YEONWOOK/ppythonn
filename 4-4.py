a = 100                                     ##a의 초기값을 100으로 설정
result = 0                                  ##result 초기값을 0으로 설정
i = 0                                       ##i의 초기값을 0으로 설정

for i in range(1, 5) :                      ##i값이 1에서 4까지 변할 때 코드를 반복한다.
    result = a << i                         ##변수 result에 a를 왼쪽으로 i만큼 시프트한 값을 저장한다.
    print("%d << %d = %d" % (a, i, result)) ##출력한다.

for i in range(1, 5) :                      ##i값이 1에서 4까지 변할 때 코드를 반복한다.
    result = a >> i                         ##변수 result에 a를 오른쪽으로 i만큼 시프트한 값을 저장한다.
    print("%d >> %d = %d" % (a, i, result)) ##출력한다.
