# Example file showing a circle moving on screen
import random

import pygame
from ethanPlatform import *
from ethanBullet import *
from ethanLevels import *

BULLET_COOLDOWN = 1.0

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
gravity = 0
canJump = False



player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


currentLevel = 1
platformList = levels[currentLevel - 1]()
SPAWN = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
gameWon = False

bulletList = []
bulletCooldown = 6.0






font = pygame.font.SysFont(None, 40)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

 
        
        
    player_rect = pygame.Rect(player_pos.x - 20, player_pos.y - 20, 40, 40)
    
    bulletCooldown -= dt
   
    if bulletCooldown < 0:
        bulletCooldown = 6.0
        randomPos = pygame.Vector2(random.randint(0, 1280), random.randint(0, 720))
        newBullet = Bullet(randomPos, player_pos)
        bulletList.append(newBullet)

    gravity += 1000 * dt
    player_pos.y += gravity * dt

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and canJump:
        gravity = -600
        canJump = False
    if keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt

    # Rebuild rect after movement so collisions use updated position
    player_rect = pygame.Rect(player_pos.x - 20, player_pos.y - 20, 40, 40)

    # Platform collisions using minimum overlap (MTV)
    canJump = False
    for platform in platformList:
        if isinstance(platform, EscapeDoor):
            continue   # door is walk-through, not solid
        if player_rect.colliderect(platform):
            overlap_top    = player_rect.bottom - platform.top
            overlap_bottom = platform.bottom - player_rect.top
            overlap_left   = player_rect.right - platform.left
            overlap_right  = platform.right - player_rect.left
            overlap_y = min(overlap_top, overlap_bottom)
            overlap_x = min(overlap_left, overlap_right)

            if overlap_y <= overlap_x:
                # Vertical collision
                if gravity >= 0 and overlap_top <= overlap_bottom:
                    player_rect.bottom = platform.top
                    gravity = 0
                    canJump = True
                else:
                    player_rect.top = platform.bottom
                    gravity = 0
            else:
                # Horizontal collision
                if overlap_left <= overlap_right:
                    player_rect.right = platform.left
                else:
                    player_rect.left = platform.right
            player_pos.x = player_rect.centerx
            player_pos.y = player_rect.centery

    player_rect.clamp_ip(screen.get_rect())
    player_pos.x = player_rect.centerx
    player_pos.y = player_rect.centery
    
    screen.fill("black")

    for platform in platformList:
        if platform.update(screen, player_rect) == "escape" and not gameWon:
            currentLevel += 1
            if currentLevel < len(levels):
                platformList = levels[currentLevel]()
                player_pos.update(SPAWN)
                gravity = 0
                bulletList.clear()
            else:
                gameWon = True
            break
    
    pygame.draw.rect(screen, "gold", player_rect)

    if gameWon:
        text = font.render("You Escaped!", True, "green")
        screen.blit(text, text.get_rect(center=screen.get_rect().center))

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()