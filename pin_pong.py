import pygame

#переменные
window_x = 700
window_y = 700
game = True
FPS = 60
clock = pygame.time.Clock()
#окно
window = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption('Пин-Понг')
#фон
#+загрузить картинку
#background = pygame.transform.scale(pygame.image.load(''), (window_x,window_y))

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,size_x,size_y, player_speed ):
        super().__init__()

        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

class Racket(GameSprite):
    def management(self):
        pass
        #управление ракетками

class Boll(GameSprite):
    def management_boll(self):
        pass
        #движение мяча

class Pictures():
    pass
    #создание надписи победа и поражение

while game:
#запуск всех циклов

    pygame.display.update()
    pygame.time.delay(FPS)