from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import time

## ghost info
color = {"pink": [0.996, 0.498, 1], "blue": [0.278, 0.729, 0.988], "orange": [1, 0.686, 0.278],
         "red": [0.988, 0.024, 0.024], "white": [1, 1, 1], "black": [0, 0, 0], "dark_blue": [0.059, 0.075, 0.839]}

changeDirPoints = {(25, 385): ["right", "down"], (115, 385): ["right", "left", "down"], (230, 385): ["left", "down"],
                   (270, 385): ["right", "down"], (385, 385): ["right", "left", "down"], (475, 385): ["left", "down"],
                   (25, 325): ["right", "up", "down"], (115, 325): ["right", "left", "up", "down"],
                   (155, 325): ["right", "left"], (230, 325): ["right", "left", "up"],
                   (270, 325): ["right", "left", "up"], (345, 325): ["right", "left", "down"],
                   (385, 325): ["right", "left", "up", "down"], (475, 325): ["left", "up", "down"],
                   (25, 285): ["right", "up", "down"], (115, 285): ["left", "up", "down"],
                   (385, 285): ["right", "up", "down"], (475, 285): ["left", "up", "down"],
                   (25, 215): ["right", "up", "down"], (115, 215): ["left", "up", "down"],
                   (385, 215): ["right", "up", "down"], (475, 215): ["left", "up", "down"],
                   (155, 220): ["right", "down"], (155, 280): ["right", "up"], (250, 280): ["right", "left", "down"],
                   (250, 220): ["right", "left", "up"], (345, 280): ["left", "up"], (345, 220): ["left", "down"],
                   (25, 175): ["right", "up", "down"], (115, 175): ["right", "left", "up", "down"],
                   (155, 175): ["right", "left"], (230, 175): ["left", "down"], (270, 175): ["right", "down"],
                   (345, 175): ["right", "left", "up"], (385, 175): ["right", "left", "up", "down"],
                   (475, 175): ["left", "up", "down"],
                   (25, 115): ["right", "up"], (115, 115): ["right", "left", "up"], (230, 115): ["right", "left", "up"],
                   (270, 115): ["right", "left", "up"], (385, 115): ["right", "left", "up"], (475, 115): ["left", "up"]
                   }


def ghost_initial():
    global ghostInfo, setGhostMouth, GhostMouthRad, powerUpMode
    ghostInfo = [{"ghostX": 230, "ghostY": 220, "color": "pink", "dir": "left"},
                 {"ghostX": 270, "ghostY": 220, "color": "blue", "dir": "right"},
                 {"ghostX": 230, "ghostY": 280, "color": "orange", "dir": "left"},
                 {"ghostX": 270, "ghostY": 280, "color": "red", "dir": "right"}]
    setGhostMouth = time.time()
    GhostMouthRad = 2
    powerUpMode = False


