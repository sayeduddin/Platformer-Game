import sys
import pygame
import random
import time
#[2895, 240, 15, 15]
class Enemy:
    def __init__(self, size, coords): 
        self.coords=coords
        self.rect=pygame.Rect(coords[0],coords[1],size[0],size[1])
        self.gravity=0.15
        self.y_speed=0
        self.x_speed=random.randint(1,2)*random.choice([1,-1])
        self.screen=screen
        self.jump_time=random.randint(1,60)
        self.x_time=random.randint(50,80)
        self.bounds=[999,-999]
        self.current_platform=0
        self.size=size
        self.health=4000
        self.land_speed=0
        self.piece_timer=0
        self.jump_count=0
        self.jump_speed=-4
        
        self.boss_colour=(50,50,50)
        self.colour_timer=0
        self.hit=False
        self.change=0
        
    def update(self):
        self.y_speed+=self.gravity
        
        self.rect.x+=self.x_speed
        self.collision=self.rect.collidelist(platforms)
        if self.collision!=-1:
            if self.rect.right>platforms[self.collision].left and self.x_speed>0:
                self.rect.right=platforms[self.collision].left
                self.x_speed*=-1
            elif self.x_speed<0:
                self.rect.left=platforms[self.collision].right
                self.x_speed*=-1        
        
        self.rect.y+=self.y_speed
        self.collision=self.rect.collidelist(platforms)
        if self.collision!=-1:
            if self.rect.bottom>platforms[self.collision].top and self.y_speed>0:
                self.rect.bottom=platforms[self.collision].top
                self.gravity=0
                self.y_speed=0
                self.current_platform=self.collision
            elif self.y_speed<0:
                self.rect.top=platforms[self.collision].bottom
                self.y_speed=0

        if self.rect.right<platforms[self.current_platform].left or self.rect.left>platforms[self.current_platform].right:
            self.gravity=0.15
        
        if count%self.jump_time==0 and self.gravity==0:
            #self.jump=True
            self.y_speed=self.jump_speed
            self.gravity=0.15
            
    def remain_update(self):
        self.piece_timer+=1
        self.jump_time=1
        #self.x_speed=self.x_speed*0.99
        self.y_speed+=self.gravity
        #if self.piece_timer%50==0:
        #    self.x_speed*=1/2
        #    print(self.x_speed)
        self.rect.x+=self.x_speed
        self.collision=self.rect.collidelist(platforms)
        if self.collision!=-1:
            if self.rect.right>platforms[self.collision].left and self.x_speed>0:
                self.rect.right=platforms[self.collision].left
                self.x_speed*=-1
            elif self.x_speed<0:
                self.rect.left=platforms[self.collision].right
                self.x_speed*=-1        
        
        self.rect.y+=self.y_speed
        self.collision=self.rect.collidelist(platforms)
        if self.collision!=-1:
            if self.rect.bottom>platforms[self.collision].top and self.y_speed>0:
                self.rect.bottom=platforms[self.collision].top
                self.gravity=0
                self.land_speed=self.y_speed
                #print(self.land_speed)
                self.y_speed=0
                self.current_platform=self.collision
            elif self.y_speed<0:
                self.rect.top=platforms[self.collision].bottom
                #self.land_speed=self.y_speed
                self.y_speed=0

        if self.rect.right<platforms[self.current_platform].left or self.rect.left>platforms[self.current_platform].right:
            self.gravity=0.15
        
        if count%self.jump_time==0 and self.gravity==0:
            #self.jump=True
            self.y_speed=self.land_speed*(-((0.5)**(self.jump_count+1)))#-(1/2)*(self.y_speed)*((1/2)**self.jump_count)
            self.jump_count+=1
            self.gravity=0.15

    def bullet_hit(self):
        self.colour_timer+=1
        self.change+=1
        #print(self.hit)
        if self.hit==True and self.colour_timer%20==0:
            self.boss_colour=(50,50,50)
            self.hit=False
                #print(self.hit)
                #self.health-=50
            
            
        
class Bullet:
    def __init__(self, direction, coords):
        self.x_speed=4*direction[0]
        self.y_speed=4*direction[1]
        self.coords=coords
        #print(self.coords)
        self.rect=pygame.Rect(coords[0]+5, coords[1]+5, 6, 6)
        self.distance_travelled=0
        self.x_travelled=0
        self.y_travelled=0
        self.x_displacement=0
        #print(direction)
    def update(self):
        self.x_travelled+=self.x_speed
        self.y_travelled+=self.y_speed
        #print(self.x_travelled)
        #print(self.y_travelled)
        self.rect.x=self.coords[0]+5+self.x_travelled+self.x_displacement
        self.rect.y=self.coords[1]+5+self.y_travelled
        self.distance_travelled+=self.x_speed
        #print(self.rect)
        
        
bullets=[]       

    

pygame.init()
screen=pygame.display.set_mode([1200,400], pygame.RESIZABLE)
pygame.display.set_caption("PLATFORMANIA")
red,black,blue,green,white=(255,0,0),(0,0,0),(0,0,255),(0,255,0),(255,255,255)
add=0

remain_size=5
remains=[Enemy([remain_size,remain_size], [100,100])]

platform_coords=[(57, 352, 437, 15), (566, 90, 15, 309),
           (539, 244, 30, 15), (527, 127, 40, 15),
           (581, 90, 69, 15), (763, 0, 15, 298),
           (763, 352, 286, 47), (1018, 318, 31, 48),
           (1049, 368, 402, 31), (1018, 292, 31, 36),
           (1451, 291, 15, 108), (735, 220, 33, 15),
           (581, 384, 15, 15), (596, 384, 15, 15),
           (581, 267, 44, 15), (1600, 213, 64, 51),
           (1732, 133, 56, 54), (1857, 76, 38, 57),
           (2030, 36, 10, 84), (2247, 317, 269, 15),
           (2201, 169, 80, 15), (2201, 122, 10, 49),
           (2271, 121, 10, 48), (2614, 365, 41, 34),
           (2655, 325, 43, 41), (2698, 286, 42, 40),
           (2740, 242, 49, 46), (2789, 197, 47, 46),
           (2836, 151, 48, 47), (2884, 107, 46, 46),
           (2930, 92, 291, 15), (3155, 14, 66, 89),
           (3387, 259, 15, 15), (3502, 173, 15, 15),
           (3635, 245, 15, 15), (3753, 175, 15, 15),
           (3910, 73, 131, 15), (3900, 291, 367, 15),
           (4437, 357, 244, 15), (4308, 83, 158, 15),
           (4780, 270, 120, 15)]

