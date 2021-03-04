import pygame
import random
import sys
from Colors import *
from PIL import Image

# Init setup
pygame.init()
pygame.font.init()
cell_pxl_size = 70
cell_count = 10
screen_width = 1200
screen_height = 700
FPS = 120
moveX, moveY = 0, 0
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("FREE_YanSan")
clock = pygame.time.Clock()
back_round_im = pygame.image.load("images/templates/Stars.png")
back_round = pygame.Surface((800, 400))
back_round.blit(back_round_im, (0, 0))
# Audio Variables
music = pygame.mixer.Sound("images/sounds/monkeys wedding_low.wav")
laser = pygame.mixer.Sound("images/sounds/laser_SE_hit.wav")
shoot_laser = pygame.mixer.Sound("images/sounds/laser_SE_shoot.wav")
# music.play(10)


# Game Font
game_font = pygame.font.Font("freesansbold.ttf", 42)
game_font_10 = pygame.font.Font("freesansbold.ttf", 10)
game_font_18 = pygame.font.Font("freesansbold.ttf", 18)
mono_font = pygame.font.SysFont("monospace", 36)

# rotate image
im = Image.open("images/ships/10.png")
angle = 45
out = im.rotate(angle)
out.save("images/ships/10.1.png")

# rotate image
im = Image.open("images/ships/SpaceHero/red_ship_micro.png")
angle = 180
out = im.rotate(angle)
out.save("images/ships/SpaceHero/red_ship_micro2.png")

# other add-ins
blue_bolt = pygame.image.load("images/planets/blue_bolt.png")
blue_bolt_rect = pygame.Rect(10, 10, 400, 301)
new_icon = pygame.image.load("images/player/Dream_Logic_new_icon.png")
new_icon_rect = pygame.Rect(230, 450, 60, 60)
dream_logo = pygame.image.load("images/templates/Dream_Logo.png")
dream_logo_2 = pygame.transform.scale(dream_logo, (40, 40))
LLC_icon = pygame.image.load("images/templates/Dream_green_title.png")
LLC_icon_micro = pygame.transform.scale(LLC_icon, (200, 40))
score: int = 0
curmov = 200

# Pop-up windows
radar_screen = pygame.image.load("images/templates/opohgknlov.jpeg")
radar_screen_rect = pygame.Rect(0, 0, 1051, 515)
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
pygame.mouse.set_visible(True)
voice1 = pygame.mixer.Sound("Voicetracks/WC-1.mp3")
voice2 = pygame.mixer.Sound("Voicetracks/WC-17.mp3")


class Pilot(pygame.sprite.Sprite):
    def __init__(self):
        super(Pilot, self).__init__()
        self.x = pygame.mouse.get_pos()[0]
        self.y = pygame.mouse.get_pos()[1]
        self.image = pygame.image.load("images/templates/crosshairs_blue.png")
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def update(self):
        self.render()

    def create_bullet(self):
        return Bullets(pygame.mouse.get_pos()[0] + 35, pygame.mouse.get_pos()[1] + 160)

    def sec_bul(self):
        return Bullets(pygame.mouse.get_pos()[0] + 65, pygame.mouse.get_pos()[1] + 160)

    def render(self):
        screen.blit(self.image, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))


class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = pygame.mouse.get_pos()[0]
        self.y = pygame.mouse.get_pos()[1]
        self.image = pygame.Surface((2, 25))
        self.im1 = pygame.Surface((2, 25))
        self.image.fill(WHITE)
        self.im1.fill(WHITE)
        self.rect = self.image.get_rect(center=(int(x), int(y)))
        self.rect_2 = self.image.get_rect(center=(int(x), int(y)))

    def checkCollision(self, score):
        if self.rect.colliderect(grey_ship.create_clone()):
            laser.play()
            self.kill()

        if self.rect.colliderect(grey_ship):
            laser.play()
            grey_ship.rect.x = 0
            grey_ship.rect.y = random.randint(80, 250)
            self.kill()

        if self.rect.colliderect(purple_ship):
            laser.play()
            purple_ship.rect.x = 0
            purple_ship.rect.y = random.randint(80, 250)
            self.kill()

        if self.rect.colliderect(asteroid):
            laser.play()
            self.kill()

            asteroid.rect.y = random.randint(80, 250)
            asteroid.rect.x = 0
        if self.rect.colliderect(drone):
            laser.play()
            self.kill()

            drone.rect.y = random.randint(80, 250)
            drone.rect.x = 0
        if self.rect.colliderect(yellow_ship):
            laser.play()
            self.kill()

            yellow_ship.rect.y = random.randint(80, 250)
            yellow_ship.rect.x = 0
        if self.rect.colliderect(red_ship):
            laser.play()
            self.kill()

            red_ship.rect.y = random.randint(80, 250)
            red_ship.rect.x = 0

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
        self.checkCollision(score)


