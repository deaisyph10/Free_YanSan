import pygame
import random
import sys
from Colors import *
from PIL import Image

# ................................................ 'Init' setup ..................................................

pygame.init()
pygame.font.init()

# ................................................... 'Display' setup .............................................

screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("FREE_YanSan")
back_round_im = pygame.image.load("images/templates/Stars.png")
back_round = pygame.Surface((800, 400))
back_round.blit(back_round_im, (0, 0))

# ................................................ 'Game Clock' setup .............................................

clock = pygame.time.Clock()
FPS = 120
game_time = pygame.time.get_ticks()
pygame.mouse.set_visible(True)

# ............................................. Audio Variables .................................................

voice1 = pygame.mixer.Sound("Voicetracks/WC-1.mp3")
voice2 = pygame.mixer.Sound("Voicetracks/WC-17.mp3")
music = pygame.mixer.Sound("Voicetracks/Uppermost.wav")
laser = pygame.mixer.Sound("images/Sprites/sounds/laser_SE_hit.wav")
shoot_laser = pygame.mixer.Sound("images/Sprites/sounds/laser_SE_shoot.wav")
sound_click = pygame.mixer.Sound("images/Sprites/sounds/click.mp3")

# ................................................ Game Fonts ....................................................

game_font_freesansbold_10 = pygame.font.Font("freesansbold.ttf", 10)
game_font_freesansbold_18 = pygame.font.Font("freesansbold.ttf", 18)
game_font_freesansbold_42 = pygame.font.Font("freesansbold.ttf", 42)
game_font_monospace_36 = pygame.font.SysFont("monospace", 36)

# .............................................. Rotate Images ..................................................

im = Image.open("images/ships/10.png")
angle = 45
out = im.rotate(angle)
out.save("images/ships/10.1.png")
im = Image.open("images/ships/SpaceHero/red_ship_micro.png")
angle = 180
out = im.rotate(angle)
out.save("images/ships/SpaceHero/red_ship_micro2.png")

# .................................................. Add-ins .....................................................

blue_bolt = pygame.image.load("images/planets/blue_bolt.png")
new_icon = pygame.image.load("images/player/Dream_Logic_new_icon.png")
new_icon_rect = pygame.Rect(230, 450, 60, 60)
dream_logo = pygame.image.load("images/templates/Dream_Logo.png")
dream_logo_2 = pygame.transform.scale(dream_logo, (40, 40))
LLC_icon = pygame.image.load("images/templates/Dream_green_title.png")
LLC_icon_micro = pygame.transform.scale(LLC_icon, (200, 40))

# ................................................. {SPRITES} ....................................................

class Start_Up(pygame.sprite.Sprite):
    def __init__(self):
        super(Start_Up, self).__init__()
        self.back = pygame.image.load("images/templates/matrix_slate_1200x800.jpg")
        self.menu_screen = pygame.image.load("images/templates/cockpit.blue.jpg")
        self.DLdisp = pygame.image.load("images/templates/DL-Display004.png")
        self.sur = pygame.Surface((1200, 800))
        self.image = self.sur
        self.menu_screen.blit(self.DLdisp, (400, 250))
        self.rect = self.sur.get_rect()
        self.image.blit(self.back, (-400, 0))
        self.back.blit(self.menu_screen, (160, 0))

    def text(self):
        text = game_font_monospace_36.render("FREE YanSan", True, WHITE)
        text_rect = text.get_rect()
        text_rect.center = (120, 20)
        self.sur.blit(text, text_rect)

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
        setup = pygame.image.load("images/icons/icons_setup_white2.png")
        setup2 = pygame.image.load("images/icons/icons_setup_gray3.png")
        backdrop = pygame.Surface((580, 300))

        if 150 > posX > 10 and 230 > posY > 120:
            self.sur.blit(starton, (16, 61))
            if click[0] == 1:
                start_group.add(galaxy_win)
                start_group.draw(screen)
                sound_click.play()
        else:
            self.back.blit(startoff, (20, 160))
            self.back.blit(start, (20, 60))

        if 150 > posX > 10 and 350 > posY > 260:
            self.back.blit(setup, (22, 260))
            if click[0] == 1:
                self.back.blit(setup2, (22, 260))
                start_group.add(setupWin)
                start_group.draw(screen)
                sound_click.play()
        else:
            self.back.blit(setup, (22, 260))

        if 180 > posX > 10 and 640 > posY > 560:
            self.sur.blit(quiton, (36, 575))
            if click[0] == 1:
                pygame.quit()
                sys.exit()

    def draw(self):
        self.sur.blit(self.back, (0, 0))

    def update(self):
        self.draw()
        self.text()
        self.icons()
        self.button()


