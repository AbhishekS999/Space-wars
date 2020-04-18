# importing Required Functions
import pygame
import random
import time
import math
from pygame.locals import QUIT
import tkinter

# get resolution of user pc
r = tkinter.Tk()
w = r.winfo_screenwidth()
h = r.winfo_screenheight()
w -= 5
h -= 5
print(w,h)
# initiate
pygame.init()

wn = pygame.display.set_mode((w, h), pygame.FULLSCREEN, 32)

# icon
pygame.display.set_caption('UFO')

icon = pygame.image.load('010-spaceship.png')
pygame.display.set_icon(icon)
fnt = pygame.font.SysFont('comicsansms', 40)

score = 0

# objects using in Programs

# Player
img = pygame.image.load('005-jet-1.png')
img_x = w / 2
img_y = h - 64
img_dx = 0
img_dy = 0

# Bullet
bull = '002-bullet-1.png'
bullet = pygame.image.load(bull)
bull_x = img_x
bull_y = 0
bull_dy_default = 15
bullet_state = 'none'
bullets = []

# Enemies
ene = '007-fighter.png'
enemy = []
ene_x = []
ene_y = []
ene_dy = []
ene_dx = []
no = 20
red = [255, 0, 0]
blue = [0, 255, 0]

life = 'life.png'
life_load = pygame.image.load(life)
lifeX = 50
life_remain = 5

fps = 100
speedy = 3

pause = False
lvl = False

# Functions

def opponent(x, y, i):
    wn.blit(enemy[i], (x, y))

def fire():
    global bullet_state
    bullet_state = 'Fire'

def iscollide(eX, eY, pX, pY):
    d = math.sqrt(math.pow((pX - eX), 2) + math.pow((pY - eY), 2))
    if d < 40:
        return 1
    else:
        return 0

def show_score(x, y):
    # fnt = pygame.font.SysFont('comicsansms', 25)
    scr = fnt.render('Score : ' + str(score), True, (0, 0, 0))
    wn.blit(scr, (x, y))

clock = pygame.time.Clock()

def exit_loop():

    exit()

def unhelp():
    global hlp
    hlp = False

def help1():
    global hlp
    import pygame
    from pygame.locals import QUIT

    pygame.init()

    hlp = True
    g = fnt.render('Press Right and left Arrow Key to Navigate', True, (0, 0, 0))
    g_rect = g.get_rect()
    g_rect.center = ((w/2, h/2))
    
    while hlp:
        global wn
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == (pygame.K_LALT and pygame.K_F4):
                    exit()
 
        wn.fill((255, 255, 255))
        wn.blit(g, g_rect)
        d = button(wn, 'Back', (w - 300), (h - 140), 200, 80, (0, 255, 0), (0, 200, 0), 40, unhelp)

        pygame.display.update()
        
def pause_handle():
    global pause
    pause = True
    paused(wn, w, h)

def unpause():
    global pause
    pause = False


def paused(wn, w, h):
    time.sleep(0.1)
    global pause
    import pygame
    from pygame.locals import QUIT

    pygame.init()

    fnt = pygame.font.SysFont('comicsansms', 150)
    head = fnt.render('Paused!', True, (255, 0, 0))
    head_rect = head.get_rect()
    head_rect.center = ((w / 2, h / 2 - 100))

    while pause:
        mouse = pygame.mouse.get_pos()

        wn.fill((255, 255, 255))
        wn.blit(head, head_rect)

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == (pygame.K_LALT and pygame.K_F4):
                    exit()

        a = button(wn, 'Continue!', (w / 2 - 100), (h / 2 + 50), 200, 80, (200, 200, 200), (150, 150, 150), 40, unpause)
        a2 = button(wn, 'Restart', (w / 2 - 100), (h / 2 + 150), 200, 80, (0, 255, 0), (0, 200, 0), 40, restart)
        b = button(wn, 'Quit', (w / 2 - 100), (h / 2 + 250), 200, 80, (255, 0, 0), (200, 0, 0), 40, exit_loop)
        c1 = button(wn, 'Main Menu', (w - 250), 30, 200, 60, (125, 100, 125), (100, 125, 100), 30,m_menu)

        pygame.display.update()

def exit_lvl():
    global lvl
    lvl = False
    gameloop()

