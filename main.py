import pygame
import random
import sys
from Colors import *
from PIL import Image
pygame.init()
pygame.font.init()
cell_pxl_size = 70
cell_count = 10
screen_width = 1200
screen_height = 700
FPS = 70
moveX, moveY = 0, 0
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("FREE_YanSan")
clock = pygame.time.Clock()
back_round_im = pygame.image.load("images/templates/Stars.png")
back_round = pygame.Surface((800, 400))
back_round.blit(back_round_im, (0, 0))
music = pygame.mixer.Sound("images/sounds/monkeys wedding_low.wav")
laser = pygame.mixer.Sound("images/sounds/laser_SE_hit.wav")
shoot_laser = pygame.mixer.Sound("images/sounds/laser_SE_shoot.wav")
dream_logo = pygame.image.load("images/templates/Dream_Logo.png")
dream_logo_2 = pygame.transform.scale(dream_logo, (40, 40))
LLC_icon = pygame.image.load("images/templates/Dream_green_title.png")
LLC_icon_micro = pygame.transform.scale(LLC_icon, (200, 40))
game_font = pygame.font.Font("freesansbold.ttf", 42)
game_font_2 = pygame.font.Font("freesansbold.ttf", 10)
mono_font = pygame.font.SysFont("monospace", 36)
pygame.mouse.set_visible(True)
x = 0
y = 0
# music.play(10)
sample_rect = pygame.Rect(15, 460, 50, 50)
sample_rect_sur = pygame.Surface((50, 50))
hit_sample_rect = pygame.draw.rect(screen, GRAY76, sample_rect)
hit_sur = pygame.Surface((50, 50))
drone_pos = []
drone_rect = []
steps = 6
motionX = 2
motionY = 1
points = 12
im = Image.open("images/ships/10.png")
angle = 235
out = im.rotate(angle)
out.save('images/ships/10_1.png')
num = []

