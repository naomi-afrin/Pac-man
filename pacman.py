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
changeDirPoints = {(155, 220): ["right", "down"], (155, 280): ["right", "up"], (345, 280): ["left", "up"], (345, 220): ["left", "down"],
                   (25, 325): ["right", "up", "down"], (115, 325): ["right", "left", "up", "down"], (155, 325): ["right", "left"], (230, 325): ["right", "left", "up"], (270, 325): ["right", "left", "up"], (345, 325): ["right", "left", "down"], (385, 325): ["right", "left", "up", "down"], (475, 325): ["left", "up", "down"],
                   (25, 175): ["right", "up", "down"], (115, 175): ["right", "left", "up", "down"], (155, 175): ["right", "left"], (230, 175): ["right", "left", "down"], (270, 175): ["right", "down"], (345, 175): ["right", "left", "up"], (385, 175): ["right", "left", "up", "down"], (475, 175): ["left", "up", "down"],
                   (25, 385): ["right", "down"], (115, 385): ["right", "left", "down"], (230, 385): ["left", "down"], (270, 385): ["right", "down"], (385, 385): ["right", "left", "down"], (475, 385): ["left", "down"]
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
    while x1<y1:
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

pause=False
pac_pos=[250,325]
game=True

def drawMaze():
    global walls
    glPointSize(10)
    glColor3f(0,0,1)
    for i in walls:
        draw_line(i[0],i[1],i[2],i[3])

def draw_pacman(l):
    x,y=l
    glColor3f(1,1,0)
    draw_circle(x,y,10)


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
    update_ghost()
    glutPostRedisplay()

def specialKeyListener():
    pass

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
glutKeyboardFunc(keyboardListener)
glutMouseFunc(mouseListener)
glutMainLoop()