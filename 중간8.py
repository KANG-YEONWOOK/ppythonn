answer = 0                                                     ##변수 선언
a = input('첫번째 숫자를 입력하세요')                          ##첫번째 수 입력받아 a에 저장
b = input('연산기호를 입력하세요(거듭제곱은 ^를 사용하세요!)') ##연산부호 입력받아 b에 저장
c = input('두번째 숫자를 입력하세요')                          ##두번째 수 입력받아 c에 저장

if b == '+':                        ##b가 +이면 덧셈연산후 answer에 값 저장
    answer = float(a) + float(c)
    
elif b == '-':                      ##b가 -이면 뺄셈연산후 answer에 값 저장
    answer = float(a) - float(c)
    
elif b == '*':                      ##b가 *이면 곱셈연산후 answer에 값 저장
    answer = float(a) * float(c)
    
elif b == '/':                      ##b가 /이면 나눗셈연산후 answer에 값 저장
    anwer = float(a) / float(c)
    
elif b == '^':                      ##b가 ^이면 거듭제곱후 answer에 값 저장
    answer = float(a) ** float(c)

else :                                 ##다른 모든 경우 지원하지 않는 연산이라고 출력
    print('지원하지 않는 연산입니다')


print(answer)           ##결과출력

input()
