from pygame import *
import os

move_u = True
move_d = True
move_l = True
move_r = True

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
        self.size_x, self.size_y = size_x, size_y 
    def reset(self): 
        window.blit(self.image, (self.rect.x, self.rect.y)) 
 
class Player(GameSprite): 
    def update(self): 
        keys = key.get_pressed() 
        if keys[K_UP] and self.rect.y > 5 and move_u: 
            self.rect.y = self.rect.y-self.speed 
        if keys[K_DOWN] and self.rect.y < win_height - 80 and move_d: 
            self.rect.y = self.rect.y+self.speed 
        if keys[K_LEFT] and self.rect.x > 5 and move_l:
            self.rect.x = self.rect.x-self.speed 
        if keys[K_RIGHT] and self.rect.x < win_width - 80 and move_r: 
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
background = transform.scale(image.load("top_back1.jpeg"), (win_width, win_height)) 

player = Player('кольт.png',75,80, 80, win_height -120, 4) 
murder = Enemy('murder.png',110, 100,win_width -90, 280, 2)
key1_up = GameSprite("key.png", 65, 25, 1000, 600, 0)

furniture = []
furniture_up = []
walls = []
walls_up = []
hides = []
hides_up = []

bed1 = GameSprite("bed.png", 125, 185, 535, 520, 0)
furniture.append(bed1)
hides.append(bed1)

bed1_up = GameSprite("bed.png", 125, 185, 0, 360, 0)
furniture_up.append(bed1_up)
hides_up.append(bed1_up)

door1 =  Wall(81, 49, 0, 70, 400, 100, 10)
walls.append(door1)

w1_up = Wall(0, 0, 0, 300, 140, 10, 340)
walls_up.append(w1_up)
w2_up = Wall(0, 0, 0, 0, 350, 300, 10)
walls_up.append(w2_up)
w3_up = Wall(0, 0, 0, 300, 600, 10, 150)
walls_up.append(w3_up)
w4_up = Wall(0, 0, 0, 800, 340, 10, 230)
walls_up.append(w4_up)
w5_up = Wall(0, 0, 0, 805, 365, 130, 10)
walls_up.append(w5_up)
w6_up = Wall(0, 0, 0, 1060, 365, 140, 10)
walls_up.append(w6_up)
w7_up = Wall(0, 0, 0, 800, 125, 10, 100)
walls_up.append(w7_up)
w8_up = Wall(0, 0, 0, 800, 125, 400, 10)
walls_up.append(w8_up)

w1 = Wall(0, 0, 0, 0, 400, 70, 10)
walls.append(w1)
w2 = Wall(0, 0, 0, 170, 400, 180, 10)
walls.append(w2)
w3 = Wall(0, 0, 0, 430, 400, 180, 10)
walls.append(w3)
w4 = Wall(0, 0, 0, 690, 400, 180, 10)
walls.append(w4)
w5 = Wall(0, 0, 0, 860, 250, 10, 250)
walls.append(w5)
w6 = Wall(0, 0, 0, 860, 250, 900, 10)
walls.append(w6)
w7 = Wall(0, 0, 0, 860, 50, 900, 10)
walls.append(w7)
w8 = Wall(0, 0, 0, 860, 0, 10, 50)
walls.append(w8)
w9 = Wall(0, 0, 0, 430, 0, 10, 150)
walls.append(w9)
w10 = Wall(0, 0, 0, 250, 400, 10, 100)
walls.append(w10)
w11 = Wall(0, 0, 0, 525, 400, 10, 120)
walls.append(w11)
w12 = Wall(0, 0, 0, 525, 510, 150, 10)
walls.append(w12)
w13 = Wall(0, 0, 0, 670, 510, 10, 300)
walls.append(w13)
w14 = Wall(0, 0, 0, 860, 500, 100, 10)
walls.append(w14)
w15 = Wall(0, 0, 0, 1065, 500, 150, 10)
walls.append(w15)
w16 = Wall(0, 0, 0, 250, 600, 10, 100)
walls.append(w16)

game = True 
clock = time.Clock() 
FPS = 60 

finish = False

floor1 = False
floor2 = True

day = 1
cover = True

