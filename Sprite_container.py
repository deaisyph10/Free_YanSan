class Alien_right(pygame.sprite.Sprite):
    def __init__(self):
        super(Alien_right, self).__init__()
        self.x = 850
        self.y = 300
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
        self.y = 300
        self.x = 850
        self.y += motionY
        self.x += motionX

    def render(self):
        screen.blit(self.image, (self.x, self.y))


class Alien_left(pygame.sprite.Sprite):
    def __init__(self):
        super(Alien_left, self).__init__()
        self.x = 40
        self.y = 300
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
        self.y = 300
        self.y += motionY
        self.x += motionX

    def render(self):
        screen.blit(self.image, (self.x, self.y))


alien_left = Alien_left()
alien_right = Alien_right()
character_group.add(alien_left, alien_right)

class Cockpit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/templates/Cockpit_Spaceship.png")
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 50

    def update(self):
        self.move()
        self.render()

    def render(self):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        if self.x >= 1:
             self.x = motionX * -1
        if self.y >= 1:
             self.y = motionY * -1
        self.y = 50
        self.y += motionY
        self.x += motionX

class Cursor(pygame.sprite.Sprite):
    def __init__(self):
        super(Cursor, self).__init__()
        self.movex = 0
        self.movey = 0
        self.sur = pygame.Surface((168, 148))
        self.rect = self.sur.get_rect()

    def curpos(self, cx, cy):
        self.movex += cx
        self.movey += cy
        posX = self.movex + 194
        posY = self.movey + 194
        self.rect = pygame.Rect(posX, posY, 194, 194)
        if self.rect.x >= 790:
            self.rect.x = 790
        if self.rect.x <= 194:
            self.rect.x = 194
        if self.rect.y >= 600:
            self.rect.y = 600
        if self.rect.y <= 194:
            self.rect.y = 194

    def update(self):
        world_map.sur.blit(self.sur, self.rect)
        self.sur.fill(WHITE)
        self.curpos(0, 0)




cockpit = Cockpit()
