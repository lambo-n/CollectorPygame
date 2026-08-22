import pygame


def level1():
    return[
        Enemy((400,500), pygame.image.load("assets/Skeleton.png"), 30),
    ]

def level2():
    return[
        Enemy((500,380), pygame.image.load("assets/Skeleton.png"), 30),
        Enemy((700,380), pygame.image.load("assets/Skeleton.png"), 30),
    ]

def level3():
    return[
        Enemy((400,500), pygame.image.load("assets/Skeleton.png"), 30),
        Enemy((500,600), pygame.image.load("assets/Skeleton.png"), 30),
        Enemy((100,300), pygame.image.load("assets/Skeleton.png"), 30),
    ]

enemies = [level1, level2, level3]

class Enemy:
    def __init__(self, pos, image, health):
        self.pos = pos
        self.image = pygame.transform.scale(image, (150,150))
        self.health = health
        self. rect = self.image.get_rect(center=self.pos)


    def update(self, dt):
        pass

    def draw(self, screen):
        screen.blit( self.image, self.rect)