mixer.init() 
mixer.music.load('Bmusic.mp3') 
mixer.music.play()
key_sound = mixer.Sound("key.ogg")
scream = mixer.Sound("hz.ogg")
font.init() 
font = font.Font(None, 70) 

day1 = font.render("DAY 1", True, (255,0,0))
day2 = font.render("DAY 2", True, (255,0,0))
day3 = font.render("DAY 3", True, (255,0,0))
day4 = font.render("DAY 4", True, (255,0,0))
day5 = font.render("DAY 5", True, (255,0,0))
lose = font.render("YOU DIED", True, (255,0,0))

while game: 
    for e in event.get(): 
        if e.type == QUIT: 
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                if sprite.collide_rect(player, bed1_up):
                    pl_x = player.rect.x
                    pl_y = player.rect.y
                    player = Player('кольт.png',0,0,player.rect.x, player.rect.y, 0) 
                else:
                    player = Player('кольт.png', 75,80, player.rect.x, player.rect.y, 5)
            
    if finish != True:
        '''
        if cover:
            window.fill((0,0,0))
            window.blit(day1, (500, 300))
            player.rect.x -= 100
            display.update()
            time.delay(4000)
            cover = False
        '''
        
        player.update() 
        murder.update()
        window.blit(background, (0, 0)) 
        player.reset() 
        murder.reset()
        if floor2:
            for wall in walls_up:
                wall.draw_wall()
            key1_up.reset()
            for lox in furniture_up:
                lox.reset()
            for wall in walls_up:
                if sprite.spritecollide(player, walls_up, False):
                    if abs(player.rect.top - wall.rect.bottom) < 5:
                        move_u = False
                    if abs(player.rect.bottom - wall.rect.top) < 5:
                        move_d = False
                    if abs(player.rect.left - wall.rect.right) < 5:
                        move_l = False
                    if abs(player.rect.right - wall.rect.left) < 5:
                        move_r = False
                else:
                    move_u = True
                    move_d = True
                    move_l = True
                    move_r = True

        elif floor1:
            for wall in walls:
                wall.draw_wall()
            for lox in furniture:
                lox.reset()
            for wall in walls:
                if sprite.spritecollide(player, walls, False):
                    if abs(player.rect.top - wall.rect.bottom) < 5:
                        move_u = False
                    if abs(player.rect.bottom - wall.rect.top) < 5:
                        move_d = False
                    if abs(player.rect.left - wall.rect.right) < 5:
                        move_l = False
                    if abs(player.rect.right - wall.rect.left) < 5:
                        move_r = False
                else:
                    move_u = True
                    move_d = True
                    move_l = True
                    move_r = True
            
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
        '''
        if sprite.collide_rect(player, w1):
        
            
            player.rect.y -= 10
        ''' 
        '''
        for door in doors:
            if sprite.collide_rect(player, door):
                w_w = door.height
                w_h = door.width
                door = Wall(81, 49, 0, door.rect.x, door.rect.y, w_w, w_h)
                display.update()
        '''
    
        if sprite.collide_rect(player, murder):  
            day += 1 
            scream.play()   
            if day == 2:
                window.fill((0,0,0))
                window.blit(day2, (500, 300))
                player.rect.x -= 100
                display.update()
                time.delay(4000)
                
            elif day == 3:
                window.fill((0,0,0))
                window.blit(day3, (500, 300))
                player.rect.x -= 100
                display.update()
                time.delay(4000)
            elif day == 4:
                window.fill((0,0,0))
                window.blit(day4, (500, 300))
                player.rect.x -= 100
                display.update()
                time.delay(4000)
            elif day == 5:
                window.fill((0,0,0))
                window.blit(day5, (500, 300))
                player.rect.x -= 100
                display.update()
                time.delay(4000)
            elif day == 6:
                window.fill((0,0,0))
                window.blit(lose, (500, 300))
                display.update()
                mixer.music.load("last.mp3")
                mixer.music.play()
                finish = True
            
        if sprite.collide_rect(player, key1_up):
            key_sound.play()
            key1_up = GameSprite("key.png", 0, 0, 450, 600, 0)
            
            
    display.update() 
    clock.tick(FPS)