def pacman_initial():
    global lifeCount, pointDots, totalPointDots, powerUpPoints, blink_counter, pause, pac_pos, pac_size, pac_direction, pac_direction_command, pac_speed, pac_valid_moves, power_up, power_up_time, game_won, game_over, score, game, lifeCount, eat, cherry_start, cherries, cherry
    lifeCount = 3
    pointDots = {(25, 115): True, (115, 115): True, (475, 115): True, (385, 115): True, (25, 130): True,
                 (115, 130): True, (475, 130): True,
                 (385, 130): True, (25, 145): True, (115, 145): True, (475, 145): True, (385, 145): True,
                 (25, 160): True, (115, 160): True,
                 (475, 160): True, (385, 160): True, (25, 175): True, (115, 175): True, (475, 175): True,
                 (385, 175): True, (25, 190): True,
                 (115, 190): True, (475, 190): True, (385, 190): True, (25, 205): True, (115, 205): True,
                 (475, 205): True, (385, 205): True,
                 (25, 220): True, (115, 220): True, (475, 220): True, (385, 220): True, (25, 235): True,
                 (115, 235): True, (475, 235): True,
                 (385, 235): True, (25, 250): True, (115, 250): True, (475, 250): True, (385, 250): True,
                 (25, 265): True, (115, 265): True,
                 (475, 265): True, (385, 265): True, (25, 280): True, (115, 280): True, (475, 280): True,
                 (385, 280): True, (25, 295): True,
                 (115, 295): True, (475, 295): True, (385, 295): True, (25, 310): True, (115, 310): True,
                 (475, 310): True, (385, 310): True,
                 (25, 325): True, (115, 325): True, (475, 325): True, (385, 325): True, (25, 340): True,
                 (115, 340): True, (475, 340): True,
                 (385, 340): True, (25, 355): True, (115, 355): True, (475, 355): True, (385, 355): True,
                 (25, 370): True, (115, 370): True,
                 (475, 370): True, (385, 370): True, (25, 385): True, (115, 385): True, (475, 385): True,
                 (385, 385): True, (230, 115): True,
                 (270, 115): True, (230, 130): True, (270, 130): True, (230, 145): True, (270, 145): True,
                 (230, 160): True, (270, 160): True,
                 (230, 175): True, (270, 175): True, (242, 115): True, (258, 115): True, (230, 325): True,
                 (270, 325): True, (230, 340): True,
                 (270, 340): True, (230, 355): True, (270, 355): True, (230, 370): True, (270, 370): True,
                 (230, 385): True, (270, 385): True,
                 (40, 115): True, (40, 385): True, (460, 385): True, (460, 115): True, (55, 115): True, (55, 385): True,
                 (445, 385): True,
                 (445, 115): True, (70, 115): True, (70, 385): True, (430, 385): True, (430, 115): True,
                 (85, 115): True, (85, 385): True,
                 (415, 385): True, (415, 115): True, (100, 115): True, (100, 385): True, (400, 385): True,
                 (400, 115): True, (130, 115): True,
                 (130, 385): True, (370, 385): True, (370, 115): True, (145, 115): True, (145, 385): True,
                 (355, 385): True, (355, 115): True,
                 (160, 115): True, (160, 385): True, (340, 385): True, (340, 115): True, (175, 115): True,
                 (175, 385): True, (325, 385): True,
                 (325, 115): True, (190, 115): True, (190, 385): True, (310, 385): True, (310, 115): True,
                 (205, 115): True, (205, 385): True,
                 (295, 385): True, (295, 115): True, (220, 115): True, (220, 385): True, (280, 385): True,
                 (280, 115): True, (40, 175): True,
                 (40, 325): True, (460, 175): True, (460, 325): True, (55, 175): True, (55, 325): True,
                 (445, 175): True, (445, 325): True,
                 (70, 175): True, (70, 325): True, (430, 175): True, (430, 325): True, (85, 175): True, (85, 325): True,
                 (415, 175): True,
                 (415, 325): True, (100, 175): True, (100, 325): True, (400, 175): True, (400, 325): True,
                 (130, 175): True, (130, 325): True,
                 (370, 175): True, (370, 325): True, (145, 175): True, (145, 325): True, (355, 175): True,
                 (355, 325): True, (160, 175): True,
                 (160, 325): True, (340, 175): True, (340, 325): True, (175, 175): True, (175, 325): True,
                 (325, 175): True, (325, 325): True,
                 (190, 175): True, (190, 325): True, (310, 175): True, (310, 325): True, (205, 175): True,
                 (205, 325): True, (295, 175): True,
                 (295, 325): True, (220, 175): True, (220, 325): True, (280, 175): True, (280, 325): True,
                 (25, 212): False, (25, 288): False,
                 (475, 212): False, (475, 288): False, (40, 212): True, (40, 288): True, (460, 212): True,
                 (460, 288): True, (55, 212): True,
                 (55, 288): True, (445, 212): True, (445, 288): True, (70, 212): True, (70, 288): True,
                 (430, 212): True, (430, 288): True,
                 (85, 212): True, (85, 288): True, (415, 212): True, (415, 288): True, (100, 212): True,
                 (100, 288): True, (400, 212): True,
                 (400, 288): True, (115, 212): False, (115, 288): False, (385, 212): False, (385, 288): False,
                 (155, 280): True, (345, 280): True,
                 (155, 220): True, (345, 220): True, (155, 295): True, (345, 295): True, (155, 205): True,
                 (345, 205): True, (155, 310): True,
                 (345, 310): True, (155, 190): True, (345, 190): True, (167, 280): True, (167, 220): True,
                 (182, 280): True, (182, 220): True,
                 (197, 280): True, (197, 220): True, (212, 280): True, (212, 220): True, (227, 280): True,
                 (227, 220): True, (242, 280): True,
                 (242, 220): True, (257, 280): True, (257, 220): True, (272, 280): True, (272, 220): True,
                 (287, 280): True, (287, 220): True,
                 (302, 280): True, (302, 220): True, (317, 280): True, (317, 220): True, (332, 280): True,
                 (332, 220): True, (242, 235): True,
                 (242, 250): True, (242, 265): True, (257, 235): True, (257, 250): True, (257, 265): True,
                 (235, 325): False, (250, 325): False,
                 (265, 325): False, (155, 325): False, (345, 325): False, (155, 175): False, (345, 175): False}

    totalPointDots = len(dict(filter(lambda x: (x[1] == True), pointDots.items())))
    powerUpPoints = [(25, 115), (25, 385), (475, 115), (475, 385)]
    blink_counter = 0

    cherries = [[115, 385], [385, 115], [430, 325], [70, 285], [350, 285],
                [475, 285], [115, 223], [170, 223], [385, 223], [25, 175],
                [270, 175], [475, 195], [115, 115], [330, 115]]

    pause = False
    pac_pos = [250, 325]
    pac_size = 10
    pac_direction = 'right'
    pac_direction_command = 'right'
    pac_speed = 1
    pac_valid_moves = {'right': False, 'left': False, 'up': False, 'down': False}
    power_up = False
    power_up_time = 0
    game_won = False
    game_over = False
    score = 0
    game = True
    eat = False
    cherry_start = time.time()
    cherry = False


