import sys
import pygame
import random
import time

class Enemy:
    def __init__(self, size, coords): 
        self.coords=coords
        self.rect=pygame.Rect(coords[0],coords[1],size[0],size[1])
        self.gravity=0#0.15
        self.y_speed=0
        self.x_speed=0#random.randint(1,2)*random.choice([1,-1])
        self.screen=screen
        self.jump_time=random.randint(1,60)
        self.x_time=random.randint(50,80)
        self.bounds=[999,-999]
        self.current_platform=0
        self.size=size
#[2895, 240, 15, 15]
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
            self.gravity=0#0.15
        
        if count%self.jump_time==0 and self.gravity==0:
            #self.jump=True
            self.y_speed=0#-4
            self.gravity=0#0.15
            




pygame.init()
screen=pygame.display.set_mode([800,400])
pygame.display.set_caption("PLATFORMANIA")
red,black,blue,green,white=(255,0,0),(0,0,0),(0,0,255),(0,255,0),(255,255,255)
add=0
platform_coords=[[1785, 345, 15, 15], [1830, 345, 15, 15], [1980, 345, 15, 15], [2595, 345, 15, 15], [2745, 345, 15, 15], [2790, 345, 15, 15], [270, 345, 15, 15], [285, 345, 15, 15], [300, 345, 15, 15], [315, 345, 15, 15], [330, 345, 15, 15], [345, 345, 15, 15], [360, 345, 15, 15], [375, 345, 15, 15], [390, 345, 15, 15], [405, 345, 15, 15], [420, 345, 15, 15], [435, 345, 15, 15], [450, 345, 15, 15], [465, 345, 15, 15], [480, 345, 15, 15], [495, 345, 15, 15], [510, 345, 15, 15], [525, 345, 15, 15], [540, 345, 15, 15], [555, 345, 15, 15], [570, 345, 15, 15], [585, 345, 15, 15], [600, 345, 15, 15], [615, 345, 15, 15], [630, 345, 15, 15], [645, 345, 15, 15], [660, 345, 15, 15], [675, 345, 15, 15], [690, 345, 15, 15], [705, 345, 15, 15], [720, 345, 15, 15], [735, 345, 15, 15], [750, 345, 15, 15], [765, 345, 15, 15], [780, 345, 15, 15], [795, 345, 15, 15], [810, 345, 15, 15], [825, 345, 15, 15], [840, 345, 15, 15], [855, 345, 15, 15], [870, 345, 15, 15], [885, 345, 15, 15], [900, 345, 15, 15], [915, 345, 15, 15], [930, 345, 15, 15], [945, 345, 15, 15], [960, 345, 15, 15], [975, 345, 15, 15], [990, 345, 15, 15], [1005, 345, 15, 15], [1020, 345, 15, 15], [1035, 345, 15, 15], [1050, 345, 15, 15], [1065, 345, 15, 15], [1080, 345, 15, 15], [1095, 345, 15, 15], [1110, 345, 15, 15], [1125, 345, 15, 15], [1140, 345, 15, 15], [1155, 345, 15, 15], [1170, 345, 15, 15], [1185, 345, 15, 15], [1200, 345, 15, 15], [1215, 345, 15, 15], [1230, 345, 15, 15], [1245, 345, 15, 15], [1260, 345, 15, 15], [1275, 345, 15, 15], [1275, 330, 15, 15], [1275, 315, 15, 15], [1275, 300, 15, 15], [1290, 300, 15, 15], [1305, 300, 15, 15], [1320, 300, 15, 15], [1335, 300, 15, 15], [1350, 300, 15, 15], [1365, 300, 15, 15], [1365, 285, 15, 15], [1365, 270, 15, 15], [1365, 255, 15, 15], [1380, 255, 15, 15], [1395, 255, 15, 15], [1410, 255, 15, 15], [1425, 255, 15, 15], [1440, 255, 15, 15], [1455, 255, 15, 15], [1455, 240, 15, 15], [1455, 225, 15, 15], [1455, 210, 15, 15], [1470, 210, 15, 15], [1485, 210, 15, 15], [1500, 210, 15, 15], [1515, 210, 15, 15], [1530, 210, 15, 15], [1545, 210, 15, 15], [1545, 195, 15, 15], [1545, 180, 15, 15], [1545, 165, 15, 15], [1560, 165, 15, 15], [1575, 165, 15, 15], [1590, 165, 15, 15], [1605, 165, 15, 15], [1620, 165, 15, 15], [1635, 165, 15, 15], [1635, 150, 15, 15], [1635, 135, 15, 15], [1635, 120, 15, 15], [1650, 120, 15, 15], [1665, 120, 15, 15], [1680, 120, 15, 15], [1695, 120, 15, 15], [1710, 120, 15, 15], [1725, 120, 15, 15], [1725, 135, 15, 15], [1725, 150, 15, 15], [1725, 165, 15, 15], [1725, 180, 15, 15], [1725, 195, 15, 15], [1725, 210, 15, 15], [1725, 225, 15, 15], [1725, 240, 15, 15], [1725, 255, 15, 15], [1725, 270, 15, 15], [1725, 285, 15, 15], [1725, 300, 15, 15], [1725, 315, 15, 15], [1725, 330, 15, 15], [1725, 345, 15, 15], [1755, 345, 15, 15], [1770, 345, 15, 15], [1800, 345, 15, 15], [1815, 345, 15, 15], [1845, 345, 15, 15], [1860, 345, 15, 15], [1875, 345, 15, 15], [1920, 345, 15, 15], [1935, 345, 15, 15], [1950, 345, 15, 15], [1965, 345, 15, 15], [1995, 345, 15, 15], [2010, 345, 15, 15], [2025, 345, 15, 15], [2040, 345, 15, 15], [2055, 345, 15, 15], [2070, 345, 15, 15], [2115, 345, 15, 15], [2130, 345, 15, 15], [2145, 345, 15, 15], [2160, 345, 15, 15], [2175, 345, 15, 15], [2190, 345, 15, 15], [2205, 345, 15, 15], [2220, 345, 15, 15], [2235, 345, 15, 15], [2250, 345, 15, 15], [2265, 345, 15, 15], [2310, 345, 15, 15], [2325, 345, 15, 15], [2340, 345, 15, 15], [2355, 345, 15, 15], [2370, 345, 15, 15], [2385, 345, 15, 15], [2400, 345, 15, 15], [2415, 345, 15, 15], [2430, 345, 15, 15], [2445, 345, 15, 15], [2460, 345, 15, 15], [2505, 345, 15, 15], [2520, 345, 15, 15], [2535, 345, 15, 15], [2550, 345, 15, 15], [2565, 345, 15, 15], [2580, 345, 15, 15], [2610, 345, 15, 15], [2625, 345, 15, 15], [2640, 345, 15, 15], [2655, 345, 15, 15], [2700, 345, 15, 15], [2715, 345, 15, 15], [2730, 345, 15, 15], [2760, 345, 15, 15], [2775, 345, 15, 15], [2805, 345, 15, 15], [2820, 345, 15, 15], [2835, 345, 15, 15], [2850, 345, 15, 15], [2865, 345, 15, 15], [2880, 345, 15, 15], [2895, 345, 15, 15], [2895, 330, 15, 15], [2895, 315, 15, 15], [2895, 300, 15, 15], [2895, 285, 15, 15], [2895, 270, 15, 15], [2895, 255, 15, 15], [2895, 240, 15, 15], [2895, 225, 15, 15], [2895, 210, 15, 15], [2895, 195, 15, 15], [2895, 180, 15, 15], [2895, 165, 15, 15], [2895, 150, 15, 15], [2895, 135, 15, 15], [2895, 120, 15, 15], [2895, 105, 15, 15], [2895, 90, 15, 15], [2895, 75, 15, 15], [2895, 60, 15, 15], [2895, 45, 15, 15], [2895, 30, 15, 15], [3015, 195, 15, 15], [3030, 195, 15, 15], [3045, 195, 15, 15], [3060, 195, 15, 15], [3075, 195, 15, 15], [3090, 195, 15, 15], [3105, 195, 15, 15], [3120, 195, 15, 15], [1350, 60, 15, 15], [1365, 60, 15, 15], [1380, 60, 15, 15], [1395, 60, 15, 15], [1410, 60, 15, 15], [1425, 60, 15, 15], [1440, 60, 15, 15], [1455, 60, 15, 15], [1470, 60, 15, 15], [1485, 60, 15, 15], [1500, 60, 15, 15], [1515, 60, 15, 15], [1530, 60, 15, 15], [1545, 60, 15, 15], [1560, 60, 15, 15], [1575, 60, 15, 15], [1590, 60, 15, 15], [1605, 60, 15, 15], [1620, 60, 15, 15], [1635, 60, 15, 15], [1650, 60, 15, 15], [1665, 60, 15, 15], [1680, 60, 15, 15], [1695, 60, 15, 15], [1710, 60, 15, 15], [1350, 45, 15, 15], [1335, 60, 15, 15], [1380, 45, 15, 15], [1410, 45, 15, 15], [1440, 45, 15, 15], [1470, 45, 15, 15], [1500, 45, 15, 15], [1530, 45, 15, 15], [1560, 45, 15, 15], [1590, 45, 15, 15], [1620, 45, 15, 15], [1650, 45, 15, 15], [1680, 45, 15, 15], [1710, 45, 15, 15], [1365, 30, 15, 15], [1395, 30, 15, 15], [1425, 30, 15, 15], [1455, 30, 15, 15], [1485, 30, 15, 15], [1515, 30, 15, 15], [1545, 30, 15, 15], [1575, 30, 15, 15], [1605, 30, 15, 15], [1635, 30, 15, 15], [1665, 30, 15, 15], [1695, 30, 15, 15], [1380, 15, 15, 15], [1410, 15, 15, 15], [1440, 15, 15, 15], [1470, 15, 15, 15], [1500, 15, 15, 15], [1530, 15, 15, 15], [1560, 15, 15, 15], [1590, 15, 15, 15], [1620, 15, 15, 15], [1650, 15, 15, 15], [1680, 15, 15, 15], [1395, 0, 15, 15], [1425, 0, 15, 15], [1455, 0, 15, 15], [1485, 0, 15, 15], [1515, 0, 15, 15], [1545, 0, 15, 15], [1575, 0, 15, 15], [1605, 0, 15, 15], [1635, 0, 15, 15], [1665, 0, 15, 15], [1890, 375, 15, 15], [1905, 375, 15, 15], [2670, 375, 15, 15], [2685, 375, 15, 15], [2085, 360, 15, 15], [2100, 360, 15, 15], [2475, 360, 15, 15], [2490, 360, 15, 15], [1740, 345, 15, 15], [1725, 60, 15, 15], [1725, 45, 15, 15], [1725, 30, 15, 15], [1725, 15, 15, 15], [1725, 0, 15, 15], [1710, 15, 15, 15], [1695, 0, 15, 15], [1785, 345, 15, 15]]











