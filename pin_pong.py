from pygame import *

#переменные
window_x = 700
window_y = 500
game = True
FPS = 120
c = False
clock = time.Clock()
ball_x = 10
ball_y = 10

#окно
window = display.set_mode((window_x, window_y))
display.set_caption('Пин-Понг')
#фон
#+загрузить картинку
background = transform.scale(image.load('фон.png'), (window_x,window_y))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,size_x,size_y, player_speed ):
        super().__init__()

        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Racket(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 20:
            self.rect.y -= self.speed

        if keys[K_DOWN] and self.rect.y < window_y-100:
            self.rect.y +=self.speed

    def update_2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 20:
            self.rect.y -= self.speed

        if keys[K_s] and self.rect.y < window_y-100:
            self.rect.y +=self.speed
        #управление ракетками

"""
        for event in event.get():
            if event.type == QUIT:
                game_over = True

            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    move_right = True
        
            elif event.type == KEYUP:
                if event.key == K_RIGHT:
                    move_right = False

            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    move_left = True
        
            elif event.type == KEYUP:
                if event.key == K_LEFT:
                    move_left = False
    
        if move_right:
            racket_1.rect.x += 3

        elif move_left:
            racket_1.rect.x -= 3
        """

class Boll(GameSprite):
    def management_boll(self):
        ball.rect.x += ball_x
        ball.rect.y += ball_y

        if ball.rect.y > 20 or ball.rect.y < window_y-100:
            ball_y *= -1
    
        if ball.rect.x > 450 or ball.rect.x < 0:
            ball_x *= -1

class Pictures():
    pass
    #создание надписи победа и поражение

racket_1 = Racket('ракетка.png',0, 150 ,10,100,30)
racket_2 = Racket('ракетка.png',690, 150 ,10,100,30)
ball = Boll('шар.png', 200, 200, 30, 30, 30)
while game:
#запуск всех циклов
    for i in event.get():
        if i.type == QUIT:
            game = False
        window.blit(background,(0,0))

        racket_1.update()
        racket_1.reset()
        ball.reset()
        racket_2.update_2()
        racket_2.reset()

        ball.rect.x += ball_x
        ball.rect.y += ball_y

        if ball.rect.y > 20 or ball.rect.y < window_y-100:
            ball_y *= -1

        display.update()
        time.delay(FPS)
