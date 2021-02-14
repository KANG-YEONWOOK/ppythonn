age = int(input("당신의 나이를 입력하세요 : "))  ##age에 나이를 입력받아 나이에 따라
                                        ##사람의 성장상태를 구분하는 프로그램을 만들었다.

if age < 6 :                     ##만약 age가 6이하이면 '유아입니다'를 출력한다.
    print('유아 입니다.')

elif age < 12 :                  ##elif문은 위의 if문에서 참이되지않은 부분을 처리한다.
    print('어린이 입니다.')      ##따라서 여기 elif문은 단순히 age가 12이하일때가 아닌
                                 ## 6 < age < 12 일 때 실행된다.
elif age < 18 :
    print('청소년 입니다.')

elif age < 35 :
    print('청년기 입니다.')

elif age < 60 :
    print('중년기 입니다.')

elif age < 70 :
    print('장년기 입니다.')

else :                           ##else문은 위의 if문과 elif문이 모두 거짓인 경우에
    print('노년기 입니다.')      ##실행된다.