platforms=[]
for platform in platform_coords:
    platforms.append(pygame.Rect(platform[0], platform[1], platform[2], platform[3]))
    
player=pygame.Rect(300,200,12,12)

enemy_coords=[[5000, 0]]
enemies=[]
size=15
for coords in enemy_coords:
    enemies.append(Enemy((size,size),coords))
#enemies=[]
gravity=0.15
y_speed=0

def drawRects(rects, colour, screen):
    for rect in rects:
        pygame.draw.rect(screen, colour, rect)
        

def reset():
    global x_difference
    global enemies
    global player
    global platforms
    global y_speed
    global spawn_coords
    global current_platform
    global checkpoints
    global won

    print("resetting")
    new=False
    if not won:
        for x in range(len(checkpoints)):
            if player.x>checkpoints[x][0]:
                player=pygame.Rect(300,checkpoints[x][1],12,12)
                new=True
                print("worked")
                difference=checkpoint_coords[x][0]-300
                break
    if not new:
        player=pygame.Rect(300,200,12,12)
        difference=0

    for x in range(len(checkpoints)):
        checkpoints[x][0]=checkpoint_coords[x][0]-difference
    
    enemies=[]
    for coords in enemy_coords:
        enemies.append(Enemy((size,size),coords))

    platforms=[]
    for platform in platform_coords:
        platforms.append(pygame.Rect(platform[0], platform[1], platform[2], platform[3]))

    y_speed=-6

    spawn_coords=[[100, 100], [555, 315], [825, 180], [1065, 90], [1560, 285], [1905, 60], [1980, 60], [3150, 135], [3150, 30], [3420, 225], [3825, 225]]
    
    for x in range(len(platforms)):
        platforms[x].left-=difference
    for x in range(len(enemies)):
        enemies[x].rect.left-=difference
    for x in range(len(spawn_coords)):
        spawn_coords[x][0]-=difference
        
    current_platform=0

    x_difference=0

        
