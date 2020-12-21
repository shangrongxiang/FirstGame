import pygame
import random
from pygame.locals import *
pygame.init()
W,H = 800,447
win = pygame.display.set_mode((W,H))
pygame.display.set_caption("side Scroller")
clock = pygame.time.Clock()
bg = pygame.image.load("bg.png")
bgX = 0
bgX2 = bg.get_width()
class player():
    run = [pygame.image.load(str(i)+".png")for i in range(8,16)]
    jump = [pygame.image.load(str(i)+".png")for i in range(1,8)]
    slide = [pygame.image.load("S1.png"),pygame.image.load("S1.png"),pygame.image.load("S2.png"),pygame.image.load("S2.png"),pygame.image.load("S2.png"),pygame.image.load("S2.png"),pygame.image.load("S2.png"),pygame.image.load("S3.png"),pygame.image.load("S3.png"),pygame.image.load("S4.png"),pygame.image.load("S5.png")]
    jumpList = [1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,-1,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4]
    def __init__(self,x,y,width,height):
        self.x = x 
        self.y = y
        self.width = width
        self.height = height
        self.jumping = False
        self.sliding = False
        self.jumpCount = 0
        self.runCount = 0
        self.slideCount = 0
    def draw(self,win):
        if self.jumping:
            self.y -=self.jumpList[self.jumpCount] * 1.2
            win.blit(self.jump[self.jumpCount//18],(self.x,self.y))
            self.jumpCount += 1
            if self.jumpCount > 108:
                self.jumpCount = 0
                self.jumping = False
                self.runCount = 0
        elif self.sliding:
            if self.slideCount < 20:
                self.y += 1
            elif self.slideCount == 70:
                self.y -= 19
            if self.slideCount > 100:
                self.slideCount = 0
                self.sliding = False
                self.runCount = 0
            win.blit(self.slide[self.slideCount//10],(self.x,self.y))
            self.slideCount += 1
        else:
            if self.runCount > 43:
                self.runCount = 0
            win.blit(self.run[self.runCount//6],(self.x,self.y))
            self.runCount += 1
class saw():
    img = [pygame.image.load("SAW0.png"),pygame.image.load("SAW1.png"),pygame.image.load("SAW2.png"),pygame.image.load("SAW3.png")]
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x,self.y,width,height)
        self.count = 0

    def draw(self,win):
        self.hitbox = (self.x + 5,self.y + 5,self.width - 10,self.height)
        if self.count >= 8:
            self.count = 0

        win.blit(pygame.transform.scale(self.img[self.count//2],(64,64)),(self.x,self.y))
        self.count += 1 
        pygame.draw.rect(win,(255,0,0),self.hitbox,2)

class spike(saw):
    img = pygame.image.load("spike.png")
    

    def draw(self,win):
        self.hitbox = (self.x+10,self.y,20,315)
        win.blit(self.img, (self.x, self.y))
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)


def redrawWin():
    win.blit(bg,(bgX,0))
    win.blit(bg,(bgX2,0))
    for ob in objects:
        ob.draw(win)
    runner.draw(win)
    pygame.display.update()
objects = []
runner = player(200,313,64,64)
pygame.time.set_timer(USEREVENT+1,500)
firtime =3000
endtime = 5000
pygame.time.set_timer(USEREVENT+2,random.randrange(firtime,endtime))
speed = 30
run = True
while run:
    for ob in objects:
        ob.x -= 1.4
        if ob.x < ob.width * -1:
            objects.pop(objects.index(ob))
    redrawWin()
    print(speed)
    bgX -= 1.4 ## 用两张相同的图片做背景，当第一张的x滚到-bg.get_width()(背景图片的宽)时，第一张回到原来起点，然后第二章图片进入GUI
    bgX2 -= 1.4
    print("x1 = {} x2 = {}".format(bgX,bgX2))
    if bgX < bg.get_width() * -1:
        bgX = bg.get_width()
    if bgX2 < bg.get_width() * -1:
        bgX2 = bg.get_width()
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
        if event.type == USEREVENT + 1:
            speed += 1
        
        if event.type == USEREVENT + 2:
            firtime -= 10
            endtime -= 10
            r = random.randrange(0,2)
            if r == 0:
                objects.append(saw(810,310,64,64))
            else:
                objects.append(spike(821,0,48,320))
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] or keys[pygame.K_UP] :
        runner.jumping = True

    if keys[pygame.K_DOWN]:
        runner.sliding = True
     
    clock.tick(speed)

