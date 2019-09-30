import pgzrun
import random
import pygame

def start_game(): #ตัวเริ่มเกม#
    global gamescreen,lchek,lchekOammo,itemC,ammo,health,Time,TimeOver,startOtime,score,damage
    gamescreen = 1
    lchek = 1
    lchekOammo = 1
    itemC = 0
    ammo = 100
    health = 4
    Time = 0
    TimeOver = 5
    startOtime = 1
    score = 0
    damage = 0
    ship.pos = 350.5,950
    shiphit.pos = 350.5,958

def end_game():
    global gamescreen
    laser.clear()
    laser1.clear()
    laser2.clear()
    meteo.clear()
    meteo1.clear()
    meteo2.clear()
    meteo3.clear()
    ammoI.clear()
    bufI.clear()
    healI.clear()
    gamescreen = 2


WIDTH = 600
HEIGHT = 1000
bg = Actor('bg1',topleft=(0,0))
bg2 = Actor('bg1',topleft=(0,-1300))
ship = Actor('ship2',center=(350.5,950))
shiphit = Actor('ship2',center=(350.5,958))
healthBar = Actor('blood0',topright=(690,20))
Ibar = Actor('cool1',topright=(690,50))
gamescreen = 0
laser = []
laser1 = []
laser2 = []
laser3 = []
meteo = []
meteo1 = []
meteo2 = []
meteo3 = []
ammoI = []
bufI = []
healI = []
lchek = 1
lchekOammo = 1
itemC = 0
ammo = 200
health = 4
Time = 0
TimeOver = 5
startOtime = 1
score = 0
damage = 0

def draw():
    global lchek,lchekOammo,itemC,Time,ammo,TimeOver,startOtime
    if gamescreen == 0:
        screen.fill((201,0,0))
        bg.draw()
        bg2.draw()
        screen.blit('pic1',(0,0))
    if gamescreen == 1:
        screen.fill((201,0,0))
        bg.draw()
        bg2.draw()
        shiphit.draw()
        ship.draw()
        #pass space
        keySPACE()
        #draw laser
        for i in laser: 
            i.draw()
        for i in range(len(laser1)): #draw laser ( use item)[1]
            laser1[i].draw()
        for i in range(len(laser2)): #draw laser ( use item)[2]
            laser2[i].draw()
        for i in range(len(laser3)):
            laser3[i].draw()
        #draw meteor
        for i in meteo:
            i.draw()
        for i in meteo1:
            i.draw()
        for i in meteo2:
            i.draw()
        for i in meteo3:
            i.draw()
        #draw ITEM
        for i in ammoI:
            i.draw()
        for i in bufI:
            i.draw()
        for i in healI:
            i.draw()
        screen.draw.text("Your Score: "+str(score),topleft=(10,30),fontsize=30,color=(255,255,255))
        screen.draw.text("Ammo: "+str(ammo),topleft=(10,10),fontsize=30,color='blue')
        healthBar.draw()
        Ibar.draw()
        
        if ammo == 0 : #เวลานับถอยหลัง#
            startOtime = 0
            screen.draw.text("!!Out of Ammo!!",midtop=(350.5,10),fontsize=50,color="yellow")
            screen.draw.text("GameOver in "+str(TimeOver),midtop=(350.5,50),fontsize=50,color="yellow")
        else:
            TimeOver = 5
            startOtime = 1
    if gamescreen == 2:
        screen.fill((201,0,0))
        bg.draw()
        bg2.draw()
        screen.draw.text("GameOver",midtop=(350.5,280),fontsize=100,color="cyan")
        screen.draw.text("Your Score : "+str(score),midtop=(350.5,380),fontsize=100,color="cyan")