enemy_coords=[(1134, 317), (1299, 339),
              (1248, 269), (1345, 267),
              (1157, 236), (2238, 139),
              (3118, 54), (3956, 30),
              (4370, 39), (4728, 39),
              (4747, 18), (4866, 244)]

spawn_coords=[[2225, 116], [3106, 49], [3956, 30], [4324, 39], [4410, 41]]

checkpoints=[[4780, 155], [3950, 261], [3178, -3], [2294, 277], [1451, 267], [300, 200]]

checkpoint_coords=[[4780, 155], [3950, 261], [3178, -3], [2294, 277], [1451, 267], [300, 200]]

player=pygame.Rect(300,200,13,13)
size=15
gravity=0.17
y_speed=-6
clock = pygame.time.Clock()
current_platform=0
fps=60
previous = time.time() * 1000
count=0
won=0
start=time.time()
font = pygame.font.Font('DO NOT REMOVE.ttf', 15) 
lvl=0
pause=0
option=0
colours=[red, red, red]
restart=0
deaths=0

platforms=[]
for platform in platform_coords:
    platforms.append(pygame.Rect(platform[0], platform[1], platform[2], platform[3]))
    

enemies=[]
for coords in enemy_coords:
    enemies.append(Enemy((size,size),coords))


lvl_times=[]
total_deaths=[]


def drawRects(rects, colour, screen):
    for rect in rects:
        pygame.draw.rect(screen, colour, rect)