class SR_22_Window(pygame.sprite.Sprite):
    def __init__(self):
        super(SR_22_Window, self).__init__()
        self.image = pygame.image.load("images/templates/level_image_galaxy1-lvls-blank.png")
        self.white_grid = pygame.image.load("images/templates/level_image_galaxy1-lvls_white-grid.png")
        self.rect = self.image.get_rect()
        self.movex = 0
        self.movey = 0
        self.logo = pygame.image.load("images/templates/Dream_Logo.png")

        # self.image.blit(planet_larger.image, (900, 40))

    def Gal_Toolbar(self):
        self.toolbar_image = pygame.image.load("images/icons/galaxy_fullscreen_toolbar.png")
        black_grid_icon = pygame.image.load("images/icons/buttons_galaxy-toolbar_map-grid_black.png")
        white_grid_icon = pygame.image.load("images/icons/buttons_galaxy-toolbar_map-grid_white.png")
        yansan_bea_icon = pygame.image.load("images/icons/buttons_galaxy-toolbar_YanSan-beacon.png")
        yansan_ship_icon = pygame.image.load("images/icons/buttons_galaxy-toolbar_YanSan-ships.png.")
        rebel_stru_icon = pygame.image.load("images/icons/buttons_galaxy-toolbar_rebel-structures_red.png")
        rebel_ship_icon = pygame.image.load("images/icons/buttons_galaxy-toolbar_rebel-icon_red.png")
        solar_icon = pygame.image.load("images/icons/buttons_galaxy-toolbar_solar_gray.png")
        planet_icon = pygame.image.load("images/icons/buttons_galaxy-toolbar_planet_gray.png")
        rogue_icon = pygame.image.load("images/icons/buttons_galaxy-toolbar_bolt_gray.png")
        screen.blit(self.toolbar_image, (880, 186))

    def mission1(self):
        asteroid_field_BOX1 = pygame.image.load("images/buttons/level_image_galaxy1-level1-asteroid_field.01.1.png")
        asteroid_field_BOX2 = pygame.image.load("images/buttons/level_image_galaxy1-level1-asteroid_field.02.png")
        asteroid_field_BOX3 = pygame.image.load("images/buttons/level_image_galaxy1-level1-asteroid_field.03.png")
        click = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        posX = pos[0]
        posY = pos[1]
        if 1080 > posX > 928 and 580 > posY > 367:
            screen.blit(asteroid_field_BOX3, (928, 367))
            if click[0] == 1:
                screen.blit(asteroid_field_BOX2, (928, 367))
        else:
            screen.blit(asteroid_field_BOX1, (928, 367))

    def mission2(self):
        rebel_control_BOX1 = pygame.image.load("images/buttons/level_image_galaxy1-level2-solar-cycle_rebelcontrol.01.png")
        rebel_control_BOX2 = pygame.image.load("images/buttons/level_image_galaxy1-level2-solar-cycle_rebelcontrol.02.1.png")
        rebel_control_BOX3 = pygame.image.load("images/buttons/level_image_galaxy1-level2-solar-cycle_rebelcontrol.03.png")
        click = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        posX = pos[0]
        posY = pos[1]
        if 820 > posX > 685 and 480 > posY > 340:
            screen.blit(rebel_control_BOX1, (690, 346))
            if click[0] == 1:
                screen.blit(rebel_control_BOX3, (690, 346))
        else:
            screen.blit(rebel_control_BOX2, (690, 346))

    def mission3(self):
        war_alarm_BOX1 = pygame.image.load("images/buttons/level_image_galaxy1-level3-planet_nine_WAR.01.png")
        war_alarm_BOX2 = pygame.image.load("images/buttons/level_image_galaxy1-level3-planet_nine_WAR.02.png")
        war_alarm_BOX3 = pygame.image.load("images/buttons/level_image_galaxy1-level3-planet_nine_WAR.03.png")
        click = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        posX = pos[0]
        posY = pos[1]
        if 560 > posX > 514 and 520 > posY > 468:
            screen.blit(war_alarm_BOX2, (514, 468))
            if click[0] == 1:
                screen.blit(war_alarm_BOX3, (514, 468))
        else:
            screen.blit(war_alarm_BOX1, (514, 468))

    def draw(self):
        self.mission1()
        self.mission2()
        self.mission3()
        screen.blit(self.image, (160, 50))
        screen.blit(self.white_grid, (400, 185))

    def update(self):
        self.draw()
        self.Gal_Toolbar()
        self.mission1()
        self.mission2()
        self.mission3()