def levels():

    global lvl
    lvl = True
    time.sleep(0.5)
    import pygame
    from pygame.locals import QUIT

    pygame.init()
    fnt = pygame.font.SysFont('comicsansms', 150)
    op = fnt.render('Options', True, (9, 9, 9))
    op_rect = op.get_rect()
    op_rect.center = (w / 2 - 20, h / 2 - 100)
    while lvl:
        mouse = pygame.mouse.get_pos()

        wn.fill((255, 255, 255))
        wn.blit(op, op_rect)

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == (pygame.K_LALT and pygame.K_F4):
                    exit()

        l1 = button(wn, 'Easy', (w / 2 - 100), (h / 2 + 50), 200, 70, (200, 200, 200), (150, 150, 150), 30, easy)
        l1 = button(wn, 'Medium', (w / 2 - 100), (h / 2 + 150), 200, 70, (0, 255, 0), (0, 200, 0), 30, medium)
        l1 = button(wn, 'Hard', (w / 2 - 100), (h / 2 + 250), 200, 70, (255, 0, 0), (200, 0, 0), 30, hard)
       

        pygame.display.update()

def easy():
    global fps, speedy, no
    fps = 150
    speedy = 2
    no = 12
    for i in range(no):
        enemy.append(pygame.image.load(ene))
        ene_x.append(random.randint(0, w - 70))
        ene_y.append(random.randint(-150, -90))
        ene_dy.append(random.randint(1, speedy))
        ene_dx.append(random.randint(-3, 3))

    exit_lvl()

def medium():
    global fps, speedy, no
    fps = 300
    speedy = 3
    no = 20
    for i in range(no):
        enemy.append(pygame.image.load(ene))
        ene_x.append(random.randint(0, w - 70))
        ene_y.append(random.randint(-150, -90))
        ene_dy.append(random.randint(1, speedy))
        ene_dx.append(random.randint(-3, 3))

    exit_lvl()

def hard():
    global fps, speedy, no
    fps = 600             
    speedy = 4
    no = 30
    for i in range(no):
        enemy.append(pygame.image.load(ene))
        ene_x.append(random.randint(0, w - 70))
        ene_y.append(random.randint(-150, -90))
        ene_dy.append(random.randint(1, speedy))
        ene_dx.append(random.randint(-3, 3))

    exit_lvl()


def menu():
    global wn, w, h
    import pygame
    from pygame.locals import QUIT

    pygame.init()

    fnt = pygame.font.SysFont('comicsansms', 150)
    head = fnt.render('UFO', True, (255, 0, 0))
    head_rect = head.get_rect()
    head_rect.center = ((w / 2, h / 2 - 150))

    while True:
        mouse = pygame.mouse.get_pos()

        wn.fill((255, 255, 255))
        wn.blit(head, head_rect)

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == (pygame.K_LALT and pygame.K_F4):
                    exit()

        a = button(wn, 'Play!', (w / 2 - 100), (h / 2 + 50), 200, 70, (0, 255, 0), (0, 200, 0), 30, levels)
        b = button(wn, 'Quit', (w / 2 - 100), (h / 2 + 250), 200, 70, (255, 0, 0), (200, 0, 0), 30, exit_loop)
        c = button(wn, 'Help', (w/2 - 100), (h / 2 + 150), 200, 70, (125, 125, 125), (100, 100, 100), 30, help1)

        pygame.display.update()

def button(disp, text, x, y, width, height, color_change, default_color, fontsz, task=None):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(disp, color_change, (x, y, width, height))
        if (click[0] == 1 and task != None):
            task()

    else:
        pygame.draw.rect(disp, default_color, (x, y, width, height))

    fnt = pygame.font.SysFont('Lucida Calligraphy', fontsz)
    txt = fnt.render(text, True, (0, 0, 0))
    txt_rect = txt.get_rect()
    txt_rect.center = ((x + width / 2), (y + height / 2))
    disp.blit(txt, txt_rect)

def restart():
    for i in range(no):
        ene_x[i] = random.randint(0, 936)
        ene_y[i] = random.randint(-100, -70)
    global score
    score = 0

    gameloop()

def m_menu():
    for i in range(no):
        ene_x[i] = random.randint(0, 936)
        ene_y[i] = random.randint(-100, -70)
    global score
    score = 0

    menu()