class Drone(pygame.sprite.Sprite):
    def __init__(self):
        super(Drone, self).__init__()
        self.image = pygame.image.load("images/ships/10.1.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self):
        self.render()
        self.move()

    def move(self):
        self.rect.x += 4
        self.rect.y += 1
        if self.rect.x > 400:
            self.rect.x += 3
            self.rect.y += 2
        if self.rect.x > 1200:
            self.rect.x = 0
            self.rect.y = 0

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
        self.white_border = pygame.Surface((200, 400))
        self.white_border.fill(WHITE)
        self.boxes()

    def boxes(self):
        self.box1 = pygame.Surface((200, 50))
        self.box1.fill(GRAY5)
        self.box2 = pygame.Surface((50, 300))
        self.box2.fill(GRAY5)
        self.box3 = pygame.Surface((125, 35))
        self.box3.fill(GRAY26)
        self.box4 = pygame.Surface((125, 35))
        self.box4.fill(GRAY26)
        self.box5 = pygame.Surface((125, 35))
        self.box5.fill(GRAY26)
        self.box6 = pygame.Surface((125, 35))
        self.box6.fill(GRAY26)
        self.box7 = pygame.Surface((125, 35))
        self.box7.fill(GRAY26)
        self.box8 = pygame.Surface((125, 35))
        self.box8.fill(GRAY26)
        self.sur.blit(self.box1, (25, 50))
        self.sur.blit(self.box2, (25, 100))
        self.sur.blit(self.box3, (75, 100))
        self.sur.blit(self.box4, (75, 150))
        self.sur.blit(self.box5, (75, 200))
        self.sur.blit(self.box6, (75, 250))
        self.sur.blit(self.box7, (75, 300))
        self.sur.blit(self.box8, (75, 350))

    def BattleKey(self):
        self.sur.blit(red_ship.image, (85, 155))
        self.sur.blit(yellow_ship.image, (84, 24))
        self.sur.blit(purple_ship.image, (80, 202))
        self.sur.blit(grey_ship.image, (85, 104))

    def render(self):
        self.white_border.blit(self.sur, (2, 2))
        screen.blit(self.white_border, (self.x, self.y))

    def update(self):
        self.BattleKey()
        self.render()


class YanSan_Window(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 998
        self.y = 50

    def window_setup(self):
        self.white_border = pygame.Surface((200, 400))
        self.white_border.fill(WHITE)
        self.sur = pygame.Surface((200, 400))
        self.rect = self.sur.get_rect()
        self.sur.fill(GRAY7)

    def YanSan_logo(self):
        self.icon_image = pygame.image.load("images/player/Yan_San_icon_blueglow.png")
        self.icon_rect = pygame.Rect(60, 360, 20, 20)
        self.dream_logo_2 = dream_logo_2
        self.blue_bor_icon = pygame.Surface((84, 84))
        self.blue_bor_icon.fill(CADETBLUE)
        self.icon_box_sur = pygame.Surface((80, 80))
        self.icon_box_sur.fill(BLACK)

    def header(self):
        self.textHeader = str("YanSan Driver Search Results:::")
        self.textHeader_sur = game_font_10.render(self.textHeader, True, WHITE)

    def Y_drive(self):
        self.textY = str("'Y'..DRIVE.. ___ Artificial Intelligence ___")
        self.textY_sur = game_font_10.render(self.textY, True, WHITE)

    def X_drive(self):
        self.textX = str("'X'..DRIVE.. ___ Artificial Intelligence ___")
        self.textX_sur = game_font_10.render(self.textX, True, WHITE)

    def Z_drive(self):
        self.textZ = str("'Z'..DRIVE.. ___ Artificial Intelligence ___")
        self.textZ_sur = game_font_10.render(self.textZ, True, WHITE)

    def render(self):
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
        self.sur.blit(self.icon_image, (10, 230))
        self.sur.blit(self.icon_image, (10, 130))
        self.sur.blit(self.icon_image, (10, 30))
        self.sur.blit(self.dream_logo_2, (160, 70))
        self.sur.blit(self.dream_logo_2, (160, 170))
        self.sur.blit(self.dream_logo_2, (160, 270))
        screen.blit(self.white_border, (1000, 50))
        screen.blit(self.sur, (self.x, self.y))

    def update(self):
        self.window_setup()
        self.header()
        self.X_drive()
        self.Y_drive()
        self.Z_drive()
        self.YanSan_logo()
        self.render()


class Menu_Box1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 10
        self.y = 60
        self.x = 0
        self.y = 450
        self.sur = pygame.Surface((200, 200))
        self.sur.fill(BLACK)
        self.white_border = pygame.Rect(self.x - 1, self.y - 1, 202, 202)

    def update(self):
        self.render()

    def render(self):
        screen.blit(self.sur, (0, 450))
        pygame.draw.rect(self.sur, GRAY7, self.white_border)


class PlayerInfobox(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 200
        self.y = 400
        self.sur = pygame.Surface((self.x, self.y))
        self.Bsur = pygame.Surface((self.x, self.y))
        self.playership()
        self.score(0)

    def update(self):
        self.render()

    def playership(self):
        self.image = pygame.image.load("images/ships/13B.png")
        self.rect = self.image.get_rect()

    def overheat(self):
        self.im2 = pygame.image.load("images/ships/13B_overheat.png")
        self.im2rect = self.im2.get_rect()
        self.sur. blit(self.im2, (15, 50))

    def score(self, Ascore):
        self.text_sur = game_font_18.render("_Asteriods_Kills_" + str(Ascore), True, WHITE)

    def render(self):
        screen.blit(self.Bsur, (998, 450))
        self.Bsur.fill(WHITE)
        self.Bsur.blit(self.sur, (1, 1))
        self.sur.blit(self.image, (15, 50))
        self.sur.blit(self.text_sur, (2, 10))


class Main_Menu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 200
        self.y = 200
        self.rectX = 200
        self.rectY = 200
        self.rect = pygame.Rect(self.x, self.y, 200, 200 - 1)
        self.white_border = pygame.Rect(self.x - 1, self.y - 1, 200 + 2, 200 + 1)
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
        self.x = 50
        self.y = 60
        self.x = 0
        self.y = 450
        self.image = pygame.image.load("images/planets/blue_bolt.png")
        self.title_text = str("PHOTON CHARGER")
        self.rect = pygame.Rect(self.x, self.y, 150, 150)
        self.white_border = pygame.Surface((152, 152))
        self.white_border_rect = self.white_border.get_rect()
        self.charger_label = game_font_10.render(self.title_text, True, GRAY76)
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
        self.charger_box.blit(self.charger_label, (20, 120))
        self.charger_box.blit(self.charger_label, (0, 120))


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
            self.rect.x = random.randint(0, 60)
            self.rect.y = random.randint(20, 360)

    def render(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))


class Red_ship(pygame.sprite.Sprite):
    def __init__(self):
        super(Red_ship, self).__init__()
        self.image = pygame.image.load("images/ships/SpaceHero/red_ship_micro2.png")
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 200

    def move(self):
        self.rect.x += 3
        self.rect.y += 1
        if self.rect.x > 800:
            self.rect.x -= 5
            self.rect.y += 10
        if self.rect.y >= 620:
            self.rect.y = 620

    def attack(self):
        self.create_bullet()
        self.sec_bullet()

    def render(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        self.move()

    def create_bullet(self):
        return Enemy_fire(self.rect.x, self.rect.y)

    def sec_bullet(self):
        return Enemy_fire(self.rect.x + 22, self.rect.y)

    def update(self):
        self.render()


class Enemy_fire(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Enemy_fire, self).__init__()
        self.x = x
        self.y = y
        self.image = pygame.Surface((1, 1))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=(int(x), int(y)))

    def update(self):
        self.rect.y += 1
        self.image = self.image
        if self.rect.y >= 800:
            self.kill()
        self.check_collision()

    def check_collision(self):
        if self.rect.colliderect(player):
            self.kill()


class Purple_ship(pygame.sprite.Sprite):
    def __init__(self):
        super(Purple_ship, self).__init__()
        self.image = pygame.image.load("images/ships/SpaceHero/purple_ship_micro.png")
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 200
        self.movex = 0
        self.movey = 0

    def move(self):
        self.rect.x += 4
        self.rect.y += 1
        if self.rect.x > 400:
            self.rect.x += 3
            self.rect.y += 2
        if self.rect.x > 1200:
            self.rect.x = 0
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
        self.move()

    def render(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))


class Enemy_Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Enemy_Bullets, self).__init__()
        self.image = pygame.Surface((1, 3))
        self.image.fill(WHITE)
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
        self.rect.x = 1000
        self.rect.y = 300
        self.movex = 0
        self.movey = 0

    def move(self):
        self.rect.x -= 3
        self.rect.y += 1
        if self.rect.x <= 100:
            self.rect.x = 1000
        if self.rect.x <= 0:
            self.rect.x = 1100
        if self.rect.y >= 800:
            self.rect.y = 0
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
        return Enemy_Bullets(self.rect.x + 20, self.y)

    def render(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))


