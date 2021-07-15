import pygame
import os
import random  
from time import sleep
pygame.init()
pygame.font.init()
width,height = 750,750
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Space Invader")
clock=pygame.time.Clock()
bg = pygame.transform.scale(pygame.image.load(os.path.join("assets","background-black.png")),(width,height)) 
playerS = pygame.image.load(os.path.join("assets","pixel_ship_yellow.png"))
playerB = pygame.image.load(os.path.join("assets","pixel_laser_yellow.png"))
blueS=pygame.image.load(os.path.join("assets","pixel_ship_blue_small.png"))
blueB=pygame.image.load(os.path.join("assets","pixel_laser_blue.png"))
redS=pygame.image.load(os.path.join("assets","pixel_ship_red_small.png"))
redB=pygame.image.load(os.path.join("assets","pixel_laser_red.png"))
greenS=pygame.image.load(os.path.join("assets","pixel_ship_green_small.png"))
greenB=pygame.image.load(os.path.join("assets","pixel_laser_green.png"))
class Laser():
    def __init__(self,x,y,img):
        self.x=x
        self.y=y
        self.img=img
        self.mask=pygame.mask.from_surface(self.img)
    def draw(self,screen):
        screen.blit(self.img,(self.x,self.y))
    def move(self,vel):
        self.y+=vel
    def off_screen(self,height):
        return not (self.y<=height and self.y>=0)
    def collision(self,obj):
        return collide(self,obj)  
class Ship():
    COOLDOWN = 30
    def __init__(self,x,y,health=100):
        self.x = x
        self.y=y
        self.health=health
        self.ship_img=None
        self.laser_img=None
        self.lasers=[]
        self.cool_down = 0
    def draw(self,screen):
        screen.blit(self.ship_img,(self.x,self.y))
        #pygame.draw.rect(screen,(255,100,0),(self.x,self.y,50,50))
        for laser in self.lasers:
            laser.draw(screen)
    
    def move_laser(self,vel,obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(height):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health-=10
                self.lasers.remove(laser)
            
    def cooldown(self):
        if self.cool_down>=self.COOLDOWN:
            self.cool_down = 0
        elif self.cool_down>0:
            self.cool_down+=1
    def shoot(self):
        if self.cool_down == 0:
            laser = Laser(self.x,self.y,self.laser_img)
            self.lasers.append(laser)
            self.cool_down = 1
                                            
    def get_height(self):
        return self.ship_img.get_height()
    
class Player(Ship):
    def __init__(self,x,y,health=100):
        super().__init__(x,y)
        self.ship_img =playerS
        self.laser_img=playerB
        self.health=health
        self.mask = pygame.mask.from_surface(self.ship_img)
    def move_laser(self,vel,objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(height):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        self.lasers.remove(laser)
                    
            
class Enemy(Ship):
    CMAP={"red":(redS,redB),"blue":(blueS,blueB),"green":(greenS,greenB)}
    def __init__(self,x,y,color):
        super().__init__(x,y)
        self.ship_img,self.laser_img = self.CMAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)
    def move(self,vel):
        self.y+=vel
def collide(obj1,obj2):
    offset_x = obj2.x-obj1.x
    offset_y = obj2.y-obj1.y
    return obj1.mask.overlap(obj2.mask,(offset_x,offset_y))!=None
def game_loop():
    FPS = 60
    crash = False 
    lives = 5
    level = 0
    x1 = int((width*0.45))
    y1 = int((height*0.8))
    movex=0
    vel = 6
    enemies =[]
    wave=5
    enemy_vel = 1
    laser_vel = 3
    lost = False
    ship = Player(x1,y1)
    mainfont = pygame.font.SysFont("comicsans",50)
    def label():
        life = mainfont.render(f"Lives:{lives}",1,(255,255,255))
        levels = mainfont.render(f"Levels:{level}",1,(255,255,255))
        llabel = mainfont.render("You Lost",1,(255,255,255))
        Health = mainfont.render(f"Health:{ship.health}",1,(255,255,255))
        screen.blit(life,(0,0))
        screen.blit(levels,(width-levels.get_width()-10,10))
        screen.blit(Health,(150,0))
        if lost:
            screen.blit(llabel,(width/2-llabel.get_width()/2,350)) #NEXT WEEK
            pygame.display.update()
            sleep(2)

    def background():
        screen.blit(bg,(0,0))
        
        for enemy in enemies:
            enemy.draw(screen)
            
            
        ship.draw(screen)

        
   
    #def ship(x,y):
       # screen.blit(player,(x,y))
    while not crash:
        pygame.display.update()
        clock.tick(60)
        if lives<1 or ship.health<1:
            lost = True #NEXT WEEK
        if lost ==True:
            crash = True
            
        if len(enemies)==0:
            level+=1
            wave+=5
            for i in range(wave):
                enemy = Enemy(random.randrange(100,width-100),random.randrange(-1500,-100),random.choice(["red","blue","green"]))
                enemies.append(enemy)  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crash= True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and ship.x-vel>0:
            ship.x-=vel
            
        elif keys[pygame.K_RIGHT]and ship.x+vel+100<width:
            ship.x+=vel
        if keys[pygame.K_SPACE]:
            ship.shoot()
            print("shhot")
            print(ship.cool_down)
            
            
        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_laser(laser_vel,ship)
            if random.randrange(0,2*FPS) == 1:
                enemy.shoot()
            if collide(enemy,ship):
                ship.health-=1
                enemies.remove(enemy)
            elif enemy.y+enemy.get_height()>height:
                lives-=1
                enemies.remove(enemy)
                
        ship.move_laser(-laser_vel,enemies)
        background()
        
        label()
        
        #ship(x,y) 
game_loop()
pygame.quit()
quit()