#in draw     
def keySPACE():
    global ammo,lchek,lchekOammo,itemC #ปืน#
    if keyboard.space:
        if lchek == 1 and ammo > 0:
            if itemC == 0: #no item
                sounds.shoot1.play()
                laser.append(Actor('laser1',(ship.x,ship.y-55)))
                ammo -= 1
                #laser[-1].draw() 
            elif itemC == 1: # have item
                laser1.append(Actor('laser1',(ship.x-40,ship.y-20)))
                laser2.append(Actor('laser1',(ship.x+40,ship.y-20)))
                sounds.shoot1.play()
                if ammo == 1:
                    ammo -= 1
                else:
                    ammo -= 2
                #laser1[-1].draw()
                #laser2[-1].draw()
            elif itemC == 2:
                laser1.append(Actor('laser1',(ship.x-15,ship.y-20)))
                laser2.append(Actor('laser1',(ship.x+15,ship.y-20)))
                laser3.append(Actor('laser1',(ship.x,ship.y-20)))
                sounds.shoot1.play()
                if ammo == 1:
                    ammo -= 1
                else:
                    ammo -= 3
                #laser1[-1].draw()
                #laser2[-1].draw()
            lchek = 0
            clock.schedule(lasercreate,0.3)
        elif lchekOammo == 1 and ammo == 0:
            sounds.outammo.play()
            lchekOammo = 0
            clock.schedule(outAmScreate,0.3)

#in keySPACE
def lasercreate(): #เช็ค เลเซอร์ #
    global lchek
    lchek = 1
def outAmScreate(): #เช็ค กระสุน #
    global lchekOammo
    lchekOammo = 1

def on_key_down(key): #ควบคุม ปืน และวิธีทำเป็น Fullscreen#
    global gamescreen
    if key == keys.F:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    if gamescreen == 0:
        if key == keys.SPACE or key == keys.RETURN:
            start_game()
    if gamescreen == 2:
        if key == keys.SPACE:
            start_game()
        if key == keys.RETURN:
            quit()

def update():
    global ammo,itemC,Time,health,startOtime,damage
    if gamescreen == 1:
        #Item Control
        ItemControl()
        #check to normal laser
        Lasernormal()
        #meteor move
        meteorControl()
        #UupdateHealthBar
        updateHealth()
        #updateItemBar
        updateITEM()         
        #laser move
        laserControl()
        #ship control
        shipControl()
        if health <= 0 or TimeOver <= 0 :
            end_game() 
    #background
    bgControl()

#inUpdate
def ItemControl(): #ไอเทมต่างๆ#
    global ammo,itemC,Time,health
    for i in ammoI:
        if i.colliderect(shiphit):
            sounds.reload.play()
            ammoI.remove(i)
            ammo+=20
        if i.y <= HEIGHT:
            i.y += 1
        else:
            ammoI.remove(i)
    for i in bufI:
        if i.colliderect(shiphit):
            sounds.reload2.play()
            bufI.remove(i)
            itemC = random.randint(1,2)
            Time = 5
            #clock.schedule(Lnormal,10)
        if i.y <= HEIGHT:
            i.y += 1
        else:
            bufI.remove(i)
    for i in healI:
        if i.colliderect(shiphit):
            sounds.repair.play()
            healI.remove(i)
            if health < 4:
                health += 1
        if i.y <= HEIGHT:
            i.y += 1
        else:
            healI.remove(i)

def Lasernormal(): #ระยะเวลา ไอเทม#
    global itemC,Time
    if Time == 0:
        itemC = 0

def meteorControl(): #โดนดาเมจ#
    global damage,health
    for i in meteo:
        if i.colliderect(shiphit):
            sounds.hit1.play()
            damage = 1
            ship.image = 'ship2'
            meteo.remove(i)
            health -= 1
            clock.schedule(shipNormal,0.1)
        c = meteoRemove(i)
        if c:
            meteo.remove(i) 
        elif i.y <= HEIGHT:
            i.y += 7
        else:
            meteo.remove(i)
    for i in meteo1:
        if i.colliderect(shiphit):
            sounds.hit1.play()
            damage = 1
            ship.image = 'ship2'
            meteo1.remove(i)
            health -= 1
            clock.schedule(shipNormal,0.1)
        c = meteoRemove(i)
        if c:
            meteo1.remove(i) 
        elif i.y <= HEIGHT:
            i.y += 6
        else:
            meteo1.remove(i)
    for i in meteo2:
        if i.colliderect(shiphit):
            sounds.hit1.play()
            damage = 1
            ship.image = 'ship2'
            meteo2.remove(i)
            health -= 1
            clock.schedule(shipNormal,0.1)
        c = meteoRemove(i)
        if c:
            meteo2.remove(i)
        elif i.y <= HEIGHT:
            i.y += 5
        else:
            meteo2.remove(i)
    for i in meteo3:
        if i.colliderect(shiphit):
            sounds.hit1.play()
            damage = 1
            ship.image = 'ship2'
            meteo3.remove(i)
            health -= 1
            clock.schedule(shipNormal,0.1)
        c = meteoRemove(i)
        if c:
            meteo3.remove(i)
        elif i.y <= HEIGHT:
            i.y += 4
        else:
            meteo3.remove(i)

