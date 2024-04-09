from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import time

## ghost info
color = {"pink": [0.996, 0.498, 1], "blue":[0.376, 1, 0.98], "orange":[1, 0.686, 0.278], "red":[0.988, 0.024, 0.024]}
ghostInfo = [ {"ghostX": 230, "ghostY": 220, "color": "pink", "dir": "left"}, 
             {"ghostX": 270, "ghostY": 220, "color": "blue", "dir": "right"},
             {"ghostX": 230, "ghostY": 280, "color": "orange", "dir": "left"},
             {"ghostX": 270, "ghostY": 280, "color": "red", "dir": "right"}]
changeDirPoints = {(25, 385): ["right", "down"], (115, 385): ["right", "left", "down"], (230, 385): ["left", "down"], (270, 385): ["right", "down"], (385, 385): ["right", "left", "down"], (475, 385): ["left", "down"],
                   (25, 325): ["right", "up", "down"], (115, 325): ["right", "left", "up", "down"], (155, 325): ["right", "left"], (230, 325): ["right", "left", "up"], (270, 325): ["right", "left", "up"], (345, 325): ["right", "left", "down"], (385, 325): ["right", "left", "up", "down"], (475, 325): ["left", "up", "down"],
                   (25, 285): ["right", "up", "down"], (115, 285): ["left", "up", "down"], (385, 285): ["right", "up", "down"], (475, 285): ["left", "up", "down"],
                   (25, 215): ["right", "up", "down"], (115, 215): ["left", "up", "down"], (385, 215): ["right", "up", "down"], (475, 215): ["left", "up", "down"],
                   (155, 220): ["right", "down"], (155, 280): ["right", "up"], (250, 280): ["right", "left", "down"], (250, 220): ["right", "left", "up"], (345, 280): ["left", "up"], (345, 220): ["left", "down"],
                   (25, 175): ["right", "up", "down"], (115, 175): ["right", "left", "up", "down"], (155, 175): ["right", "left"], (230, 175): ["left", "down"], (270, 175): ["right", "down"], (345, 175): ["right", "left", "up"], (385, 175): ["right", "left", "up", "down"], (475, 175): ["left", "up", "down"],
                   (25, 115): ["right", "up"], (115, 115): ["right", "left", "up"], (230, 115): ["right", "left", "up"], (270, 115): ["right","left", "up"], (385, 115): ["right", "left", "up"], (475, 115): ["left", "up"]       
                   }

def to_zone0(x1,y1,x2,y2,z):
    if z==1:
        m1=y1
        n1=x1
        m2=y2
        n2=x2
    elif z==2:
        m1=y1
        n1=-x1
        m2=y2
        n2=-x2
    elif z==3:
        m1=-x1
        n1=y1
        m2=-x2
        n2=y2
    elif z==4:
        m1=-x1
        n1=-y1
        m2=-x2
        n2=-y2
    elif z==5:
        m1=-y1
        n1=-x1
        m2=-y2
        n2=-x2
    elif z==6:
        m1=-y1
        n1=x1
        m2=-y2
        n2=x2
    else:
        m1=x1
        n1=-y1
        m2=x2
        n2=-y2
    return (m1,n1,m2,n2)

def from_zone0(lst,z):
    p=[]
    if z==1:
        for i in lst:
            p.append([i[1],i[0]])
    elif z==2:
        for i in lst:
            p.append([-i[1],i[0]])
    elif z==3:
        for i in lst:
            p.append([-i[0],i[1]])
    elif z==4:
        for i in lst:
            p.append([-i[0],-i[1]])
    elif z==5:
        for i in lst:
            p.append([-i[1],-i[0]])
    elif z==6:
        for i in lst:
            p.append([i[1],-i[0]])
    else:
        for i in lst:
            p.append([i[0],-i[1]])
    
    return p

def generate_points(x1,y1,x2,y2):
    x=x1
    y=y1
    p=[]
    p.append([x,y])
    a=2*(y2-y1)
    b=-2*(x2-x1)
    d=a-(x2-x1)

    while(x<x2):
        if d>0:
            x+=1
            y+=1
            d=d+a+b
        else:
            x+=1
            d=d+a
        p.append([x,y])
    p.append([x2,y2])
    return p