class Grey_ship(pygame.sprite.Sprite):
    def __init__(self):
        super(Grey_ship, self).__init__()
        self.image = pygame.image.load("images/ships/SpaceHero/grey_ship_micro.png")
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 500
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
        screen.blit(self.image, (self.rect.x, self.rect.y))


class Start_Up(pygame.sprite.Sprite):
    def __init__(self):
        super(Start_Up, self).__init__()
        self.image = pygame.image.load("images/templates/cockpit.blue.jpg")
        self.sur = pygame.Surface((1200, 800))
        self.rect = self.sur.get_rect()
        self.rect.x = 1200
        self.rect.y = 800
        self.sur.blit(self.image, (160, 0))

    def DL_display(self):
        DLdisp = pygame.image.load("images/templates/DL-Display004.png")
        self.sur.blit(DLdisp, (560, 250))

    def text(self):
        font = mono_font
        text = font.render("FREE YanSan", True, WHITE)
        surfaceR = text.get_rect()
        surfaceR.center = (120, 50)
        self.sur.blit(text, surfaceR)
        YanSan_window.render()
        pygame.display.update()

    def icons(self):
        quit = pygame.image.load("images/icons/icons_quit_white.png")
        start = pygame.image.load("images/icons/icons_play_white.png")
        setup = pygame.image.load("images/icons/icons_setup_white2.png")
        insert = pygame.image.load("images/icons/icons_insert_white.png")
        self.sur.blit(quit, (36, 575))
        self.sur.blit(start, (20, 60))
        self.sur.blit(setup, (22, 260))
        self.sur.blit(insert, (20, 400))

    def button(self):
        click = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        posX = pos[0]
        posY = pos[1]
        start = pygame.image.load("images/icons/icons_play_white.png")
        starttxt = pygame.image.load("images/Sprites/transparentLight/transparentLight40.png")
        starton = pygame.image.load("images/icons/icons_play_gray.png")
        startoff = pygame.image.load("images/Sprites/transparentDark/transparentDark40.png")
        quiton = pygame.image.load("images/icons/icons_quit_gray.png")
        quitoff = pygame.image.load("images/icons/icons_quit_white.png")
        startgalaxy = pygame.Surface((600, 160))
        startgalaxy.fill(GRAY3)
        startgalaxy.blit(dream_logo, (200, 0))
        setup = pygame.image.load("images/icons/icons_setup_white2.png")
        setup2 = pygame.image.load("images/icons/icons_setup_gray3.png")
        backdrop = pygame.Surface((300, 500))
        backdrop.fill(GRAY3)

        if 150 > posX > 10 and 230 > posY > 120:
            self.sur.blit(startgalaxy, (150, 80))
            self.sur.blit(starttxt, (20, 160))
            self.sur.blit(starton, (16, 61))
            if click[0] == 1:
                self.kill()
        else:
            self.sur.blit(startoff, (20, 160))
            self.sur.blit(start, (20, 60))

        if 150 > posX > 10 and 350 > posY > 260:
            self.icons()
            self.sur.blit(backdrop, (150, 250))
            if click[0] == 1:
                self.sur.blit(setup2, (22, 260))
                backdrop.fill(BLACK)
                self.sur.blit(backdrop, (150, 250))

        else:
            self.sur.blit(setup, (22, 260))
            backdrop.fill(GRAY3)

        if 180 > posX > 10 and 640 > posY > 560:
            self.sur.blit(quiton, (36, 575))
            if click[0] == 1:
                pygame.quit()
                sys.exit()
        else:
            self.sur.blit(quitoff, (36, 575))

    def setup_menu(self):
        click = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        posX = pos[0]
        posY = pos[1]
        backdrop = pygame.Surface((300, 500))
        backdrop.fill(GRAY3)
        if 150 > posX > 10 and 350 > posY > 260:
            self.icons()
            if click[0] == 1:
                self.sur.blit(backdrop, (150, 250))


    def update(self):
        screen.blit(self.sur, (0, 0))
        self.DL_display()
        self.text()
        self.icons()
        self.button()
        self.setup_menu()