def reset():
    global enemies
    global player
    global platforms
    global y_speed
    global spawn_coords
    global current_platform
    global checkpoints
    global won
    global restart
    global checkpoint_coords
    global platform_coords
    global enemy_coords
    global deaths
    global boss_alive
    global boss
    global boss_beaten

    if won:
        deaths=0
        won=0
        if lvl==1:
            enemies=[[5000,0]]
            enemy_coords=[[5000,0]]
            platform_coords=[[270, 345, 15, 15], [285, 345, 15, 15], [300, 345, 15, 15], [315, 345, 15, 15], [330, 345, 15, 15], [345, 345, 15, 15], [360, 345, 15, 15], [375, 345, 15, 15], [390, 345, 15, 15], [405, 345, 15, 15], [420, 345, 15, 15], [435, 345, 15, 15], [450, 345, 15, 15], [465, 345, 15, 15], [480, 345, 15, 15], [495, 345, 15, 15], [510, 345, 15, 15], [525, 345, 15, 15], [540, 345, 15, 15], [555, 345, 15, 15], [570, 345, 15, 15], [585, 345, 15, 15], [585, 330, 15, 15], [585, 315, 15, 15], [585, 300, 15, 15], [600, 300, 15, 15], [615, 300, 15, 15], [630, 300, 15, 15], [630, 285, 15, 15], [630, 270, 15, 15], [630, 255, 15, 15], [645, 255, 15, 15], [660, 255, 15, 15], [675, 255, 15, 15], [675, 240, 15, 15], [675, 225, 15, 15], [675, 210, 15, 15], [690, 210, 15, 15], [705, 210, 15, 15], [720, 210, 15, 15], [735, 210, 15, 15], [750, 210, 15, 15], [765, 210, 15, 15], [780, 210, 15, 15], [795, 210, 15, 15], [810, 210, 15, 15], [825, 210, 15, 15], [840, 210, 15, 15], [855, 210, 15, 15], [855, 195, 15, 15], [855, 180, 15, 15], [855, 165, 15, 15], [870, 165, 15, 15], [885, 165, 15, 15], [900, 165, 15, 15], [900, 150, 15, 15], [900, 135, 15, 15], [900, 120, 15, 15], [915, 120, 15, 15], [930, 120, 15, 15], [945, 120, 15, 15], [960, 120, 15, 15], [975, 120, 15, 15], [990, 120, 15, 15], [1005, 120, 15, 15], [1020, 120, 15, 15], [1035, 120, 15, 15], [1050, 120, 15, 15], [1065, 120, 15, 15], [1080, 120, 15, 15], [1095, 120, 15, 15], [1095, 105, 15, 15], [1095, 90, 15, 15], [1095, 75, 15, 15], [1095, 60, 15, 15], [1095, 45, 15, 15], [1170, 345, 15, 15], [1185, 345, 15, 15], [1200, 345, 15, 15], [1215, 345, 15, 15], [1230, 345, 15, 15], [1245, 345, 15, 15], [1260, 345, 15, 15], [1275, 345, 15, 15], [1290, 345, 15, 15], [1305, 345, 15, 15], [1320, 345, 15, 15], [1335, 345, 15, 15], [1350, 345, 15, 15], [1365, 345, 15, 15], [1380, 345, 15, 15], [1395, 345, 15, 15], [1410, 345, 15, 15], [1425, 345, 15, 15], [1440, 345, 15, 15], [1455, 345, 15, 15], [1470, 345, 15, 15], [1485, 345, 15, 15], [1500, 345, 15, 15], [1515, 345, 15, 15], [1530, 345, 15, 15], [1545, 345, 15, 15], [1560, 345, 15, 15], [1575, 345, 15, 15], [1590, 345, 15, 15], [1170, 300, 15, 15], [1170, 285, 15, 15], [1590, 300, 15, 15], [1590, 285, 15, 15], [1590, 270, 15, 15], [1590, 255, 15, 15], [1590, 240, 15, 15], [1605, 240, 15, 15], [1620, 240, 15, 15], [1635, 240, 15, 15], [1650, 240, 15, 15], [1665, 240, 15, 15], [1680, 240, 15, 15], [1695, 240, 15, 15], [1710, 255, 15, 15], [1725, 255, 15, 15], [1740, 255, 15, 15], [1695, 255, 15, 15], [1740, 270, 15, 15], [1755, 270, 15, 15], [1770, 270, 15, 15], [1785, 270, 15, 15], [1785, 285, 15, 15], [1800, 285, 15, 15], [1815, 285, 15, 15], [1830, 285, 15, 15], [1845, 285, 15, 15], [1920, 120, 15, 15], [1965, 120, 15, 15], [1905, 105, 15, 15], [1980, 105, 15, 15], [1995, 90, 15, 15], [1890, 90, 15, 15], [1890, 75, 15, 15], [1995, 75, 15, 15], [1890, 60, 15, 15], [1995, 60, 15, 15], [1905, 45, 15, 15], [1980, 45, 15, 15], [1905, 30, 15, 15], [1980, 30, 15, 15], [1920, 30, 15, 15], [1965, 30, 15, 15], [1980, 315, 15, 15], [1995, 315, 15, 15], [2010, 315, 15, 15], [2025, 315, 15, 15], [2040, 315, 15, 15], [1965, 315, 15, 15], [1950, 315, 15, 15], [2055, 315, 15, 15], [2070, 315, 15, 15], [2085, 315, 15, 15], [2100, 315, 15, 15], [2115, 315, 15, 15], [2130, 315, 15, 15], [2145, 315, 15, 15], [2160, 315, 15, 15], [2235, 210, 15, 15], [2250, 210, 15, 15], [2265, 210, 15, 15], [2280, 210, 15, 15], [2295, 210, 15, 15], [2310, 210, 15, 15], [2325, 210, 15, 15], [2340, 210, 15, 15], [2355, 210, 15, 15], [2475, 135, 15, 15], [2625, 135, 15, 15], [2775, 135, 15, 15], [2925, 270, 15, 15], [2925, 285, 15, 15], [2925, 300, 15, 15], [2925, 315, 15, 15], [2925, 330, 15, 15], [2925, 345, 15, 15], [2925, 360, 15, 15], [2925, 375, 15, 15], [2925, 390, 15, 15], [3015, 345, 15, 15], [3030, 345, 15, 15], [3045, 345, 15, 15], [3135, 270, 15, 15], [3150, 270, 15, 15], [3165, 270, 15, 15], [3255, 195, 15, 15], [3270, 195, 15, 15], [3285, 195, 15, 15], [3405, 195, 15, 15], [3405, 210, 15, 15], [3405, 225, 15, 15], [3405, 240, 15, 15], [3405, 255, 15, 15], [3405, 270, 15, 15], [3420, 270, 15, 15], [3435, 270, 15, 15], [3450, 270, 15, 15], [3495, 270, 15, 15], [3510, 270, 15, 15], [3525, 270, 15, 15], [3570, 270, 15, 15], [3585, 270, 15, 15], [3600, 270, 15, 15], [3645, 270, 15, 15], [3660, 270, 15, 15], [3675, 270, 15, 15], [3720, 270, 15, 15], [3735, 270, 15, 15], [3750, 270, 15, 15], [3795, 270, 15, 15], [3810, 270, 15, 15], [3825, 270, 15, 15], [3840, 270, 15, 15], [3840, 255, 15, 15], [3840, 240, 15, 15], [3840, 225, 15, 15], [3840, 210, 15, 15], [3840, 195, 15, 15], [3975, 240, 15, 15], [3990, 240, 15, 15], [4005, 240, 15, 15], [4020, 240, 15, 15], [4035, 240, 15, 15], [4050, 240, 15, 15], [4065, 240, 15, 15], [4080, 240, 15, 15], [3465, 270, 15, 15], [3780, 270, 15, 15], [3465, 270, 15, 15], [3480, 270, 15, 15], [3765, 270, 15, 15], [3780, 270, 15, 15], [3540, 270, 15, 15], [3705, 270, 15, 15], [1170, 315, 15, 15], [1170, 330, 15, 15]]
            spawn_coords=[[100, 100], [555, 315], [825, 180], [1065, 90], [1200, 285], [1560, 285], [1890, 45], [1905, 60], [1980, 60], [1995, 45], [2625, 0], [3150, 30], [3150, 135], [3420, 225], [3825, 225]]
            checkpoint_coords=[[3975, 120], [3030, 315], [2355, 180], [1590, 210], [1095, 15], [300, 200]]
            checkpoints=[[3975, 120], [3030, 315], [2355, 180], [1590, 210], [1095, 15], [300, 200]]
        elif lvl==2:
            enemies=[[5000,0]]
            enemy_coords=[[5000,0]]
            platform_coords=[[1785, 345, 15, 15], [1830, 345, 15, 15], [1980, 345, 15, 15], [2595, 345, 15, 15], [2745, 345, 15, 15], [2790, 345, 15, 15], [270, 345, 15, 15], [285, 345, 15, 15], [300, 345, 15, 15], [315, 345, 15, 15], [330, 345, 15, 15], [345, 345, 15, 15], [360, 345, 15, 15], [375, 345, 15, 15], [390, 345, 15, 15], [405, 345, 15, 15], [420, 345, 15, 15], [435, 345, 15, 15], [450, 345, 15, 15], [465, 345, 15, 15], [480, 345, 15, 15], [495, 345, 15, 15], [510, 345, 15, 15], [525, 345, 15, 15], [540, 345, 15, 15], [555, 345, 15, 15], [570, 345, 15, 15], [585, 345, 15, 15], [600, 345, 15, 15], [615, 345, 15, 15], [630, 345, 15, 15], [645, 345, 15, 15], [660, 345, 15, 15], [675, 345, 15, 15], [690, 345, 15, 15], [705, 345, 15, 15], [720, 345, 15, 15], [735, 345, 15, 15], [750, 345, 15, 15], [765, 345, 15, 15], [780, 345, 15, 15], [795, 345, 15, 15], [810, 345, 15, 15], [825, 345, 15, 15], [840, 345, 15, 15], [855, 345, 15, 15], [870, 345, 15, 15], [885, 345, 15, 15], [900, 345, 15, 15], [915, 345, 15, 15], [930, 345, 15, 15], [945, 345, 15, 15], [960, 345, 15, 15], [975, 345, 15, 15], [990, 345, 15, 15], [1005, 345, 15, 15], [1020, 345, 15, 15], [1035, 345, 15, 15], [1050, 345, 15, 15], [1065, 345, 15, 15], [1080, 345, 15, 15], [1095, 345, 15, 15], [1110, 345, 15, 15], [1125, 345, 15, 15], [1140, 345, 15, 15], [1155, 345, 15, 15], [1170, 345, 15, 15], [1185, 345, 15, 15], [1200, 345, 15, 15], [1215, 345, 15, 15], [1230, 345, 15, 15], [1245, 345, 15, 15], [1260, 345, 15, 15], [1275, 345, 15, 15], [1275, 330, 15, 15], [1275, 315, 15, 15], [1275, 300, 15, 15], [1290, 300, 15, 15], [1305, 300, 15, 15], [1320, 300, 15, 15], [1335, 300, 15, 15], [1350, 300, 15, 15], [1365, 300, 15, 15], [1365, 285, 15, 15], [1365, 270, 15, 15], [1365, 255, 15, 15], [1380, 255, 15, 15], [1395, 255, 15, 15], [1410, 255, 15, 15], [1425, 255, 15, 15], [1440, 255, 15, 15], [1455, 255, 15, 15], [1455, 240, 15, 15], [1455, 225, 15, 15], [1455, 210, 15, 15], [1470, 210, 15, 15], [1485, 210, 15, 15], [1500, 210, 15, 15], [1515, 210, 15, 15], [1530, 210, 15, 15], [1545, 210, 15, 15], [1545, 195, 15, 15], [1545, 180, 15, 15], [1545, 165, 15, 15], [1560, 165, 15, 15], [1575, 165, 15, 15], [1590, 165, 15, 15], [1605, 165, 15, 15], [1620, 165, 15, 15], [1635, 165, 15, 15], [1635, 150, 15, 15], [1635, 135, 15, 15], [1635, 120, 15, 15], [1650, 120, 15, 15], [1665, 120, 15, 15], [1680, 120, 15, 15], [1695, 120, 15, 15], [1710, 120, 15, 15], [1725, 120, 15, 15], [1725, 135, 15, 15], [1725, 150, 15, 15], [1725, 165, 15, 15], [1725, 180, 15, 15], [1725, 195, 15, 15], [1725, 210, 15, 15], [1725, 225, 15, 15], [1725, 240, 15, 15], [1725, 255, 15, 15], [1725, 270, 15, 15], [1725, 285, 15, 15], [1725, 300, 15, 15], [1725, 315, 15, 15], [1725, 330, 15, 15], [1725, 345, 15, 15], [1755, 345, 15, 15], [1770, 345, 15, 15], [1800, 345, 15, 15], [1815, 345, 15, 15], [1845, 345, 15, 15], [1860, 345, 15, 15], [1875, 345, 15, 15], [1920, 345, 15, 15], [1935, 345, 15, 15], [1950, 345, 15, 15], [1965, 345, 15, 15], [1995, 345, 15, 15], [2010, 345, 15, 15], [2025, 345, 15, 15], [2040, 345, 15, 15], [2055, 345, 15, 15], [2070, 345, 15, 15], [2115, 345, 15, 15], [2130, 345, 15, 15], [2145, 345, 15, 15], [2160, 345, 15, 15], [2175, 345, 15, 15], [2190, 345, 15, 15], [2205, 345, 15, 15], [2220, 345, 15, 15], [2235, 345, 15, 15], [2250, 345, 15, 15], [2265, 345, 15, 15], [2310, 345, 15, 15], [2325, 345, 15, 15], [2340, 345, 15, 15], [2355, 345, 15, 15], [2370, 345, 15, 15], [2385, 345, 15, 15], [2400, 345, 15, 15], [2415, 345, 15, 15], [2430, 345, 15, 15], [2445, 345, 15, 15], [2460, 345, 15, 15], [2505, 345, 15, 15], [2520, 345, 15, 15], [2535, 345, 15, 15], [2550, 345, 15, 15], [2565, 345, 15, 15], [2580, 345, 15, 15], [2610, 345, 15, 15], [2625, 345, 15, 15], [2640, 345, 15, 15], [2655, 345, 15, 15], [2700, 345, 15, 15], [2715, 345, 15, 15], [2730, 345, 15, 15], [2760, 345, 15, 15], [2775, 345, 15, 15], [2805, 345, 15, 15], [2820, 345, 15, 15], [2835, 345, 15, 15], [2850, 345, 15, 15], [2865, 345, 15, 15], [2880, 345, 15, 15], [2895, 345, 15, 15], [2895, 330, 15, 15], [2895, 315, 15, 15], [2895, 300, 15, 15], [2895, 285, 15, 15], [2895, 270, 15, 15], [2895, 255, 15, 15], [2895, 240, 15, 15], [2895, 225, 15, 15], [2895, 210, 15, 15], [2895, 195, 15, 15], [2895, 180, 15, 15], [2895, 165, 15, 15], [2895, 150, 15, 15], [2895, 135, 15, 15], [2895, 120, 15, 15], [2895, 105, 15, 15], [2895, 90, 15, 15], [2895, 75, 15, 15], [2895, 60, 15, 15], [2895, 45, 15, 15], [2895, 30, 15, 15], [3015, 195, 15, 15], [3030, 195, 15, 15], [3045, 195, 15, 15], [3060, 195, 15, 15], [3075, 195, 15, 15], [3090, 195, 15, 15], [3105, 195, 15, 15], [3120, 195, 15, 15], [1350, 60, 15, 15], [1365, 60, 15, 15], [1380, 60, 15, 15], [1395, 60, 15, 15], [1410, 60, 15, 15], [1425, 60, 15, 15], [1440, 60, 15, 15], [1455, 60, 15, 15], [1470, 60, 15, 15], [1485, 60, 15, 15], [1500, 60, 15, 15], [1515, 60, 15, 15], [1530, 60, 15, 15], [1545, 60, 15, 15], [1560, 60, 15, 15], [1575, 60, 15, 15], [1590, 60, 15, 15], [1605, 60, 15, 15], [1620, 60, 15, 15], [1635, 60, 15, 15], [1650, 60, 15, 15], [1665, 60, 15, 15], [1680, 60, 15, 15], [1695, 60, 15, 15], [1710, 60, 15, 15], [1350, 45, 15, 15], [1335, 60, 15, 15], [1380, 45, 15, 15], [1410, 45, 15, 15], [1440, 45, 15, 15], [1470, 45, 15, 15], [1500, 45, 15, 15], [1530, 45, 15, 15], [1560, 45, 15, 15], [1590, 45, 15, 15], [1620, 45, 15, 15], [1650, 45, 15, 15], [1680, 45, 15, 15], [1710, 45, 15, 15], [1365, 30, 15, 15], [1395, 30, 15, 15], [1425, 30, 15, 15], [1455, 30, 15, 15], [1485, 30, 15, 15], [1515, 30, 15, 15], [1545, 30, 15, 15], [1575, 30, 15, 15], [1605, 30, 15, 15], [1635, 30, 15, 15], [1665, 30, 15, 15], [1695, 30, 15, 15], [1380, 15, 15, 15], [1410, 15, 15, 15], [1440, 15, 15, 15], [1470, 15, 15, 15], [1500, 15, 15, 15], [1530, 15, 15, 15], [1560, 15, 15, 15], [1590, 15, 15, 15], [1620, 15, 15, 15], [1650, 15, 15, 15], [1680, 15, 15, 15], [1395, 0, 15, 15], [1425, 0, 15, 15], [1455, 0, 15, 15], [1485, 0, 15, 15], [1515, 0, 15, 15], [1545, 0, 15, 15], [1575, 0, 15, 15], [1605, 0, 15, 15], [1635, 0, 15, 15], [1665, 0, 15, 15], [1740, 345, 15, 15], [1725, 60, 15, 15], [1725, 45, 15, 15], [1725, 30, 15, 15], [1725, 15, 15, 15], [1725, 0, 15, 15], [1710, 15, 15, 15], [1695, 0, 15, 15], [1785, 345, 15, 15], [2670, 360, 15, 15], [2685, 360, 15, 15], [1890, 360, 15, 15], [1905, 360, 15, 15]]
