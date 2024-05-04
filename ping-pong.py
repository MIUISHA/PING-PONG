from pygame import *

clock = time.Clock()
FPS = 60
win_width, win_height = 700, 500
window = display.set_mode((win_width, win_height))
display.set_caption('ping-pong')

background = transform.scale(image.load('galaxy.jpg'), (win_width, win_height))

class GameSprite(sprite.Sprite): 
    def __init__(self, player_image, player_x, player_y, sizeX, sizeY, player_speed): 
        super().__init__() 
        self.image = transform.scale(image.load(player_image), (sizeX,sizeY)) 
        self.speed = player_speed
        self.rect = self.image.get_rect() 
        self.rect.x = player_x 
        self.rect.y = player_y 
    def reset(self): 
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 490:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 490:
            self.rect.y += self.speed



racket_1 = Player("racket.png",10, 245, 39, 136, 5)
racket_2 = Player("racket.png",475, 245, 39, 136, 5)





game=True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background, (0, 0))
    racket_1.reset()
    racket_2.reset()

    
    racket_1.update_l()
    racket_2.update_r()

    display.update()
    clock.tick(FPS)