class World_map(pygame.sprite.Sprite):
    def __init__(self):
        super(World_map, self).__init__()
        self.sur = pygame.Surface((1200, 800))
        self.image = self.sur
        self.rect = self.sur.get_rect()
        self.sur.fill(GRAY4)
        self.movex = 0
        self.movey = 0

    def icons(self):
        quit = pygame.image.load("images/icons/icons_quit_white.png")
        start = pygame.image.load("images/icons/icons_play_white.png")
        setup = pygame.image.load("images/icons/icons_setup_white2.png")
        insert = pygame.image.load("images/icons/icons_insert_white.png")
        self.sur.blit(quit, (6, 540))

    def text(self):
        font = game_font.render("Level 1", True, BLACK)
        surfaceR = font.get_rect()
        surfaceR.center = (280, 270)
        screen.blit(font, surfaceR)

    def button(self):
        click = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        surfacefont = game_font.render("Level 1", True, ROYALBLUE2)
        surfaceR = surfacefont.get_rect()
        surfaceR.center = (280, 270)
        posX = pos[0]
        posY = pos[1]
        quiton = pygame.image.load("images/Sprites/transparentLight/transparentLight45.png")
        quitoff = pygame.image.load("images/Sprites/transparentDark/transparentDark45.png")

        if 400 > posX > 180 and 400 > posY > 200:
            screen.blit(surfacefont, surfaceR)
            if click[0] == 1:
                self.kill()
                pygame.mouse.set_visible(False)
        if 180 > posX > 10 and 630 > posY > 550:
            self.sur.blit(quiton, (36, 565))
            if click[0] == 1:
                pygame.quit()
                sys.exit()
            else:
                self.sur.blit(quitoff, (36, 565))

    def threeDship(self, TDx, TDy):
        thrDship = pygame.image.load("images/ships/Delux_ships1.2_1.png")
        self.sur.blit(thrDship, (TDx, TDy))

    def world_tiles(self):
        T1 = pygame.image.load("images/Extras/tile-01.png")
        T2 = pygame.image.load("images/Extras/tile-02.png")
        T3 = pygame.image.load("images/Extras/tile-03.png")
        T4 = pygame.image.load("images/Extras/tile-04.png")
        T5 = pygame.image.load("images/Extras/tile-05.png")
        T6 = pygame.image.load("images/Extras/tile-06.png")
        T7 = pygame.image.load("images/Extras/tile-07.png")
        self.sur.blit(T1, (4, 10))
        self.sur.blit(T2, (28, 10))
        self.sur.blit(T3, (52, 10))
        self.sur.blit(T4, (76, 10))
        self.sur.blit(T5, (100,10))
        self.sur.blit(T6, (124, 10))
        self.sur.blit(T7, (148, 10))

    def banner(self):
        bufRect= pygame.Rect(212, 20, 960, 160)
        bufSur = pygame.Surface((960, 160))
        bufSur.fill(GRAY5)
        lvl_1_text = pygame.image.load("images/Textures/trak_trim22.jpg")
        self.sur.blit(bufSur, bufRect)
        self.logo = pygame.image.load("images/templates/Dream_Logo.png")
        bufSur.blit(lvl_1_text, (100, 10))
        bufSur.blit(lvl_1_text, (300, 10))
        bufSur.blit(lvl_1_text, (500, 10))
        bufSur.blit(lvl_1_text, (700, 10))
        self.sur.blit(planet_larger.image, (900, 40))
        self.logoR = self.logo.get_rect()
        bufSur.blit(self.logo, (20, 4))
        bufSur.blit(game_title.title_surface, (80, 10))

    def lvl_1(self):
        lvl_1_box = pygame.Rect(200, 210, 190, 190)
        lvl_1_sur = pygame.Surface((190, 190))
        lvl_1 = str("Level 1")
        lvl_1_text = game_font.render(lvl_1, True, WHITE)
        text = pygame.image.load("images/Textures/trak_trim22.jpg")
        planet = pygame.image.load("images/planets/planet4.png")
        shipIcon = pygame.image.load("images/ships/Delux_ships1.2_1.png")
        lvl_1_sur.blit(text, (5, 5))
        lvl_1_sur.blit(planet, (10, 10))

        lvl_1_sur.blit(shipIcon, (0, 60))
        lvl_1_sur.blit(shipIcon, (-15, 15))
        lvl_1_sur.blit(shipIcon, (-60, 80))
        lvl_1_sur.blit(lvl_1_text, (10, 40))
        self.sur.blit(lvl_1_sur, lvl_1_box)

    def lvl_2(self):
        text = pygame.image.load("images/Textures/trak_trimplain_warning_g.jpg")
        planet = pygame.image.load("images/planets/planet17.png.")
        lvl_2_sur = pygame.Surface((190, 190))
        lvl_2 = str("Level 2")
        lvl_2_text = game_font_18.render(lvl_2, True, GRAY6)
        lvl_2_sur.blit(lvl_2_text, (5, 0))
        lvl_2_sur.blit(text, (5, 5))
        lvl_2_sur.blit(planet, (10, 10))
        lvl_2_sur.blit(lvl_2_text, (15, 55))
        lvl_2_box = pygame.Rect(400, 210, 190, 190)
        self.sur.blit(lvl_2_sur, lvl_2_box)

    def lvl_3(self):
        text = pygame.image.load("images/Textures/trak_trimplain_warning_g.jpg")
        planet = pygame.image.load("images/planets/planet6.png.")
        lvl_3 = str("Level 3")
        lvl_3_text = game_font_18.render(lvl_3, True, GRAY6)
        lvl_3_sur = pygame.Surface((190, 190))
        lvl_3_sur.blit(lvl_3_text, (5, 0))
        lvl_3_sur.blit(text, (5, 5))
        lvl_3_sur.blit(planet, (10, 10))
        lvl_3_sur.blit(lvl_3_text, (15, 55))
        lvl_3_box = pygame.Rect(600, 210, 190, 190)
        self.sur.blit(lvl_3_sur, lvl_3_box)

    def lvl_4(self):
        text = pygame.image.load("images/Textures/trak_trimplain_warning_g.jpg")
        planet = pygame.image.load("images/planets/planet2.png")
        lvl_4 = str("Level 4")
        lvl_4_text = game_font_18.render(lvl_4, True, GRAY6)
        lvl_4_sur = pygame.Surface((190, 190))
        lvl_4_sur.blit(lvl_4_text, (5, 0))
        lvl_4_sur.blit(text, (5, 5))
        lvl_4_sur.blit(planet, (10, 10))
        lvl_4_sur.blit(lvl_4_text, (15, 55))
        lvl_4_box = pygame.Rect(800, 210, 190, 190)
        self.sur.blit(lvl_4_sur, lvl_4_box)

    def lvl_5(self):
        text = pygame.image.load("images/Textures/trak_trimplain_warning_g.jpg")
        planet = pygame.image.load("images/planets/planet19.png")
        lvl_5 = str("Level 5")
        lvl_5_text = game_font_18.render(lvl_5, True, GRAY6)
        lvl_5_sur = pygame.Surface((190, 190))
        lvl_5_sur.blit(lvl_5_text, (5, 0))
        lvl_5_sur.blit(text, (5, 5))
        lvl_5_sur.blit(planet, (10, 10))
        lvl_5_sur.blit(lvl_5_text, (15, 55))
        lvl_5_box = pygame.Rect(1000, 210, 190, 190)
        self.sur.blit(lvl_5_sur, lvl_5_box)
        R1_10 = pygame.Rect(400, 410, 190, 190)
        pygame.draw.rect(self.sur, BLACK, R1_10)

    def bottom(self):
        self.Sur = pygame.Surface((1200, 60))
        self.Rect = pygame.Rect(0, 600, 1190, 60)
        texture = pygame.image.load("images/Textures/trak_trimplain_warning_g.jpg")
        world_map.sur.blit(self.Sur, self.Rect)
        self.sur.blit(texture, (0, 600))
        self.sur.blit(texture, (300, 600))
        self.sur.blit(texture, (600, 600))
        self.sur.blit(texture, (900, 600))
        self.sur.blit(planet_yellow.image, (266, 600))
        self.sur.blit(planet_yellow.image, (566, 600))
        self.sur.blit(planet_yellow.image, (866, 600))
        self.sur.blit(planet_yellow.image, (1166, 600))

    def Grid(self):
        RT = pygame.Rect(200, 10, 990, 190)
        RL = pygame.Rect(0, 10, 190, 590)
        R2_6 = pygame.Rect(600, 410, 190, 190)
        R2_8 = pygame.Rect(800, 410, 190, 190)
        R2_10 = pygame.Rect(1000, 410, 190, 190)

        pygame.draw.rect(self.sur, BLACK, RT)
        pygame.draw.rect(self.sur, BLACK, RL)
        pygame.draw.rect(self.sur, BLACK, R2_6)
        pygame.draw.rect(self.sur, BLACK, R2_8)
        pygame.draw.rect(self.sur, BLACK, R2_10)

    def update(self):
        screen.blit(self.sur, (0, 0))
        self.sur.blit(self.image, (0, 0))
        self.lvl_1()
        self.lvl_2()
        self.lvl_3()
        self.lvl_4()
        self.lvl_5()
        self.Grid()
        self.bottom()
        self.banner()
        self.world_tiles()
        self.icons()
        self.threeDship(400, 10)
        self.threeDship(500, 10)
        self.threeDship(600, 10)
        self.threeDship(700, 10)
        self.text()
        self.button()


