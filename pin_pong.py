from pygame import *

#переменные
window_x = 700
window_y = 500
game = True
FPS = 60
c = False
clock = time.Clock()

#окно
window = display.set_mode((window_x, window_y))
display.set_caption('Пин-Понг')
#фон
#+загрузить картинку
background = transform.scale(image.load('fon.jpg'), (window_x,window_y))

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
        for keys[K_UP] or keys[K_DOWN]:
            if c == True and self.rect.y > 20:
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

class Boll(GameSprite):
    def management_boll(self):
        pass
        #движение мяча

class Pictures():
    pass
    #создание надписи победа и поражение

racket_1 = Racket('фон.png',0, 150 ,10,100,30)
racket_2 = Racket('фон.png',690, 150 ,10,100,30)
while game:
#запуск всех циклов
    for i in event.get():
        if i.type == QUIT:
            game = False
        window.blit(background,(0,0))

        racket_1.update()
        racket_1.reset()
        racket_2.update_2()
        racket_2.reset()

        display.update()
        time.delay(FPS)