def updateHealth(): # เลือด ใน เกม #
    if health == 4:
        healthBar.image = 'blood1'
    elif health == 3:
        healthBar.image = 'blood2'
    elif health == 2:
        healthBar.image = 'blood3'
    elif health == 1:
        healthBar.image = 'blood4'
    elif health == 0:
        healthBar.image = 'blood5'

def updateITEM(): # ระยะเวลา ไอเทม #
    if Time == 5:
        Ibar.image = 'cool1'
    elif Time == 4:
        Ibar.image = 'cool2'
    elif Time == 3:
        Ibar.image = 'cool3'
    elif Time == 2:
        Ibar.image = 'cool4'
    elif Time == 1:
        Ibar.image = 'cool5'
    else:
        Ibar.image = 'cool5'

def laserControl(): #ตัวควบคุมปืน#
    #if itemC == 0: #laser no item
    for i in range(len(laser)):
        laser[i].y -= 7
    for i in range(len(laser)):
        if laser[i].y < -10 :
            laser.pop(i)
            break
    #if itemC == 1:
            #laser use item [1]
    for i in range(len(laser1)):
        laser1[i].y -= 5
    for i in range(len(laser1)):
        if laser1[i].y < -10 :
            laser1.pop(i)
            break
        #laser use item [2]
    for i in range(len(laser2)):
        laser2[i].y -= 5
    for i in range(len(laser2)):
        if laser2[i].y < -10 :
            laser2.pop(i)
            break
    
    for i in range(len(laser3)):
        laser3[i].y -=5
    for i in range(len(laser3)):
        if laser3[i].y < -10 :
            laser3.pop(i)
            break

def bgControl(): # รูปภาพเลื่อน #
    bg.y += 0.5
    bg2.y += 0.5
    if bg.top > HEIGHT:
        bg.top = -1300
    if bg2.top > HEIGHT:
        bg2.top = -1300