class Main:
    def __init__(self):
        self.update()
        clock.tick(FPS)

    def update(self):
        screen.fill(BLACK)
        screen.blit(back_round, (0, 0))
        grid_group.update()
        self.statments()
        all_sprites.update()
        self.belt()
        asteroid_group.update()
        bullet_group.draw(screen)
        planet_group.update()
        menu_group.update()
        bullet_group.update()
        map_group.update()
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

    def belt(self):
        for a in range(len(asteroid_list)):
            pygame.draw.circle(screen, GRAY78, asteroid_list[a], 1)
            asteroid_list[a][1] += motionY
            asteroid_list[a][0] += motionX
            if asteroid_list[a][0] >= 950:
                Ay = random.randrange(28, 240)
                asteroid_list[a][1] = Ay
                Ax = random.randrange(40, 50)
                asteroid_list[a][0] = Ax

    def statments(self):
        for i in range(len(star_list)):
            pygame.draw.circle(screen, GRAY3, star_list[i], 1)
            star_list[i][1] -= 0
            star_list[i][0] += 0
            if star_list[i][0] > 10:
                y = random.randrange(68, 510)
                star_list[i][1] = y
                x = random.randrange(68, 1030)
                star_list[i][0] = x


# Lists
star_list = []
asteroid_list = []

