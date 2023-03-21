from pygame import *
from random import *
font.init()
PLS = (10,100)
BS = (50,50)
window_size = (750,750)
fps = 60
font2 = font.Font(None, 70)
window= display.set_mode(window_size)
PPoseX1 = 0+PLS[0]
PPoseY1 = window_size[1] - PLS[1]
PPoseX2 = window_size[0] - PLS[0]
PPoseY2 = window_size[1] - PLS[1]
VECTOR = Vector2
color = (255,255,255)

class GameSprite(sprite.Sprite):
    def __init__(self, playerImage, playerX, playerY, playerSpeed, SPSize1):
        super().__init__()
        self.spsize = SPSize1
        self.image = transform.scale(image.load(playerImage), self.spsize)
        self.playerSpeed = playerSpeed
        self.rect = self.image.get_rect()
        self.rect.x = playerX
        self.rect.y = playerY
        self.rect.centerx = playerX
        self.rect.top = playerY

    def spawn(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0 :
            self.rect.y -= self.playerSpeed
        if keys[K_s] and self.rect.y < window_size[1] - PLS[1] :
            self.rect.y += self.playerSpeed
class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0 :
            self.rect.y -= self.playerSpeed
        if keys[K_DOWN] and self.rect.y < window_size[1] - PLS[1] :
            self.rect.y += self.playerSpeed
class Ball:
    def __init__(self):
       self.color=color
       self.rad = 25
       self.speed = 3
       self.rect = Rect(0, 0, self.rad * 2, self.rad * 2)
       self.rect.x = window_size[0]/2
       self.rect.y = window_size[1]/2
       self.dir = VECTOR(choice((self.speed,-self.speed)),choice((self.speed,-self.speed)))
    def draw(self):
        draw.circle(window,self.color,(self.rect.x,self.rect.y),self.rad)
    def move(self,player1,player2):
        self.rect.move_ip(self.dir)
        if sprite.collide_rect(player1,self) or sprite.collide_rect(player2,self):
            self.dir[0]*= -1
        if self.rect.y >= window_size[1] - self.rad or self.rect.y <= 0:
            self.dir[1] *= -1