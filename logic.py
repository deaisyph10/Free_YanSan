def text(self):
    text = game_font_monospace_36.render("FREE YanSan", True, WHITE)
    text_rect = text.get_rect()
    text_rect.center = (120, 20)


def button():
    click = pygame.mouse.get_pressed()
    pos = pygame.mouse.get_pos()
    posX = pos[0]
    posY = pos[1]

