import pygame

class Player:
    def __init__(self, pos, image, gravity, canJump):
        self.pos = pos
        self.image = pygame.transform.scale(image, (140, 140))
        self.rect = pygame.Rect(self.pos.x-70, self.pos.y-70, 140, 140)
        self.gravity = gravity
        self.canJump = canJump
    
    def update(self, dt):
        self.gravity += 1000 * dt
        self.pos.y += self.gravity * dt
        self.rect = pygame.Rect(self.pos.x-70, self.pos.y-70, 140, 140)
        
    def input(self, keys, dt):
        if keys[pygame.K_UP] and self.canJump:
                self.gravity = -600
                self.canJump = False
        if keys[pygame.K_LEFT]:
                self.pos.x -= 300 * dt
        if keys[pygame.K_RIGHT]:
                self.pos.x += 300 * dt
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)