def draw_line(x1,y1,x2,y2):
    zone=None
    dx=x2-x1
    dy=y2-y1

    if dx>=0 and dy>=0:
        if abs(dx)>abs(dy):
            zone=0
        else:
            zone=1
    elif dx<0 and dy>0:
        if abs(dx)>abs(dy):
            zone=3
        else:
            zone=2
    elif dx<0 and dy<0:
        if abs(dx)>abs(dy):
            zone=4
        else:
            zone=5
    else:
        if abs(dx)>abs(dy):
            zone=7
        else:
            zone=6

    if zone==0:
        a=x1
        b=y1
        c=x2
        d=y2
    else:
        a,b,c,d=to_zone0(x1,y1,x2,y2,zone)


    points=generate_points(a,b,c,d)
    if zone!=0:
        points=from_zone0(points,zone)

    glPointSize(2)
    glBegin(GL_POINTS)
    for p in points:
        glVertex2f(p[0],p[1])
    glEnd()

def draw_points(x, y):
    glPointSize(10) #pixel size. by default 1 thake
    glBegin(GL_POINTS) 
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()

def circle_to_zone0(lst):
    p=[]
    for i in lst:
        x=i[1]
        y=i[0]
        p.append([x,y])
    return p
    
def circle_to_zone2(lst):
    p=[]
    for i in lst:
        p.append([-i[0],i[1]])
    return p

def circle_to_zone3(lst):
    p=[]
    for i in lst:
        p.append([-i[1],i[0]])
    return p
 
def circle_to_zone4(lst):
    p=[]
    for i in lst:
        p.append([-i[1],-i[0]])
    return p

def circle_to_zone5(lst):
    p=[]
    for i in lst:
        p.append([-i[0],-i[1]])
    return p

def circle_to_zone6(lst):
    p=[]
    for i in lst:
        p.append([i[0],-i[1]])
    return p

def circle_to_zone7(lst):
    p=[]
    for i in lst:
        p.append([i[1],-i[0]])
    return p

def draw_circle(x,y,r):
    p=[]
    
    x1=0
    y1=r
    d=1-r
    while x1<=y1:
        p.append([x1,y1])
        if d>=0:
            d=d+2*x1-2*y1+5
            x1=x1+1
            y1=y1-1
        else:
            d=d+2*x1+3
            x1=x1+1
    t1=circle_to_zone0(p)
    t2=circle_to_zone2(p)
    t3=circle_to_zone3(p)
    t4=circle_to_zone4(p)
    t5=circle_to_zone5(p)
    t6=circle_to_zone6(p)
    t7=circle_to_zone7(p)

    p=p+t1+t2+t3+t4+t5+t6+t7
    
    if x!=0 or y!=0:
        for i in p:
            i[0]=i[0]+x
            i[1]=i[1]+y

    glPointSize(2)
    glBegin(GL_POINTS)
    for i in p:
        glVertex2f(i[0],i[1])
    glEnd()


W_Height = 500
walls=[[0,410,500,410],[500,410,500,90],[0,410,0,90],[0,90,500,90],
       [10,400,245,400],[255,400,490,400],[490,400,490,100],[10,100,490,100],[10,100,10,400],
       [40,370,100,370],[40,340,100,340],[40,370,40,340],[100,340,100,370],
       [130,370,215,370],[130,340,215,340],[130,370,130,340],[215,370,215,340],[245,400,245,340],[255,400,255,340],[245,340,255,340],
       [170,310,330,310],[170,300,330,300],[330,300,330,310],[170,300,170,310],
       [285,370,370,370],[285,340,370,340],[285,370,285,340],[370,370,370,340],
       [400,370,460,370],[400,340,460,340],[400,370,400,340],[460,370,460,340],
       [40,310,100,310], [40,300,100,300],[40,310,40,300],[100,310,100,300],
       [40,270,40,230],[40,230,100,230],[100,230,100,270],[40,270,100,270],
       [40,200,40,190],[40,200,100,200],[100,200,100,190],[40,190,100,190],
       [40,160,40,130],[40,130,100,130],[100,130,100,160],[40,160,100,160],
       
       [170,200,170,190],[170,200,330,200],[170,190,245,190],[245,190,245,130],[245,130,255,130],[255,190,255,130],[255,190,330,190],[330,190,330,200],

       [360,310,370,310],[360,310,360,255],[285,255,360,255],[285,245,360,245],[285,255,285,245],[360,245,360,190],[360,190,370,190],[370,310,370,190],

       [400,310,460,310],[400,300,460,300],[400,310,400,300],[460,310,460,300],
       [285,160,370,160],[285,130,370,130],[285,160,285,130],[370,160,370,130],
       [400,270,460,270],[400,230,460,230],[400,270,400,230],[460,270,460,230],
       [400,200,460,200],[400,190,460,190],[400,200,400,190],[460,200,460,190],
       [400,160,460,160],[400,130,460,130],[400,160,400,130],[460,160,460,130],
       [130,160,130,130],[130,160,215,160],[215,160,215,130],[130,130,215,130],
       [130,310,130,190],[140,310,140,255],[130,310,140,310],[130,190,140,190],
       [140,255,215,255],[215,255,215,245],[140,245,215,245],[140,245,140,190]]