"""
enemies=reset_enemies(enemy_coords)
player=pygame.Rect(300,200,10,10)
platforms=reset_platforms(platform_coords)
y_speed=-6
spawn_coords=[[2225, 116], [3106, 49], [3956, 30], [4324, 39], [4410, 41]]
current_platform=0
"""

clock = pygame.time.Clock()
#count=0
current_platform=0
fps=60
previous = time.time() * 1000
count=0
spawn_coords=[[100, 100], [555, 315], [825, 180], [1065, 90], [1560, 285], [1905, 60], [1980, 60], [3150, 135], [3150, 30], [3420, 225], [3825, 225]]
map_spawn=[[100, 100], [555, 315], [825, 180], [1065, 90], [1560, 285], [1905, 60], [1980, 60], [3150, 135], [3150, 30], [3420, 225], [3825, 225]]

checkpoints=[[300, 200]]
checkpoint_coords=[[300, 200]]
checkpoints=sorted(checkpoints, key=lambda n: n[0], reverse=True)

won=0
start=time.time()
font = pygame.font.Font('freesansbold.ttf', 15)

vertical_gridlines=[]
for x in range(0,5000,15):
        vertical_gridlines.append([x, 0])
#pygame.draw.line(screen, (0,0,0), (pos[0]+2000, pos[1]), (pos[0]-2000, pos[1]))######################
#print(vertical_gridlines)