def shipControl(): # การชยับตัว #
    if (keyboard.left or keyboard.a) and (keyboard.up or keyboard.w):
        if ship.left > 0 and ship.top > 0:
            ship.x -= 5
            ship.y -= 5
            shiphit.x -= 5
            shiphit.y -= 5
            if damage == 0:
                ship.image = '123'
        elif ship.left > 0:
            ship.x -= 5
            shiphit.x -= 5
            if damage == 0:
                ship.image = '234'
        elif ship.top > 0:
            ship.y -= 5
            shiphit.y -= 5
            if damage == 0:
                ship.image = '234'
        else:
            if damage == 0:
                ship.image = '123'
    elif (keyboard.left or keyboard.a) and (keyboard.down or keyboard.s):
        if ship.left > 0 and ship.bottom < HEIGHT:
            ship.x -= 5
            ship.y += 5
            shiphit.x -= 5
            shiphit.y += 5
            if damage == 0:
                ship.image = '123'
        elif ship.bottom < HEIGHT:
            ship.y += 5
            shiphit.y += 5
            if damage == 0:
                ship.image = 'ship2'
        elif ship.left > 0:
            ship.x -= 5
            shiphit.x -= 5
            if damage == 0:
                ship.image = '234'
        else:
            if damage == 0:
                ship.image = '123'
    elif (keyboard.right or keyboard.d) and (keyboard.up or keyboard.w):
        if ship.right < WIDTH and ship.top > 0:
            ship.x += 5
            ship.y -= 5
            shiphit.x += 5
            shiphit.y -= 5
            if damage == 0:
                ship.image = '123'
        elif ship.right < WIDTH:
            ship.x += 5
            shiphit.x += 5
            if damage == 0:
                ship.image = 'ship2'
        elif ship.top > 0:
            ship.y -= 5
            shiphit.y -= 5
            if damage == 0:
                ship.image = '234'
        else:
            if damage == 0:
                ship.image = '123'
    elif (keyboard.right or keyboard.d) and (keyboard.down or keyboard.s):
        if ship.right < WIDTH and ship.bottom < HEIGHT:
            ship.x += 5
            ship.y += 5
            shiphit.x += 5
            shiphit.y += 5
            if damage == 0:
                ship.image = '123'
        elif ship.right < WIDTH:
            ship.x += 5
            shiphit.x += 5
            if damage == 0:
                ship.image = '234'
        elif ship.bottom < HEIGHT:
            ship.y += 5
            shiphit.y += 5
            if damage == 0:
                ship.image = 'ship2'
        else:
            if damage == 0:
                ship.image = '123'
    elif keyboard.left or keyboard.a:
        if ship.left > 0:
            ship.x -= 5
            shiphit.x -= 5
            #ship.image = 'shipl'
    elif keyboard.right or keyboard.d:
        if ship.right < WIDTH:
            ship.x += 5
            shiphit.x += 5
            #ship.image = 'shipr'
    elif keyboard.up or keyboard.w:
        if ship.top > 0:
            ship.y -= 5
            shiphit.y -= 5
            if damage == 0:
                ship.image = '234'
    elif keyboard.down or keyboard.s:
        if ship.bottom < HEIGHT:
            ship.y += 5
            shiphit.y += 5
            if damage == 0:
                ship.image = 'ship2'
    else:
        if damage == 0:
            ship.image = '123'
    
#in meteorControl
def shipNormal(): #เครื่องบิน#
    global damage
    damage = 0
    ship.image = 'ship2'

def meteoRemove(i): #ยานโดนลบ#
    global score
    for n in laser:
        if n.colliderect(i):
            #print("test")
            sounds.exploxion1.play()
            laser.remove(n)
            randomItem(i)
            score += 1
            return(True)
    for n2 in laser1:
        if n2.colliderect(i):
            sounds.exploxion1.play()
            laser1.remove(n2)
            randomItem(i)
            score += 1
            return(True)
    for n3 in laser2:
        if n3.colliderect(i):
            sounds.exploxion1.play()
            laser2.remove(n3)
            randomItem(i)
            score += 1
            return(True)
    for n4 in laser3:
        if n4.colliderect(i):
            sounds.exploxion1.play()
            laser3.remove(n4)
            randomItem(i)
            score += 1
            return(True)
    return(False) 

#in meteo Remove
def randomItem(i): #สุ่มไอเทม#
    R = random.randint(1,100)
    if R >= 1 and R <= 10:
        ammoI.append(Actor('item',(i.x,i.y)))
    elif R >= 11 and R <= 15:
        bufI.append(Actor('item',(i.x,i.y)))
    elif R ==97 or R == 98:
        healI.append(Actor('item',(i.x,i.y)))

#in Clock before game start
def timeCount(): 
    global Time,itemC
    if Time > 0:
        Time -= 1
    else:
        pass
def timeOcount():
    global TimeOver
    if startOtime == 0:
        if TimeOver > 0:
            TimeOver -= 1
def spawnMeteo(): #สุ่มเกิดเอเลื่อน#
    global gamescreen
    if gamescreen == 1:
        R = random.randint(1,4)
        if R == 1:
            meteo.append(Actor('1',midbottom=(random.randint(100,650),0)))
        elif R == 2:
            meteo1.append(Actor('2',midbottom=(random.randint(100,650),0)))
        elif R == 3:
            meteo2.append(Actor('3',midbottom=(random.randint(100,650),0)))
        elif R == 4:
            meteo3.append(Actor('3',midbottom=(random.randint(100,650),0)))

clock.schedule_interval(spawnMeteo,0.1)
clock.schedule_interval(timeCount,1.0)
clock.schedule_interval(timeOcount,1.0)
pgzrun.go()