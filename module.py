##1번 함수는 사람들의 키의 평균을 계산해주는 프로그램으로 제작했다.
List = []

def height() :                  ##height라는 함수에 대해 정의한다
    hap = 0
    while True :                ##무한루프를 사용해
                                ##사람들의 키를 입력받아 리스트 a에 저장하고        
        a = 0 
        a = input('평균을 구할 사람의 키를 한사람씩 입력하세요. 다됐으면 stop을 입력하세요')
        if a == 'stop' :
            break
        else :
            List.append(a)
    avg = 0
    for i in range(0, len(List)) :    ##avg에 리스트a의 각 원소들의 평균을 저장,출력하는 함수이다.
        avg = avg + float(List[i])

    avg = avg / len(List)
    print(avg)

##2번 함수는 간단하게 2번 함수가 출력되었다고 출력되는 프로그램으로 제작했다.

def num2() :
    print('2번 함수가 출력되었습니다.')

