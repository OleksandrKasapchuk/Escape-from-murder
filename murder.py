from pygame import *
import os
from random import randint
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
        if keys[K_LEFT] and self.rect.x > 2 and move_l:
            self.rect.x = self.rect.x-self.speed 
        if keys[K_RIGHT] and self.rect.x < win_width - 60 and move_r: 
            self.rect.x = self.rect.x+self.speed 
    def collide(self, targets):
        global move_u, move_d, move_r, move_l
        for target in targets:
            if sprite.spritecollide(self, targets, False):
                if abs(self.rect.top - target.rect.bottom) < 5:
                    move_u = False
                    self.rect.y += 1
                if abs(self.rect.bottom - target.rect.top) < 5:
                    move_d = False
                    self.rect.y -= 1
                if abs(self.rect.left - target.rect.right) < 5:
                    move_l = False
                    self.rect.x += 1
                if abs(self.rect.right - target.rect.left) < 5:
                    move_r = False
                    self.rect.x -= 1
            else:
                move_u = True
                move_d = True
                move_l = True
                move_r = True

speed_x = randint(-3,3)
speed_y = randint(-3,3)
class Enemy(GameSprite): 
    def update(self): 
        self.rect.x += speed_x
        self.rect.y += speed_y
        
    def collide_something(self, targets):
        global speed_x, speed_y
        if sprite.spritecollide(self, targets, False) or self.rect.y < 5 or self.rect.y > win_height - 100 or self.rect.x < 3 or self.rect.x > win_width - 110:
            speed_x = randint(-5,5)
            speed_y = randint(-5,5)
    def follow(self, target):
        if abs(self.rect.x - target.rect.x) <= 200 or abs(self.rect.y - target.rect.y) <= 200:
            global hz_y, hz_x
            hz_x = (self.rect.x - target.rect.x) / 240
            hz_y = (self.rect.y - target.rect.y) / 240
            self.rect.x -= hz_x
            self.rect.y -= hz_y
    '''
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
    '''
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

#window
win_width = 1200 
win_height = 700
window = display.set_mode((win_width, win_height)) 
display.set_caption("Escape from murder") 
background = transform.scale(image.load("floor.png"), (win_width, win_height)) 

#lists
furniture = []
furniture_up = []
walls = []
walls_up = []
hides = sprite.Group()
hides_up = sprite.Group()
refls = []
refls_up = []
keys_down = []
keys_up = []
doors = []
doors_up = []

#sprites
player = Player('кольт.png',60,80, 80, win_height -120, 4) 
murder = Enemy('murder.png',110, 100,625,275, 3)

key1_up = GameSprite("key.png", 65, 25, 1000, 600, 0)
keys_up.append(key1_up)

#furiture
bed1 = GameSprite("bed.png", 125, 185, 535, 520, 0)
furniture.append(bed1)
hides.add(bed1)

bed1_up = GameSprite("bed.png", 125, 185, 0, 360, 0)
furniture_up.append(bed1_up)
hides_up.add(bed1_up)

wardrobe_up = GameSprite('wardrobe.png', 200, 90, 0, 275, 0) 
furniture_up.append(wardrobe_up) 
hides_up.add(wardrobe_up)

washbashin = GameSprite('washbashin.png', 75, 75, 900, 250, 0)
furniture.append(washbashin)

bath = GameSprite('bath.png', 185, 100, 1025, 260, 0)
furniture.append(bath)

toilet = GameSprite('toilet.png', 100, 90, 865, 420, 0) 
furniture.append(toilet)

sofa = GameSprite('sofa.png', 250, 80, 685, 615, 0 ) 
furniture.append(sofa)

carpet = GameSprite('carpet.png', 100, 180, 425, 525, 0) 

table_lr = GameSprite('table_lr.png', 125, 80, 950, 610, 0) 
furniture.append(table_lr)

table = GameSprite('table.png', 300, 100, 900, 375, 0) 
furniture_up.append(table)

table_main = GameSprite('table_main.png', 150, 200, 1050, 150, 0) 
furniture_up.append(table_main)

dresser = GameSprite('dresser.png', 150, 100, 135, 370, 0)
furniture_up.append(dresser)

g_stove = GameSprite('g_stove.png', 100, 100, 810, 375, 0) 
furniture_up.append(g_stove)

fridge = GameSprite('fridge.png', 100, 100, 1100, 600, 0) 
furniture_up.append(fridge)

#doors
door1 =  Wall(81, 49, 0, 70, 400, 100, 10)
doors.append(door1)

door2 =  Wall(81, 49, 0, 250, 500, 10, 100)
doors.append(door2)

door3 =  Wall(81, 49, 0, 350, 400, 100, 10)
doors.append(door3)

door4 =  Wall(81, 49, 0, 590, 400, 100, 10)
doors.append(door4)

