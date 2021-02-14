import turtle                                                   ##거북이모듈, 랜덤모듈을 임포트한다.
import random

## 전역 변수 선언 부분 ##
swidth, sheight, pSize, exitCount = 300, 300, 3, 0              ##이 프로그램 내에서 어떤함수에서나 같은값을 가지는 전역변수를 설정한다
r, g, b, angle, dist, curX, curY = [0] * 7                      ## r,g,b,angle,dist,curX,curY는 0만 있는 리스트 7개로 값을 지정한다.

## 메인 코드 부분 ##
turtle.title('거북이가 맘대로 다니기')                          ##프로그램이름을 '거북이가 맘대로 다니기'로 정한다.
turtle.shape('turtle')                                          ##거북이의 모양을 정한다.
turtle.pensize(pSize)                                           ##거북이가 그릴 선의 크기를 위에서 지정한 변수 pSize값으로 지정한다.
turtle.setup(width=swidth+30, height=sheight+30)                ##프로그램이 열릴 창의 크기를 위에서 지정한 변수 swidth,sheight값+30 으로 지정한다.
turtle.screensize(swidth, sheight)                              ##안쪽 화면크기도 지정한다.

while True :                                                    ##참일경우, 무한 반복한다.
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pencolor((r, g, b))                                  ##거북이가 그릴 선의 색을 랜덤으로 지정한다.
    
    angle = random.randrange(0,360)                             ##각도는 0~360범위에서 랜덤으로 지정한다.
    dist = random.randrange(1,100)                              ##거리는 0~100범위에서 랜덤으로 지정한다.
    turtle.left(angle)                                          ##거북이가 angle만큼 왼쪽으로 회전한다.
    turtle.forward(dist)                                        ##거북이가 dist만큼 직진한다.
    curX = turtle.xcor()                                        ##거북이의 현재위치를 구한다.
    curY = turtle.ycor()

    if (-swidth / 2 <= curX and curX <= swidth / 2) and (-sheight / 2<= curY and curY <= sheight / 2) : ##거북이의 현재위치가 화면 안임을 확인한다.
        pass                                                                                            ##화면 안이면 거북이는 계속 움직이고
                                                                                                        ##아무일도 일어나지 않는다.
    else :                                                                                              ##화면밖으로 거북이가 나갈경우
        turtle.penup()                                                                                  ##거북이가 선그리는것을 중단하고
        turtle.goto( 0, 0 )                                                                             ##화면 중앙으로 이동한 후
        turtle.pendown()                                                                                ##다시 선그리기를 시작한다.
        
        exitCount += 1                                                                                  ##거북이가 화면밖으로 나갈때마다
                                                                                                        ##exitCount가 하나씩 증가하고,
        if exitCount >= 5 :                                                                           ##exitCount가 5 이상이되면 반복문을 멈춘다.
            break
  
turtle.done()
