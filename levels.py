
class Level1(pygame.sprite.Sprite):
    def __init__(self):
        super(Level1, self).__init__()
        self.YSimage_Down02 = pygame.image.load("images/templates/Yan_San_viewer_BOX_downloading_file2.png")
        self.YSimage_Down01 = pygame.image.load("images/templates/Yan_San_viewer_BOX_downloading_file1.png")
        self.YSimage_Down00 = pygame.image.load("images/templates/Yan_San_viewer_BOX_downloading.png")
        self.YSimage_load = pygame.image.load("images/templates/Yan_San_viewer_BOX_loading.png")
        self.YSimage_blank = pygame.image.load("images/templates/Yan_San_viewer_BOX_blank.png")
        self.YSrect_Y = 544
        self.YSrect_X = 1030
        self.YSN_asset00 = pygame.image.load("images/templates/templates_message_BOX_2x1_beacon-info.png")
        # self.YSN_icon = icon
        self.YSN_Y = 510
        self.YSN_X = 200
        self.image = pygame.image.load("images/templates/templates_gameplay_sceen.png")
        self.rect = self.image.get_rect()

    def yan_san_network(self):
        #        self.YSN_sound =
        #        self.YSN_Temp =
        #        self.YSN_title =
        pass

    #        self.YSN_asset01 =
    #        self.YSN_asset02 =

    def yan_san_viewer(self):
        pass

    def draw(self):
        self.yan_san_viewer()
        self.yan_san_network()
        self.image.blit(self.YSimage_Down00, (self.YSrect_X, self.YSrect_Y))
        self.image.blit(self.YSN_asset00, (self.YSN_X, self.YSN_Y))
        screen.blit(self.image, (0, 0))

    def update(self):
        self.draw()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load("images/ships/Yan_San FIGHTER_DRONE_dark.png")
        self.rect = self.image.get_rect()

    def draw(self):
        screen.blit(self.image, (240, 160))

    def update(self):
        self.draw()


def mission2():
    rebel_control_BOX1 = pygame.image.load(
        "images/buttons/level_image_galaxy1-level2-solar-cycle_rebelcontrol.02.2.png")
    rebel_control_BOX2 = pygame.image.load(
        "images/buttons/level_image_galaxy1-level2-solar-cycle_rebelcontrol.02.1.png")
    rebel_control_BOX3 = pygame.image.load("images/buttons/level_image_galaxy1-level2-solar-cycle_rebelcontrol.03.png")
    click = pygame.mouse.get_pressed()
    pos = pygame.mouse.get_pos()
    posX = pos[0]
    posY = pos[1]
    if 820 > posX > 685 and 480 > posY > 340:
        screen.blit(rebel_control_BOX1, (690, 346))
        text_group.add(briefing_Win)
        if click[0] == 1:
            sound_click.play()
            screen.blit(rebel_control_BOX3, (690, 346))
            text_group.add(briefing_Win)
    else:
        screen.blit(rebel_control_BOX2, (690, 346))
        text_group.remove(briefing_Win)


def mission3():
    war_alarm_BOX1 = pygame.image.load("images/buttons/level_image_galaxy1-level3-planet_nine_WAR.01.png")
    war_alarm_BOX2 = pygame.image.load("images/buttons/level_image_galaxy1-level3-planet_nine_WAR.02.png")
    war_alarm_BOX3 = pygame.image.load("images/buttons/level_image_galaxy1-level3-planet_nine_WAR.03.png")
    click = pygame.mouse.get_pressed()
    pos = pygame.mouse.get_pos()
    posX = pos[0]
    posY = pos[1]
    if 560 > posX > 514 and 520 > posY > 468:
        screen.blit(war_alarm_BOX2, (514, 468))
        text_group.add(briefing_Win)
        if click[0] == 1:
            sound_click.play()
            screen.blit(war_alarm_BOX3, (514, 468))
            text_group.add(briefing_Win)
    else:
        screen.blit(war_alarm_BOX1, (514, 468))
        text_group.remove(briefing_Win)
