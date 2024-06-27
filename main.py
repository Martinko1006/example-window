
from pygame import *


WIN_WIDTH = 800
WIN_HEIGHT = 600
FPS = 40

class Player(sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = 10
        self.rect = draw.rect(window, color, (x, y, width, height))

    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y = self.rect.y - self.speed
            #self.rect.y -= self.speed 
        if keys[K_DOWN] and self.rect.y < WIN_HEIGHT - self.height:
            self.rect.y = self.rect.y + self.speed   

    def update_left(self):
        keys = key.get_pressed()
        if keys[K_q] and self.rect.y > 0:
            self.rect.y = self.rect.y - self.speed
            #self.rect.y -= self.speed 
        if keys[K_a] and self.rect.y < WIN_HEIGHT - self.height:
            self.rect.y = self.rect.y + self.speed   

    def draw(self):
        draw.rect(window, self.color, (self.rect.x, self.rect.y, self.width, self.height))

class Ball(sprite.Sprite):
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed_x = 5
        self.speed_y = 5
        self.rect = draw.circle(window, color,(x, y),radius)

    def update(self):
        self.rect.x = self.rect.x + self.speed_x
        self.rect.y = self.rect.y + self.speed_y

        if self.rect.y < 0 or self.rect.y > WIN_HEIGHT:
            self.speed_y *= -1

    def draw(self):
        draw.circle(window,(255,255,255),(self.rect.x, self.rect.y), self.radius)


window = display.set_mode((WIN_WIDTH,WIN_HEIGHT))
display.set_caption("Ping pong")

clock = time.Clock()

#objekty
   
player1 = Player(5,100, 20, 100, (255,0,0))
player2 = Player(WIN_WIDTH - 25, 100, 20, 100, (0,255,0))
ball = Ball(100, 100, 20, (255,255,255))

font.init()
font = font.Font(None, 35)
lose1 = font.render("Player 1 Lose", True, (180,0,0))
lose2 = font.render("Player 2 Lose", True, (180,0,0))

#herna slucka
run = True
while run:

    for e in event.get():
        if e.type == QUIT:
            run = False

    # cierne pozadie
    window.fill((0,0,0)) 
    
    player2.update_right()
    player1.update_left()
    player1.draw()
    player2.draw()
    ball.draw()
    ball.update()

    if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
        ball.speed_x *= -1

    if ball.rect.x > WIN_WIDTH:
        window.blit(lose2, (200,200))

    if ball.rect.x < 0:
        window.blit(lose1, (200,200))


    display.update()
    clock.tick(FPS)

quit()