# Variables
steps = 6
motionX = 2
motionY = 1
points = 12

x = 1010
y = 520
enemy_bullets = Enemy_Bullets(x, y)
bullet = Bullets(x, y)
# Variables
world_map = World_map()
drone = Drone()
asteroid = Asteroid()
purple_ship = Purple_ship()
yellow_ship = Yellow_ship()
grey_ship = Grey_ship()
red_ship = Red_ship()
player = Pilot()
planet_larger = Planet_larger()
planet_yellow = Planet_yellow()
# Variables
start_up = Start_Up()
LeftToolbar = LeftToolbar()
header = Header()
YanSan_window = YanSan_Window()
playerInfobox = PlayerInfobox()
photon_charger_window = Photon_Charger_Window()
Main_Menu = Main_Menu()
Menu_Box1 = Menu_Box1()
game_title = Title_text()
# Sprite Groups
grid_group = pygame.sprite.Group()
battle_sprites = pygame.sprite.Group()
menu_group = pygame.sprite.Group()
start_group = pygame.sprite.Group()
draw_group = pygame.sprite.Group()
bullets_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
planet_group = pygame.sprite.Group()
character_group = pygame.sprite.Group()
asteroid_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
map_group = pygame.sprite.Group()
net_menu = pygame.sprite.Group()
net_menu_sprite = Network_Map_Window()
# Fill the groups with their Sprites
net_menu.add(net_menu_sprite)
menu_group.add(header, game_title, photon_charger_window, YanSan_window, Menu_Box1)
bullets_group.add(enemy_bullets)
battle_sprites.add(red_ship, yellow_ship, purple_ship)
menu_group.add(playerInfobox, photon_charger_window, YanSan_window, LeftToolbar)
all_sprites.add(planet_larger, planet_yellow, asteroid, drone, grey_ship, red_ship, purple_ship, yellow_ship, player)
start_group.add(world_map, start_up)
grid_group.add(Main_Menu)
map_group.add(world_map)
# 'for' statements
voice1.play()
# voice2.play()
for i in range(760):
    x = random.randrange(140, 1000)
    y = random.randrange(14, 36)
    star_list.append([x, y])
