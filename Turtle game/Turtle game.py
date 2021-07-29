import turtle as t #turtle import 하기 
import random #random 변수 생성
import math #수식을 사용하기 위함

#기본 화면 출력
screen = t.Screen() #스크린 객체 생성
screen.bgcolor('lightgreen') #스크린 배경색 지정
screen.tracer(2) #다수의 거북이(bugs)를 생성하면 속도가 느려지므로 그래픽에서 그림을 그리는 속도를 높여준다. 

#울타리 만들기
mypen = t.Turtle() #turtle을 mypen에 저장한다. 
mypen.penup() #원하는 위치까지 펜이 이동하는데 이동하는 자국이 안남도록 펜을 들어준다.
mypen.setposition(-300, 300) #Turtle을 원하는 좌표의 위치에 도착하게 한다. 
mypen.pendown() # 원하는 위치에 펜이 도착했으면 펜을 그리기위해 내려놓는다. 
mypen.pensize(3) #pen의 선 두께 설정

for x in range(4): #x가 4번 아래조건을 반복한다. 
    mypen.forward(600) #앞으로 600만큼 이동한 후 
    mypen.right(90) #90도 회전

mypen.hideturtle() #mypen울타리를 그린 화살표가 사라지게 해준다. 


#Bug 만들기, 위치
#하나의 Bug를 위치를 지정해서 생성하려면 Turtle을 이용해서 하면 된다. 
maxBugs = 20#벌레의 갯수 지정
bugs = [] #벌레 리스트 생성
colors = ['red', 'blue', 'purple', 'white', 'black', 'pink', '#FFFF00'] #벌레의 다양한 색상을 위한 색상 리스트
shapes = ['arrow', 'blank', 'circle', 'classic', 'square', 'triangle'] #벌레의 다양한 모양을 위해 shape 리스트 생성
tcolors = ['#95B9D3', '#77ADD3', '#4497D2', '#2A84c5', '#1A5D8E', '#CE8F91', '#CB4E53', '#B4252A', '#8B1317', '#780409'] #거북이의 색상

for count in range(maxBugs):
    c = random.randint(0,6) #0 <= N <= 6 사이의 랜덤한 수를 선택 : 색상을 랜덤하게 선택
    s = random.randint(0,5) #0 <= N <= 5 사이의 랜덤한 수를 선택 : 모양을 랜덤하게 선택

    #Turtle()객체를 생성하여 bugs리스트에 하나씩 추가
    bugs.append(t.Turtle())
    bugs[count].color(colors[c])
    bugs[count].shape(shapes[s])
    bugs[count].penup()
    bugs[count].speed(0)

    bugs[count].setposition(random.randint(-300, 300), random.randint(-300, 300)) #X좌표, y좌표를 랜덤으로 생성해서 위치를 이동
    bugs[count].right(random.randint(0,360)) #0~360도까지 방향을 랜덤으로 생성

#Turtle 만들기, 기본위치
turtlesize = 1 #거북이의 크기 변수
p = t.Turtle() #Turtle 객체 p 생성
p.shape('turtle')#p 객체의 모양을 거북이로 만들기
p.turtlesize(turtlesize, turtlesize) #p 객체 크기 설정
p.color(tcolors[0]) #객체 색상 설정 (색상은 색상 이름 또는 색상 코드(#FFFFFF)등을 이용하여 설정 할 수 있다.)
p.penup() #거북이를 따라다니는 선 제거
speed = 1 #거북이의 움직임 속도

#거북이 점수
score = 0

#Turtle 위치 정의
def turnleft():
    p.left(30) #괄호 안의 값은 회전 각도

def turnright():
    p.right(30)

def increasespeed():
    global speed #speed는 모든 곳에서 샤용되어야 하므로 전역변수(global 변수)로 선언
    speed += 1

def decreasespeed():
    global speed
    speed -= 1

#점수 입력 함수
def setScore(score):
    mypen.undo()
    mypen.penup()
    mypen.hideturtle()
    mypen.setposition(-290, 310)
    scorestring = 'score : %s' %score
    mypen.write(scorestring, False, align='left', font=('Arial', 14, 'normal'))

#충돌 확인 함수
def isCollision(t1, t2):
    #수학식에서 두 점 사이의 거리(turtle과 bug사이)
    d = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))

    coll = turtlesize * 10
    if d< coll:
        return True
    else:
        return False

#키보드 입력을 통해서 Turtle 조종
screen.listen() #키보드의 입력을 기다리기 위함
screen.onkey(turnleft, "Left") #onket() : 키보드의 키를 눌렀다가 뗄 때 발생하는 이벤트
screen.onkey(turnright, "Right")#onkeypress() : 키보드를 누르고 있을 때 발생하는 이벤트 
screen.onkey(increasespeed, "Up") #screen.onkey(함수, 키보드의 키 심볼)
screen.onkey(decreasespeed, "Down") #'키보드의 키'를 눌렀다가 뗄 때, '함수'를 실행시킨다. 


#Output : 화면 내에서 turtle, bugs 들의 움직임과 상호작용
while True:
    p.forward(speed)
    # screen.mainloop() # while Ture: 문이 있으므로 screen.mainloop()문은 없애도 된다. 
    
    #Turtle 울타리에서 못나가게 하기
    if p.xcor() > 300 or p.xcor() < -300: # xcor : Turtle의 x좌표
        p.right(180) #울타리에 부딪히면 오른쪽으로 180도 회전
    if p.ycor() > 300 or p.ycor() < -300: # ycor : Turtle의 y좌표
        p.right(180) #울타리에 부딪히면 오른쪽으로 180도 회전
    
    #다수의 bugs 움직이기
    for count in range(maxBugs):
        bugs[count].forward(5)
        #bug 울타리에서 못나가게 하기
        if bugs[count].xcor() > 300 or bugs[count].xcor() < -300:
            bugs[count].right(180)
        if bugs[count].ycor() > 300 or bugs[count].ycor() < -300:
            bugs[count].right(180)
    
    
    #두 점과의 거리가 0일때 일치, 서로간의 거리가 20정도 되면 먹은 것으로 생각
        if isCollision(p, bugs[count]):
            #벌레가 먹히면 색상, 모양 변경후 다른 곳으로 이동
            bugs[count].setposition(random.randint(-300, 300), random.randint(-300, 300))
            bugs[count].right(random.randint(0,360))
            s = random.randint(0,5)
            c = random.randint(0,6)
            bugs[count].shape(shapes[s])
            bugs[count].color(colors[c])
            
            score += 1 #벌레를 먹었을 때, 점수 1 추가
            setScore(score) #점수를 표시

            #점수에 따라 거북이 크기와 색상 변경하기
            if(score%10 == 0): 
                turtlesize += 1
                if turtlesize > 30:
                    turtlesize = 30
                p.turtlesize(turtlesize, turtlesize)

                k = score // 10
                if k < 10:
                    p.color(tcolors[k])

        else:
            #벌레 못 먹음
            pass




