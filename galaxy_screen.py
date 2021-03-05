class GalaxyWin(pygame.sprite.Sprite):
    def __init__(self):
        super(GalaxyWin, self).__init__()
        self.sur = pygame.Surface((600, 300))
        self.rect = self.sur.get_rect()
        self.sur.fill(GRAY31)
        self.moveX = 0
        self.moveY = 0
        self.move(0, 0)
        self.headertext()
        self.buttons()

    def move(self, mx, my):
        self.moveX += mx
        self.moveY += my
        self.rect.x = self.moveX + self.rect.x
        self.rect.y = self.moveY + self.rect.y

    def buttons(self):
        choice1 = pygame.Surface((120, 80))
        choice2 = pygame.Surface((120, 80))
        choice3 = pygame.Surface((120, 80))
        choice4 = pygame.Surface((120, 80))
        click = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        posX = pos[0]
        posY = pos[1]
        if 300 > posX > 180 and 300 > posY > 220:
            self.sur.blit(choice1, (10, 80))
            choice1.fill(GRAY54)
        if 440 > posX > 320 and 300 > posY > 220:
            self.sur.blit(choice2, (160, 80))
            choice2.fill(GRAY54)
        if 580 > posX > 460 and 300 > posY > 220:
            self.sur.blit(choice3, (310, 80))
            choice3.fill(GRAY54)
        if 720 > posX > 600 and 300 > posY > 220:
            self.sur.blit(choice4, (460, 80))
            choice4.fill(GRAY34)
            if click[0] == 1:
                self.kill()

    def headertext(self):
        select = str("Select a Galaxy to Explore")
        headertxt = game_font.render(select, True, WHITE)
        self.sur.blit(headertxt, (0, 10))

    def render(self):
        screen.blit(self.sur, (160, 120))

    def update(self):
        self.render()