pointDots = {(25, 115): True, (115, 115): True, (475, 115): True, (385, 115): True, (25, 130): True, (115, 130): True, (475, 130): True, 
             (385, 130): True, (25, 145): True, (115, 145): True, (475, 145): True, (385, 145): True, (25, 160): True, (115, 160): True, 
             (475, 160): True, (385, 160): True, (25, 175): True, (115, 175): True, (475, 175): True, (385, 175): True, (25, 190): True, 
             (115, 190): True, (475, 190): True, (385, 190): True, (25, 205): True, (115, 205): True, (475, 205): True, (385, 205): True, 
             (25, 220): True, (115, 220): True, (475, 220): True, (385, 220): True, (25, 235): True, (115, 235): True, (475, 235): True, 
             (385, 235): True, (25, 250): True, (115, 250): True, (475, 250): True, (385, 250): True, (25, 265): True, (115, 265): True, 
             (475, 265): True, (385, 265): True, (25, 280): True, (115, 280): True, (475, 280): True, (385, 280): True, (25, 295): True, 
             (115, 295): True, (475, 295): True, (385, 295): True, (25, 310): True, (115, 310): True, (475, 310): True, (385, 310): True, 
             (25, 325): True, (115, 325): True, (475, 325): True, (385, 325): True, (25, 340): True, (115, 340): True, (475, 340): True, 
             (385, 340): True, (25, 355): True, (115, 355): True, (475, 355): True, (385, 355): True, (25, 370): True, (115, 370): True, 
             (475, 370): True, (385, 370): True, (25, 385): True, (115, 385): True, (475, 385): True, (385, 385): True, (230, 115): True, 
             (270, 115): True, (230, 130): True, (270, 130): True, (230, 145): True, (270, 145): True, (230, 160): True, (270, 160): True, 
             (230, 175): True, (270, 175): True, (242, 115): True, (258, 115): True, (230, 325): True, (270, 325): True, (230, 340): True, 
             (270, 340): True, (230, 355): True, (270, 355): True, (230, 370): True, (270, 370): True, (230, 385): True, (270, 385): True, 
             (40, 115): True, (40, 385): True, (460, 385): True, (460, 115): True, (55, 115): True, (55, 385): True, (445, 385): True, 
             (445, 115): True, (70, 115): True, (70, 385): True, (430, 385): True, (430, 115): True, (85, 115): True, (85, 385): True, 
             (415, 385): True, (415, 115): True, (100, 115): True, (100, 385): True, (400, 385): True, (400, 115): True, (130, 115): True, 
             (130, 385): True, (370, 385): True, (370, 115): True, (145, 115): True, (145, 385): True, (355, 385): True, (355, 115): True, 
             (160, 115): True, (160, 385): True, (340, 385): True, (340, 115): True, (175, 115): True, (175, 385): True, (325, 385): True, 
             (325, 115): True, (190, 115): True, (190, 385): True, (310, 385): True, (310, 115): True, (205, 115): True, (205, 385): True, 
             (295, 385): True, (295, 115): True, (220, 115): True, (220, 385): True, (280, 385): True, (280, 115): True, (40, 175): True, 
             (40, 325): True, (460, 175): True, (460, 325): True, (55, 175): True, (55, 325): True, (445, 175): True, (445, 325): True, 
             (70, 175): True, (70, 325): True, (430, 175): True, (430, 325): True, (85, 175): True, (85, 325): True, (415, 175): True, 
             (415, 325): True, (100, 175): True, (100, 325): True, (400, 175): True, (400, 325): True, (130, 175): True, (130, 325): True, 
             (370, 175): True, (370, 325): True, (145, 175): True, (145, 325): True, (355, 175): True, (355, 325): True, (160, 175): True, 
             (160, 325): True, (340, 175): True, (340, 325): True, (175, 175): True, (175, 325): True, (325, 175): True, (325, 325): True, 
             (190, 175): True, (190, 325): True, (310, 175): True, (310, 325): True, (205, 175): True, (205, 325): True, (295, 175): True, 
             (295, 325): True, (220, 175): True, (220, 325): True, (280, 175): True, (280, 325): True, (25, 212): False, (25, 288): False, 
             (475, 212): False, (475, 288): False, (40, 212): True, (40, 288): True, (460, 212): True, (460, 288): True, (55, 212): True, 
             (55, 288): True, (445, 212): True, (445, 288): True, (70, 212): True, (70, 288): True, (430, 212): True, (430, 288): True, 
             (85, 212): True, (85, 288): True, (415, 212): True, (415, 288): True, (100, 212): True, (100, 288): True, (400, 212): True, 
             (400, 288): True, (115, 212): False, (115, 288): False, (385, 212): False, (385, 288): False, (155, 280): True, (345, 280): True, 
             (155, 220): True, (345, 220): True, (155, 295): True, (345, 295): True, (155, 205): True, (345, 205): True, (155, 310): True, 
             (345, 310): True, (155, 190): True, (345, 190): True, (167, 280): True, (167, 220): True, (182, 280): True, (182, 220): True, 
             (197, 280): True, (197, 220): True, (212, 280): True, (212, 220): True, (227, 280): True, (227, 220): True, (242, 280): True, 
             (242, 220): True, (257, 280): True, (257, 220): True, (272, 280): True, (272, 220): True, (287, 280): True, (287, 220): True, 
             (302, 280): True, (302, 220): True, (317, 280): True, (317, 220): True, (332, 280): True, (332, 220): True, (242, 235): True, 
             (242, 250): True, (242, 265): True, (257, 235): True, (257, 250): True, (257, 265): True, (235, 325): False, (250, 325): False, 
             (265, 325): False, (155, 325): False, (345, 325): False, (155, 175): False, (345, 175): False}


