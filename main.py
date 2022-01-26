import os
import sys
import pygame

FPS = 50


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
        pygame.draw.rect(screen, (153, 153, 255), [self.left, self.top, self.cell_size * 12, self.cell_size * 12], 0)
        for i in range(self.width):
            for j in range(self.height):
                pygame.draw.rect(screen, pygame.Color(255, 255, 255),
                                 [self.left + self.cell_size * i,
                                  self.top + self.cell_size * j,
                                  self.cell_size, self.cell_size], 1)


class Menu:
    def __init__(self):
        font1 = pygame.font.Font(None, 30)
        font2 = pygame.font.Font(None, 60)
        text1 = font2.render('Save Xmas', True, (179, 222, 255))
        text_x1 = width // 2 - text1.get_width() // 2
        text_y1 = height // 7 - text1.get_height() // 2
        text2 = font1.render("Добро пожаловать в игру «Спаси Рождество»", True, (255, 255, 255))
        text_x2 = width // 2 - text2.get_width() // 2
        text_y2 = height // 5 - text2.get_height() // 2
        screen.blit(text2, (text_x2, text_y2))
        screen.blit(text1, (text_x1, text_y1))
        text2 = font1.render("Гринч - похититель Рождества.", True, (255, 255, 255))
        text_x2 = width // 2 - text2.get_width() // 2
        text_y2 = height // 4 - text2.get_height() // 2
        screen.blit(text2, (text_x2, text_y2))
        text2 = font1.render("Он пробрался к Санте на завод игрушек и хочет все сломать.", True,
                             (255, 255, 255))
        text_x2 = width // 2 - text2.get_width() // 2
        text_y2 = height // 3.4 - text2.get_height() // 2
        screen.blit(text2, (text_x2, text_y2))
        text2 = font1.render("Ваша задача отбиваться от Гринча снежками. Желаем удачи!", True,
                             (255, 255, 255))
        text_x2 = width // 2 - text2.get_width() // 2
        text_y2 = height // 2.9 - text2.get_height() // 2
        screen.blit(text2, (text_x2, text_y2))
        text2 = font1.render("Чтобы начать игру нажмите Enter", True, (255, 255, 255))
        text_x2 = width // 2 - text2.get_width() // 2
        text_y2 = height // 2 - text2.get_height() // 2
        screen.blit(text2, (text_x2, text_y2))
        pygame.display.flip()


class Character(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = load_image("character.jpg", -1)
        self.rect = self.image.get_rect()
        self.coords = self.rect.x, self.rect.y = 75, 775
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        pass

    def get_coords(self):
        return self.coords

    def shoot(self):
        self.snowball = Snowball(snows_group)

class Enemy:
    pass


class Shop:
    pass


class Snowball(pygame.sprite.Sprite):
    global character

    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_image('snow.jpg', -1)
        self.rect = self.image.get_rect()
        self.coords = self.rect.x, self.rect.y = character.get_coords()[0] + 15, 700
        self.mask = pygame.mask.from_surface(self.image)
        self.fly()

    def fly(self):
        self.rect = self.rect.move(0, 1)


pygame.init()
size = width, height = 650, 850
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Save Xmas")
img = load_image('xmas.jpg')
img = pygame.transform.scale(img, size)
screen.blit(img, (0, 0))
menu = Menu()
clock = pygame.time.Clock()
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        quit(0)
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
            break
board = Board(12, 12)
character_sprites = pygame.sprite.Group()
character = Character(character_sprites)
snows_group = pygame.sprite.Group()
board.set_view(25, 220, 50)
pygame.mouse.set_visible(True)
running = True
while running:
    screen.blit(img, (0, 0))
    board.render(screen)
    character_sprites.draw(screen)
    snows_group.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                character.shoot()
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
        clock.tick(FPS)
pygame.quit()