class GalaxyWin(pygame.sprite.Sprite):
    def __init__(self):
        super(GalaxyWin, self).__init__()
        self.sur = pygame.Surface((600, 250))
        self.stars = pygame.image.load("images/templates/frame_YanSan600X250.png")
        self.frame = pygame.image.load("images/templates/BOX.galaxyWin2.png")
        self.image = self.stars
        self.rect = self.image.get_rect()
        self.sur.blit(self.stars, (0, 0))
        self.stars.blit(self.frame, (-1, 0))
        self.moveX = 0
        self.moveY = 0
        self.rect.y = 50
        self.arrow = pygame.image.load("images/icons/arrow.50x50.png")
        self.image.blit(self.arrow, (-10, 30))

    def nav_box(self):
        navstring = str("Send coordinate-cache data block via ::// SHIP_navigation.SYSTEMS")
        ship_image = pygame.image.load("images/ships/Ship_ICON.png")
        self.navtext = game_font_freesansbold_10.render(navstring, True, GRAY95)
        self.navimage = pygame.Surface((360, 60))
        self.navimage.fill(GRAY9)
        self.navimage.blit(self.navtext, (5, 10))
        self.navimage.blit(ship_image, (260, 0))
        self.image.blit(self.navimage, (220, 178))

    def move(self, mx, my):
        self.moveX += mx
        self.moveY += my
        self.rect.x = self.moveX + self.rect.x
        self.rect.y = self.moveY + self.rect.y

    def buttons(self):
        choice1 = pygame.image.load("images/templates/BOX.4star.png")
        choice2 = pygame.image.load("images/templates/BOX.4star.png")
        choice3 = pygame.image.load("images/templates/BOX.4star.png")
        choice4 = pygame.image.load("images/templates/BOX.4star.png")
        choice1_1 = pygame.image.load("images/icons/BOX.4star.innerblack.png")
        choice2_1 = pygame.image.load("images/icons/BOX.4star.innerblack.png")
        choice3_1 = pygame.image.load("images/icons/BOX.4star.innerblack.png")
        choice4_1 = pygame.image.load("images/icons/BOX.4star.innerblack.png")
        choice1_2 = pygame.image.load("images/icons/BOX.4star.outerblack.png")
        choice2_2 = pygame.image.load("images/icons/BOX.4star.outerblack.png")
        choice3_2 = pygame.image.load("images/icons/BOX.4star.outerblack.png")
        choice4_2 = pygame.image.load("images/icons/BOX.4star.outerblack.png")

        click = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        posX = pos[0]
        posY = pos[1]

        self.gal1 = pygame.image.load("images/planets/galaxy_1s.jpg")
        self.image.blit(self.gal1, (2, 78))
        self.gal2 = pygame.image.load("images/planets/galaxy_2s.jpg")
        self.image.blit(self.gal2, (146, 78))
        self.gal3 = pygame.image.load("images/planets/galaxy_3.png")
        self.image.blit(self.gal3, (316, 78))
        self.gal4 = pygame.image.load("images/planets/galaxy_4s.jpg")
        self.image.blit(self.gal4, (466, 78))

        if 220 > posX > 180 and 115 > posY > 70:
            if click[0] == 1:
                self.kill()
                sound_click.play()
        if 300 > posX > 180 and 200 > posY > 120:
            self.image.blit(choice1, (2, 78))
            self.image.blit(choice1_1, (2, 78))
            if click[0] == 1:
                self.image.blit(choice1_2, (2, 78))
                self.nav_box()
                Galaxy_group.add(galaxy_data_win)
                sound_click.play()
        if 420 > posX > 360 and 200 > posY > 120:
            self.image.blit(choice2, (146, 78))
            self.image.blit(choice2_1, (146, 78))
            if click[0] == 1:
                self.image.blit(choice2_2, (146, 78))
                sound_click.play()
        if 580 > posX > 500 and 200 > posY > 120:
            self.image.blit(choice3, (316, 78))
            self.image.blit(choice3_1, (316, 78))
            if click[0] == 1:
                self.image.blit(choice3_2, (316, 78))
                sound_click.play()
        if 720 > posX > 640 and 200 > posY > 120:
            self.image.blit(choice4, (466, 78))
            self.image.blit(choice4_1, (466, 78))
            if click[0] == 1:
                self.image.blit(choice4_2, (466, 78))
                sound_click.play()

    def headertext(self):
        select = str("Select a Galaxy to Explore")
        headertxt = game_font_freesansbold_42.render(select, True, WHITE)
        self.image.blit(headertxt, (40, 10))

    def draw(self):
        screen.blit(self.image, (200, 400))

    def update(self):
        self.headertext()
        self.buttons()
        self.move(10, 0)
        if self.rect.x >= 180:
            self.rect.x = 180


