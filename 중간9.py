dic = {}                            ##빈 딕셔너리 dic을 만든다

while True :                        ##무한루프를 사용해 아래문장을 반복한다
    
    print('현재주소록 : ', dic)     ##현재주소록을 출력한다
    name = input('주소록에 추가하거나 제거할 사람의 이름을 입력하세요. "끝"을 입력하면 종료됩니다 \n')  ##사람이름을 입력받거나
    if name == '끝' :                                                                    ##끝을 입력받아 끝이면 프로그램을 종료하고
        break
    else :                                                                               ##그렇지 않으면
        a = input('주소록에 추가하시려면 "추가", 제거하시려면 "제거"를 입력하세요 : ')   ##추가,제거여부를 물어봐서
        if a == '추가' :                                              ##'추가'면 주소를 입력받아 딕셔너리에 추가한다
            print(name, end = '')
            address = input('님의 주소를 입력하세요 : ')
            dic[name] = str(address)

        elif a == '제거' :                                            ##'제거'이면 그사람을 딕셔너리에서 제거한다 
            del(dic[name])
            
        else :                                                        ##'추가','제거' 이외의 말이 입력되면 안내문구 출력
            print('이해할 수 없습니다.')