def to_zone0(x1, y1, x2, y2, z):
    if z == 1:
        m1 = y1
        n1 = x1
        m2 = y2
        n2 = x2
    elif z == 2:
        m1 = y1
        n1 = -x1
        m2 = y2
        n2 = -x2
    elif z == 3:
        m1 = -x1
        n1 = y1
        m2 = -x2
        n2 = y2
    elif z == 4:
        m1 = -x1
        n1 = -y1
        m2 = -x2
        n2 = -y2
    elif z == 5:
        m1 = -y1
        n1 = -x1
        m2 = -y2
        n2 = -x2
    elif z == 6:
        m1 = -y1
        n1 = x1
        m2 = -y2
        n2 = x2
    else:
        m1 = x1
        n1 = -y1
        m2 = x2
        n2 = -y2
    return (m1, n1, m2, n2)


def from_zone0(lst, z):
    p = []
    if z == 1:
        for i in lst:
            p.append([i[1], i[0]])
    elif z == 2:
        for i in lst:
            p.append([-i[1], i[0]])
    elif z == 3:
        for i in lst:
            p.append([-i[0], i[1]])
    elif z == 4:
        for i in lst:
            p.append([-i[0], -i[1]])
    elif z == 5:
        for i in lst:
            p.append([-i[1], -i[0]])
    elif z == 6:
        for i in lst:
            p.append([i[1], -i[0]])
    else:
        for i in lst:
            p.append([i[0], -i[1]])

    return p


def generate_points(x1, y1, x2, y2):
    x = x1
    y = y1
    p = []
    p.append([x, y])
    a = 2 * (y2 - y1)
    b = -2 * (x2 - x1)
    d = a - (x2 - x1)

    while (x < x2):
        if d > 0:
            x += 1
            y += 1
            d = d + a + b
        else:
            x += 1
            d = d + a
        p.append([x, y])
    p.append([x2, y2])
    return p


def draw_line(x1, y1, x2, y2, pointSize=2):
    zone = None
    dx = x2 - x1
    dy = y2 - y1

    if dx >= 0 and dy >= 0:
        if abs(dx) > abs(dy):
            zone = 0
        else:
            zone = 1
    elif dx < 0 and dy > 0:
        if abs(dx) > abs(dy):
            zone = 3
        else:
            zone = 2
    elif dx < 0 and dy < 0:
        if abs(dx) > abs(dy):
            zone = 4
        else:
            zone = 5
    else:
        if abs(dx) > abs(dy):
            zone = 7
        else:
            zone = 6

    if zone == 0:
        a = x1
        b = y1
        c = x2
        d = y2
    else:
        a, b, c, d = to_zone0(x1, y1, x2, y2, zone)

    points = generate_points(a, b, c, d)
    if zone != 0:
        points = from_zone0(points, zone)

    glPointSize(pointSize)
    glBegin(GL_POINTS)
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()


def draw_points(x, y, pointSize=2):
    glPointSize(pointSize)  # pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x, y)  # jekhane show korbe pixel
    glEnd()


def circle_to_zone0(lst):
    p = []
    for i in lst:
        x = i[1]
        y = i[0]
        p.append([x, y])
    return p


def circle_to_zone2(lst):
    p = []
    for i in lst:
        p.append([-i[0], i[1]])
    return p


def circle_to_zone3(lst):
    p = []
    for i in lst:
        p.append([-i[1], i[0]])
    return p


def circle_to_zone4(lst):
    p = []
    for i in lst:
        p.append([-i[1], -i[0]])
    return p


def circle_to_zone5(lst):
    p = []
    for i in lst:
        p.append([-i[0], -i[1]])
    return p


def circle_to_zone6(lst):
    p = []
    for i in lst:
        p.append([i[0], -i[1]])
    return p


def circle_to_zone7(lst):
    p = []
    for i in lst:
        p.append([i[1], -i[0]])
    return p


def draw_circle(x, y, r):
    p = []

    x1 = 0
    y1 = r
    d = 1 - r
    while x1 <= y1:
        p.append([x1, y1])
        if d >= 0:
            d = d + 2 * x1 - 2 * y1 + 5
            x1 = x1 + 1
            y1 = y1 - 1
        else:
            d = d + 2 * x1 + 3
            x1 = x1 + 1
    t1 = circle_to_zone0(p)
    t2 = circle_to_zone2(p)
    t3 = circle_to_zone3(p)
    t4 = circle_to_zone4(p)
    t5 = circle_to_zone5(p)
    t6 = circle_to_zone6(p)
    t7 = circle_to_zone7(p)

    p = p + t1 + t2 + t3 + t4 + t5 + t6 + t7

    if x != 0 or y != 0:
        for i in p:
            i[0] = i[0] + x
            i[1] = i[1] + y

    glPointSize(2)
    glBegin(GL_POINTS)
    for i in p:
        glVertex2f(i[0], i[1])
    glEnd()


def draw_cross():
    pointSize = 4
    glColor3f(1.0, .0, 0.0)
    draw_line(460, 495, 490, 465, pointSize)
    draw_line(460, 465, 490, 495, pointSize)


def draw_play():
    glColor3f(0, 1, 0)
    pointSize = 4
    draw_line(246, 495, 246, 465, pointSize)
    draw_line(266, 480, 246, 465, pointSize)
    draw_line(246, 495, 266, 480, pointSize)