#[2895, 225, 15, 15]
#[2880, 240, 15, 15]
            boss_alive=False
            boss_beaten=False
            #boss=Enemy([135, 135], [2370, 105])#2370
            #boss.jump_speed=-8
            #print("spawned")
            spawn_coords=[[1245, 315], [1425, 225], [1605, 135]]
            checkpoint_coords=[[3015, 75], [1710, 90], [300, 200]]
            checkpoints=[[3015, 75], [1710, 90], [300, 200]]
            
        elif lvl==3:
            platform_coords=[[300, 240, 15, 15], [300, 150, 15, 15], [345, 195, 15, 15], [255, 195, 15, 15], [345, 240, 15, 15], [255, 240, 15, 15], [255, 150, 15, 15], [345, 150, 15, 15], [255, 165, 15, 15], [255, 180, 15, 15], [255, 210, 15, 15], [255, 225, 15, 15], [270, 240, 15, 15], [285, 240, 15, 15], [315, 240, 15, 15], [330, 240, 15, 15], [345, 210, 15, 15], [345, 225, 15, 15], [345, 180, 15, 15], [345, 165, 15, 15], [330, 150, 15, 15], [315, 150, 15, 15], [285, 150, 15, 15], [270, 150, 15, 15]]
#[345, 150, 15, 15]
            checkpoint_coords=[[3015, 75], [300, 195]]
            checkpoints=[[3015, 75], [300, 195]]
    #print("resetting")
    new=False
    if not won:
        deaths+=1
        for x in range(len(checkpoints)):
            #print(player.x,">",checkpoints[x][0], ";", restart)
            if player.x>checkpoints[x][0] and not restart:
                player=pygame.Rect(300,checkpoints[x][1],13,13)
                new=True
                #print("worked")
                difference=checkpoint_coords[x][0]-300
                #print("reset to checkpoint")
                break
    if not new:
        player=pygame.Rect(300,200,13,13)
        difference=0
        restart=0
        deaths=0

    for x in range(len(checkpoints)):
        checkpoints[x][0]=checkpoint_coords[x][0]-difference
    
    enemies=[]
    for coords in enemy_coords:
        enemies.append(Enemy((size,size),coords))

    platforms=[]
    for platform in platform_coords:
        platforms.append(pygame.Rect(platform[0], platform[1], platform[2], platform[3]))

    y_speed=-6
    if lvl==0:
        spawn_coords=[[2225, 116], [3106, 49], [3956, 30], [4324, 39], [4410, 41]]
    elif lvl==1:
        spawn_coords=[[100, 100], [555, 315], [825, 180], [1065, 90], [1200, 285], [1560, 285], [1890, 45], [1905, 60], [1980, 60], [1995, 45], [2625, 0], [3150, 30], [3150, 135], [3420, 225], [3825, 225]]
    elif lvl==2:
        boss_beaten=False
        #boss=Enemy([135, 135], [2370-difference, 105])
        spawn_coords=spawn_coords=[[1245, 315], [1425, 225], [1605, 135]] #[boss.rect.left, boss.rect.top], [boss.rect.right-20, boss.rect.top], [boss.rect.left+57.5, boss.rect.top]]
        boss_alive=False
        #boss.jump_speed=-8
        #boss.x_speed=random.choice([-1,1])
    for x in range(len(platforms)):
        platforms[x].left-=difference
    for x in range(len(enemies)):
        enemies[x].rect.left-=difference
    for x in range(len(spawn_coords)):
        spawn_coords[x][0]-=difference
        
    current_platform=0
    #print(deaths)
        