horizontal_gridlines=[]
for y in range(0,450,15):
    horizontal_gridlines.append([0,y])

x_distance=0
vertical_gridlines.reverse()
horizontal_gridlines.reverse()

mode_count=0
mode=["Platform Mode", "Spawner Mode", "Enemy Mode", "Checkpoint Mode"]

while True:
    count+=1

    if count%10000==0:
        for coord in spawn_coords:
            enemies.append(Enemy((size,size),coord))

    for x in range(len(enemies)):
        if enemies[x].rect.top>450:
            enemies.pop(x)
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
        print("hit from above")
        enemies.pop(collision)
        y_speed=-6
    elif collision!=-1:
        print("dead")
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
                x=0
                y=0
                mouse_x=pygame.mouse.get_pos()[0]
                mouse_y=pygame.mouse.get_pos()[1]
                for line in vertical_gridlines:
                    if mouse_x>line[0]:
                        x=line[0]
                        #print(x)
                        break
                for line in horizontal_gridlines:
                    if mouse_y>line[1]:
                        y=line[1]
                        #print(y)
                        break
                if mode[mode_count%4]=="Platform Mode":
                    #print(event.type)
                    #print(pygame.mouse.get_pressed())
                    #print(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                    
                    #platforms.append(pygame.Rect(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],50,50))
                    #platforms=sorted(platforms, key=lambda x: x.top, reverse=False)#remove if you want

                    for line in horizontal_gridlines:
                        if mouse_y>line[1]:
                            y=line[1]
                            #print(y)
                            break
                    platforms.append(pygame.Rect(x,y,15,15))
                    plat_list=[]
                    for platform in platforms:
                        plat_list.append([platform.left-x_distance, platform.top, 15, 15])
                        
                    print(plat_list)
                    print(x_distance)
                    
                elif mode[mode_count%4]=="Enemy Mode":
                    print("enemy placed")
                    enemies.append(Enemy((size,size),(x,y)))
                    enemy_coords.append([x-x_distance,y])
                    print(enemy_coords)

                elif mode[mode_count%4]=="Checkpoint Mode":
                    print("checkpoint placed")
                    checkpoints.append([x,y])
                    checkpoint_coords.append([x-x_distance,y])
                    enemy_coords.append([x-x_distance,y])
                    print(checkpoint_coords)
                    checkpoints=sorted(checkpoints, key=lambda n: n[0], reverse=True)

                elif mode[mode_count%4]=="Spawner Mode":
                    print("spawner placed")
                    spawn_coords.append([x,y])
                    map_spawn.append([x-x_distance,y])
                    enemy_coords.append([x-x_distance,y])
                    print(map_spawn)
            
                
            elif pressed[2]:
                
                #enemies.append(Enemy((size,size),(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])))
                #print(pygame.mouse.get_pos())
                mode_count+=1

            elif pressed[1]:
                #platforms.pop(len(platforms)-1)
                #plat_list.pop(len(plat_list)-1)
                x=0
                """
                y=0
                mouse_x=pygame.mouse.get_pos()[0]
                mouse_y=pygame.mouse.get_pos()[1]
                for line in vertical_gridlines:
                    if mouse_x>line[0]:
                        x=line[0]
                        #print(x)
                        break
                for line in horizontal_gridlines:
                    if mouse_y>line[1]:
                        y=line[1]
                        #print(y)
                        break
                #print(platforms)
                if pygame.Rect(x, y, 15, 15) in platforms:
                    platforms.remove(pygame.Rect(x, y, 15, 15))
                plat_list=[]
                for platform in platforms:
                    plat_list.append([platform.left-x_distance, platform.top, 15, 15])
                print(plat_list)
                #print(x, y)
                #print(x-x_distance, y)"""
                
    pressed=pygame.mouse.get_pressed()
    removed=False
    if pressed[1]:
        x=0
        y=0
        mouse_x=pygame.mouse.get_pos()[0]
        mouse_y=pygame.mouse.get_pos()[1]
        for line in vertical_gridlines:
            if mouse_x>line[0]:
                x=line[0]
                break
        for line in horizontal_gridlines:
            if mouse_y>line[1]:
                y=line[1]
                break
        if pygame.Rect(x, y, 15, 15) in platforms:
            platforms.remove(pygame.Rect(x, y, 15, 15))
            removed=True
        plat_list=[]
        for platform in platforms:
            plat_list.append([platform.left-x_distance, platform.top, 15, 15])
        if removed==True:
            print(plat_list)
    
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
        #player=player.move(3,0)
        for x in range(len(platforms)):
            platforms[x]=platforms[x].move(-2,0)
        for x in range(len(enemies)):
            enemies[x].rect.x-=2
        for x in range(len(checkpoints)):###########################
            checkpoints[x][0]-=2
        for x in range(len(vertical_gridlines)):
                vertical_gridlines[x][0]-=2
        x_distance-=2
            
        collision=player.collidelist(enemies)
        if collision!=-1:
            print("dead")
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
                platforms[x]=platforms[x].move(2,0)
            for x in range(len(checkpoints)):########################
                checkpoints[x][0]+=2
            player.right=platforms[collision].left
            for x in range(len(vertical_gridlines)):
                vertical_gridlines[x][0]+=2
            x_distance+=2
            #if player.right>platforms[collision].left:
            #    player.right=platforms[collision].left
            #    collision=player.collidelist(platforms)
                
    if keys[pygame.K_a]:
        #player=player.move(-3,0)
        for x in range(len(platforms)):
            platforms[x]=platforms[x].move(2,0)
        for x in range(len(enemies)):
            enemies[x].rect.x+=2
        for x in range(len(checkpoints)):
            checkpoints[x][0]+=2
        collision=player.collidelist(enemies)
        for x in range(len(vertical_gridlines)):
            vertical_gridlines[x][0]+=2
        x_distance+=2
        if collision!=-1:
            print("dead")
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
                platforms[x]=platforms[x].move(-2,0)
            for x in range(len(checkpoints)):
                checkpoints[x][0]-=2
            for x in range(len(vertical_gridlines)):
                vertical_gridlines[x][0]-=2
            x_distance-=2
            player.left=platforms[collision].right
            #if player.left<platforms[collision].right:
            #    player.left=platforms[collision].right
            #    collision=player.collidelist(platforms)

    if keys[pygame.K_w]:
        if gravity==0:
            gravity=0.15
            y_speed=-6
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
        gravity=0.15
        

    #print(y_speed)
    
    for enemy in enemies:
        enemy.update()
    
    screen.fill(white)

    #pygame.draw.rect(screen, (255,255,0), (4780, 155, 140, 127))    #(4780, 155), (4920, 282)




    #checkpoints=sorted(checkpoints)
    for x in checkpoints:
        pygame.draw.rect(screen, blue, (x[0], x[1], 15, 15))
    pygame.draw.rect(screen, (255,192,203), (checkpoints[0][0], checkpoints[0][1], 120, 120))
    for x in spawn_coords:
        pygame.draw.rect(screen, (255,255,0), (x[0], x[1], 15, 15))




    """
    if player.x>checkpoints[0][0] and won==0:
        won=1
        
    if won:
        text=font.render("WON", True, black)
        screen.blit(text, (checkpoints[0][0],checkpoints[0][1], 50, 20))

        text=font.render(run_time, True, black)
        screen.blit(text, (checkpoints[0][0]+50,checkpoints[0][1]+50, 50, 20))
        start=time.time()
    """
    
    for line in vertical_gridlines:
        pygame.draw.line(screen, (0,0,0), (line[0], line[1]), (line[0], line[1]+450))
    for line in horizontal_gridlines:
        pygame.draw.line(screen, (0,0,0), (0, line[1]), (5000, line[1]))
    drawRects(platforms, black, screen)
    drawRects([player], green, screen)
    drawRects(enemies, red, screen)

    if not won:
        run_time=str(round(time.time()-start, 2))
    
    

    text=font.render(run_time, True, black, white)
    screen.blit(text, (10,10, 50, 20))

    #print(x_distance)
    text=font.render(mode[mode_count%4], True, black, white)
    screen.blit(text, (650,10, 50, 20))
        
    pygame.display.flip()
    #clock.tick(120)
    pygame.time.delay(delay)
    """
    if won:
        time.sleep(3)
        reset()
        won=0
    """

    





