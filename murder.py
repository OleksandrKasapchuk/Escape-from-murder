from pygame import*
import os

murder = 'murder.png'

'''
stationary = image.load(os.path.join('images/Hero', "0.png"))

left = [None] * 10
for picIndex in range(0,9):
    left[picIndex] = pygame.image.load(os.path.join('images/Hero',str(picIndex+1)+'_1.png' ))
    picIndex +=1
right = [None] * 10
for picIndex in range(0,9):
    right[picIndex] = pygame.image.load(os.path.join('images/Hero',str(picIndex+1)+'.png' ))
    picIndex +=1

stepIndex = 0

step = 10
move_right = False
move_left = False

def draw_step():
    global stepIndex
    if stepIndex >=9:
        stepIndex = 0
        
    if move_left:
        window.blit(left[stepIndex], (x, y))
        stepIndex += 1
        
    elif move_right:
        window.blit(right[stepIndex], (x, y))
        stepIndex += 1
    else:
        window.blit(stationary, (x,y))
'''       
    
class GameSprite(sprite.Sprite): 
    def __init__(self, player_image, size_x, size_y, player_x, player_y, player_speed): 
        super().__init__() 
        self.image = transform.scale(image.load(player_image), (size_x, size_y)) 
        self.speed = player_speed 
        self.rect = self.image.get_rect() 
        self.rect.x = player_x 
        self.rect.y = player_y 
 
    def reset(self): 
        window.blit(self.image, (self.rect.x, self.rect.y)) 
 
class Player(GameSprite): 
    def update(self): 
        keys = key.get_pressed() 
        if keys[K_UP] and self.rect.y > 5: 
            self.rect.y = self.rect.y-self.speed 
        if keys[K_DOWN] and self.rect.y < win_height - 80: 
            self.rect.y = self.rect.y+self.speed 
        if keys[K_LEFT] and self.rect.x > 5:  
            self.rect.x = self.rect.x-self.speed 
        if keys[K_RIGHT] and self.rect.x < win_width - 80: 
            self.rect.x = self.rect.x+self.speed 
class Enemy(GameSprite): 
    direction = 'left' 
    def update(self): 
        if self.rect.x <= 470: 
            self.direction = 'right' 
        if self.rect.x >= win_width-85: 
            self.direction = 'left' 
        if self.direction == 'right': 
            self.rect.x = self.rect.x+self.speed 
        else: 
            self.rect.x = self.rect.x-self.speed
 
class Wall(sprite.Sprite): 
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_w, wall_h): 
        super().__init__() 
        self.color_1 = color_1 
        self.color_2 = color_2 
        self.color_3 = color_3 
        self.width = wall_w 
        self.height = wall_h 
        self.image = Surface((self.width, self.height)) 
        self.image.fill((color_1, color_2, color_3)) 
        self.rect = self.image.get_rect() 
        self.rect.x = wall_x 
        self.rect.y = wall_y 
    def draw_wall(self): 
        window.blit(self.image, (self.rect.x, self.rect.y)) 
 
 
win_width = 1200 
win_height = 700
window = display.set_mode((win_width, win_height)) 
display.set_caption("Escape from murder") 
background = transform.scale(image.load("top_back.jpg"), (win_width, win_height)) 

player = Player('кольт.png',90,100, 5, win_height -80, 4) 
murder = Enemy(murder,110, 100,win_width -80, 280, 2) 

w1 = Wall(0, 0, 0, 200, 300, 200, 10)

walls = sprite.Group()

game = True 
clock = time.Clock() 
FPS = 60 
finish = False

floor1 = False
floor2 = True

mixer.init() 
mixer.music.load('b_music.mp3') 
mixer.music.play()


font.init() 
font = font.Font(None, 70) 
win = font.render('YOU WIN!', True, (255, 215, 0)) 
lose = font.render('YOU LOSE!', True, (255, 0, 0)) 
 
while game: 
    for e in event.get(): 
        if e.type == QUIT: 
            game = False 
    if finish != True: 
        player.update() 
        murder.update()
        w1.update()
        window.blit(background, (0, 0)) 
        player.reset() 
        murder.reset() 
        w1.draw_wall()
        '''      
        draw_step()
        
        keyPressed = pygame.key.get_pressed()
        if keyPressed[pygame.K_LEFT]  and x > 0:
            x -= step*2
            move_left = True
            move_right = False
        elif keyPressed[pygame.K_RIGHT]  and x < width:
            x +=step*2
            move_left = False
            move_right = True
        else:
            move_right = False
            move_left = False
            stepIndex = 0
        '''
        
        if sprite.collide_rect(player, w1):
            player.speed_x = 0
            player.speed_y = 0
        if sprite.collide_rect(player, murder):  
            finish = True 
            window.blit(lose, (200, 200)) 
        
    display.update() 
    clock.tick(FPS)