def draw_pause():
    glColor3f(1, 1, 0)
    pointSize = 3
    draw_line(245, 495, 245, 465, pointSize)
    draw_line(255, 495, 255, 465, pointSize)


def draw_pause_or_play(pause):
    if pause == True:
        draw_play()
    else:
        draw_pause()


def draw_replay():
    pointSize = 4
    glColor3f(0, 1, 1)
    draw_line(45, 495, 20, 480, pointSize)
    draw_line(20, 480, 45, 465, pointSize)
    draw_line(20, 480, 55, 480, pointSize)


def initiate_cherry():
    global cherry, cherries, cherry_start
    if cherry == False and (time.time() - cherry_start) >= 15 and pause == False:
        cherry = random.choice(cherries)
        cherry_start = time.time()

    if cherry != False:
        draw_cherry(cherry)
        eat_cherry()
        if (time.time() - cherry_start) >= 6.0 and pause == False:
            cherry = False
            cherry_start = time.time()


def draw_cherry(c):
    x, y = c
    glColor3f(1, 0, 0)
    for i in range(1, 6):
        draw_circle(x - 5, y - 4, i)
        draw_circle(x + 5, y - 4, i)
    glColor3f(0.9, 0.5, 0.4)
    draw_circle(x - 5, y - 4, 5)
    draw_circle(x + 5, y - 4, 5)
    glColor3f(0, 1, 0)
    glPointSize(1)
    draw_line(x - 3, y, x, y + 7)
    draw_line(x + 3, y, x, y + 7)
    glColor3f(1, 1, 1)
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2f(x - 3, y - 2)
    glVertex2f(x + 8, y - 2)
    glEnd()


def eat_cherry():
    global cherry, pac_pos, score
    p_x, p_y = pac_pos

    c_x, c_y = cherry
    if c_x - 10 <= p_x <= c_x + 10 and c_y - 10 <= p_y <= c_y + 10:
        score += 30
        cherry = False



def draw_pac_circle(x, y, r):
    global pac_direction
    p = []

    x1 = 0
    y1 = r
    d = 1 - r
    while x1 <= y1:
        p.append([x1, y1])
        if d >= 0:
            d = d + 2 * x1 - 2 * y1 + 5
            x1 = x1 + 1
            y1 = y1 - 1
        else:
            d = d + 2 * x1 + 3
            x1 = x1 + 1
    t1 = circle_to_zone0(p)
    t2 = circle_to_zone2(p)
    t3 = circle_to_zone3(p)
    t4 = circle_to_zone4(p)
    t5 = circle_to_zone5(p)
    t6 = circle_to_zone6(p)
    t7 = circle_to_zone7(p)

    if pac_direction == 'right':
        p = p + t2 + t3 + t4 + t5 + t6
    elif pac_direction == 'left':
        p = p + t1 + t2 + t5 + t6 + t7
    elif pac_direction == 'up':
        p = t1 + t3 + t4 + t5 + t6 + t7
    elif pac_direction == 'down':
        p = p + t1 + t2 + t3 + t4 + t7

    if x != 0 or y != 0:
        for i in p:
            i[0] = i[0] + x
            i[1] = i[1] + y

    glPointSize(2)
    glBegin(GL_POINTS)
    for i in p:
        glVertex2f(i[0], i[1])
    glEnd()


W_Height = 500
walls = [[0, 410, 500, 410], [500, 410, 500, 90], [0, 410, 0, 90], [0, 90, 500, 90],
         [10, 400, 245, 400], [255, 400, 490, 400], [490, 400, 490, 100], [10, 100, 490, 100], [10, 100, 10, 400],
         [40, 370, 100, 370], [40, 340, 100, 340], [40, 370, 40, 340], [100, 340, 100, 370],
         [130, 370, 215, 370], [130, 340, 215, 340], [130, 370, 130, 340], [215, 370, 215, 340], [245, 400, 245, 340],
         [255, 400, 255, 340], [245, 340, 255, 340],
         [170, 310, 330, 310], [170, 300, 330, 300], [330, 300, 330, 310], [170, 300, 170, 310],
         [285, 370, 370, 370], [285, 340, 370, 340], [285, 370, 285, 340], [370, 370, 370, 340],
         [400, 370, 460, 370], [400, 340, 460, 340], [400, 370, 400, 340], [460, 370, 460, 340],
         [40, 310, 100, 310], [40, 300, 100, 300], [40, 310, 40, 300], [100, 310, 100, 300],
         [40, 270, 40, 230], [40, 230, 100, 230], [100, 230, 100, 270], [40, 270, 100, 270],
         [40, 200, 40, 190], [40, 200, 100, 200], [100, 200, 100, 190], [40, 190, 100, 190],
         [40, 160, 40, 130], [40, 130, 100, 130], [100, 130, 100, 160], [40, 160, 100, 160],

         [170, 200, 170, 190], [170, 200, 330, 200], [170, 190, 245, 190], [245, 190, 245, 130], [245, 130, 255, 130],
         [255, 190, 255, 130], [255, 190, 330, 190], [330, 190, 330, 200],

         [360, 310, 370, 310], [360, 310, 360, 255], [285, 255, 360, 255], [285, 245, 360, 245], [285, 255, 285, 245],
         [360, 245, 360, 190], [360, 190, 370, 190], [370, 310, 370, 190],

         [400, 310, 460, 310], [400, 300, 460, 300], [400, 310, 400, 300], [460, 310, 460, 300],
         [285, 160, 370, 160], [285, 130, 370, 130], [285, 160, 285, 130], [370, 160, 370, 130],
         [400, 270, 460, 270], [400, 230, 460, 230], [400, 270, 400, 230], [460, 270, 460, 230],
         [400, 200, 460, 200], [400, 190, 460, 190], [400, 200, 400, 190], [460, 200, 460, 190],
         [400, 160, 460, 160], [400, 130, 460, 130], [400, 160, 400, 130], [460, 160, 460, 130],
         [130, 160, 130, 130], [130, 160, 215, 160], [215, 160, 215, 130], [130, 130, 215, 130],
         [130, 310, 130, 190], [140, 310, 140, 255], [130, 310, 140, 310], [130, 190, 140, 190],
         [140, 255, 215, 255], [215, 255, 215, 245], [140, 245, 215, 245], [140, 245, 140, 190]]


