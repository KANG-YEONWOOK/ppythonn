s = 0                                              ##변수 s의 초기값을 0으로 설정한다.

while True:                                        ##무한루프를 생성하고 현재 잔액을 출력한다.
    print('현재 계좌의 잔액은', s, '원 입니다.')
    job = input('할 작업을 선택해 숫자를 입력해 주세요. (1.입금 2.출금 3.종료) : ') ##1,2,3중 할 작업중 선택한다.
    if job == '1' :                                                    ##입금을 하려고 하면
        moneyIn = int(input('입금하실 돈의 액수를 입력해 주세요. : ')) ##액수를 입력받아
        s = s + moneyIn                                                ##계좌 잔액에 더하고
        print(moneyIn, '원이 정상적으로 입금되었습니다.')              ##안내문구를 출력한다.

    elif job == '2' :                                                   ##출금을 하려고 하면
         moneyOut = int(input('출금하실 돈의 액수를 입력해 주세요. : '))##액수를 입력받고
         if moneyOut > s :                                              ##그 액수가 계좌 잔액보다 크면
             cha = moneyOut - s                                         ##잔액부족문구를 출력한다.
             print('계좌의 잔액이', cha ,'원 부족합니다.')
         else :                                                         ##잔액이 충분할경우
             s = s - moneyOut                                           ##잔액에서 출금액만큼 빼서 잔액을 갱신하고
             print(moneyOut, '원이 정상적으로 출금되었습니다.')         ##안내문구를 출력한다.
             
    elif job == '3' :                                                   ##job이 3이면 반복문을 종료한다.           
        break
    else :                                                              ##1,2,3이 아닌 다른것이 입력되면
        print('1은 입금, 2는 출금, 3은 종료입니다. 1,2,3중 하나만 입력해주십시오.')  ##1,2,3중 하나만 입력하라는
                                                                                     ##문구를 출력한다.
    
