# Example file showing a circle moving on screen
import random

import pygame
from platformTemplate import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((920, 720))
clock = pygame.time.Clock()
running = True
dt = 0
gravity = 0
canJump = False
playerList = []

player1_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player2_pos = pygame.Vector2(screen.get_width() / 2 + 200, screen.get_height() / 2)

# xpos, ypos, xwidth, yheight
platformGround = CustomPlatform(0, 600, 920, 20, "white")
platform1 = CustomPlatform(50, 250, 180, 20, "white")
platform2 = CustomPlatform(400, 450, 180, 20, "white")
platform3 = CustomPlatform(700, 250, 180, 20, "white")


platformList = [platformGround, platform1, platform2, platform3]

player1_image = pygame.image.load("assets/jumpboy.png")
player1_image = pygame.transform.scale(player1_image, (140, 140))

player2_image = pygame.image.load("assets/cryingChild.png")
player2_image = pygame.transform.scale(player2_image, (140, 140))

font = pygame.font.SysFont(None, 40)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

 
        
        
    
   
    
    gravity += 1000 * dt
    player1_pos.y += gravity * dt

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and canJump:
        gravity = -600
        canJump = False
    if keys[pygame.K_LEFT]:
        player1_pos.x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        player1_pos.x += 300 * dt

    # Rebuild rect after movement so collisions use updated position
    player1_rect = pygame.Rect(player1_pos.x-70, player1_pos.y-70, 140, 140)
    player2_rect = pygame.Rect(player2_pos.x-70, player2_pos.y-70, 140, 140)

    playerList = [player1_rect, player2_rect]

    # Platform collisions using minimum overlap (MTV)
    canJump = False
    for platform in platformList:
        for player_rect in playerList:
            if player1_rect.colliderect(platform):
                overlap_top    = player1_rect.bottom - platform.top
                overlap_bottom = platform.bottom - player1_rect.top
                overlap_left   = player1_rect.right - platform.left
                overlap_right  = platform.right - player1_rect.left
                overlap_y = min(overlap_top, overlap_bottom)
                overlap_x = min(overlap_left, overlap_right)

                if overlap_y <= overlap_x:
                    # Vertical collision
                    if gravity >= 0 and overlap_top <= overlap_bottom:
                        player1_rect.bottom = platform.top
                        gravity = 0
                        canJump = True
                    else:
                        player1_rect.top = platform.bottom
                        gravity = 0
                else:
                    # Horizontal collision
                    if overlap_left <= overlap_right:
                        player1_rect.right = platform.left
                    else:
                        player1_rect.left = platform.right
                player1_pos.x = player1_rect.centerx
                player1_pos.y = player1_rect.centery

    player1_rect.clamp_ip(screen.get_rect())
    player1_pos.x = player1_rect.centerx
    player1_pos.y = player1_rect.centery
    
    screen.fill("black")

    for platform in platformList:
        platform.update(screen)
    
    # draw player 1
    screen.blit(player1_image, player1_rect)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()