for a in range(140):
    Ax = random.randrange(100, 950)
    Ay = random.randrange(228, 340)
    asteroid_list.append([Ax, Ay])
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                bullet_group.add(red_ship.create_bullet())
                bullet_group.add(red_ship.sec_bullet())
            if event.key == pygame.K_0:
                net_menu_window = True
            if event.key == pygame.K_LSHIFT:
                interior_window = True
                int_window.blit(interior_layout, (10, 10))
#            if event.key == pygame.K_RETURN:
# radar_screen_value = True
            if event.key == pygame.K_SPACE:
                shoot_laser.play()
                bullet_group.add(player.create_bullet())
                bullet_group.add(player.sec_bul())
                playerInfobox.overheat()
            if event.key == pygame.K_RETURN:
                planet_group.add(grey_ship.create_clone())
            # if event.key == pygame.K_LEFT:
            #    cursor.curpos(-curmov, 0)
            # if event.key == pygame.K_RIGHT:
            #   cursor.curpos(curmov, 0)
            # if event.key == pygame.K_DOWN:
            #    cursor.curpos(0, curmov)
            # if event.key == pygame.K_UP:
            #    cursor.curpos(0, -curmov)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_1:
                battle = False
            if event.key == pygame.K_0:
                net_menu_window = False
            if event.key == pygame.K_LSHIFT:
                interior_window = False
            if event.key == pygame.K_RETURN:
                radar_screen_value = False
            #if event.key == pygame.K_DOWN:
            #    world_map.cursor(0, curmov)
            #if event.key == pygame.K_LEFT:
            #    world_map.cursor(-curmov, 0)
            #if event.key == pygame.K_RIGHT:
            #    world_map.cursor(curmov, 0)
            #if event.key == pygame.K_UP:
            #    world_map.cursor(0, -curmov)
            if event.key == pygame.K_SPACE:
                purple_ship.attack()
    Main()
    pygame.display.update()