pause=False
pac_pos=[250,325]
pac_direction = 'right'
pac_direction_command = 'right'
pac_speed = 1
pac_valid_moves = {'right' : False, 'left' : False, 'up' : False, 'down' : False}
score = 0
game=True

def drawMaze():
    global walls
    glPointSize(10)
    glColor3f(0,0,1)
    for i in walls:
        draw_line(i[0],i[1],i[2],i[3])

def draw_point_dots():
    global pointDots
    glPointSize(3)
    glColor3f(1,1,1)
    glBegin(GL_POINTS)
    for point in pointDots:
        if pointDots[point]:
            glVertex2f(*point)
    glEnd()

def draw_score():
    global score
    for i, digit in enumerate(str(score)):
        start = 20 + 40 * i, 30
        pointA = start
        pointB = pointA[0] + 30, pointA[1]
        pointC = pointA[0], pointA[1] + 20
        pointD = pointB[0], pointB[1] + 20
        pointE = pointC[0], pointC[1] + 20
        pointF = pointD[0], pointD[1] + 20
        
        if digit in "0,2,3,5,6,7,8,9":
            draw_line(*pointE, *pointF)
        if digit in "2,3,4,5,6,8,9":
            draw_line(*pointC, *pointD)
        if digit in "0,2,3,5,6,8,9":
            draw_line(*pointA, *pointB)
        if digit in "0,2,6,8":
            draw_line(*pointA, *pointC)
        if digit in "0,4,5,6,7,8,9":
            draw_line(*pointC, *pointE)
        if digit in "0,1,3,4,5,6,7,8,9":
            draw_line(*pointB, *pointD)
        if digit in "0,1,2,3,4,7,8,9":
            draw_line(*pointD, *pointF)

def draw_pacman(l):
    x,y=l
    glColor3f(1,1,0)
    draw_circle(x,y,10)

def check_valid_moves():
    global pac_pos, pac_direction, pac_speed, pac_valid_moves
    pac_valid_moves = {'right' : False, 'left' : False, 'up' : False, 'down' : False}
    x, y = pac_pos
    for i in range(1, 20+1):
        if (x+i, y) in pointDots and not pac_valid_moves["right"]:
            pac_valid_moves["right"] = True
        if (x-i, y) in pointDots and not pac_valid_moves["left"]:
            pac_valid_moves["left"] = True
        if (x, y+i) in pointDots and not pac_valid_moves["up"]:
            pac_valid_moves["up"] = True
        if (x, y-i) in pointDots and not pac_valid_moves["down"]:
            pac_valid_moves["down"] = True

def set_direction():
    global pac_direction, pac_direction_command, pac_valid_moves
    for i in pac_valid_moves:
        if pac_direction_command == i and pac_valid_moves[i]:
            pac_direction = i

def move_pacman():
    global pac_pos, pac_direction, pac_speed, pac_valid_moves
    if pac_direction == 'right' and pac_valid_moves['right']:
        pac_pos[0] += pac_speed
    elif pac_direction == 'left' and pac_valid_moves['left']:
        pac_pos[0] -= pac_speed
    elif pac_direction == 'up'  and pac_valid_moves['up']:
        pac_pos[1] += pac_speed
    elif pac_direction == 'down' and pac_valid_moves['down']:
        pac_pos[1] -= pac_speed