class Galaxy_data_Window(pygame.sprite.Sprite):
    def __init__(self):
        super(Galaxy_data_Window, self).__init__()
        self.frame = pygame.image.load("images/templates/frame_YanSan300x600.png")
        self.image = pygame.Surface((300, 600))
        self.rect = self.image.get_rect()
        self.moveX = 0
        self.moveY = 0
        self.arrow = pygame.image.load("images/icons/arrow.50x50.png")

    def galaxy_image(self):
        self.image1 = pygame.image.load("images/icons/icon_galaxy_1data.jpg")
        self.image_rect = self.image1.get_rect()
        self.image_label_str = str("'SR22-87.23'")
        self.image_label = game_font_freesansbold_42.render(self.image_label_str, True, GRAY95)
        self.image_label_rect = self.image_label.get_rect()
        self.image_label_icon = pygame.image.load("images/icons/saturn_icon.png")


    def button(self):
        self.data()
        self.text_sur = pygame.Surface((300, 70))
        self.text_sur.fill(BLACK)
        click = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        posX = pos[0]
        posY = pos[1]

        if 900 > posX > 850 and 190 > posY > 140:
            if click[0] == 1:
                sound_click.play()
                self.kill()

        if 1110 > posX > 880 and 590 > posY > 525:
            self.image.blit(self.start2, (55, 470))
            if click[0] == 1:
                galaxy_win.kill()
                setupWin.kill()
                self.kill()
                map_group.draw(screen)
                map_group.add(SR_22_Window)

        else:
            self.image.blit(self.start, (55, 470))

    def data(self):
        self.box_select = pygame.image.load("images/templates/Box_SELECT_white_1.1.png")
        self.start_box = pygame.Surface((280, 80))
        self.start_box.fill(GRAY4)
        self.start = pygame.image.load("images/buttons/buttons_select_white.png")
        self.start2 = pygame.image.load("images/buttons/buttons_select_blue.png")
        self.text_sur = pygame.Surface((300, 60))
        self.text_sur.fill(GRAY14)
        self.text_sur_rect = self.text_sur.get_rect()
        self.text_str = str("Galaxy 1")
        self.text = game_font_freesansbold_18.render(self.text_str, True, GRAY95)
        self.text_rect = self.text.get_rect()
        self.text_icon = pygame.image.load("images/icons/galaxy_description.png")

    def move(self, mx, my):
        self.moveX = mx
        self.moveY = my
        self.rect.x = self.rect.x + self.moveX
        self.rect.y = self.rect.y + self.moveY

    def draw(self):
        self.galaxy_image()
        self.image.blit(self.image1, (0, 0))
        self.image.blit(self.image_label, (30, 55))
        self.image.blit(self.text, (35, 410))
        self.image.blit(self.frame, (0, 0))
        self.image.blit(self.text_icon, (80, 360))
        self.image.blit(self.image_label_icon, (28, 362))
        self.image.blit(self.arrow, (0, 80))
        self.image.blit(self.box_select, (10, 440))
        screen.blit(self.image, (850, 60))

    def update(self):
        self.button()
        self.data()
        self.draw()
        self.galaxy_image()


