import turtle                                           ##거북이 모듈 가져오기

## 전역 변수 선언 부분 ##
num = 0 
swidth, sheight= 1000, 300
curX, curY = 0, 0

## 메인 코드 부분 ##
if __name__ == "__main__" :                             ##메인코드 실행
    turtle.title('거북이 이진법!')                      ##프로그램제목 설정
    turtle.shape('turtle')                              ##거북이 모양설정
    turtle.setup(width=swidth+50, height=sheight+50)    ##화면창크기 설정
    turtle.screensize(swidth, sheight)                  ##화면 내부 창크기 설정
    turtle.penup()                                      ##거북이가 이동하면서 선 그리지 않음
    turtle.left(90)                                     ##거북이가 좌측으로 90도 회전

    a=int(input("숫자1을 입력하세요 : "))               ##a에 숫자1입력받음
    b=int(input("숫자2을 입력하세요 : "))               ##b에 숫자2입력받음
    c= a & b                                            ##c에 a와b의 비트 논리곱값 저장

    
    binary = bin(a)                                     ##a를 이진수로 변환
    curX = swidth / 2                                   ##거북이의 초기위치 설정
    curY = 100
    for  i  in  range(len(binary)-2) :                  ##변환한 이진수의 자릿수만큼 코드 반복
        turtle.goto( curX, curY )
        if a & 1 :                                      ##이진수가 1일 때 빨간 거북이 출력
            turtle.color('red')                         
            turtle.turtlesize(2)
        else :                                          ##이진수가 0일 떄 파란 거북이 출력
            turtle.color('blue')
            turtle.turtlesize(1)
        turtle.stamp()                                  ##거북이 도장 찍기
        curX -= 50
        a >>= 1                                         ##오른쪽 비트 하나 제거

    binary = bin(b)                                     ##b를 이진수로 변환
    curX = swidth / 2                                   ##위와 같은 작업
    curY = 0
    for  i  in  range(len(binary)-2) :
        turtle.goto( curX, curY )
        if b & 1 :
            turtle.color('red')
            turtle.turtlesize(2)
        else :
            turtle.color('blue')
            turtle.turtlesize(1)
        turtle.stamp()
        curX -= 50
        b >>= 1

    binary = bin(c)                                     ##c를 이진수로 변환
    curX = swidth / 2                                   ##마찬가지로 위와 같은 작업
    curY = -100
    for  i  in  range(len(binary)-2) :
        turtle.goto( curX, curY )
        if c & 1 :
            turtle.color('red')
            turtle.turtlesize(2)
        else :
            turtle.color('blue')
            turtle.turtlesize(1)
        turtle.stamp()
        curX -= 50
        c >>= 1
        
turtle.done()