def drawMaze():
    global walls
    glPointSize(10)
    glColor3f(0, 0, 1)
    for i in walls:
        draw_line(i[0], i[1], i[2], i[3])


def draw_point_dots():
    global pointDots, powerUpPoints, blink_counter
    glColor3f(1, 1, 1)
    for point in pointDots:
        if pointDots[point]:
            if point in powerUpPoints:
                if blink_counter < 5:
                    for i in range(5):
                        draw_circle(*point, i + 1)
            else:
                draw_circle(*point, 1)


def draw_score():
    global score
    glColor3f(1, 1, 1)
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
    global pac_size, eat
    x, y = l
    glColor3f(1, 1, 0)
    if eat == False:
        for i in range(pac_size):
            draw_pac_circle(x, y, i + 1)
    else:
        draw_pac_eating(l)
        eat = False
    draw_pac_eyes()


def draw_pac_eating(l):
    global pac_size
    x, y = l
    glColor3f(1, 1, 0)
    for i in range(pac_size):
        draw_circle(x, y, i + 1)


def draw_pac_eyes():
    global pac_direction, pac_pos
    x, y, r = *pac_pos, 1
    if pac_direction == 'right' or pac_direction == 'left':
        y += 5
    elif pac_direction == 'up':
        x -= 5
    elif pac_direction == 'down':
        x += 5
    glColor3f(0, 0, 0)
    draw_circle(x, y, r)


def check_valid_moves():
    global pac_pos, pac_direction, pac_speed, pac_valid_moves
    pac_valid_moves = {'right': False, 'left': False, 'up': False, 'down': False}
    x, y = pac_pos
    for i in range(1, 20 + 1):
        if (x + i, y) in pointDots and not pac_valid_moves["right"]:
            pac_valid_moves["right"] = True
        if (x - i, y) in pointDots and not pac_valid_moves["left"]:
            pac_valid_moves["left"] = True
        if (x, y + i) in pointDots and not pac_valid_moves["up"]:
            pac_valid_moves["up"] = True
        if (x, y - i) in pointDots and not pac_valid_moves["down"]:
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
    elif pac_direction == 'up' and pac_valid_moves['up']:
        pac_pos[1] += pac_speed
    elif pac_direction == 'down' and pac_valid_moves['down']:
        pac_pos[1] -= pac_speed


def collision_with_point_dots():
    global pac_pos, pac_size, pointDots, score, totalPointDots, powerUpPoints, power_up, power_up_time, game_won, eat
    x, y = pac_pos
    if (x, y) in pointDots:
        if pointDots[x, y]:
            pointDots[x, y] = False
            if (x, y) in powerUpPoints:
                power_up = True
                pac_size = 12
                powerUp_mode(True)  # To start powerUp mode ghost
                power_up_time = 400
                score += 10
                eat = time.time()
            else:
                score += 5
                eat = True
            totalPointDots -= 1
    if totalPointDots <= 0:
        game_won = True


def collision_with_ghost():
    global pac_pos, pac_size, ghostInfo, score, pac_direction, pac_direction_command, lifeCount, game_over
    x, y, r = *pac_pos, pac_size
    for ghost in ghostInfo:
        gx, gy, gr = ghost["ghostX"], ghost["ghostY"], 10
        center_distance = (x - gx) ** 2 + (y - gy) ** 2
        radius_sum = (r + gr) ** 2
        if center_distance < radius_sum - 2:
            time.sleep(0.5)
            if power_up:
                score += 50
                reposition_ghost(ghost)
            else:
                lifeCount -= 1
                if lifeCount <= 0:
                    game_over = True
                ghost_initial()
                pac_pos = [250, 325]
                pac_direction = 'right'
                pac_direction_command = 'right'


