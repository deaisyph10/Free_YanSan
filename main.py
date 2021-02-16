import pygame
import random
import sys
from Colors import *
pygame.init()
pygame.font.init()
cell_pxl_size = 96
cell_count = 12
screen_width = int(cell_count * cell_pxl_size)
screen_height = int(cell_count * cell_pxl_size)
FPS = 160
moveX, moveY = 0, 0
screen = pygame.display.set_mode((cell_pxl_size * cell_count, cell_pxl_size * cell_count))
pygame.display.set_caption("FREE_YanSan")
clock = pygame.time.Clock()
back_round_im = pygame.image.load("images/templets/Stars.png")
back_round = pygame.Surface((800, 400))
back_round.blit(back_round_im, (0, 0))
music = pygame.mixer.Sound("images/sounds/monkeys wedding_low.wav")
laser = pygame.mixer.Sound("images/sounds/laser_SE_hit.wav")
shoot_laser = pygame.mixer.Sound("images/sounds/laser_SE_shoot.wav")
dream_logo = pygame.image.load("images/templets/Dream_Logo.png")
dream_logo_2 = pygame.transform.scale(dream_logo, (40, 40))
LLC_icon = pygame.image.load("images/templets/Dream_green_title.png")
LLC_icon_micro = pygame.transform.scale(LLC_icon, (200, 40))
game_font = pygame.font.Font("freesansbold.ttf", 42)
game_font_2 = pygame.font.Font("freesansbold.ttf", 10)
mono_font = pygame.font.SysFont("monospace", 36)
pygame.mouse.set_visible(True)
x = 0
y = 0
music.play(10)
sample_rect = pygame.Rect(800, 650, 50, 50)
sample_rect_sur = pygame.Surface((50, 50))
hit_sample_rect = pygame.draw.rect(screen, GRAY76, sample_rect)
hit_sur = pygame.Surface((50, 50))
drone_pos = []
drone_rect = []
x = 0
y = 0
steps = 6


class Cockpit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/templets/Cockpit_Spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 90

    def update(self):
        self.render()

    def render(self):
        screen.blit(self.image, (0, 100))


class Pilot(pygame.sprite.Sprite):
    def __init__(self):
        super(Pilot, self).__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/templets/crosshairs_blue.png")
        self.rect = self.image.get_rect()

    def update(self):
        self.rect = pygame.mouse.get_pos()

    def create_bullet(self):
        return Bullets(pygame.mouse.get_pos()[0] + 150, pygame.mouse.get_pos()[1] + 150)

    def sec_bul(self):
        return Bullets(pygame.mouse.get_pos()[0] + 170, pygame.mouse.get_pos()[1] + 150)

    def render(self):
        screen.blit(self.image, (self.x, self.y))


class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.Surface((12, 3))
        self.im1 = pygame.Surface((12, 3))
        # self.image.fill(white)
        self.im1.fill(WHITE)
        self.rect = self.image.get_rect(center=(int(x), int(y)))
        self.rect_2 = self.image.get_rect(center=(int(x), int(y)))

    def checkCollision(self):
        if self.rect.colliderect(asteroid):
            laser.play()
            self.kill()
            screen.blit(hit_sur, hit_sample_rect)
            asteroid.rect.y = random.randint(80, 250)
            asteroid.rect.x = 0

    def update(self):
        self.rect.y -= 25
        self.rect.x -= 25
        self.rect_2.y -= 25
        self.rect_2.x -= 25
        self.image = self.im1
        self.image = self.image
        if self.rect.x >= screen_width - 100:
            self.kill()
        if self.rect_2.x >= screen_width - 100:
            self.kill()

        self.checkCollision()


class Drone(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super(Drone, self).__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self):
        self.render()

    def render(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))


class Purple_fighter(pygame.sprite.Sprite):
    def __init__(self):
        super(Purple_fighter, self).__init__()
        self.image = pygame.image.load("images/ships/13B.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.render()

    def render(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))


