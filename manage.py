import pygame
import random
from Colors import *
from levels import *
# .............................................. 'Init' add-in mods ..................................................
pygame.init()
pygame.font.init()
# ............................................ 'Game Clock' setup ..............................................
clock = pygame.time.Clock()
FPS = 120
game_time = pygame.time.get_ticks()
# ............................................. 'Display' setup ................................................
screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("FREE_YanSan")
icon = pygame.image.load("images/icons/Dream_Logo.ico")
pygame.display.set_icon(icon)
back_round_im = pygame.image.load("images/templates/Stars.png")
back_round = pygame.Surface((800, 400))
back_round.blit(back_round_im, (0, 0))
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
# .................................................. MISC .....................................................
blue_bolt = pygame.image.load("images/planets/blue_bolt.png")
new_icon = pygame.image.load("images/player/Dream_Logic_new_icon.png")
new_icon_rect = pygame.Rect(230, 450, 60, 60)
dream_logo = pygame.image.load("images/templates/Dream_Logo.png")
dream_logo_2 = pygame.transform.scale(dream_logo, (40, 40))
LLC_icon = pygame.image.load("images/templates/Dream_green_title.png")
LLC_icon_micro = pygame.transform.scale(LLC_icon, (200, 40))
# ........................................... Functions and Variables .............................................
cell_pxl_size = 70
cell_count = 10
screen_width = 1200
screen_height = 700
moveX, moveY = 0, 0
x = 0
y = 0
steps = 6
motionX = 2
motionY = 1
points = 12
star_list = []
asteroid_list = []
main_menu = main_menu()
briefing_Win = briefing_Win()
toolbar = Toolbar()
setupWin = setupWin()
galaxy_data_win = Galaxy_data_Window()
galaxy_win = GalaxyWin()
SR_22_Window = SR_22_Window()
start_up = Start_Up()

# ............................................... Audio Functions ................................................

voice1.play()
music.play()


# ............................................... 'for' Statements ................................................

for i in range(760):
    x = random.randrange(140, 1000)
    y = random.randrange(14, 36)
    star_list.append([x, y])
for a in range(140):
    Ax = random.randrange(100, 950)
    Ay = random.randrange(228, 340)
    asteroid_list.append([Ax, Ay])



class Start_Up(pygame.sprite.Sprite):
    def __init__(self):
        super(Start_Up, self).__init__()
        self.back = pygame.image.load("images/templates/matrix_slate_1200x800.jpg")
        self.menu_screen = pygame.image.load("images/templates/cockpit.blue.jpg")
        self.sur = pygame.Surface((1200, 800))
        self.image = self.sur
        self.rect = self.sur.get_rect()
        self.image.blit(self.back, (-400, 0))
        self.back.blit(self.menu_screen, (160, 0))

    def text(self):
        text = game_font_monospace_36.render("FREE YanSan", True, WHITE)
        text_rect = text.get_rect()
        text_rect.center = (120, 20)
        self.sur.blit(text, text_rect)

    def icons(self):
        QUIT = pygame.image.load("images/icons/icons_quit_white.png")
        start = pygame.image.load("images/icons/icons_play_white.png")
        setup = pygame.image.load("images/icons/icons_setup_white2.png")
        insert = pygame.image.load("images/icons/icons_insert_white.png")
        quit_txt_image = pygame.image.load("images/txt_Images/txt_Images -- txt_quit_darkgray_tilt.png")
        upload_txt_image = pygame.image.load("images/txt_Images/txt_Images -- txt_upload_darkgray_tilt.png")
        settings_txt_image = pygame.image.load("images/txt_Images/txt_Images -- txt_settings_darkgray_tilt.png")
        play_txt_image = pygame.image.load("images/txt_Images/txt_Images -- txt_play_darkgray_tilt.png")
        self.sur.blit(quit_txt_image, (10, 575))
        self.sur.blit(upload_txt_image, (10, 420))
        self.sur.blit(settings_txt_image, (6, 260))
        self.sur.blit(play_txt_image, (15, 60))
        self.sur.blit(start, (20, 60))
        self.sur.blit(setup, (22, 260))
        self.sur.blit(insert, (20, 400))
        self.sur.blit(QUIT, (36, 575))

    def button(self):
        click = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        posX = pos[0]
        posY = pos[1]
        start = pygame.image.load("images/icons/icons_play_white.png")
        pygame.image.load("images/Sprites/transparentLight/transparentLight40.png")
        starton = pygame.image.load("images/icons/icons_play_gray.png")
        startoff = pygame.image.load("images/Sprites/transparentDark/transparentDark40.png")
        quiton = pygame.image.load("images/icons/icons_quit_gray.png")
        pygame.image.load("images/icons/icons_quit_white.png")
        setup = pygame.image.load("images/icons/icons_setup_white2.png")
        setup2 = pygame.image.load("images/icons/icons_setup_gray3.png")
        pygame.Surface((580, 300))

        if 150 > posX > 10 and 230 > posY > 120:
            self.sur.blit(starton, (16, 61))
            if click[0] == 1:
                movement_group.add(galaxy_win)
                sound_click.play()
        else:
            self.back.blit(startoff, (20, 160))
            self.back.blit(start, (20, 60))

        if 150 > posX > 10 and 350 > posY > 260:
            self.back.blit(setup, (22, 260))
            if click[0] == 1:
                self.back.blit(setup2, (22, 260))
                sound_click.play()
                movement_group.add(setupWin)
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