class Pilot(pygame.sprite.Sprite):
    def __init__(self):
        super(Pilot, self).__init__()
        self.x = pygame.mouse.get_pos()[0]
        self.y = pygame.mouse.get_pos()[1]
        self.image = pygame.image.load("images/templates/crosshairs_blue.png")
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def update(self):
        self.render()

    def create_bullet(self):
        return Bullets(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

    def sec_bul(self):
        return Bullets(pygame.mouse.get_pos()[0]+ 10, pygame.mouse.get_pos()[1]+ 10)

    def render(self):
        screen.blit(self.image, (pygame.mouse.get_pos()[0] - 40, pygame.mouse.get_pos()[1] - 10))


class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = pygame.mouse.get_pos()[0]
        self.y = pygame.mouse.get_pos()[1]
        self.image = pygame.Surface((2, 5))
        self.im1 = pygame.Surface((2, 5))
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
        if self.rect.colliderect(drone):
            laser.play()
            self.kill()
            screen.blit(hit_sur, hit_sample_rect)
            drone.rect.y = random.randint(80, 250)
            drone.rect.x = 0

    def update(self):
        self.rect.y -= 15
        self.rect.x -= 0
        self.rect_2.y -= 15
        self.rect_2.x -= 0
        self.image = self.im1
        self.image = self.image
        if self.rect.y <= pygame.mouse.get_pos()[1] - 40:
            self.kill()
        if self.rect_2.y <= pygame.mouse.get_pos()[1] - 40:
            self.kill()

        self.checkCollision()


class Cockpit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/templates/Cockpit_Spaceship.png")
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 150

    def update(self):
        self.render()
        self.move()

    def render(self):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        if self.x >= 1:
             self.x = motionX * -1
        if self.y >= 1:
             self.y = motionY * -1
        self.y = 150
        self.y += motionY
        self.x += motionX


class Drone(pygame.sprite.Sprite):
    def __init__(self):
        super(Drone, self).__init__()
        self.image = pygame.image.load("images/ships/10_1.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 30

    def update(self):
        self.render()
        self.move()
        self.clone(0, 100)

    def clone(self, copyX, copyY):
        selfX = copyX
        selfY = copyY
        im_clone = self.image
        copyX += 1
        copyY += 1
        screen.blit(im_clone, (selfX, selfY))


    def move(self):
        self.rect.y += motionY
        self.rect.x += motionX
        if self.rect.x > 550:
            self.rect.x += 6
        if self.rect.y >= 600:
            self.rect.y += 10
        if self.rect.x >= 1200:
            self.rect.x = 0
            self.rect.y = 30

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
        self.title_text = str("----FREE-------(Y//:YanSan)----")
        self.title_surface = mono_font.render(self.title_text, True, WHITE)
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
        self.dream_title = pygame.image.load("images/templates/Dream_green_title.png")

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


class LeftToolbar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 50
        self.sur = pygame.Surface((200, 400))
        self.rect = self.sur.get_rect()
        self.sur.fill(GRAY7)
        self.white_border = pygame.Rect(self.x, self.y, 202, 402)

    def update(self):
        self.render()

    def render(self):
        pygame.draw.rect(screen, WHITE, self.white_border)
        screen.blit(self.sur, (self.x, self.y))
        self.sur.fill(GRAY7)


class YanSan_Window(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 998
        self.y = 50
        self.sur = pygame.Surface((200, 400))
        self.rect = self.sur.get_rect()
        self.sur.fill(GRAY7)
        self.white_border = pygame.Rect(self.x, self.y, 202, 402)
        self.icon_rect = pygame.Rect(60, 360, 20, 20)
        self.icon_box_sur = pygame.Surface((80, 80))
        self.icon_box_sur.fill(BLACK)
        self.blue_bor_icon = pygame.Surface((84, 84))
        self.blue_bor_icon.fill(CADETBLUE)
        self.icon_image = pygame.image.load("images/player/Yan_San_icon_blueglow.png")
        self.icon_rect = self.icon_image.get_rect()
        self.textHeader = str("YanSan Driver Search Results:::")
        self.textY = str("'Y'..DRIVE.. ___ Artificial Intelligence ___")
        self.textX = str("'X'..DRIVE.. ___ Artificial Intelligence ___")
        self.textZ = str("'Z'..DRIVE.. ___ Artificial Intelligence ___")
        self.textHeader_sur = game_font_2.render(self.textHeader, True, WHITE)
        self.textY_sur = game_font_2.render(self.textY, True, WHITE)
        self.textX_sur = game_font_2.render(self.textX, True, WHITE)
        self.textZ_sur = game_font_2.render(self.textZ, True, WHITE)
        self.textHeader_im = self.textHeader_sur
        self.textY_im = self.textY_sur
        self.textX_im = self.textX_sur
        self.textZ_im = self.textZ_sur
        self.dream_logo_2 = dream_logo_2

    def update(self):
        self.render()

    def render(self):
        pygame.draw.rect(screen, WHITE, self.white_border)
        self.sur.blit(self.textHeader_sur, (25, 10))
        self.sur.blit(self.textY_sur, (20, 115))
        self.sur.blit(self.textX_sur, (20, 215))
        self.sur.blit(self.textZ_sur, (20, 315))
        self.sur.blit(self.blue_bor_icon, (10, 28))
        self.sur.blit(self.blue_bor_icon, (10, 128))
        self.sur.blit(self.blue_bor_icon, (10, 228))
        self.sur.blit(self.icon_box_sur, (10, 230))
        self.sur.blit(self.icon_box_sur, (10, 130))
        self.sur.blit(self.icon_box_sur, (10, 30))
        self.sur.blit(self.icon_image, (10, 30))
        self.sur.blit(self.dream_logo_2, (160, 70))
        self.sur.blit(self.dream_logo_2, (160, 170))
        self.sur.blit(self.dream_logo_2, (160, 270))
        screen.blit(self.sur, (self.x, self.y))
        self.sur.fill(GRAY7)


class Menu_Box1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 450
        self.rect = pygame.Rect(self.x, self.y, 200, 200)
        self.white_border = pygame.Rect(self.x - 1, self.y - 1, 202, 202)

    def score(self):
        score_text = str(points)
        score_surface = game_font.render(score_text, True, WHITE)
        score_x = 60
        score_y = 100
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        screen.blit(score_surface, score_rect)

    def update(self):
        self.render()

    def render(self):
        pygame.draw.rect(screen, GRAY7, self.white_border)
        pygame.draw.rect(screen, BLACK, self.rect)
        self.score()


class Menu_box2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 1000
        self.y = 450
        self.rect = pygame.Rect(self.x, self.y, 200, 200)
        self.white_border = pygame.Rect(self.x -1, self.y -1, 202, 202)

    def update(self):
        self.render()

    def render(self):
        pygame.draw.rect(screen, WHITE, self.white_border)
        pygame.draw.rect(screen, BLACK, self.rect)


class Main_Menu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 200
        self.y = 200
        self.rectX = 200
        self.rectY = 200
        self.rect = pygame.Rect(self.x, self.y, self.rectX, self.rectY)
        self.Wrect = pygame.Rect(self.x - 1, self.y - 1, self.rectX - 2, self.rect.y - 2)

    def update(self):
        self.render()
        self.copy1(200, 50)
        self.copy2(400, 50)
        self.copy3(600, 50)
        self.copy4(800, 50)
        self.copy5(200, 250)
        self.copy6(400, 250)
        self.copy7(600, 250)
        self.copy8(800, 250)
        self.copy9(200, 450)
        self.copy10(400, 450)
        self.copy11(600, 450)
        self.copy12(800, 450)

    def copy1(self, copyX, copyY):
        self.rectX = copyX
        self.rectY = copyY
        self.rect1 = pygame.Rect(copyX, copyY, self.x, self.y)
        self.Wrect1 = pygame.Rect(copyX - 2, copyY - 2, self.x - 1, self.y - 1)
        pygame.draw.rect(screen, GRAY7, self.Wrect1)
        pygame.draw.rect(screen, BLACK, self.rect1)

    def copy2(self, copyX, copyY):
        self.rectX = copyX
        self.rectY = copyY
        self.rect2 = pygame.Rect(copyX, copyY, self.x, self.y)
        self.Wrect2 = pygame.Rect(copyX - 2, copyY - 2, self.x - 1, self.y - 1)
        pygame.draw.rect(screen, GRAY7, self.Wrect2)
        pygame.draw.rect(screen, BLACK, self.rect2)

    def copy3(self, copyX, copyY):
        self.rectX = copyX
        self.rectY = copyY
        self.rect3 = pygame.Rect(copyX, copyY, self.x, self.y)
        self.Wrect3 = pygame.Rect(copyX - 2, copyY - 2, self.x - 1, self.y - 1)
        pygame.draw.rect(screen, GRAY7, self.Wrect3)
        pygame.draw.rect(screen, BLACK, self.rect3)

    def copy4(self, copyX, copyY):
        self.rectX = copyX
        self.rectY = copyY
        self.rect4 = pygame.Rect(copyX, copyY, self.x, self.y)
        self.Wrect4 = pygame.Rect(copyX - 2, copyY - 2, self.x - 1, self.y - 1)
        pygame.draw.rect(screen, GRAY7, self.Wrect4)
        pygame.draw.rect(screen, BLACK, self.rect4)

    def copy5(self, copyX, copyY):
        self.rectX = copyX
        self.rectY = copyY
        self.rect5 = pygame.Rect(copyX, copyY, self.x, self.y)
        self.Wrect5 = pygame.Rect(copyX - 2, copyY - 2, self.x - 1, self.y - 1)
        pygame.draw.rect(screen, GRAY7, self.Wrect5)
        pygame.draw.rect(screen, BLACK, self.rect5)

    def copy6(self, copyX, copyY):
        self.rectX = copyX
        self.rectY = copyY
        self.rect6 = pygame.Rect(copyX, copyY, self.x, self.y)
        self.Wrect6 = pygame.Rect(copyX - 2, copyY - 2, self.x - 1, self.y - 1)
        pygame.draw.rect(screen, GRAY7, self.Wrect6)
        pygame.draw.rect(screen, BLACK, self.rect6)

    def copy7(self, copyX, copyY):
        self.rectX = copyX
        self.rectY = copyY
        self.rect7 = pygame.Rect(copyX, copyY, self.x, self.y)
        self.Wrect7 = pygame.Rect(copyX - 2, copyY - 2, self.x - 1, self.y - 1)
        pygame.draw.rect(screen, GRAY7, self.Wrect7)
        pygame.draw.rect(screen, BLACK, self.rect7)

    def copy8(self, copyX, copyY):
        self.rectX = copyX
        self.rectY = copyY
        self.rect8 = pygame.Rect(copyX, copyY, self.x, self.y)
        self.Wrect8 = pygame.Rect(copyX - 2, copyY - 2, self.x - 1, self.y - 1)
        pygame.draw.rect(screen, GRAY7, self.Wrect8)
        pygame.draw.rect(screen, BLACK, self.rect8)

    def copy9(self, copyX, copyY):
        self.rectX = copyX
        self.rectY = copyY
        self.rect9 = pygame.Rect(copyX, copyY, self.x, self.y)
        self.Wrect9 = pygame.Rect(copyX - 2, copyY - 2, self.x - 1, self.y - 1)
        pygame.draw.rect(screen, GRAY7, self.Wrect9)
        pygame.draw.rect(screen, BLACK, self.rect9)

    def copy10(self, copyX, copyY):
        self.rectX = copyX
        self.rectY = copyY
        self.rect10 = pygame.Rect(copyX, copyY, self.x, self.y)
        self.Wrect10 = pygame.Rect(copyX - 2, copyY - 2, self.x - 1, self.y - 1)
        pygame.draw.rect(screen, GRAY7, self.Wrect10)
        pygame.draw.rect(screen, BLACK, self.rect10)

    def copy11(self, copyX, copyY):
        self.rectX = copyX
        self.rectY = copyY
        self.rect11 = pygame.Rect(copyX, copyY, self.x, self.y)
        self.Wrect11 = pygame.Rect(copyX - 2, copyY - 2, self.x - 1, self.y - 1)
        pygame.draw.rect(screen, GRAY7, self.Wrect11)
        pygame.draw.rect(screen, BLACK, self.rect11)

    def copy12(self, copyX, copyY):
        self.rectX = copyX
        self.rectY = copyY
        self.rect12 = pygame.Rect(copyX, copyY, self.x, self.y)
        self.Wrect12 = pygame.Rect(copyX - 2, copyY - 2, self.x - 1, self.y - 1)
        pygame.draw.rect(screen, GRAY7, self.Wrect12)
        pygame.draw.rect(screen, BLACK, self.rect12)


    def render(self):
        pygame.draw.rect(screen, GRAY7, self.Wrect)
        pygame.draw.rect(screen, BLACK, self.rect)


class Photon_Charger_Window(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 450
        self.image = pygame.image.load("images/planets/blue_bolt.png")
        self.title_text = str("PHOTON CHARGER")
        self.rect = pygame.Rect(self.x, self.y, 150, 150)
        self.white_border = pygame.Surface((152, 152))
        self.white_border_rect = self.white_border.get_rect()
        self.charger_label = game_font_2.render(self.title_text, True, GRAY76)
        self.charger_box = pygame.Surface((150, 150))
        self.charger_box_rect = self.charger_box.get_rect()

    def update(self):
        self.render()

    def render(self):
        screen.blit(self.white_border, (self.x, self.y))
        self.white_border.fill(WHITE)
        screen.blit(self.charger_box, (self.x, self.y))
        self.charger_box.fill(BLACK)
        self.charger_box.blit(self.image, self.rect)
        self.charger_box.blit(self.charger_label, (0, 120))


class Alien_right(pygame.sprite.Sprite):
    def __init__(self):
        super(Alien_right, self).__init__()
        self.x = 850
        self.y = 400
        self.image = pygame.image.load("images/player/profile_allien_2.png")
        self.rect = self.image.get_rect()

    def update(self):
        self.render()
        self.move()

    def move(self):
        if self.x >= 851:
            self.x = motionX * -1
        if self.y >= 301:
            self.y = motionY * -1
        self.y = 400
        self.x = 850
        self.y += motionY
        self.x += motionX

    def render(self):
        screen.blit(self.image, (self.x, self.y))


class Alien_left(pygame.sprite.Sprite):
    def __init__(self):
        super(Alien_left, self).__init__()
        self.x = 40
        self.y = 700
        self.image = pygame.image.load("images/player/profile_allien.png")
        self.rect = self.image.get_rect()

    def update(self):
        self.render()
        self.move()

    def move(self):
        if self.x >= 41:
            self.x = motionX * -1
        if self.y >= 301:
            self.y = motionY * -1
        self.x = 40
        self.y = 400
        self.y += motionY
        self.x += motionX

    def render(self):
        screen.blit(self.image, (self.x, self.y))


class Planet_larger(pygame.sprite.Sprite):
    def __init__(self):
        self.x = 734
        self.y = 222
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
        self.x = 0
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
        self.rect.y += motionY
        self.rect.x += motionX

    def update(self):
        self.spin()
        self.move()
        self.render()

    def spin(self):
        self.index += 1
        if self.index >= 40:
            self.index = 0
        self.image = self.images[self.index]
        if self.rect.x >= 1400 or self.rect.y >= 950:
            self.rect.x = random.randint(-50, 0)
            self.rect.y = random.randint(20, 360)

    def render(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))


class Red_ship(pygame.sprite.Sprite):
        def __init__(self):
            super(Red_ship, self).__init__()
            self.image = pygame.image.load("images/ships/SpaceHero/red_ship_micro.png")
            self.im2 = pygame.image.load("images/ships/SpaceHero/red_ship_micro_hit.png")
            self.rect = self.image.get_rect()
            self.rect.x = 250
            self.rect.y = 325
            self.movex = 0
            self.movey = 0

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
            self.movex = 0
            self.movey = 0

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
        self.movex = 0
        self.movey = 0

    def move(self):
        self.rect.x += 1
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
        self.movex = 0
        self.movey = 0

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
        self.image = pygame.image.load("images/templates/cockpit.blue.jpg")
        self.sur = pygame.Surface((1200, 800))
        self.rect = self.sur.get_rect()
        self.rect.x = 1200
        self.rect.y = 800
        self.sur.blit(self.image, (160, 0))

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
        YanSan_window.render()
        pygame.display.update()

    def button(self):
        click = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        posX = pos[0]
        posY = pos[1]

        if 190 > posX > 10 and 230 > posY > 180:
            pygame.draw.rect(self.sur, SLATEGRAY3, (80, 175, 160, 50))
            if click[0] == 1:
                self.kill()
                pygame.mouse.set_visible(False)
            else:
                pygame.draw.rect(self.sur, BLACK, (80, 175, 160, 50))
        if 180 > posX > 10 and 275 > posY > 230:
            pygame.draw.rect(self.sur, SLATEGRAY3, (80, 230, 160, 50))
            if click[0] == 1:
                pygame.quit()
                sys.exit()
            else:
                pygame.draw.rect(self.sur, BLACK, (80, 230, 160, 50))

    def RunGame(self):
        self.sur.fill(BLACK)


class Main:
    def __init__(self):
        self.update()
        clock.tick(FPS)

    def update(self):
        screen.fill(BLACK)
        screen.blit(back_round, (0, 0))
        menu_group.update()
        self.statments()
        planet_group.update()
        asteroid_group.update()
        bullet_group.draw(screen)
        all_sprites.update()
        character_group.update()
        screen.blit(sample_rect_sur, sample_rect)
        sample_rect_sur.fill(MIDNIGHTBLUE)
        bullet_group.update()
        start_group.update()
        if battle is True:
            screen.blit(battle_screen, (280, 280))
            battle_screen.fill(BLACK)
            battle_screen.blit(back_round, (0, 0))
            back_round.fill(BLACK)
            bullets_group.draw(battle_screen)
            battle_sprites.update()
            character_group.update()
            menu_group.update()

            draw_group.update()

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

            for a in range(len(asteroid_list)):
                pygame.draw.circle(screen, GRAY78, asteroid_list[a], 1)
                asteroid_list[a][1] += 1
                asteroid_list[a][0] += 8
                if asteroid_list[a][0] >= 950:
                    Ay = random.randrange(228, 340)
                    asteroid_list[a][1] = Ay
                    Ax = random.randrange(40, 50)
                    asteroid_list[a][0] = Ax
        if net_menu_window is True:
            screen.blit(net_menu_sprite.sur, (100, 100))
            screen.blit(net_menu_sprite.dream_logo, (700, 100))
            screen.blit(net_menu_sprite.dream_title, (150, 150))
        if interior_window is True:
            screen.blit(int_window, int_window_rect)
            screen.blit(net_menu_sprite.dream_logo, (700, 100))
        if radar_screen_value is True:
            screen.blit(radar_screen, radar_screen_rect)

    def statments(self):
        for a in range(len(asteroid_list)):
            pygame.draw.circle(screen, GRAY78, asteroid_list[a], 1)
            asteroid_list[a][1] += motionY
            asteroid_list[a][0] += motionX
            if asteroid_list[a][0] >= 950:
                Ay = random.randrange(28, 240)
                asteroid_list[a][1] = Ay
                Ax = random.randrange(40, 50)
                asteroid_list[a][0] = Ax
        #for i in range(len(star_list)):
        #    pygame.draw.circle(screen, GRAY3, star_list[i], 1)
        #    star_list[i][1] -= 0
        ##    star_list[i][0] += 0
         #   if star_list[i][0] > 10:
         #       y = random.randrange(68, 510)
         #       star_list[i][1] = y
          #      x = random.randrange(68, 1030)
           #     star_list[i][0] = x


x = 1010
y = 520
drone = Drone()
start_group = pygame.sprite.Group()
start_up = Start_Up()
start_group.add(start_up)
LeftToolbar = LeftToolbar()
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
YanSan_window = YanSan_Window()
Menu_box2 = Menu_box2()
photon_charger_window = Photon_Charger_Window()
Main_Menu = Main_Menu()
Menu_Box1 = Menu_Box1()
alien_left = Alien_left()
alien_right = Alien_right()
planet_larger = Planet_larger()
planet_yellow = Planet_yellow()
game_title = Title_text()
purple_fighter = Purple_fighter()
blue_bolt = pygame.image.load("images/planets/blue_bolt.png")
blue_bolt_rect = pygame.Rect(10, 10, 400, 301)
new_icon = pygame.image.load("images/player/Dream_Logic_new_icon.png")
new_icon_rect = pygame.Rect(230, 450, 60, 60)
radar_screen = pygame.image.load("images/templates/opohgknlov.jpeg")
radar_screen_rect = pygame.Rect(0, 0, 1051, 515)
menu_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
planet_group = pygame.sprite.Group()
character_group = pygame.sprite.Group()
asteroid_group = pygame.sprite.Group()
net_menu = pygame.sprite.Group()
net_menu_sprite = Network_Map_Window()
net_menu.add(net_menu_sprite)
menu_group.add(header, game_title, Main_Menu, Menu_Box1)
menu_group.add(Menu_box2, photon_charger_window, YanSan_window, purple_fighter, LeftToolbar)
planet_group.add(planet_larger, planet_yellow)
character_group.add(alien_left, alien_right)
asteroid_group.add(asteroid, drone)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
star_list = []
asteroid_list = []
for i in range(760):
    x = random.randrange(140, 1000)
    y = random.randrange(14, 36)
    star_list.append([x, y])
for a in range(80):
    Ax = random.randrange(100, 950)
    Ay = random.randrange(228, 340)
    asteroid_list.append([Ax, Ay])
game_time = pygame.time.get_ticks()
interior_layout = pygame.image.load("images/templates/interior_edit_600x450.jpg").convert()
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
                WHITE = RED1
                RED1 = BLUE
                BLUE = WHEAT1
                WHEAT1 = WHITE
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
                purple_ship.control(steps, 0)
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
    Main()
    pygame.display.update()
