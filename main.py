import pygame
import os
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join('img', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 12
        self.top = 12
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.width):
            for j in range(self.height):
                pygame.draw.rect(screen, pygame.Color(255, 255, 255),
                                 [self.left + self.cell_size * i,
                                  self.top + self.cell_size * j,
                                  self.cell_size, self.cell_size], 1)


class Menu:
    pass


class Character(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = load_image("character.jpg", -1)
        self.rect = self.image.get_rect()
        self.coords = self.rect.x, self.rect.y = 75, 775
        self.mask = pygame.mask.from_surface(self.image)


class Enemy:
    pass


class Shop:
    pass


class Snowball:
    pass

if __name__ == '__main__':
    pygame.init()
    size = 650, 850
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Инициализация игры")
    board = Board(12, 12)
    character_sprites = pygame.sprite.Group()
    character = Character(character_sprites)
    running = True
    board.set_view(25, 220, 50)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        character_sprites.draw(screen)
        board.render(screen)
        pygame.display.flip()
    pygame.quit()