class Title_text(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 280
        self.y = 4
        self.title_text = str("----FREE-------(Y//:AinSan)----")
        self.title_surface = game_font.render(self.title_text, True, WHITE)
        self.image = self.title_surface
        self.rect = self.image.get_rect()

    def update(self):
        self.render()

    def render(self):
        screen.blit(self.image, (self.x, self.y))


class Network_Map_Window(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 50
        self.y = 100
        self.sur = pygame.Surface((900, 500))
        self.dream_title_rect = pygame.Rect(250, 300, 200, 200)
        self.dream_logo_rect = pygame.Rect(600, 100, 200, 200)
        self.dream_logo = dream_logo
        self.dream_title = pygame.image.load("images/templets/Dream_green_title.png")

    def update(self):
        self.render()

    def render(self):
        self.sur.fill(GRAY7)
        back_round.blit(self.sur, (self.x, self.y))


class Header(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 1
        self.y = 1
        self.rect = pygame.Rect(self.x, self.y, screen_width - 2, cell_pxl_size - 32)
        self.white_border = pygame.Rect(self.x - 1, self.y - 1, screen_width, cell_pxl_size - 30)
        self.dream_logo_2 = dream_logo_2
        self.LLC_icon = LLC_icon_micro

    def update(self):
        self.render()

    def render(self):
        pygame.draw.rect(screen, GRAY76, self.white_border)
        pygame.draw.rect(screen, GRAY7, self.rect)
        screen.blit(self.dream_logo_2, (10, 10))
        screen.blit(self.LLC_icon, (60, 10))


class YainSan_Window(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 5
        self.y = 400
        self.sur = pygame.Surface(((cell_pxl_size * 3), int(cell_pxl_size * 3)))
        self.rect = self.sur.get_rect()
        self.sur.fill(GRAY7)
        self.white_border = pygame.Rect((self.x - 1, self.y - 1, (cell_pxl_size * 3) + 2, int(cell_pxl_size * 3)+2))
        self.icon_rect = pygame.Rect(self.x + (cell_pxl_size * 2), self.y, cell_pxl_size, cell_pxl_size)
        self.icon_box_sur = pygame.Surface((80, 80))
        self.icon_box_sur.fill(BLACK)
        self.blue_bor_icon = pygame.Surface((84, 84))
        self.blue_bor_icon.fill(CADETBLUE)
        self.icon_image = pygame.image.load("images/player/Yan_San_icon_blueglow.png")
        self.icon_rect = self.icon_image.get_rect()
        self.text = str("_____'Y'..DRIVE.. _____ Artificial Intelligence _____")
        self.text_sur = game_font_2.render(self.text, True, WHITE)
        self.text_im = self.text_sur
        self.text_rect = self.text_im.get_rect()
        self.dream_logo_2 = dream_logo_2

    def update(self):
        self.render()
        self.call_window()

    def call_window(self):
        self.rect.y -= 5
        if self.rect.y <= 500:
            self.rect.y = 500

    def render(self):
        pygame.draw.rect(screen, WHITE, self.white_border)
        self.sur.blit(self.icon_box_sur, ((self.x + 140), (self.y + 5)))
        self.sur.blit(self.text_sur, (40, 5))
        self.sur.blit(self.blue_bor_icon, (198, 18))
        self.sur.blit(self.icon_box_sur, (200, 20))
        self.sur.blit(self.icon_image, (190, 20))
        self.sur.blit(self.dream_logo_2, (5, 5))
        screen.blit(self.sur, (self.x, self.y))
        self.sur.fill(GRAY7)


class Bottom_mid_textbox(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 330
        self.y = 620
        self.rect = pygame.Rect(self.x, self.y, (cell_pxl_size * 3) - 2, int(cell_pxl_size))
        self.white_border = pygame.Rect(self.x - 1, self.y - 1, (cell_pxl_size * 3), int(cell_pxl_size) + 2)

    def update(self):
        self.render()

    def render(self):
        pygame.draw.rect(screen, GRAY7, self.white_border)
        pygame.draw.rect(screen, BLACK, self.rect)


class Photon_Charger_Window(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 550
        self.y = 620
        self.title_text = str("PHOTON CHARGER")
        self.rect = pygame.Rect(self.x, self.y, (cell_pxl_size * 2), int(cell_pxl_size))
        self.white_border = pygame.Rect(self.x - 1, self.y - 1, (cell_pxl_size * 2) + 2, int(cell_pxl_size) + 2)
        self.charger_label = game_font_2.render(self.title_text, True, GRAY76)
        self.charger_box = pygame.Surface((cell_pxl_size * 2, (cell_pxl_size * 2) - 6))
        self.text = self.charger_box
        self.text_rect_2 = self.text.get_rect()

    def update(self):
        self.render()

    def render(self):
        pygame.draw.rect(screen, GRAY7, self.white_border)
        pygame.draw.rect(screen, BLACK, self.rect)
        screen.blit(self.charger_box, (self.x, self.y))
        self.charger_box.fill(GRAY7)
        self.charger_box.blit(self.charger_label, (5, 10))


class Message_textbox(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 780
        self.y = 620
        self.rect = pygame.Rect(self.x, self.y, 200, 300 - 1)
        self.white_border = pygame.Rect(self.x - 1, self.y - 1, 200 + 2, 300 + 1)

    def update(self):
        self.render()

    def render(self):
        pygame.draw.rect(screen, GRAY7, self.white_border)
        pygame.draw.rect(screen, BLACK, self.rect)


class Main_radar_textbox(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 880
        self.y = 620
        self.rect = pygame.Rect(self.x, self.y, 200, 200 - 1)
        self.white_border = pygame.Rect(self.x - 1, self.y - 1, 200 + 2, 200 + 1)

    def update(self):
        self.render()

    def render(self):
        pygame.draw.rect(screen, GRAY7, self.white_border)
        pygame.draw.rect(screen, BLACK, self.rect)


class Alien_full_body(pygame.sprite.Sprite):
    def __init__(self):
        self.x = 850
        self.y = 300
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/player/profile_allien_2.png")
        self.surface = self.image
        self_rect = self.image.get_rect()

    def update(self):
        self.render()

    def render(self):
        screen.blit(self.image, (self.x, self.y))


class Alien_close_up(pygame.sprite.Sprite):
    def __init__(self):
        self.x = 40
        self.y = 300
        self.layer = 0
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/player/profile_allien.png")
        self.surface = self.image
        self.rect = self.image.get_rect()

    def update(self):
        self.render()

    def render(self):
        screen.blit(self.image, (self.x, self.y))


class Planet_larger(pygame.sprite.Sprite):
    def __init__(self):
        self.x = 734
        self.y = 222
        self. layer = 0
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/planets/planet7.png")
        self.surface = self.image
        self.rect = self.image.get_rect()

    def update(self):
        self.render()

    def render(self):
        screen.blit(self.image, (self.x, self.y))


class Planet_yellow(pygame.sprite.Sprite):
    def __init__(self):
        self.x = 900
        self.y = 230
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("micro_images/planet1.png")
        self.surface = self.image
        self.rect = self.image.get_rect()

    def update(self):
        self.render()

    def render(self):
        screen.blit(self.image, (self.x, self.y))


class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 50
        self.y = 200
        self.rect = pygame.Rect(self.x, self.y, 40, 40)
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.images.append(pygame.image.load("images/planets/asteroid_1.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_1.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_1.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_1.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_2.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_2.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_2.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_2.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_3.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_3.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_3.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_3.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_4.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_4.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_4.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_4.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_5.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_5.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_5.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_5.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_6.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_6.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_6.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_6.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_7.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_7.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_7.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_7.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_8.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_8.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_8.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_8.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_9.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_9.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_9.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_9.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_10.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_10.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_10.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_11.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_11.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_11.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_11.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_12.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_12.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_12.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_12.png"))
        self.images.append(pygame.image.load("images/planets/asteroid_12.png"))
        self.index = 0
        self.image = self.images[self.index]

    def move(self):
        dist = 1
        self.rect.y += int(dist) * 1
        self.rect.x += int(dist) * 5

    def update(self):
        self.spin()
        self.move()

    def spin(self):
        self.index += 1
        if self.index >= 40:
            self.index = 0
        self.image = self.images[self.index]
        if self.rect.x >= 1000 or self.rect.y >= 450:
            self.rect.x = random.randint(40, 60)
            self.rect.y = random.randint(120, 360)


class Red_ship(pygame.sprite.Sprite):
        def __init__(self):
            super(Red_ship, self).__init__()
            self.image = pygame.image.load("images/ships/SpaceHero/red_ship_micro.png")
            self.im2 = pygame.image.load("images/ships/SpaceHero/red_ship_micro_hit.png")
            self.rect = self.image.get_rect()
            self.rect.x = 250
            self.rect.y = 325
            self.movex = 0  # move along X
            self.movey = 0  # move along Y

        def update(self):
            self.rect.x = self.rect.x + self.movex
            self.rect.y = self.rect.y + self.movey
            self.render()

        def attack(self):
            self.create_bullet()
            self.sec_bullet()

        def control(self, x, y):
            self.movex += x
            self.movey += y

        def create_bullet(self):
            return Bullet(self.rect.x, self.rect.y)

        def sec_bullet(self):
            return Bullet(self.rect.x + 20, self.rect.y)

        def render(self):
            battle_screen.blit(self.image, (self.rect.x, self.rect.y))


class Bullet(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super(Bullet, self).__init__()
            self.x = x
            self.y = y
            self.image = pygame.Surface((1, 1))
            self.image.fill((255, 255, 255))
            self.rect = self.image.get_rect(center=(int(x), int(y)))

        def update(self):
            self.rect.y += -1
            self.image = self.image
            if self.rect.y <= 0:
                self.kill()
            self.check_collision()

        def check_collision(self):
            if self.rect.colliderect(grey_ship):
                self.kill()


class Purple_ship(pygame.sprite.Sprite):
        def __init__(self):
            super(Purple_ship, self).__init__()
            self.image = pygame.image.load("images/ships/SpaceHero/purple_ship_micro.png")
            self.rect = self.image.get_rect()
            self.rect.x = 130
            self.rect.y = 50
            self.movex = 0  # move along X
            self.movey = 0  # move along Y

        def move(self):
            self.rect.x += random.randint(-1, 1)
            self.rect.y += random.randint(-1, 1)
            if self.rect.x >= 470:
                self.rect.x = 470
            if self.rect.x <= 0:
                self.rect.x = 0
            if self.rect.y >= 500:
                self.rect.y = 500
            if self.rect.y <= 0:
                self.rect.y = 0

        def control(self, x, y):
            self.movex += x
            self.movey += y

        def create_bullet(self):
            return Enemy_Bullets(self.rect.x, self.rect.y)

        def sec_bullet(self):
            return Enemy_Bullets(self.rect.x + 20, self.rect.y)

        def attack(self):
            self.create_bullet()
            self.sec_bullet()
            bullets_group.add(purple_ship.create_bullet())
            bullets_group.add(purple_ship.sec_bullet())

        def update(self):
            self.rect.x = self.rect.x + self.movex
            self.rect.y = self.rect.y + self.movey
            self.render()

        def render(self):
            battle_screen.blit(self.image, (self.rect.x, self.rect.y))


class Enemy_Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Enemy_Bullets, self).__init__()
        self.image = pygame.Surface((1, 3))
        self.image.fill((255, 255, 255))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        self.rect.y += 5
        self.image = self.image
        if self.rect.y >= 500:
            self.kill()
            self.check_collision()

    def check_collision(self):
        if self.rect.colliderect(red_ship):
            self.kill()


class Yellow_ship(pygame.sprite.Sprite):
    def __init__(self):
        super(Yellow_ship, self).__init__()
        self.image = pygame.image.load("images/ships/SpaceHero/yellow_ship_micro.png")
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 200
        self.movex = 0  # move along X
        self.movey = 0  # move along Y

    def move(self):
        self.rect.x += 0
        self.rect.y += 0
        if self.rect.x >= 500:
            self.rect.x = 500
        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.y >= 500:
            self.rect.y = 500
        if self.rect.y <= 0:
            self.rect.y = 0

    def update(self):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
        self.render()
        self.move()

    def attack(self):
        self.create_bullet()
        self.sec_bullet()
        bullets_group.add(yellow_ship.create_bullet())
        bullets_group.add(yellow_ship.sec_bullet())

    def control(self, x, y):
        self.movex += x
        self.movey += y

    def create_bullet(self):
        return Enemy_Bullets(self.rect.x, self.rect.y)

    def sec_bullet(self):
        return Enemy_Bullets(self.rect.x + 20, self.rect.y)

    def render(self):
        battle_screen.blit(self.image, (self.rect.x, self.rect.y))


class Grey_ship(pygame.sprite.Sprite):
    def __init__(self):
        super(Grey_ship, self).__init__()
        self.image = pygame.image.load("images/ships/SpaceHero/grey_ship_micro.png")
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 20
        self.movex = 0  # move along X
        self.movey = 0  # move along Y

    def move(self):
        self.rect.x += random.randint(-3, 3)
        self.rect.y += random.randint(-3, 3)
        if self.rect.x >= 500:
            self.rect.x = 500

        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.y >= 200:
            self.rect.y = 200
        if self.rect.y <= 0:
            self.rect.y = 0

    def update(self):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
        self.check_collision()
        self.render()
        self.move()

    def attack(self):
        self.create_bullet()
        self.sec_bullet()
        bullets_group.add(grey_ship.create_bullet())
        bullets_group.add(grey_ship.sec_bullet())

    def control(self, x, y):
        self.movex += x
        self.movey += y

    def create_bullet(self):
        return Enemy_Bullets(self.rect.x, self.rect.y)

    def sec_bullet(self):
        return Enemy_Bullets(self.rect.x + 20, self.rect.y)

    def create_clone(self):
        return Grey_ship()

    def render(self):
        battle_screen.blit(self.image, (self.rect.x, self.rect.y))

    def check_collision(self):
        if self.rect.colliderect(bullets):
            return self.kill()


class Start_Up(pygame.sprite.Sprite):
    def __init__(self):
        super(Start_Up, self).__init__()
        self.image = pygame.image.load("opening_backround.png")
        self.sur = pygame.Surface((1200, 800))
        self.rect = self.sur.get_rect()
        self.rect.x = 1200
        self.rect.y = 800
        self.sur.blit(self.image, (250, 0))

    def update(self):
        screen.blit(self.sur, (0, 0))
        self.button()
        self.text()


    def text(self):
        font = mono_font
        surfacefont = font.render("FREE YanSan", True, MIDNIGHTBLUE)
        surfaceR = surfacefont.get_rect()
        surfaceR.center = (120, 50)
        self.sur.blit(surfacefont, surfaceR)
        text = font.render("Start game", True, MIDNIGHTBLUE)
        textpos = surfacefont.get_rect()
        textpos.center = (120, 200)
        self.sur.blit(text, textpos)
        text = font.render("Exit Game", True, MIDNIGHTBLUE)
        surfacefont.get_rect()
        textpos.center = (120, 260)
        self.sur.blit(surfacefont, surfaceR)
        self.sur.blit(text, textpos)
        yainsan_window.render()
        pygame.display.update()

    def button(self):
        click = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()

        if 190 > pos[0] > 10 and 230 > pos[1] > 180:
            pygame.draw.rect(self.sur, SLATEGRAY3, (80, 175, 160, 50))
            if click[0] == 1:
                self.kill()
            else:
                pygame.draw.rect(self.sur, BLACK, (80, 175, 160, 50))
        if 180 > pos[0] > 10 and 275 > pos[1] > 230:
            pygame.draw.rect(self.sur, SLATEGRAY3, (80, 230, 160, 50))
            if click[0] == 1:
                pygame.quit()
                sys.exit()
            else:
                pygame.draw.rect(self.sur, BLACK, (80, 230, 160, 50))

    def RunGame(self):
        self.sur.fill(BLACK)


start_group = pygame.sprite.Group()
start_up = Start_Up()
start_group.add(start_up)

x = 350
y = 600
purple_ship = Purple_ship()
yellow_ship = Yellow_ship()
grey_ship = Grey_ship()
red_ship = Red_ship()
bullets = Bullet(x, y)
enemy_bullets = Enemy_Bullets(x, y)
battle_sprites = pygame.sprite.Group()
battle_sprites.add(red_ship, yellow_ship, purple_ship)
draw_group = pygame.sprite.Group()
bullets_group = pygame.sprite.Group()
bullets_group.add(bullets, enemy_bullets)
asteroid = Asteroid()
bullet = Bullets(x, y)
player = Pilot()
header = Header()
cockpit = Cockpit()
yainsan_window = YainSan_Window()
bottom_mid_textbox = Bottom_mid_textbox()
photon_charger_window = Photon_Charger_Window()
message_textbox = Message_textbox()
main_radar_textbox = Main_radar_textbox()
alien_close_up = Alien_close_up()
alien_full_body = Alien_full_body()
planet_larger = Planet_larger()
planet_yellow = Planet_yellow()
game_title = Title_text()
purple_fighter = Purple_fighter()
blue_bolt = pygame.image.load("images/planets/blue_bolt.png")
blue_bolt_rect = pygame.Rect(10, 10, 400, 301)
new_icon = pygame.image.load("images/player/Dream_Logic_new_icon.png")
new_icon_rect = pygame.Rect(230, 450, 60, 60)
radar_screen = pygame.image.load("images/templets/opohgknlov.jpeg")
radar_screen_rect = pygame.Rect(0, 0, 1051, 515)
menu_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
planet_group = pygame.sprite.Group()
character_group = pygame.sprite.Group()
asteroid_group = pygame.sprite.Group()
net_menu = pygame.sprite.Group()
net_menu_sprite = Network_Map_Window()
net_menu.add(net_menu_sprite)
menu_group.add(header, game_title, message_textbox, main_radar_textbox)
menu_group.add(bottom_mid_textbox, photon_charger_window, yainsan_window)
planet_group.add(planet_larger, planet_yellow)
character_group.add(alien_close_up, alien_full_body)
asteroid_group.add(asteroid)
star_list = []
asteroid_list = []
all_sprites = pygame.sprite.LayeredUpdates()
cockpit_group = pygame.sprite.Group()
cockpit_group.add(cockpit)
all_sprites.add(player, asteroid, purple_fighter)
for i in range(7600):
    x = random.randrange(140, 1000)
    y = random.randrange(14, 36)
    star_list.append([x, y])
for a in range(140):
    Ax = random.randrange(100, 950)
    Ay = random.randrange(228, 340)
    asteroid_list.append([Ax, Ay])

game_time = pygame.time.get_ticks()
interior_layout = pygame.image.load("images/templets/interior_edit_600x450.jpg").convert()
interior_layout_sur = pygame.Surface((600, 450))
int_window_rect = pygame.Rect(250, 120, 610, 460)
int_window = pygame.Surface((610, 460))

battle_screen_width = 495
battle_screen_height = 170
battle_screen = pygame.Surface((battle_screen_width, battle_screen_height))
battle = False
net_menu_window = False
interior_window = False
radar_screen_value = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                back_round.blit(start_up.image, (280, 110))

            if event.key == pygame.K_0:
                net_menu_window = True
            if event.key == pygame.K_LSHIFT:
                interior_window = True
                int_window.blit(interior_layout, (10, 10))
            if event.key == pygame.K_RETURN:
                radar_screen_value = True
            if event.key == pygame.K_SPACE:
                shoot_laser.play()
                bullet_group.add(player.create_bullet())
                bullet_group.add(player.sec_bul())
            if event.key == pygame.K_RETURN:
                draw_group.add(grey_ship.create_clone())
            if event.key == pygame.K_LEFT:
                purple_ship.control(-steps, 0)
            if event.key == pygame.K_RIGHT:
                purple_ship.control(steps, 0)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_1:
                battle = False
            if event.key == pygame.K_0:
                net_menu_window = False
            if event.key == pygame.K_LSHIFT:
                interior_window = False
            if event.key == pygame.K_RETURN:
                radar_screen_value = False
            if event.key == pygame.K_LEFT:
                purple_ship.control(steps, 0)
            if event.key == pygame.K_RIGHT:
                purple_ship.control(-steps, 0)
            if event.key == pygame.K_UP:
                bullets_group.add(purple_ship.create_bullet())
                bullets_group.add(purple_ship.sec_bullet())
            if event.key == pygame.K_SPACE:
                purple_ship.attack()

    if player.x >= 400:
        player.x = 400
    if player.x <= 0:
        player.x = 1
    if player.y >= 500:
        player.y = 500
    if player.y <= 50:
        player.y = 50
    player.x += moveX
    player.y += moveY
    screen.fill(BLACK)
    screen.blit(back_round, (0, 0))
    for a in range(len(asteroid_list)):
        pygame.draw.circle(screen, GRAY78, asteroid_list[a], 1)
        asteroid_list[a][1] += 1
        asteroid_list[a][0] += 8
        if asteroid_list[a][0] >= 950:
            Ay = random.randrange(228, 340)
            asteroid_list[a][1] = Ay
            Ax = random.randrange(40, 50)
            asteroid_list[a][0] = Ax

    for i in range(len(star_list)):
        pygame.draw.circle(screen, GRAY3, star_list[i], 1)
        star_list[i][1] -= 0
        star_list[i][0] += 0
        if star_list[i][0] > 10:
            y = random.randrange(68, 510)
            star_list[i][1] = y
            x = random.randrange(68, 1030)
            star_list[i][0] = x

    planet_group.update()
    all_sprites.draw(screen)
    bullet_group.draw(screen)
    all_sprites.update()
    cockpit_group.update()
    character_group.update()
    menu_group.update()
    screen.blit(sample_rect_sur, sample_rect)
    sample_rect_sur.fill(MIDNIGHTBLUE)
    asteroid_group.update()
    all_sprites.update()
    bullet_group.update()

    if net_menu_window is True:
        screen.blit(net_menu_sprite.sur, (100, 100))
        screen.blit(net_menu_sprite.dream_logo, (700, 100))
        screen.blit(net_menu_sprite.dream_title, (150, 150))

    if interior_window is True:
        screen.blit(int_window, int_window_rect)
        screen.blit(net_menu_sprite.dream_logo, (700, 100))
    if radar_screen_value is True:
        screen.blit(radar_screen, radar_screen_rect)
    start_group.update()
    pygame.display.update()
    clock.tick(FPS)

    if battle is True:
        screen.blit(battle_screen, (280, 280))
        battle_screen.fill(BLACK)
        battle_screen.blit(back_round, (0, 0))
        back_round.fill(BLACK)
        bullets_group.draw(battle_screen)
        battle_sprites.update()
        cockpit_group.update()
        character_group.update()
        menu_group.update()

        draw_group.update()
        for a in range(len(asteroid_list)):
            pygame.draw.circle(screen, GRAY78, asteroid_list[a], 1)
            asteroid_list[a][1] += 1
            asteroid_list[a][0] += 8
            if asteroid_list[a][0] >= 950:
                Ay = random.randrange(228, 340)
                asteroid_list[a][1] = Ay
                Ax = random.randrange(40, 50)
                asteroid_list[a][0] = Ax
