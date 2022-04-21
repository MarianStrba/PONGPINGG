#Importy z knihoven
import pygame
from pygame import mixer
import math

# Zahájení programu odtud dolu se updatuje obrazovka
pygame.init()

# Definování a vytvoření obrazovky 800 x 600 pixelů
obrazovka = pygame.display.set_mode((800, 600))

# Jméno hry na vytvořeném okně
pygame.display.set_caption("PING-PONG")

# Definování a import obrázku na vytvořené okno
x = pygame.image.load("idk.png")
pygame.display.set_icon(x)

hrac_jedna_obrazek = pygame.image.load("hrackaa.png")
player1X = 0
player1Y = 300
player1X_change = 0
player1Y_change = 0

hrac_dva_obrazek = pygame.image.load("hrackaa.png")
player2X = 736
player2Y = 300
player2X_change = 0
player2Y_change = 0

micek_obrazek = pygame.image.load("micek.png")
micekX = 400
micekY = 300
micekX_change = 0.3
micekY_change = 0.3

score1_hodnota = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10

score2_hodnota = 0
font2 = pygame.font.Font("freesansbold.ttf", 32)
text2X = 650
text2Y = 10

def player1(x, y):
    obrazovka.blit(hrac_jedna_obrazek, (player1X, player1Y))

def player2(x, y):
    obrazovka.blit(hrac_dva_obrazek, (player2X, player2Y))

def micek(x, y):
    obrazovka.blit(micek_obrazek, (x, y))

def ukaz_score(x, y):
    score = font.render("Score: " + str(score1_hodnota), True, (255, 255, 255))
    obrazovka.blit(score, (x, y))

def ukaz_score2(x, y):
    score = font.render("Score: " + str(score2_hodnota), True, (255, 255, 255))
    obrazovka.blit(score, (x, y))

def Kolize1(micekX, micekY, player1X, player1Y):
    distance = math.sqrt((math.pow(player1X - micekX, 2)) + (math.pow(player1Y - micekY, 2)))
    if distance < 25:
        return True
    else:
        return False

def Kolize2(micekX, micekY, player2X, player2Y):
    distance = math.sqrt((math.pow(player2X - micekX, 2)) + (math.pow(player2Y - micekY, 2)))
    if distance < 25:
        return True
    else:
        return False

spusteno = True
while spusteno:
    obrazovka.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spusteno = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player2Y_change = - 0.5
            if event.key == pygame.K_DOWN:
                player2Y_change = 0.5
            if event.key == pygame.K_w:
                player1Y_change = - 0.5
            if event.key == pygame.K_s:
                player1Y_change = 0.5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                player2Y_change = 0
                player1Y_change = 0

    if micekX <= 0:
        score2_hodnota += 1
        micekX = 400
        micekY = 300


    elif micekX >= 768:
        score1_hodnota += 1
        micekX = 400
        micekY = 300


    player1Y += player1Y_change
    if player1Y <= 0:
        player1Y = 0
    elif player1Y >= 536:
        player1Y = 536

    player2Y += player2Y_change
    if player2Y <= 0:
        player2Y = 0
    elif player2Y >= 536:
        player2Y = 536

    micekY += micekY_change
    if micekY <= 0:
        micekY_change *= -1
    elif micekY >= 568:
        micekY_change *= -1

    Kolize4 = Kolize2(micekX, micekY, player2X, player2Y)
    Kolize3 = Kolize1(micekX, micekY, player1X, player1Y)
    if Kolize3 and micekX_change < 0:
        micekX_change *= - 1
        micekY_change *= 1
    elif Kolize4 and micekX_change > 0:
        micekX_change *= - 1
        micekY_change *= 1

    player1(player1X, player1Y)
    player2(player2X, player2Y)
    micek(micekX, micekY)
    micekX += micekX_change
    ukaz_score(textX, textY)
    ukaz_score2(text2X, text2Y)
    pygame.display.update()

