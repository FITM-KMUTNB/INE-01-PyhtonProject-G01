import pgzrun
import math
import re
import time
from random import randint
player = Actor('3')
alien = Actor('4')
background = Actor('2')
highScore = []

gameStatus = 0

def draw():
    screen.blit('2',(0,0))
    if gameStatus == 0:
        drawCentreText("Nova Space Time \n\n\n Enter your name ")
    screen.draw.text(player.name, center=(400, 500), owidth=1, ocolor=(
            105, 70, 60), color=(15, 80, 120), fontsize=50)
    if gameStatus == 1:
        player.image = player.images[math.floor(player.status/6)]
        player.draw()
        if player.status >= 30:
                if player.lives > 0:
                    drawCentreText("YOU WERE HIT!\nPress Enter to re-spawn")
                else:
                    drawCentreText("GAME OVER!\nPress Enter to continue")
    if gameStatus == 2:
        drawHighScore()    


def update():  
    global player,gameStatus
    if gameStatus == 0:
        if keyboard.RETURN and player.name != "":
            gameStatus = 1
    if gameStatus == 1:
        if player.status < 30 :


def on_key_down(key):
    global player
    if gameStatus == 0 and key.name != "RETURN":
        if len(key.name) == 1:
            player.name += key.name
        else:
            if key.name == "BACKSPACE":
                player.name = player.name[:-1]

def checkKeys():
    global player, score
    if keyboard.left:
        if player.x > 40:
            player.x -= 5
    if keyboard.right:
        if player.x < 760:
            player.x += 5
    if keyboard.up:
        if Human.y > 40:
            Human.y -= 2
    if keyboard.down:
        if Human.y < 570:
            Human.y += 2
    if keyboard.space:
        if player.laserActive == 1:
            sounds.gun.play()
            player.laserActive = 0
            clock.schedule(makeLaserActive, 1.0)
            lasers.append(Actor("laser2", (player.x, player.y-32)))
            lasers[len(lasers)-1].status = 0
            lasers[len(lasers)-1].type = 1
            score -= 100

def drawCentreText(t):
    screen.draw.text(t, center=(400, 300), owidth=0.5, ocolor=(
        255, 255, 255), color=(255, 64, 0), fontsize=60)

def listCleanup(l):
    newList = []
    for i in range(len(l)):
        if l[i].status == 0:
            newList.append(l[i])
    return newList

def place_Alien():
    alien.pos = 400,50
    alien.draw()

def init():
    global player
    player.name = ""

init()
pgzrun.go()