class Galaxy_data_Window(pygame.sprite.Sprite):
    def __init__(self):
        super(Galaxy_data_Window, self).__init__()
        self.button_image = pygame.image.load("images/buttons/button_black_blue_none-none.png")
        self.image_label_icon = pygame.image.load("images/icons/saturn_icon.png")
        self.image_label_str = str("'SR22-87.23'")
        self.image_label = game_font_freesansbold_18.render(self.image_label_str, True, GRAY95)
        self.image1 = pygame.image.load("images/icons/icon_galaxy_1data.jpg")
        self.frame = pygame.image.load("images/templates/frame_YanSan400X167.png")
        self.image = self.frame
        self.rect = self.image.get_rect()
        self.moveX = 0
        self.moveY = 0
        self.arrow = pygame.image.load("images/icons/arrow.50x50.png")

    def galaxy_image(self):
        pass

    def button(self):
        click = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        posX = pos[0]
        posY = pos[1]
        if 1070 > posX > 800 and 260 > posY > 200:
            if click[0] == 1:
                map_group.add(SR_22_Window)
                movement_group.remove(galaxy_win)
                movement_group.remove(setupWin)
                self.kill()
        if 850 > posX > 794 and 170 > posY > 108:
            if click[0] == 1:
                self.kill()
                sound_click.play()

    def move(self, mx, my):
        self.moveX = mx
        self.moveY = my
        self.rect.x = self.rect.x + self.moveX
        self.rect.y = self.rect.y + self.moveY

    def draw(self):
        self.button()
        self.image.blit(self.button_image, (10, 100))
        self.image.blit(self.arrow, (0, 20))
        screen.blit(self.image, (790, 108))

    def update(self):
        self.draw()


class setupWin(pygame.sprite.Sprite):
    def __init__(self):
        super(setupWin, self).__init__()
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
        if 225 > posX > 185 and 405 > posY > 370:
            if click[0] == 1:
                sound_click.play()
                self.kill()

    def move(self, mx, my):
        self.moveX = mx
        self.moveY = my
        self.rect.x = self.rect.x + self.moveX
        self.rect.y = self.rect.y + self.moveY
        if self.rect.x >= 180:
            self.rect.x = 180

    def draw(self):
        screen.blit(self.image, (0, 310))

    def update(self):
        self.button()
        self.move(50, 0)


