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