def collision_with_point_dots():
    global pac_pos, pointDots, score
    x, y = pac_pos
    if (x, y) in pointDots:
        if pointDots[x, y]:
            pointDots[x, y] = False
            score += 5


def draw_ghost():
    for ghost in ghostInfo:
        cl1, cl2, cl3 = color[ghost["color"]]
        glColor3f(cl1, cl2, cl3)
        draw_circle(ghost["ghostX"], ghost["ghostY"], 10)


def change_dir():
    for ghost in ghostInfo:
        for points in changeDirPoints:
            x, y = points
            if ghost["ghostX"] == x and ghost["ghostY"] == y:
                idx = random.randint(0, len(changeDirPoints[points])-1)
                ghost["dir"] = changeDirPoints[points][idx]


def update_ghost():
    change_dir()
    for ghost in ghostInfo:
        if ghost["dir"] == "right":
            ghost["ghostX"] += 1
        if ghost["dir"] == "left":
            ghost["ghostX"] -= 1
        if ghost["dir"] == "up":
            ghost["ghostY"] += 1
        if ghost["dir"] == "down":
            ghost["ghostY"] -= 1


def animate():
    check_valid_moves()
    set_direction()
    move_pacman()
    collision_with_point_dots()
    update_ghost()
    glutPostRedisplay()

def specialKeyListener(key, x, y):
    global pac_direction_command
    
    if key==GLUT_KEY_RIGHT:
        pac_direction_command = 'right'
    if key==GLUT_KEY_LEFT:
        pac_direction_command = 'left'
    if key==GLUT_KEY_UP:
        pac_direction_command = 'up'
    if key== GLUT_KEY_DOWN:
        pac_direction_command = 'down'
    
def specialKeyUpListener(key, x, y):
    global pac_direction_command, pac_direction

    if key==GLUT_KEY_RIGHT and pac_direction_command == 'right':
        pac_direction_command = pac_direction
    if key==GLUT_KEY_LEFT and pac_direction_command == 'left':
        pac_direction_command = pac_direction
    if key==GLUT_KEY_UP and pac_direction_command == 'up':
        pac_direction_command = pac_direction
    if key== GLUT_KEY_DOWN and pac_direction_command == 'down':
        pac_direction_command = pac_direction

def keyboardListener():
    pass

def coordinate_converter(x,y):
    global W_Height
    y=W_Height-y
    return x,y

def mouseListener(button, state, x, y):
    global walls, game, pause

    if button== GLUT_LEFT_BUTTON:
        print(x, y)
        if (state == GLUT_DOWN):
            x1,y1=coordinate_converter(x,y)
            
            #pause
            if 244<=x1<=256 and 465<=y1<=500:
                if pause==False:
                    pause=speed
                    speed=0
                else:
                    speed=pause
                    pause=False

            #restart
            elif 20<=x1<=45 and 465<=y1<=500:
                pass
                print("Game restarted")
            
            #exit
            elif 460<=x1<=490 and 465<=y1<=500:
                glutLeaveMainLoop()
    glutPostRedisplay()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glLoadIdentity()
    iterate()
    
    global pause, walls, game, pac_pos
    
    glPointSize(3)
    glColor3f(1, 1, 1)
    glBegin(GL_POINTS)
    
    glEnd()

    #cross
    glColor3f(1.0, .0, 0.0) 
    draw_line(460,495,490,465)
    draw_line(460,465,490,495)

    #play/pause
    if pause!=False:
        glColor3f(1.0, 0.9, 0.2)
        draw_line(246,495,246,465)
        draw_line(266,480,246,465)
        draw_line(246,495,266,480)
    else:
        glColor3f(1.0, 0.9, 0.2)
        draw_line(246,495,246,465)
        draw_line(254,495,254,465)

    #arrow
    glColor3f(0.2, 0.6, 1)
    draw_line(45,495,20,480)
    draw_line(20,480,45,465)
    draw_line(20,480,55,480)

    drawMaze()
    draw_point_dots()
    draw_score()
    draw_pacman(pac_pos)
    draw_ghost()
    
    glutSwapBuffers()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()


glutInit() 
glutInitDisplayMode(GLUT_RGBA) 
glutInitWindowSize(500, 500) 
glutInitWindowPosition(0, 0) 
wind = glutCreateWindow(b"PACMAN") 

glutDisplayFunc(showScreen) 
glutIdleFunc(animate)
glutSpecialFunc(specialKeyListener)
glutSpecialUpFunc(specialKeyUpListener)
glutKeyboardFunc(keyboardListener)
glutMouseFunc(mouseListener)
glutMainLoop()