class Toolbar(pygame.sprite.Sprite):
    def __init__(self):
        super(Toolbar, self).__init__()
        self.save_on = pygame.image.load("images/Sprites/shadedLight/shadedLight34.png")
        self.setup_on = pygame.image.load("images/Sprites/shadedLight/shadedLight31.png")
        self.mainmenu_on = pygame.image.load("images/Sprites/shadedLight/shadedLight33.png")
        self.quit_on = pygame.image.load("images/Sprites/shadedLight/shadedLight35.png")
        self.volume_off = pygame.image.load("images/Sprites/shadedDark/shadedDark15.png")
        self.volume_on = pygame.image.load("images/Sprites/shadedDark/shadedDark13.png")
        self.pause = pygame.image.load("images/Sprites/shadedDark/shadedDark14.png")
        self.select = pygame.image.load("images/Sprites/shadedDark/shadedDark33.png")
        self.check = pygame.image.load("images/Sprites/shadedDark/shadedDark33.png")
        self.save = pygame.image.load("images/Sprites/shadedDark/shadedDark34.png")
        self.maximize = pygame.image.load("images/Sprites/shadedDark/shadedDark30.png")
        self.search = pygame.image.load("images/Sprites/shadedDark/shadedDark32.png")
        self.setup = pygame.image.load("images/Sprites/shadedDark/shadedDark31.png")
        self.music_off = pygame.image.load("images/Sprites/shadedDark/shadedDark19.png")
        self.music_on = pygame.image.load("images/Sprites/shadedDark/shadedDark17.png")
        self.quit = pygame.image.load("images/Sprites/shadedDark/shadedDark35.png")
        self.slot1 = pygame.image.load("images/buttons/buttons_mainmenu_toolbar.png")
        self.mainmenu = pygame.image.load("images/Sprites/shadedDark/shadedDark33.png")
        self.slot3 = pygame.image.load("images/buttons/buttons_inventory1.png")
        self.slot2 = pygame.image.load("images/buttons/buttons_gallaxymenu2.png")
        self.menubar = pygame.image.load("images/templates/button_container_mainmenu.png")
        self.menubar_rect = self.menubar.get_rect()
        self.back = pygame.Surface((260, 200))
        self.back_rect = self.back.get_rect()
        self.sur = pygame.Surface((300, 50))
        self.sur.fill(BLACK)
        self.image = self.sur
        self.rect = self.image.get_rect()
        self.mainmenu_bar()
        screen.blit(self.back, (740, 60))
        self.buttons()
        self.icons()

    def mainmenu_bar(self):
        self.back.fill(GRAY19)
        self.back.blit(self.menubar, (0, 0))
        self.back.blit(self.slot1, (4, 0))
        self.back.blit(self.slot2, (4, 60))
        self.back.blit(self.slot3, (4, 110))

    def icons(self):
        pass

    def buttons(self):
        self.mainmenu_bar()
        self.icons()
        click = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        posX = pos[0]
        posY = pos[1]
        if 950 > posX > 900 and 46 > posY > 1:
            menu_group.add(main_menu)
            screen.blit(self.mainmenu_on, (902, 0))
            if click[0] == 1:
                sound_click.play()
                menu_group.add(main_menu)
                screen.blit(self.mainmenu, (902, 0))
        else:
            menu_group.remove(main_menu)
        if 1000 > posX > 952 and 46 > posY > 1:
            screen.blit(self.setup_on, (952, 0))
            if click[0] == 1:
                sound_click.play()
                movement_group.add(setupWin)
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
                sound_click.play()
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


class briefing_Win(pygame.sprite.Sprite):
    def __init__(self):
        super(briefing_Win, self).__init__()
        self.image = pygame.image.load("images/templates/templates_mission_briefing.png")
        self.rect = self.image.get_rect()
        self.movex = 0
        self.movey = 0

    def draw(self):
        screen.blit(self.image, (480, 40))

    def update(self):
        self.draw()


