import turtle                        ##거북이 프로그램을 위해 거북이 모듈을 가져온다.##
import random                        ##랜덤모듈을 가져온다.##

def mlc(x,y) :                       ##함수 'mlc'를 정의한다.##
    global r,g,b                     ##아래에서 기본r,g,b값을 지정하기위해 r,g,b를 전역변수로 선언한다.##
    size = random.randrange(1, 12)   ##거북이의 크기가 1에서 12까지 랜덤으로 변하게한다.##
    turtle.shapesize(size)           ####
    turtle.penup()                   ##거북이 이동경로에 선이 생기지 않도록한다.##
    turtle.goto(x,y)                 ##거북이가 마우스왼쪽클릭으로 지정한 곳으로 이동하게 한다##
    turtle.stamp()                   ##그 위치에 거북이모양 도장을 찍는다##
    turtle.color((r,g,b))            ##거북이의 색을 랜덤으로 변하게 한다.##
    r = random.random()
    g = random.random()
    b = random.random()

r,g,b = 0.0,0.0,0.0

turtle.title('거북도장찍기!')        ##프로그램 제목을 '거북도장찍기!'로 설정한다.##
turtle.shape('turtle')               ##거북이의 모양을 지정해준다.##
turtle.hideturtle()                  ##거북이의 모습을 숨겨 도장찍히는것처럼 보이게 만든다##
turtle.onscreenclick(mlc,1)          ##마우스 왼쪽클릭을하면 함수 mlc가 실행되게 한다.##
input()
