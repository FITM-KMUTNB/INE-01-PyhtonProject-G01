import pgzrun
import math
import re
import time
from random import randint
player = Actor('3',(400,500))
alien = Actor('4')
balien = Actor('1')
gameStatus = 0

def draw():
    screen.blit('2',(0,0))
    if gameStatus == 0:
        drawCentreText("PYGAMEZERO\n\n\nTYPE your name")
    screen.draw.text(player.name, center=(200, 250), owidth=0.5, ocolor=(
            255, 0, 0), color=(0, 64, 255), fontsize=40)
    if gameStatus == 1:
        player.draw()
        drawLasers()
        drawAliens()
        if balien.active:
            balien.draw()

def update():  # Pygame Zero update function
    global player,gameStatus,lasers,moveCounter,balien
    if gameStatus == 0:
        if keyboard.RETURN and player.name != "":
            gameStatus = 1
    if gameStatus == 1:
        if gameStatus == 1:
            checkKeys()
            updateLasers()
            updateBoss()
            if moveCounter == 0 :
                updateAliens()
            moveCounter += 1
            if moveCounter == moveDelay:
                moveCounter = 0
    if gameStatus == 2:
        if keyboard.ESCAPE:
            init()
            gameStatus = 0

def makeLaserActive():
    global player
    player.laserActive = 1

def drawAliens():
    for a in range(len(alien)):
        alien[a].draw()

def updateLasers():
    global lasers,alien
    for l in range(len(lasers)):
        if lasers[l].type == 0:
            lasers[l].y += 2
            if lasers[l].y > 600:
                lasers[l].status = 1
        if lasers[l].type == 1:
            lasers[l].y -= 5
            if lasers[l].y < 10:
                lasers[l].status = 1
    lasers = listCleanup(lasers)
    alien = listCleanup(alien)

def checkKeys():
    global player, score
    if keyboard.left:
        if player.x > 40:
            player.x -= 2
    if keyboard.right:
        if player.x < 800:
            player.x += 2
    if keyboard.up:
        if player.y > 40:
            player.y -= 2
    if keyboard.down:
        if player.y < 800:
            player.y += 2
    if keyboard.space:
        if player.laserActive == 1:
            player.laserActive = 0
            clock.schedule(makeLaserActive, 1.0)
            lasers.append(Actor("8", (player.x, player.y-32)))
            lasers[len(lasers)-1].status = 0
            lasers[len(lasers)-1].type = 1

def drawLasers():
    for l in range(len(lasers)):
        lasers[l].draw()

def updateAliens():
    global moveSequence, lasers, moveDelay
    movex = movey = 0
    if moveSequence < 10 or moveSequence > 30:
        movex = -15
    if moveSequence == 10 or moveSequence == 30:
        movey = 40 
        moveDelay -= 1
    if moveSequence > 10 and moveSequence < 30:
        movex = 15
    for a in range(len(alien)):
        animate(alien[a], pos=(alien[a].x + movex,
                                alien[a].y + movey), duration=0.5, tween='linear')
        if randint(0, 1) == 0:
            alien[a].image = "4"
            if randint(0, 5) == 0:
                lasers.append(Actor("9", (alien[a].x, alien[a].y)))
                lasers[len(lasers)-1].status = 0
                lasers[len(lasers)-1].type = 0
    moveSequence += 1
    if moveSequence == 40:
        moveSequence = 0

def natural_key(string_):
    return [int(s) if s.isdigit() else s for s in re.split(r'(\d+)', string_)]

def listCleanup(l):
    newList = []
    for i in range(len(l)):
        if l[i].status == 0:
            newList.append(l[i])
    return newList

def on_key_down(key):
    global player
    if gameStatus == 0 and key.name != "RETURN":
        if len(key.name) == 1:
            player.name += key.name
        else:
            if key.name == "BACKSPACE":
                player.name = player.name[:-1]

def drawCentreText(t):
    screen.draw.text(t, center=(400, 300), owidth=0.5, ocolor=(
        255, 255, 255), color=(255, 64, 0), fontsize=60)

def drawClipped(self):
    screen.surface.blit(self._surf, (self.x-32, self.y -
                                     self.height+30), (0, 0, 64, self.height))


def collideLaser(self, other):
    return (
        self.x-20 < other.x+5 and
        self.y-self.height+30 < other.y and
        self.x+32 > other.x+5 and
        self.y-self.height+30 + self.height > other.y
    )

def updateBoss():
    global balien, player, lasers
    if balien.active:
        balien.y += (0.3)
        if balien.direction == 0:
            balien.x -= (1)
        else:
            balien.x += (1)
        if balien.x < 100:
            balien.direction = 1
        if balien.x > 700:
            balien.direction = 0
        if balien.y > 500:
            player.status = 1
            balien.active = False
        if randint(0, 30) == 0:
            lasers.append(Actor("9", (balien.x, balien.y)))
            lasers[len(lasers)-1].status = 0
            lasers[len(lasers)-1].type = 0
    else:
        if randint(0, 800) == 0:
            balien.active = True
            balien.x = 800
            balien.y = 100
            balien.direction = 0

def checkLaserHit(l):
    global player
    if player.collidepoint((lasers[l].x, lasers[l].y)):
        player.status = 1
        lasers[l].status = 1

def drawAliens():
    for a in range(len(alien)):
        alien[a].draw()

def initAliens():
    global alien, moveCounter, moveSequence
    alien = []
    moveCounter = moveSequence = 0
    for a in range(18):
        alien.append(Actor("4", (210+(a % 6)*80, 100+(int(a/6)*64))))
        alien[a].status = 0


def init():
    global player, lasers ,moveSequence,moveCounter,moveDelay,boss
    moveDelay = 30
    initAliens()
    balien.active = False
    lasers = []
    player.laserActive = 1
    player.name = ""

init()
pgzrun.go()