"""
enemies=reset_enemies(enemy_coords)
player=pygame.Rect(300,200,10,10)
platforms=reset_platforms(platform_coords)
y_speed=-6
spawn_coords=[[2225, 116], [3106, 49], [3956, 30], [4324, 39], [4410, 41]]
current_platform=0
"""
direction=1
boss_alive=False
bullet_remains=[]
bullet_timer=0
boss_beaten=False
#MAIN
while True:
    if not pause:
        count+=1
        bullet_timer+=1

        if count%100==0:
            for coord in spawn_coords:
                enemies.append(Enemy((size,size),coord))
        if count%3==0 and lvl==3:
            #print("bullet spawned")
            direction=[1, 1]
            coords=[random.randint(0,800), 0]
            bullets.append(Bullet(direction, coords))
            #bullets[-1].x_speed/=random.randint(1,3)
            #bullets[-1].y_speed=bullets[-1].x_speed
            coords=[0, random.randint(0,800)]
            bullets.append(Bullet(direction, coords))
            #bullets[-1].x_speed/=random.randint(1,3)
            #bullets[-1].y_speed=bullets[-1].x_speed
        #print(boss_alive, boss_beaten)
        if lvl==2 and not boss_alive and player.left>platforms[-1].right and player.left<platforms[-1].right+10 and not boss_beaten:
            #print("everything in order")
            boss_alive=True
            boss=Enemy([135, 135], [700, -200])#2370
            spawn_coords.extend([[boss.rect.left, boss.rect.top], [boss.rect.right-20, boss.rect.top], [boss.rect.left+57.5, boss.rect.top]])
            boss.x_speed=random.choice([1,-1])
            boss.jump_speed=-10
        if boss_alive:
            #if count%boss.jump_time==0:
            boss.jump_time=1#random.randint(30,120)
            collision=boss.rect.collidelist(bullets)
            
            #print(collision)
            boss.bullet_hit()
            if collision!=-1:
                #print("collision")
                boss.colour_timer=0
                boss.hit=True
                boss.boss_colour=(158, 33, 33)
                #print("hit with bullet")
                boss.health-=25
                #print(boss.health)
                if boss.health<=0:
                    boss_alive=False
                    #print("boss is dead")
                    boss_beaten=True
                    platforms.append(pygame.Rect(platforms[202].left-15, 240, 15, 15))
                    platforms.append(pygame.Rect(platforms[212].left-15, 120, 15, 15))
                    spawn_coords=spawn_coords[:-3]
                    for a in range(0,135,9):
                        for b in range(0,135,9):
                            remains.append(Enemy((remain_size, remain_size), (boss.rect.left+a, boss.rect.top+b)))
                            remains[-1].y_speed=random.randint(-7,2)
                            remains[-1].x_speed=random.randint(1,4)*random.choice([-1,1])
                bullets.pop(collision)
            if player.colliderect(boss):
                reset()

        for x in range(len(enemies)):
            if enemies[x].rect.top>450:
                enemies.pop(x)
                break
            #if enemies[x].health==0:
            #    enemies.pop(x)
            #    break
            collision=enemies[x].rect.collidelist(bullets)
            if collision!=-1:
                #print("explode")
                for a in range(0,15,5):
                    for b in range(0,15,5):
                        remains.append(Enemy((remain_size, remain_size), (enemies[x].rect.left+a, enemies[x].rect.top+b)))
                        remains[-1].y_speed=random.randint(-5,1)
                
                            
                enemies.pop(x)
                bullets.pop(collision)
                break
        for x in range(len(remains)):
            if remains[x].piece_timer>150:
                remains.pop(x)
                break

        for x in range(len(bullet_remains)):
            if bullet_remains[x].piece_timer>100:
                bullet_remains.pop(x)
                break

        for x in range(len(bullets)):
            collision=bullets[x].rect.collidelist(platforms)
            if collision!=-1:
                #print("hit wall")
                for a in range(0,6,2):
                    for b in range(0,6,2):
                        bullet_remains.append(Enemy((2, 2), (bullets[x].rect.left+a, bullets[x].rect.top+b)))
                        bullet_remains[-1].y_speed=random.randint(-3,1)#bullets
                bullets.pop(x)
                break
            if abs(bullets[x].distance_travelled)>800:
                bullets.pop(x)
                break
        
        current = time.time() * 1000
        elapsed = current - previous
        previous = current
        delay = 1000.0/fps - elapsed
        delay = max(int(delay), 0)
        #print(pygame.mouse.get_pos())
        #draw_platforms=[]
        #for platform in platforms:
        #    if platform.left<800:
        #        draw_platforms.append(platform)
        #print(fps)
        #if fps%1==0:
        #    x=random.randint(0,600)
        #    enemies.append(Enemy((50,50),(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])))#(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
        #print(clock)
        player.y+=y_speed
        collision=player.collidelist(enemies)
        if collision!=-1 and player.top<enemies[collision].rect.top and player.bottom<enemies[collision].rect.bottom:#not y_speed==0:
            #print("hit from above")
            for x in range(0,15,5):
                for y in range(0,15,5):
                    remains.append(Enemy((remain_size, remain_size), (enemies[collision].rect.left+x, enemies[collision].rect.top+y)))
            enemies.pop(collision)
            y_speed=-6
        elif collision!=-1:
            #print("dead")
            reset()
            """
            enemies=reset_enemies(enemy_coords)
            player=pygame.Rect(300,200,10,10)
            platforms=reset_platforms(platform_coords)
            y_speed=-6
            spawn_coords=[[2225, 116], [3106, 49], [3956, 30], [4324, 39], [4410, 41]]
            current_platform=0
            """
        y_speed+=gravity

        if player.y>450:
            """
            enemies=reset_enemies(enemy_coords)
            player=pygame.Rect(300,200,10,10)
            platforms=reset_platforms(platform_coords)
            y_speed=-6
            spawn_coords=[[2225, 116], [3106, 49], [3956, 30], [4324, 39], [4410, 41]]
            current_platform=0
            """
            reset()
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                pressed=pygame.mouse.get_pressed()
                if pressed[0]:
                    #print(event.type)
                    #print(pygame.mouse.get_pressed())
                    #print(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                    #mouse=pygame.mouse.get_pos()
                    #divisor=((mouse[0]-player.left)**2+(mouse[1]-player.top)**2)**(0.5)
                    #direction=[(mouse[0]-player.left)/divisor, (mouse[1]-player.top)/divisor]
                    #bullets.append(Bullet(direction, [player.left, player.top]))
                    #print("")
                    bullet_timer=0
                    #print(player.top)
                    #platforms.append(pygame.Rect(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],15,15))
                    #platforms=sorted(platforms, key=lambda x: x.top, reverse=False)#remove if you want
                #elif pressed[2]:
                    #for x in range(0, 15, 5):
                    #    remains.append(Enemy((remain_size, remain_size),(pygame.mouse.get_pos()[0]+x,pygame.mouse.get_pos()[1]+x)))
                    #for piece in remains[-3:]:
                    #    #print(remains[-3:])
                    #    piece.y_speed=random.randint(-3,0)
                    #enemies.append(Enemy((size,size),(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])))
                    #print(pygame.mouse.get_pos())
                    #print(enemies[0].health)
                    #enemies[0].health-=1
                    #print(enemies[0].health)
                    #won=1
                
            if event.type==pygame.KEYDOWN:
                #print("key pressed")
                if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    #print("Paused")
                    pause=1
                    save_time=time.time()-start
                    option=0
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    #print("shoot", direction)
                    bullets.append(Bullet([direction, 0], [player.left, player.top]))


        pressed=pygame.mouse.get_pressed()
        if pressed[0] and bullet_timer%15==0:
            #print(bullet_timer)
            mouse=pygame.mouse.get_pos()
            divisor=((mouse[0]-player.left)**2+(mouse[1]-player.top)**2)**(0.5)
            direction=[(mouse[0]-player.left)/divisor, (mouse[1]-player.top)/divisor]
            bullets.append(Bullet(direction, [player.left, player.top]))
        
        collision=player.collidelist(platforms)
        if player.collidelist(platforms)!=-1:
            if y_speed>0:
                gravity=0
                y_speed=0
                #count=0
                player.bottom=platforms[collision].top
                current_platform=collision
                #print(current_platform)
            elif y_speed<0:
                y_speed=0
                player.top=platforms[collision].bottom
        keys=pygame.key.get_pressed()
        
        if keys[pygame.K_d]:
            direction=1
            #player=player.move(3,0)
            for x in range(len(platforms)):
                platforms[x].left-=2
            for x in range(len(enemies)):
                enemies[x].rect.x-=2
            for x in range(len(checkpoints)):###########################
                checkpoints[x][0]-=2
            for x in range(len(remains)):
                remains[x].rect.x-=2
            for x in range(len(bullets)):
                bullets[x].x_displacement-=2
            for remain in bullet_remains:
                remain.rect.x-=2
            if boss_alive:
                boss.rect.x-=2
                
            collision=player.collidelist(enemies)
            if collision!=-1:
                #print("dead")
                """
                enemies=reset_enemies(enemy_coords)
                player=pygame.Rect(300,200,10,10)
                platforms=reset_platforms(platform_coords)
                y_speed=-6
                spawn_coords=[[2225, 116], [3106, 49], [3956, 30], [4324, 39], [4410, 41]]
                current_platform=0
                """
                reset()
                
            for x in range(len(spawn_coords)):
                spawn_coords[x][0]-=2
            collision=player.collidelist(platforms)
            if collision!=-1:
                for x in range(len(enemies)):
                    enemies[x].rect.x+=2
                for x in range(len(spawn_coords)):
                    spawn_coords[x][0]+=2
                for x in range(len(platforms)):
                    platforms[x].left+=2
                for x in range(len(checkpoints)):########################
                    checkpoints[x][0]+=2
                for x in range(len(remains)):
                    remains[x].rect.x+=2
                for x in range(len(bullets)):
                    bullets[x].x_displacement+=2
                for remain in bullet_remains:
                    remain.rect.x+=2
                if boss_alive:
                    boss.rect.x+=2
                player.right=platforms[collision].left
                #if player.right>platforms[collision].left:
                #    player.right=platforms[collision].left
                #    collision=player.collidelist(platforms)
                    
        if keys[pygame.K_a]:
            direction=-1
            #player=player.move(-3,0)
            for x in range(len(platforms)):
                platforms[x].left+=2
            for x in range(len(enemies)):
                enemies[x].rect.x+=2
            for x in range(len(checkpoints)):
                checkpoints[x][0]+=2
            for x in range(len(remains)):
                remains[x].rect.x+=2
            for x in range(len(bullets)):
                bullets[x].x_displacement+=2
            for remain in bullet_remains:
                remain.rect.x+=2
            if boss_alive:
                boss.rect.x+=2
            collision=player.collidelist(enemies)
            if collision!=-1:
                #print("dead")
                """
                enemies=reset_enemies(enemy_coords)
                player=pygame.Rect(300,200,10,10)
                platforms=reset_platforms(platform_coords)
                y_speed=-6
                spawn_coords=[[2225, 116], [3106, 49], [3956, 30], [4324, 39], [4410, 41]]
                current_platform=0
                """
                reset()
            for x in range(len(spawn_coords)):
                spawn_coords[x][0]+=2
            collision=player.collidelist(platforms)
            if collision!=-1:
                for x in range(len(enemies)):
                    enemies[x].rect.x-=2
                for x in range(len(spawn_coords)):
                    spawn_coords[x][0]-=2
                for x in range(len(platforms)):
                    platforms[x].left-=2
                for x in range(len(checkpoints)):
                    checkpoints[x][0]-=2
                for x in range(len(remains)):
                    remains[x].rect.x-=2
                for x in range(len(bullets)):
                    bullets[x].x_displacement-=2
                for remain in bullet_remains:
                    remain.rect.x-=2
                if boss_alive:
                    boss.rect.x-=2
                
                player.left=platforms[collision].right
                #if player.left<platforms[collision].right:
                #    player.left=platforms[collision].right
                #    collision=player.collidelist(platforms)




        if keys[pygame.K_w]:
            if gravity==0:
                gravity=0.17
                y_speed=-6.5
                collision=player.collidelist(platforms)
                """
                if collision!=1:
                    if player.bottom<platforms[collision].top and y_speed<0:
                        player.bottom=platforms[collision].top
                        print("down ho")
                """

        if keys[pygame.K_s] and gravity!=0:
            if y_speed<0:
                y_speed=0
            y_speed+=0.5


        if player.left>platforms[current_platform].right or player.right<platforms[current_platform].left or y_speed!=0:
            gravity=0.17
            

        #print(y_speed)
        
        for enemy in enemies:
            enemy.update()

        for piece in remains:
            piece.remain_update()

        #DRAWING
        screen.fill(white)

        #pygame.draw.rect(screen, (255,255,0), (4780, 155, 140, 127))    #(4780, 155), (4920, 282)


        if lvl==3:
            final_total_time=float(lvl_times[0])+float(lvl_times[1])+float(lvl_times[2])
            text=font.render("Total Time: "+str(round(final_total_time, 2))+" secs", True, black)
            screen.blit(text, (platforms[7].right+10,platforms[7].top, 50, 20))
            text=font.render("Total Deaths: "+str(total_deaths[0]+total_deaths[1]+total_deaths[2]), True, black)
            screen.blit(text, (platforms[7].right+10,platforms[7].top+18, 50, 20))

            
        if lvl==2 and boss_alive==True:
            
            boss.update()
            spawn_coords[-2]=[boss.rect.left, boss.rect.top]
            spawn_coords[-1]=[boss.rect.right-20, boss.rect.top]
            spawn_coords[-3]=[boss.rect.left+57.5, boss.rect.top]
            drawRects([boss], boss.boss_colour, screen)
            if boss.health>0:
                #print(boss.rect.left, boss.rect.top-15)
                pygame.draw.rect(screen, (0, 200, 0), (boss.rect.left, boss.rect.top-15, 135*(boss.health/4000), 5))


        for x in checkpoints:
            pygame.draw.rect(screen, blue, (x[0], x[1], 15, 15))
        pygame.draw.rect(screen, (255,192,203), (checkpoints[0][0], checkpoints[0][1], 120, 120))
        for x in spawn_coords:
            pygame.draw.rect(screen, (255,255,0), (x[0], x[1], 15, 15))
        if boss_alive:
            for x in spawn_coords[-3:]:
                pygame.draw.rect(screen, (240,0,0), (x[0], x[1], 20, 20))

        if player.x>checkpoints[0][0] and gravity==0 and won==0:
            won=1
            text=font.render("WON", True, black)
            screen.blit(text, (checkpoints[0][0],checkpoints[0][1], 50, 20))

            text=font.render(run_time, True, black)
            screen.blit(text, (checkpoints[0][0]+50,checkpoints[0][1]+50, 50, 20))
            start=time.time()

        for bullet in bullets:
            bullet.update()

        for remain in bullet_remains:
            remain.remain_update()

        drawRects(bullets, [255,165,0], screen)
        drawRects(platforms, black, screen)
        drawRects([player], green, screen)
        drawRects(enemies, red, screen)
        drawRects(remains, blue, screen)
        drawRects(bullet_remains, [0, 0, 0], screen)

        if not won:
            run_time=str(round(time.time()-start, 2))

        

        text=font.render(run_time, True, black)
        screen.blit(text, (10,50, 50, 20))
            
        text=font.render("LEVEL "+str(lvl+1), True, black)
        screen.blit(text, (10,10, 50, 20))

        text=font.render("DEATHS: "+str(deaths), True, black)
        screen.blit(text, (10,30, 50, 20))
        
        pygame.display.flip()
        #clock.tick(120)
        pygame.time.delay(delay)
        if won:
            lvl_times.append(run_time)
            total_deaths.append(deaths)
            #print(lvl_times, total_deaths)
            time.sleep(0.5)
            lvl+=1
            reset()
            won=0
    else:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                #print("key pressed")
                if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    #print("Unpaused")
                    pause=0
                    start=time.time()-save_time
                if pygame.key.get_pressed()[pygame.K_s] and not pygame.key.get_pressed()[pygame.K_RETURN]:
                    option+=1
                    #print("added 1")
                    colours=colours[::-1]
                    #print("colour")
                if pygame.key.get_pressed()[pygame.K_w] and not pygame.key.get_pressed()[pygame.K_RETURN]:
                    option-=1
                    #print("subtracted 1")
                    colours=colours[::-1]
                if pygame.key.get_pressed()[pygame.K_RETURN]:
                    if option%3==0:
                        pause=0
                    elif option%3==1:
                        pause=0
                        start=time.time()
                        restart=1
                        reset()
                    elif option%3==2:
                        #print(option%3,"=",2)
                        #print("quit")
                        pygame.quit()
                        sys.exit()
        #screen.fill(white)
        #pygame.display.flip()
        menu_width=100
        menu_height=90
        menu=pygame.Rect(int((800-menu_width)/2), int((400-menu_height)/2), menu_width, menu_height)
        pygame.draw.rect(screen, (255, 255, 255), menu)
        pygame.draw.rect(screen, (0,255,50), menu, 3)
        #print(option%3)
        #print("option", option%3)

        colours=[black, black, black]
        colours[option%3]=red
        
        
        text=font.render("RESUME", True, colours[0])
        screen.blit(text, (367, 180-10, 50, 20))

        text=font.render("RESTART", True, colours[1])
        screen.blit(text, (365, 203-10, 50, 20))

        text=font.render("QUIT", True, colours[2])
        screen.blit(text, (380, 227-10, 50, 20))
        
        
        #screen.blit(screen, menu)
        pygame.display.flip()




