import pygame
pygame.init()
##Hello
win = pygame.display.set_mode((800,480))
pygame.display.set_caption("First_game")
clock = pygame.time.Clock()
bulletSound = pygame.mixer.Sound("bullet.mp3")
hitSound = pygame.mixer.Sound("hit.mp3")
music = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)
score = 0
def fade(width,height):
    fade = pygame.Surface((width,height))
    fade.fill((0,0,0))
    for alpha in range(0,300):
        fade.set_alpha(alpha)
        win.fill((255,255,255))
        win.blit(fade,(0,0))
        pygame.display.update()
        pygame.time.delay(10)


    
   
class projectile():
    def __init__(self,x,y,radius,color,facing):
        self.x = x 
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8*facing
    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)

class enemy():
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'),pygame.image.load('R10E.png'),pygame.image.load('R11E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'),pygame.image.load('L10E.png'),pygame.image.load('L11E.png')]

    def __init__(self,x,y,width,height,end):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.end = end
        self.vel = 3
        self.path = [self.x,self.end] 
        self.walcount = 0
        self.hibox = (self.x+17,self.y+4,31,57)
        self.health = 10
        self.visible = True
    def draw(self,win):
        
        self.move()
        if self.walcount +1>= 33:
            self.walcount = 0
        if self.vel > 0:
            win.blit(self.walkRight[self.walcount // 3],(self.x,self.y))
            self.walcount+=1
        else:
            win.blit(self.walkLeft[self.walcount // 3],(self.x,self.y))
            self.walcount+=1
        self.hibox = (self.x+17,self.y+4,31,57)
        pygame.draw.rect(win,(255,0,0),(self.hibox[0],self.hibox[1]-20,50,10))
        pygame.draw.rect(win,(5,255,0),(self.hibox[0],self.hibox[1]-20,50-(5 * (10 - self.health)),10))
        ##pygame.draw.rect(win,(255,00,00),self.hibox,2)
        if self.visible == False:
            self.x = -10000
            self.y = 10000
    def move(self):
        if self.visible == True:
            if self.vel > 0:
                if self.x +self.vel < self.path[1]:
                    self.x +=self.vel
                else:
                    self.vel = self.vel*-1
                    self.walcount = 0
            else:
                if self.x -self.vel > self.path[0]:
                    self.x +=self.vel
                else:
                    self.vel = self.vel*-1
                    self.walcount = 0
        
    def hit(self):
        if self.visible == True:
            if self.health > 0:
                self.health -= 1 
            else:
                self.visible = False

class player():
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = 0
        self.hibox = (self.x+19,self.y+8,31,57)
    def hit(self):
        self.x  = 60
        self.walkCount = 0
        font = pygame.font.SysFont(None,100)
        text = font.render('-1',1,(255,0,0))
        win.blit(text,(250-(text.get_width()/2),200))
        pygame.display.update()
        i = 0
        while i < 100:
            pygame.time.delay(5)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()
    def draw(self,wind):
        if self.walkCount +1 >= 27:
            self.walkCount = 0
        elif not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3],(self.x,self.y))
                self.walkCount +=1
            elif self.right:
                win.blit(walkRight[self.walkCount//3],(self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                win.blit(walkRight[0],(self.x,self.y))
            else:
                win.blit(walkLeft[0],(self.x,self.y))
        self.hibox = (self.x+19,self.y+8,31,57)
        ##pygame.draw.rect(win,(255,0,0),self.hibox,2)
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')
def redrawGameWindow():
    win.blit(bg,(0,0))
    man.draw(win)
    text = font.render('Score: ' + str(score), True, (0,0,0))
    win.blit(text, (700, 10))
    gobblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()
man = player(300,410,64,64)
run = True
bullets = []
font = pygame.font.SysFont(None, 30)
gobblin = enemy(100,410,64,64,400)
shootLoop =0
while run:
    clock.tick(27)
    if man.hibox[1] < gobblin.hibox[1] + gobblin.hibox[3] and  man.hibox[3] + man.hibox[1] > gobblin.hibox[1]:
            if man.hibox[0] + man.hibox[2] > gobblin.hibox[0] and man.hibox[0] < gobblin.hibox[0] + gobblin.hibox[2]:
                man.hit()
                score -= 1
    if shootLoop > 0:
        shootLoop +=1
    if shootLoop > 3:
        shootLoop = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for bullet in bullets:
        if bullet.y - bullet.radius < gobblin.hibox[1] + gobblin.hibox[3] and  bullet.y + bullet.radius > gobblin.hibox[1]:
            if bullet.x + bullet.radius > gobblin.hibox[0] and bullet.x-bullet.radius < gobblin.hibox[0] + gobblin.hibox[2]:
                gobblin.hit()
                hitSound.play()
                score += 1
                bullets.pop(bullets.index(bullet))
        if bullet.x < 800 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    keys = pygame.key.get_pressed()
    if event.type == pygame.MOUSEBUTTONDOWN:
        fade(800,480)
    if keys[pygame.K_SPACE] and shootLoop == 0:

        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            shootLoop=1
            bullets.append(projectile(round(man.x + man.width//2),man.y+man.height//2,6,(0,0,0),facing))
    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -=man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 800 - man.width -man.vel:
        man.x +=man.vel
        man.left = False
        man.right = True
        man.standing = False
    else:
        man.walkCount = 0
        man.standing = True
##go left go right go up go down and jump
    if not(man.isJump):
        if keys[pygame.K_UP] and man.y > 0:
            man.isJump = True
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount**2)*0.5*neg
            man.jumpCount -= 2
        else:
            man.isJump = False
            man.jumpCount = 10
    redrawGameWindow()
pygame.quit()