class main_menu(pygame.sprite.Sprite):
    def __init__(self):
        super(main_menu, self).__init__()
        # self.image = pygame.image.load("images/templates/templates_main_menu_dropdown.png")
        self.slot1 = pygame.image.load("images/txt_Images/txt_Images -- txt_galaxy menu_white.png")
        self.slot2 = pygame.image.load("images/txt_Images/txt_Images -- txt_YanSan Network Map_white.png")
        self.menu_icon_1 = pygame.image.load("images/icons/icons_darkgray_V.png")
        self.divider_line = pygame.image.load("images/templates/templates_lightgray-divide_300px.png")
        self.slot3 = pygame.image.load("images/txt_Images/txt_Images -- txt_player controls_white.png")
        self.slot4 = pygame.image.load("images/txt_Images/txt_Images -- txt_assets_white.png")
        self.image = pygame.image.load("images/templates/templates_main_menu_dropdown_white_light_Lrg.png")
        self.rect = self.image.get_rect()

    def slots(self):
        pass
        # self.slot5 = pygame.image.load("images/txt_Images/txt_Images -- )
        # self.slot6 = pygame.image.load("images/txt_Images/txt_Images -- )

    def draw(self):
        screen.blit(self.image, (710, 50))
        self.slots()
        self.image.blit(self.divider_line, (40, 20))
        self.image.blit(self.divider_line, (40, 60))
        self.image.blit(self.divider_line, (40, 100))
        self.image.blit(self.divider_line, (40, 140))
        self.image.blit(self.divider_line, (40, 180))
        self.image.blit(self.divider_line, (40, 220))
        self.image.blit(self.divider_line, (40, 260))
        self.image.blit(self.divider_line, (40, 300))
        self.image.blit(self.slot1, (93, 40))
        self.image.blit(self.slot2, (96, 88))
        self.image.blit(self.slot3, (96, 124))
        self.image.blit(self.slot4, (96, 164))
        self.image.blit(self.menu_icon_1, (44, 48))
        self.image.blit(self.menu_icon_1, (44, 88))
        self.image.blit(self.menu_icon_1, (44, 128))
        self.image.blit(self.menu_icon_1, (44, 168))
        self.image.blit(self.menu_icon_1, (44, 208))
        self.image.blit(self.menu_icon_1, (44, 248))
        self.image.blit(self.menu_icon_1, (44, 288))

    def update(self):
        self.draw()


class GalaxyWin(pygame.sprite.Sprite):
    def __init__(self):
        super(GalaxyWin, self).__init__()
        self.str = str("Send coordinate-cache data block via ::// SHIP_navigation.SYSTEMS")
        self.navtext = game_font_freesansbold_10.render(self.str, True, GRAY95)
        self.gal4 = pygame.image.load("images/planets/galaxy_4s.jpg")
        self.gal3 = pygame.image.load("images/planets/galaxy_3.png")
        self.gal2 = pygame.image.load("images/planets/galaxy_2s.jpg")
        self.gal1 = pygame.image.load("images/planets/galaxy_1s.jpg")
        self.navimage = pygame.image.load("images/buttons/button_black_blue_none-none.png")
        self.image = pygame.image.load("images/templates/frame_YanSan600X250.png")
        self.frame = pygame.image.load("images/templates/BOX.galaxyWin2.png")
        self.rect = self.image.get_rect()
        self.image.blit(self.frame, (-1, 0))
        self.arrow = pygame.image.load("images/icons/arrow.50x50.png")
        self.image.blit(self.arrow, (-10, 30))
        self.moveX = 0
        self.moveY = 0
        self.rect.y = 50

    def nav_box(self):
        ship_image = pygame.image.load("images/ships/Ship_ICON.png")
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

        self.image.blit(self.gal1, (2, 78))
        self.image.blit(self.gal2, (146, 78))
        self.image.blit(self.gal3, (316, 78))
        self.image.blit(self.gal4, (466, 78))

        if 220 > posX > 180 and 115 > posY > 70:
            if click[0] == 1:
                self.kill()
                sound_click.play()
        if 300 > posX > 180 and 200 > posY > 120:
            self.image.blit(choice1, (2, 78))
            self.image.blit(choice1_1, (2, 78))
            self.nav_box()
            if click[0] == 1:
                self.image.blit(choice1_2, (2, 78))
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
        screen.blit(self.image, (0, 60))

    def update(self):
        self.headertext()
        self.buttons()
        self.move(10, 0)
        if self.rect.x >= 180:
            self.rect.x = 180


