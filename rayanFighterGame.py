# Example file showing a circle moving on screen
import random

import pygame
from platformTemplate import *
from rayanPlayer import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((920, 720))
clock = pygame.time.Clock()
running = True
dt = 0
gravity1 = 0
canJump = False
playerList = []

player1_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player2_pos = pygame.Vector2(screen.get_width() / 2 + 200, screen.get_height() / 2)



# xpos, ypos, xwidth, yheight
platformGround = CustomPlatform(0, 600, 920, 100, "white")
platform1 = CustomPlatform(50, 250, 180, 20, "white")
platform2 = CustomPlatform(400, 400, 180, 20, "white")
platform3 = CustomPlatform(700, 250, 180, 20, "white")


platformList = [platformGround, platform1, platform2, platform3]

player1_image = pygame.image.load("assets/jumpboy.png")
player1_image = pygame.transform.scale(player1_image, (140, 140))

player1_punch = pygame.image.load("assets/cops.png")
player1_punch = pygame.transform.scale(player1_punch, (140, 140))

player2_image = pygame.image.load("assets/cryingChild.png")
player2_image = pygame.transform.scale(player2_image, (140, 140))

player2_punch = pygame.image.load("assets/cave.png")
player2_punch = pygame.transform.scale(player2_punch, (140, 140))

player1 = Player(player1_pos, pygame.image.load("assets/jumpboy.png"), 0, canJump, "p1")
player2 = Player(player2_pos, pygame.image.load("assets/cryingChild.png"), 0, canJump, "p2")

playerList = [player1, player2]

font = pygame.font.SysFont(None, 40)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

 
        
        
    
    keys = pygame.key.get_pressed()
    for player in playerList:
        player.input(keys, dt)
        player.update(dt)



    # Platform collisions using minimum overlap (MTV)
    canJump = False
    for platform in platformList:
        for player in playerList:
            if player.rect.colliderect(platform):
                overlap_top    = player.rect.bottom - platform.top
                overlap_bottom = platform.bottom - player.rect.top
                overlap_left   = player.rect.right - platform.left
                overlap_right  = platform.right - player.rect.left
                overlap_y = min(overlap_top, overlap_bottom)
                overlap_x = min(overlap_left, overlap_right)

                if overlap_y <= overlap_x:
                    # Vertical collision
                    if overlap_top <= overlap_bottom:
                        # Landing on top: only if not moving upward
                        if player.gravity >= 0:
                            player.rect.bottom = platform.top
                            player.gravity = 0
                            player.canJump = True
                    else:
                        # Head bump: only if actually moving upward
                        if player.gravity < 0:
                            player.rect.top = platform.bottom
                            player.gravity = 0
                else:
                    # Horizontal collision
                    if overlap_left <= overlap_right:
                        player.rect.right = platform.left
                    else:
                        player.rect.left = platform.right
                player.pos.x = player.rect.centerx
                player.pos.y = player.rect.centery
    
    screen.fill("black")

    for platform in platformList:
        platform.update(screen)
    
    for player in playerList:
        player.draw(screen)


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()