def draw_end_screen(word):
    glColor3f(1, 1, 0)
    start = 250 - (len(word) / 2) * 40
    for i, char in enumerate(word.upper()):
        pointA = start + 40 * i, 250 - 20
        pointB = pointA[0] + 30, pointA[1]
        pointC = pointA[0], pointA[1] + 20
        pointD = pointB[0], pointB[1] + 20
        pointE = pointC[0], pointC[1] + 20
        pointF = pointD[0], pointD[1] + 20

        if char in "A,E,G,O,R":
            draw_line(*pointE, *pointF)
        if char in "A,R":
            draw_line(*pointC, *pointD)
        if char in "E,G,O,U":
            draw_line(*pointA, *pointB)
        if char in "A,E,G,M,N,O,R,U,W":
            draw_line(*pointA, *pointC)
        if char in "A,E,G,M,N,O,R,U,W":
            draw_line(*pointC, *pointE)
        if char in "A,G,M,N,O,U,W":
            draw_line(*pointB, *pointD)
        if char in "A,M,N,O,R,U,W":
            draw_line(*pointD, *pointF)
        if char in "E":
            draw_line(*pointC, (pointC[0] + pointD[0]) // 2, pointC[1])
        if char in "G":
            draw_line((pointC[0] + pointD[0]) // 2, pointC[1], *pointD)
        if char in "N":
            draw_line(*pointB, *pointE)
        if char in "R":
            draw_line(*pointC, *pointB)
        if char in "W":
            draw_line(*pointA, (pointC[0] + pointD[0]) // 2, pointC[1])
            draw_line(*pointB, (pointC[0] + pointD[0]) // 2, pointC[1])
        if char in "V":
            draw_line((pointA[0] + pointB[0]) // 2, pointA[1], *pointE)
            draw_line((pointA[0] + pointB[0]) // 2, pointA[1], *pointF)
        if char in "M,Y":
            draw_line(*pointE, (pointC[0] + pointD[0]) // 2, pointC[1])
            draw_line(*pointF, (pointC[0] + pointD[0]) // 2, pointC[1])
        if char in "Y":
            draw_line((pointA[0] + pointB[0]) // 2, pointA[1], (pointC[0] + pointD[0]) // 2, pointC[1])


def reposition_ghost(ghost):
    global ghostInfo
    ghost["ghostX"] = 250
    ghost["ghostY"] = 280


def draw_ghost_eyes(ghostX, ghostY, ghostRad, dir):
    cl1, cl2, cl3 = color["white"]
    glColor3f(cl1, cl2, cl3)
    outerEyeRad = 3
    left_eyeX = ghostX - (ghostRad // 2)
    left_eyeY = ghostY + (ghostRad // 2)
    right_eyeX = ghostX + (ghostRad // 2)
    right_eyeY = ghostY + (ghostRad // 2)
    for rad in range(outerEyeRad, -1, -1):
        draw_circle(left_eyeX, left_eyeY, rad)
        draw_circle(right_eyeX, right_eyeY, rad)

    cl1, cl2, cl3 = 0.055, 0.376, 0.922
    glColor3f(cl1, cl2, cl3)
    innerEyeRad = 1
    left_eyeX = ghostX - (ghostRad // 2)
    left_eyeY = ghostY + (ghostRad // 2)
    right_eyeX = ghostX + (ghostRad // 2)
    right_eyeY = ghostY + (ghostRad // 2)
    addX, addY = 0, 0
    if dir == "right":
        addX = 2
    elif dir == "left":
        addX = -2
    elif dir == "up":
        addY = 2
    elif dir == "down":
        addY = -2
    for rad in range(innerEyeRad, -1, -1):
        draw_circle(left_eyeX + addX, left_eyeY + addY, rad)
        draw_circle(right_eyeX + addX, right_eyeY + addY, rad)


def draw_ghost_mouth(ghostX, ghostY):
    global GhostMouthRad, setGhostMouth, pause

    cl1, cl2, cl3 = color["white"]
    glColor3f(cl1, cl2, cl3)
    mouthX = ghostX
    mouthY = ghostY - 4
    curTime = time.time()
    if curTime - setGhostMouth >= 0.3 and not pause:
        setGhostMouth = curTime
        if GhostMouthRad == 2:
            GhostMouthRad = 1
        elif GhostMouthRad == 1:
            GhostMouthRad = 0
        elif GhostMouthRad == 0:
            GhostMouthRad = 2
    for r in range(GhostMouthRad, -1, -1):
        draw_circle(mouthX, mouthY, r)


def draw_ghost():
    for ghost in ghostInfo:
        cl1, cl2, cl3 = color[ghost["color"]]
        glColor3f(cl1, cl2, cl3)
        ghostRad = 10
        for rad in range(ghostRad, -1, -1):
            draw_circle(ghost["ghostX"], ghost["ghostY"], rad)

        lineX = ghost["ghostX"] - ghostRad
        lineY = ghost["ghostY"]

        for lines in range(2 * ghostRad + 1):
            draw_line(lineX, lineY, lineX, lineY - 10)
            lineX += 1

        draw_ghost_eyes(ghost["ghostX"], ghost["ghostY"], ghostRad, ghost["dir"])
        draw_ghost_mouth(ghost["ghostX"], ghost["ghostY"])


def powerUp_mode(start):
    global powerUpMode, powerUp_mode_start, powerUp_mode_color
    if start:
        powerUpMode = True
        powerUp_mode_start = time.time()
    else:
        powerUpMode = False
    powerUp_mode_color = "white"


def draw_powerUp_mode_eyes(ghostX, ghostY, ghostRad):
    glColor3f(0, 0, 0)
    halfWidth = 2
    left_eyeX1 = ghostX - (ghostRad // 2) - halfWidth
    left_eyeX2 = ghostX - (ghostRad // 2) + halfWidth
    left_eyeY1 = ghostY + (ghostRad // 2) + halfWidth
    left_eyeY2 = ghostY + (ghostRad // 2) - halfWidth
    left_eyeX3 = left_eyeX2
    left_eyeX4 = left_eyeX1
    left_eyeY3 = left_eyeY1
    left_eyeY4 = left_eyeY2
    right_eyeX1 = ghostX + (ghostRad // 2) - halfWidth
    right_eyeX2 = ghostX + (ghostRad // 2) + halfWidth
    right_eyeY1 = ghostY + (ghostRad // 2) - halfWidth
    right_eyeY2 = ghostY + (ghostRad // 2) + halfWidth
    right_eyeX3 = right_eyeX2
    right_eyeX4 = right_eyeX1
    right_eyeY3 = right_eyeY1
    right_eyeY4 = right_eyeY2

    draw_line(left_eyeX1, left_eyeY1, left_eyeX2, left_eyeY2, 1.5)
    draw_line(left_eyeX4, left_eyeY4, left_eyeX3, left_eyeY3, 1.5)
    draw_line(right_eyeX1, right_eyeY1, right_eyeX2, right_eyeY2, 1.5)
    draw_line(right_eyeX4, right_eyeY4, right_eyeX3, right_eyeY3, 1.5)


def draw_powerUp_mode_mouth(ghostX, ghostY, ghostRad):
    glColor3f(0, 0, 0)
    halfLen = 5
    mouthX1 = ghostX - halfLen
    mouthX2 = ghostX + halfLen
    mouthY1 = ghostY - halfLen
    mouthY2 = ghostY - halfLen
    draw_line(mouthX1, mouthY1, mouthX2, mouthY2, 3)


def draw_special_ghost():
    global powerUpMode, powerUp_mode_start, powerUp_mode_color
    curTime = time.time()
    if curTime - powerUp_mode_start >= 0.5:
        powerUp_mode_start = curTime
        if powerUp_mode_color == "white":
            powerUp_mode_color = "dark_blue"
        else:
            powerUp_mode_color = "white"
    for ghost in ghostInfo:
        cl1, cl2, cl3 = color[powerUp_mode_color]
        glColor3f(cl1, cl2, cl3)
        ghostRad = 10
        for rad in range(ghostRad, -1, -1):
            draw_circle(ghost["ghostX"], ghost["ghostY"], rad)

        lineX = ghost["ghostX"] - ghostRad
        lineY = ghost["ghostY"]

        for lines in range(2 * ghostRad + 1):
            draw_line(lineX, lineY, lineX, lineY - 10)
            lineX += 1
        draw_powerUp_mode_eyes(ghost["ghostX"], ghost["ghostY"], ghostRad)
        draw_powerUp_mode_mouth(ghost["ghostX"], ghost["ghostY"], ghostRad)


def choose_ghost():
    global powerUpMode
    if powerUpMode:
        draw_special_ghost()
    else:
        draw_ghost()


def change_dir():
    for ghost in ghostInfo:
        for points in changeDirPoints:
            x, y = points
            if ghost["ghostX"] == x and ghost["ghostY"] == y:
                idx = random.randint(0, len(changeDirPoints[points]) - 1)
                ghost["dir"] = changeDirPoints[points][idx]


def update_ghost():
    change_dir()
    ghostSpeed = 1
    for ghost in ghostInfo:
        if ghost["dir"] == "right":
            ghost["ghostX"] += ghostSpeed
        if ghost["dir"] == "left":
            ghost["ghostX"] -= ghostSpeed
        if ghost["dir"] == "up":
            ghost["ghostY"] += ghostSpeed
        if ghost["dir"] == "down":
            ghost["ghostY"] -= ghostSpeed





def add_shine_to_hearts(cx, cy):
    glColor3f(1, 1, 1)
    pointSize = 3
    draw_points(cx - 3 * pointSize, cy, pointSize)
    draw_points(cx - 2 * pointSize, cy, pointSize)
    draw_points(cx - 3 * pointSize, cy - pointSize, pointSize)
    draw_points(cx - pointSize, cy - 2 * pointSize, pointSize)


def fill_hearts(cx, cy, base_width):
    glColor3f(0.988, 0.455, 0.643)
    red = 2
    red2 = 0.4
    for i in range(4):
        draw_line(cx + red, cy + i, cx + 3 * base_width - red - red2, cy + i)
        red += 1

    red = 2
    for i in range(4):
        draw_line(cx - 3 * base_width + red, cy + i, cx - red - red2, cy + i)
        red += 1

    red = 2
    for i in range(1, 5):
        draw_line(cx - 3 * base_width + red, cy - i, cx + 3 * base_width - red - red2, cy - i)

    red = 2
    for i in range(14):
        draw_line(cx - 3 * base_width + red, cy - base_width - i, cx + 3 * base_width - red - red2, cy - base_width - i)
        red += 1


def draw_hearts():
    glColor3f(0.914, 0.306, 0.518)
    cx, cy = 390, 50
    height = 25
    base_width = 5
    between_gap = 40
    red = 0
    pointSize = 4
    for i in range(lifeCount):
        glColor3f(0.922, 0, 0.396)
        draw_line(cx, cy, cx + base_width, cy + base_width, pointSize)
        draw_line(cx + base_width, cy + base_width, cx + 2 * base_width, cy + base_width, pointSize)
        draw_line(cx + 2 * base_width, cy + base_width, cx + 3 * base_width, cy, pointSize)
        draw_line(cx + 3 * base_width, cy, cx + 3 * base_width, cy - base_width, pointSize)
        draw_line(cx + 3 * base_width, cy - base_width, cx, cy - 4 * base_width, pointSize)
        draw_line(cx, cy, cx - base_width, cy + base_width, pointSize)
        draw_line(cx - 2 * base_width, cy + base_width, cx - base_width, cy + base_width, pointSize)
        draw_line(cx - 2 * base_width, cy + base_width, cx - 3 * base_width, cy, pointSize)
        draw_line(cx - 3 * base_width, cy, cx - 3 * base_width, cy - base_width, pointSize)
        draw_line(cx - 3 * base_width, cy - base_width, cx, cy - 4 * base_width, pointSize)
        fill_hearts(cx, cy, base_width)
        add_shine_to_hearts(cx, cy)
        cx += between_gap


def game_restart():
    print("Game restarted")
    pacman_initial()            
    ghost_initial()




def animate():
    global blink_counter, power_up, power_up_time, pac_pos, pac_size, pause, game_won, game_over, special
    if not pause:
        if score == 0 and pac_pos[0] == 250:
            time.sleep(0.5)
        if pause or game_won or game_over:
            return
        blink_counter = blink_counter + 1 if blink_counter < 10 else 0
        if power_up:
            power_up_time -= 1
            if power_up_time <= 0:
                power_up = False
                pac_size = 10
                powerUp_mode(False)  # To end powerUp mode ghost

        check_valid_moves()
        set_direction()
        move_pacman()
        collision_with_point_dots()
        collision_with_ghost()
        update_ghost()

    glutPostRedisplay()


def specialKeyListener(key, x, y):
    global pac_direction_command

    if key == GLUT_KEY_RIGHT:
        pac_direction_command = 'right'
    if key == GLUT_KEY_LEFT:
        pac_direction_command = 'left'
    if key == GLUT_KEY_UP:
        pac_direction_command = 'up'
    if key == GLUT_KEY_DOWN:
        pac_direction_command = 'down'


def specialKeyUpListener(key, x, y):
    global pac_direction_command, pac_direction

    if key == GLUT_KEY_RIGHT and pac_direction_command == 'right':
        pac_direction_command = pac_direction
    if key == GLUT_KEY_LEFT and pac_direction_command == 'left':
        pac_direction_command = pac_direction
    if key == GLUT_KEY_UP and pac_direction_command == 'up':
        pac_direction_command = pac_direction
    if key == GLUT_KEY_DOWN and pac_direction_command == 'down':
        pac_direction_command = pac_direction


def keyboardListener():
    pass


def coordinate_converter(x, y):
    global W_Height
    y = W_Height - y
    return x, y


def mouseListener(button, state, x, y):
    global walls, game, pause

    if button == GLUT_LEFT_BUTTON:
        if (state == GLUT_DOWN):
            x1, y1 = coordinate_converter(x, y)

            # pause
            if 244 <= x1 <= 256 and 465 <= y1 <= 500:
                if pause == False:
                    pause = True
                    # speed=0
                else:
                    # speed=pause
                    pause = False

            # restart
            elif 20 <= x1 <= 45 and 465 <= y1 <= 500:
                game_restart()
                

            # exit
            elif 460 <= x1 <= 490 and 465 <= y1 <= 500:
                glutLeaveMainLoop()
    glutPostRedisplay()


def showScreen():
    global special
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    global pause, walls, game, pac_pos, game_won, game_over, eat, eat_time
    ## buttons
    draw_cross()
    draw_pause_or_play(pause)
    draw_replay()

    if game_won:
        draw_end_screen("You won")
    elif game_over:
        draw_end_screen("Game over")
    else:
        drawMaze()
        draw_point_dots()
        draw_pacman(pac_pos)
        choose_ghost()
        draw_hearts()
        initiate_cherry()
    draw_score()
    glutSwapBuffers()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(500, 100)
wind = glutCreateWindow(b"PACMAN")
ghost_initial()
pacman_initial()
glutDisplayFunc(showScreen)
glutIdleFunc(animate)
glutSpecialFunc(specialKeyListener)
glutSpecialUpFunc(specialKeyUpListener)
glutKeyboardFunc(keyboardListener)
glutMouseFunc(mouseListener)
glutMainLoop()