def lives():
    global lifeX
    if life_remain == 5:
        wn.blit(life_load, (lifeX, h - 50))
        wn.blit(life_load, (lifeX + 50, h - 50))
        wn.blit(life_load, (lifeX + 100, h - 50))
        wn.blit(life_load, (lifeX + 150, h - 50))
        wn.blit(life_load, (lifeX + 200, h - 50))
    if life_remain == 4:
        wn.blit(life_load, (lifeX, h - 50))
        wn.blit(life_load, (lifeX + 50, h - 50))
        wn.blit(life_load, (lifeX + 100, h - 50))
        wn.blit(life_load, (lifeX + 150, h - 50))

    if life_remain == 3:
        wn.blit(life_load, (lifeX, h - 50))
        wn.blit(life_load, (lifeX + 50, h - 50))
        wn.blit(life_load, (lifeX + 100, h - 50))

    if life_remain == 2:
        wn.blit(life_load, (lifeX, h - 50))
        wn.blit(life_load, (lifeX + 50, h - 50))

    if life_remain == 1:
        wn.blit(life_load, (lifeX, h - 50))
  
def gameloop():
    global img_dy, img_y, bull_dy_default, h_scr
    global img_x, bullet_state, img_dx, bull_x, bull_y, score, no, life_remain, score
    j = 1
    life_remain = 5
    while j:
        clock.tick(fps)
        wn.fill((255, 255, 255))
        wn.blit(img, (img_x, img_y))
        lives()

        a = button(wn, 'Pause', (w - 150), 30, 100, 40, (125, 100, 125), (100, 125, 100), 30, pause_handle)


        # Check for Keystroke
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    img_dx = -5
                if event.key == pygame.K_RIGHT:
                    img_dx = 5
                if event.key == pygame.K_UP:
                    img_dy = -5
                if event.key == pygame.K_DOWN:
                    img_dy = 5
                if event.key == (pygame.K_LALT and pygame.K_F4):
                    exit()
    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    img_dx = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    img_dy = 0
        fire()
        # player checking
        if img_x < 0:
            img_x = 0
        
        if img_x > w - 64:
            img_x = w - 64
        
        img_x += img_dx
        img_y += img_dy

        if no == 30:

            if bullet_state is 'Fire':
                wn.blit(bullet, (bull_x + 2, bull_y))
                bull_y -= bull_dy_default
                if bull_y < 0:
                    g1 = img_y
                    bull_y = g1
                    g = img_x
                    bull_x = g

            if bullet_state is 'Fire':
                wn.blit(bullet, (bull_x + 30, bull_y))
                bull_y -= bull_dy_default
                if bull_y < 0:
                    g1 = img_y
                    bull_y = g1
                    g = img_x
                    bull_x = g
        if no == 20:
            #global bull_dy_default
            bull_dy_default = 20
            if bullet_state is 'Fire':
                wn.blit(bullet, (bull_x + 16, bull_y))
                bull_y -= bull_dy_default
                if bull_y < 0:
                    g1 = img_y
                    bull_y = g1
                    g = img_x
                    bull_x = g

        if no == 12:
            #global bull_dy_default
            bull_dy_default = 15
            if bullet_state is 'Fire':
                wn.blit(bullet, (bull_x + 16, bull_y))
                bull_y -= bull_dy_default
                if bull_y < 0:
                    g1 = img_y
                    bull_y = g1
                    g = img_x
                    bull_x = g

        if img_y > h - 70:
            img_y = h - 70

        # enemies
        for i in range(no):
            ene_y[i] += ene_dy[i] / 5
            ene_x[i] += ene_dx[i] / 5
            collision = iscollide(bull_x, bull_y, ene_x[i], ene_y[i])

            if ene_x[i] < 0:
                ene_dx[i] *= -1

            if ene_x[i] > w - 64:
                ene_dx[i] *= -1

            if ene_y[i] > h + 20:
                ene_x[i] = random.randint(0, 936)
                ene_y[i] = random.randint(-100, -70)
                life_remain -= 1 

            if collision:
                g = img_x
                g1 = img_y
                bull_y = g1
                bull_x = g
                bullet_state = 'Fire'
                score += 1


                ene_dy[i] += 0.1
                print(ene_dy[i])

                ene_x[i] = random.randint(0, 936)
                ene_y[i] = random.randint(-100, -70)

            opponent(ene_x[i], ene_y[i], i)

            show_score(20, 20)
            


            collision_over = iscollide(img_x, img_y, ene_x[i], ene_y[i])

            if collision_over or life_remain == 0:
                # Final Ending Message
                fnt = pygame.font.SysFont('comicsansms', 50)
                text = fnt.render('Game Over', True, red)
                textRect = text.get_rect()
                textRect.center = (w / 2, h / 2)

                wn.blit(text, textRect)

                for i in range(no):
                    ene_x[i] = random.randint(0, 936)
                    ene_y[i] = random.randint(-100, -70)

                pygame.display.update()

                time.sleep(3)
                j = 0

        pygame.display.update()

        a = open ("Score.txt", "w")
        a.write(str(score))
        a.close()