door5 =  Wall(81, 49, 0, 960, 500, 110, 10)
doors.append(door5)

door1_up =  Wall(81, 49, 0, 300, 0, 10, 150)
doors_up.append(door1_up)

door2_up =  Wall(81, 49, 0, 300, 475, 10, 125)
doors_up.append(door2_up)

door3_up =  Wall(81, 49, 0, 800, 225, 10, 115)
doors_up.append(door3_up)

door4_up =  Wall(81, 49, 0, 800, 570, 10, 130)
doors_up.append(door4_up)

door_main = Wall(81, 49, 0, 0, 200, 10, 100) 
doors.append(door_main)
door_to_up = Wall(81, 49, 0, 1190, 100, 10, 100) 
doors.append(door_to_up) 
door_to_down = Wall(81, 49, 0, 1190, 5, 10, 120) 
doors_up.append(door_to_down)

#walls
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
w6_up = Wall(0, 0, 0, 900, 365, 500, 10) 
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

#game
game = True 
clock = time.Clock() 
FPS = 60 

finish = False

floor1 = False
floor2 = True

hidden = False

add_list = True
add_list_up = True
day = 1
cover = True

#music
mixer.init() 
mixer.music.load('Bmusic.mp3') 
mixer.music.play()
key_sound = mixer.Sound("key.ogg")
scream = mixer.Sound("scream.ogg")
happy = mixer.Sound("happy.ogg")
#text
font.init() 
font = font.Font(None, 70) 

day1 = font.render("DAY 1", True, (255,0,0))
day2 = font.render("DAY 2", True, (255,0,0))
day3 = font.render("DAY 3", True, (255,0,0))
day4 = font.render("DAY 4", True, (255,0,0))
day5 = font.render("DAY 5", True, (255,0,0))
lose = font.render("YOU DIED", True, (255,0,0))
won = font.render("CONGRATULATIONS! YOU ESCAPED!", True, (230,230,0))

while game: 
    for e in event.get(): 
        if e.type == QUIT: 
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE and not hidden:
                if floor2:
                    if sprite.spritecollide(player, hides_up, False):
                        player = Player('кольт.png',0,0,player.rect.x, player.rect.y, 0)
                        hidden = True
                        player.collide(refls_up)
                if floor1:
                    if sprite.spritecollide(player, hides, False):
                        player = Player('кольт.png',0,0,player.rect.x, player.rect.y, 0) 
                        hidden = True
                        player.collide(refls)
            else:
                player = Player('кольт.png',60,80,player.rect.x, player.rect.y, 4)
                hidden = False
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
        if floor1:
            carpet.reset()
            player.reset() 
            murder.reset()
            for wall in walls:
                wall.draw_wall()
            for lox in furniture:
                lox.reset()
            for door in doors:
                door.draw_wall()
            if add_list:
                for wall in walls:
                    refls.append(wall)
                for lox in furniture:
                    refls.append(lox)
                add_list = False
            player.collide(refls)
            murder.collide_something(refls)

            for key_down in keys_down:
                key_down.reset()
            if sprite.collide_rect(player, door_to_up): 
                floor1 = False
                floor2 = True 
                player = Player('кольт.png',60,80, 1050, 40, 4)

            if sprite.collide_rect(player, door_main): 
                window.fill((0,0,0)) 
                window.blit(won, (150, 300)) 
                display.update()
                happy.play()
                time.delay(3000)
                mixer.music.load("ending.ogg")
                mixer.music.play() 
                finish = True
        elif floor2:
            
            for wall in walls_up:
                wall.draw_wall()
            for lox in furniture_up:
                lox.reset()
            for door in doors_up:
                door.draw_wall()
            if add_list_up:
                for wall in walls_up:
                    refls_up.append(wall)
                for lox in furniture_up:
                    refls_up.append(lox)
                add_list_up = False
            for key_up in keys_up:
                key_up.reset()

            if sprite.collide_rect(player, key1_up):
                key_sound.play()
                keys_up.remove(key1_up)
                key1_up = GameSprite("key.png", 0, 0, 0, 0, 0)

            player.collide(refls_up)
            murder.collide_something(refls_up)
            murder.follow(player)
            if sprite.collide_rect(player, door_to_down):
                floor2 = False 
                floor1 = True 
                player = Player('кольт.png',60,80, 1050, 100, 4)  
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
        for door in doors:
            if sprite.collide_rect(player, door):
                w_w = door.height
                w_h = door.width
                door = Wall(81, 49, 0, door.rect.x, door.rect.y, door.height, door.width)
                display.update()
        
        if sprite.collide_rect(player, murder) and not hidden:  
            day += 1 
            scream.play()   
            player = Player('кольт.png',70,80, 80, win_height -120, 4)
            floor1 = False
            floor2 = True
            murder = Enemy('murder.png',110, 100,625,275, 3)
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

    display.update() 
    clock.tick(FPS)