class setupWin(pygame.sprite.Sprite):
    def __init__(self):
        super(setupWin, self).__init__()
        self.sur = pygame.Surface((300, 220))
        self.sur.fill(GRAY16)
        self.image = pygame.image.load("images/templates/frame_YanSan600X250.png")
        self.rect = self.image.get_rect()
        self.moveX = 0
        self.moveY = 350
        self.rect.y = 350
        self.rect.x = 0
        self.arrow = pygame.image.load("images/icons/arrow.50x50.png")
        self.image.blit(self.arrow, (0, 10))

    def button(self):

        click = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        posX = pos[0]
        posY = pos[1]

        if 220 > posX > 180 and 360 > posY > 310:
            if click[0] == 1:
                sound_click.play()
                pygame.mouse.set_visible(True)

    def move(self, mx, my):
        self.moveX = mx
        self.moveY = my
        self.rect.x = self.rect.x + self.moveX
        self.rect.y = self.rect.y + self.moveY

    def draw(self):
        screen.blit(self.image, (0, 310))

    def update(self):
        self.button()
        self.move(50, 0)
        if self.rect.x >= 180:
            self.rect.x = 180


class Toolbar(pygame.sprite.Sprite):
    def __init__(self):
        super(Toolbar, self).__init__()
        self.sur = pygame.Surface((300, 50))
        self.sur.fill(BLACK)
        self.image = self.sur
        self.rect = self.image.get_rect()
        self.mainmenu_bar()
        screen.blit(self.back, (740, 60))
        self.buttons()
        self.icons()

    def mainmenu_bar(self):
        self.back = pygame.Surface((260, 200))
        self.back_rect = self.back.get_rect()
        self.back.fill(GRAY19)
        self.menubar = pygame.image.load("images/templates/button_container_mainmenu.png")
        self.menubar_rect = self.menubar.get_rect()
        self.slot1 = pygame.image.load("images/buttons/buttons_mainmenu_toolbar.png")
        self.slot2 = pygame.image.load("images/buttons/buttons_gallaxymenu2.png")
        self.slot3 = pygame.image.load("images/buttons/buttons_inventory1.png")
        self.back.blit(self.menubar, (0, 0))
        self.back.blit(self.slot1, (4, 0))
        self.back.blit(self.slot2, (4, 60))
        self.back.blit(self.slot3, (4, 110))

    def icons(self):
        self.mainmenu = pygame.image.load("images/Sprites/shadedDark/shadedDark33.png")
        self.quit = pygame.image.load("images/Sprites/shadedDark/shadedDark35.png")
        self.music_on = pygame.image.load("images/Sprites/shadedDark/shadedDark17.png")
        self.music_off = pygame.image.load("images/Sprites/shadedDark/shadedDark19.png")
        self.setup = pygame.image.load("images/Sprites/shadedDark/shadedDark31.png")
        self.search = pygame.image.load("images/Sprites/shadedDark/shadedDark32.png")
        self.maximize = pygame.image.load("images/Sprites/shadedDark/shadedDark30.png")
        self.save = pygame.image.load("images/Sprites/shadedDark/shadedDark34.png")
        self.check = pygame.image.load("images/Sprites/shadedDark/shadedDark33.png")
        self.select = pygame.image.load("images/Sprites/shadedDark/shadedDark33.png")
        self.pause = pygame.image.load("images/Sprites/shadedDark/shadedDark14.png")
        self.volume_on = pygame.image.load("images/Sprites/shadedDark/shadedDark13.png")
        self.volume_off = pygame.image.load("images/Sprites/shadedDark/shadedDark15.png")
        self.quit_on = pygame.image.load("images/Sprites/shadedLight/shadedLight35.png")
        self.mainmenu_on = pygame.image.load("images/Sprites/shadedLight/shadedLight33.png")
        self.setup_on = pygame.image.load("images/Sprites/shadedLight/shadedLight31.png")
        self.save_on = pygame.image.load("images/Sprites/shadedLight/shadedLight34.png")

    def buttons(self):
        self.mainmenu_bar()
        self.icons()
        click = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        posX = pos[0]

        posY = pos[1]

        if 950 > posX > 900 and 46 > posY > 1:
            screen.blit(self.mainmenu_on, (902, 0))
            screen.blit(self.back, (722, 60))
            if click[0] == 1:
                screen.blit(self.back, (722, 60))
        else:
            screen.blit(self.mainmenu, (902, 0))
        if 1000 > posX > 952 and 46 > posY > 1:
            screen.blit(self.setup_on, (952, 0))
            if click[0] == 1:
                setupWin.update()
        else:
            screen.blit(self.setup, (952, 0))
        if 1050 > posX > 1002 and 46 > posY > 1:
            screen.blit(self.volume_on, (1002, 0))
        else:
            screen.blit(self.volume_off, (1002, 0))
        if 1100 > posX > 1052 and 46 > posY > 1:
            screen.blit(self.music_off, (1052, 0))
            if click[0] == 1:
                music.stop()
                screen.blit(self.music_off, (1052, 0))
        else:
            screen.blit(self.music_on, (1052, 0))
        if 1150 > posX > 1102 and 46 > posY > 1:
            screen.blit(self.save_on, (1102, 0))
        else:
            screen.blit(self.save, (1102, 0))
        if 1200 > posX > 1152 and 46 > posY > 1:
            screen.blit(self.quit_on, (1152, 0))
            if click[0] == 1:
                pygame.quit()
                sys.exit()
        else:
            screen.blit(self.quit, (1152, 0))

    def draw(self):
        screen.blit(self.image, (900, 0))
        screen.blit(self.save, (1102, 0))
        screen.blit(self.music_on, (1052, 0))
        screen.blit(self.volume_off, (1002, 0))
        screen.blit(self.setup, (952, 0))
        screen.blit(self.mainmenu, (902, 0))
        screen.blit(self.quit, (1152, 0))
        self.buttons()

    def update(self):
        self.draw()
        self.icons()