class SR_22_Window(pygame.sprite.Sprite):
    def __init__(self):
        super(SR_22_Window, self).__init__()
        self.toolbar_image = pygame.image.load("images/icons/galaxy_fullscreen_toolbar.png")
        self.image = pygame.image.load("images/templates/level_image_galaxy1-lvls-blank.png")
        self.white_grid = pygame.image.load("images/templates/level_image_galaxy1-lvls_white-grid.png")
        self.rect = self.image.get_rect()
        self.movex = 0
        self.movey = 0
        self.logo = pygame.image.load("images/templates/Dream_Logo.png")
        self.start_BOX = pygame.image.load("images/buttons/buttons_wide_button-gray.png")
        self.start_button_w = pygame.image.load("images/buttons/buttons_start_white_320x70.png")
        self.start_button_b = pygame.image.load("images/buttons/buttons_start_blue_320x70.png")

    def gal_toolbar(self):
        pygame.image.load("images/icons/buttons_galaxy-toolbar_map-grid_black.png")
        pygame.image.load("images/icons/buttons_galaxy-toolbar_map-grid_white.png")
        pygame.image.load("images/icons/buttons_galaxy-toolbar_YanSan-beacon.png")
        pygame.image.load("images/icons/buttons_galaxy-toolbar_YanSan-ships.png.")
        pygame.image.load("images/icons/buttons_galaxy-toolbar_rebel-structures_red.png")
        pygame.image.load("images/icons/buttons_galaxy-toolbar_rebel-icon_red.png")
        pygame.image.load("images/icons/buttons_galaxy-toolbar_solar_gray.png")
        pygame.image.load("images/icons/buttons_galaxy-toolbar_planet_gray.png")
        pygame.image.load("images/icons/buttons_galaxy-toolbar_bolt_gray.png")
        screen.blit(self.toolbar_image, (880, 186))

    def mission1(self):
        asteroid_field_BOX1 = pygame.image.load("images/buttons/level_image_galaxy1-level1-asteroid_field.01.1.png")
        asteroid_field_BOX2 = pygame.image.load("images/buttons/level_image_galaxy1-level1-asteroid_field.02.png")
        lvl_1_start_label = pygame.image.load("images/txt_Images/txt_Images -- level_1.1-start.label.png")
        click = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        posX = pos[0]
        posY = pos[1]
        if 1080 > posX > 928 and 580 > posY > 367:
            screen.blit(asteroid_field_BOX2, (928, 367))
            text_group.add(briefing_Win)
            if click[0] == 1:
                sound_click.play()
                screen.blit(asteroid_field_BOX2, (928, 367))
                text_group.add(briefing_Win)
                screen.blit(lvl_1_start_label, (450, 600))
                screen.blit(self.start_button_b, (600, 600))
        else:
            screen.blit(asteroid_field_BOX1, (928, 367))
            text_group.remove(briefing_Win)

    def draw(self):
        screen.blit(self.image, (160, 50))
        screen.blit(self.white_grid, (400, 185))
        screen.blit(self.start_BOX, (550, 580))
        screen.blit(self.start_button_w, (600, 600))

    def update(self):
        self.draw()
        self.gal_toolbar()
        mission3()
        mission2()
        self.mission1()
        yan_san_beacon()


def update():
    screen.fill(BLACK)
    screen.blit(back_round, (0, 0))

    setup_group.draw(screen)
    start_group.draw(screen)
    setup_group.update()
    map_group.update()
    start_group.update()
    Galaxy_group.update()
    movement_group.draw(screen)
    movement_group.update()
    text_group.update()
    menu_group.update()


def belt():
    for A in range(len(asteroid_list)):
        pygame.draw.circle(screen, GRAY78, asteroid_list[A], 1)
        asteroid_list[A][1] += motionY
        asteroid_list[A][0] += motionX
        if asteroid_list[A][0] >= 950:
            ay = random.randrange(28, 240)
            asteroid_list[A][1] = ay
            ax = random.randrange(40, 50)
            asteroid_list[A][0] = ax


def statments():
    for I in range(len(star_list)):
        pygame.draw.circle(screen, GRAY3, star_list[I], 1)
        star_list[I][1] -= 0
        star_list[I][0] += 0
        if star_list[I][0] > 10:
            y1 = random.randrange(68, 510)
            star_list[I][1] = y1
            x1 = random.randrange(68, 1030)
            star_list[I][0] = x1


# ............................................... Sprite Groups ..................................................
level_group = pygame.sprite.Group()
movement_group = pygame.sprite.Group()
setup_group = pygame.sprite.Group()
grid_group = pygame.sprite.Group()
menu_group = pygame.sprite.Group()
start_group = pygame.sprite.Group()
draw_group = pygame.sprite.Group()
bullets_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
planet_group = pygame.sprite.Group()
asteroid_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
map_group = pygame.sprite.Group()
net_menu = pygame.sprite.Group()
Galaxy_group = pygame.sprite.Group()
text_group = pygame.sprite.Group()
level_1 = Level1()

# .............................................. Add Sprites to Groups ............................................

start_group.add(start_up)
Galaxy_group.add(toolbar)