class Main:
    def __init__(self):
        self.update()
        clock.tick(FPS)

    def update(self):
        screen.fill(BLACK)
        screen.blit(back_round, (0, 0))
        start_group.draw(screen)
        start_group.update()
        map_group.update()
        Galaxy_group.update()


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


# ........................................... Functions and Variables .............................................

cell_pxl_size = 70
cell_count = 10
screen_width = 1200
screen_height = 700
moveX, moveY = 0, 0
x = 1010
y = 520
steps = 6
motionX = 2
motionY = 1
points = 12
star_list = []
asteroid_list = []
toolbar = Toolbar()
setupWin = setupWin()
galaxy_data_win = Galaxy_data_Window()
galaxy_win = GalaxyWin()
SR_22_Window = SR_22_Window()
start_up = Start_Up()

# ............................................... Audio Functions ................................................

voice1.play()
music.play()

# ............................................... Sprite Groups ..................................................

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
Galaxy_group = pygame.sprite.Group()

# .............................................. Add Sprites to Groups ............................................

start_group.add(start_up)
Galaxy_group.add(toolbar)

# ............................................... 'for' Statements ................................................

for i in range(760):
    x = random.randrange(140, 1000)
    y = random.randrange(14, 36)
    star_list.append([x, y])
for a in range(140):
    Ax = random.randrange(100, 950)
    Ay = random.randrange(228, 340)
    asteroid_list.append([Ax, Ay])

# ................................................. {Game Loop} ...................................................

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    Main()
    pygame.display.update()
