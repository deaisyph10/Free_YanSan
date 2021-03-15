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

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
        self.move()


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

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
        self.move()


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

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
        self.move()


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

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def create_bullet(self):
        return Enemy_fire(self.rect.x, self.rect.y)

    def sec_bullet(self):
        return Enemy_fire(self.rect.x + 22, self.rect.y)

    def update(self):
        self.move()


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

    def spin(self):
        self.index += 1
        if self.index >= 40:
            self.index = 0
        self.image = self.images[self.index]
        if self.rect.x >= 1400 or self.rect.y >= 950:
            self.rect.x = random.randint(0, 60)
            self.rect.y = random.randint(20, 360)

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))


class Planet_yellow(pygame.sprite.Sprite):
    def __init__(self):
        self.x = 900
        self.y = 230
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("micro_images/planet1.png")
        self.surface = self.image
        self.rect = self.image.get_rect()

    def draw(self):
        screen.blit(self.image, (self.x, self.y))


class Planet_larger(pygame.sprite.Sprite):
    def __init__(self):
        self.x = 734
        self.y = 222
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/planets/planet7.png")
        self.surface = self.image
        self.rect = self.image.get_rect()

    def draw(self):
        screen.blit(self.image, (self.x, self.y))


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

    def draw(self):
        screen.blit(self.white_border, (self.x, self.y))
        self.white_border.fill(WHITE)
        screen.blit(self.charger_box, (self.x, self.y))
        self.charger_box.fill(BLACK)
        self.charger_box.blit(self.image, self.rect)
        self.charger_box.blit(self.charger_label, (20, 120))
        self.charger_box.blit(self.charger_label, (0, 120))


class Pilot(pygame.sprite.Sprite):
    def __init__(self):
        super(Pilot, self).__init__()
        self.x = pygame.mouse.get_pos()[0]
        self.y = pygame.mouse.get_pos()[1]
        self.image = pygame.image.load("images/templates/crosshairs_blue.png")
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def create_bullet(self):
        return Bullets(pygame.mouse.get_pos()[0] + 35, pygame.mouse.get_pos()[1] + 160)

    def sec_bul(self):
        return Bullets(pygame.mouse.get_pos()[0] + 65, pygame.mouse.get_pos()[1] + 160)

    def draw(self):
        screen.blit(self.image, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))

    def update(self):
        self.x = pygame.mouse.get_pos()[0]
        self.y = pygame.mouse.get_pos()[1]


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

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def move(self):
        self.rect.x += 4
        self.rect.y += 1
        if self.rect.x > 400:
            self.rect.x += 3
            self.rect.y += 2
        if self.rect.x > 1200:
            self.rect.x = 0
            self.rect.y = 0

    def update(self):
        self.move()


class Title_text(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 280
        self.y = 4
        self.title_text = str("----FREE-------(Y//:YanSan)----")
        self.title_surface = mono_font.render(self.title_text, True, WHITE)
        self.image = self.title_surface
        self.rect = self.image.get_rect()

    def draw(self):
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

    def draw(self):
        self.sur.fill(GRAY7)
        back_round.blit(self.sur, (self.x, self.y))


class Header(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 1
        self.y = 1
        self.sur = pygame.Surface((screen_width - 2, cell_pxl_size - 32))
        self.rect = self.sur.get_rect()
        self.image = self.sur
        self.white_border = pygame.Rect(self.x - 1, self.y - 1, screen_width, cell_pxl_size - 30)
        self.dream_logo_2 = dream_logo_2
        self.LLC_icon = LLC_icon_micro

    def draw(self):
        screen.blit(self.white_border, (0, 0))
        screen.blit(self.image, (1, 1))
        screen.blit(self.dream_logo_2, (10, 10))
        screen.blit(self.LLC_icon, (60, 10))


class LeftToolbar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sur = pygame.Surface((200, 400))
        self.rect = self.sur.get_rect()
        self.image = self.sur
        self.sur.fill(GRAY7)
        self.white_border = pygame.Surface((200, 400))
        self.white_border.fill(WHITE)

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

    def draw(self):
        self.white_border.blit(self.sur, (2, 2))
        screen.blit(self.white_border, (0, 50))

    def update(self):
        self.BattleKey()
        self.boxes()


class YanSan_Window(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 998
        self.y = 50
        self.white_border = pygame.Surface((200, 400))
        self.white_border.fill(WHITE)
        self.sur = pygame.Surface((200, 400))
        self.rect = self.sur.get_rect()
        self.image = self.sur
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

    def draw(self):
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
        self.header()
        self.X_drive()
        self.Y_drive()
        self.Z_drive()
        self.YanSan_logo()


class Menu_Box1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 450
        self.sur = pygame.Surface((200, 200))
        self.rect = self.sur.get_rect()
        self.image = self.sur
        self.sur.fill(BLACK)
        self.white_border = pygame.Surface((202, 202))
        self.Wrect = self.white_border.get_rect()
        self.white_border.fill(WHITE)

    def draw(self):
        screen.blit(self.image, (0, 450))
        screen.blit(self.white_border, (0, 450))


class PlayerInfobox(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 200
        self.y = 400
        self.sur = pygame.Surface((self.x, self.y))
        self.Bsur = pygame.Surface((self.x, self.y))
        self.playership()
        self.score(0)

    def playership(self):
        self.image = pygame.image.load("images/ships/13B.png")
        self.rect = self.image.get_rect()

    def overheat(self):
        self.im2 = pygame.image.load("images/ships/13B_overheat.png")
        self.im2rect = self.im2.get_rect()
        self.sur.blit(self.im2, (15, 50))

    def score(self, Ascore):
        self.text_sur = game_font_18.render("_Asteriods_Kills_" + str(Ascore), True, WHITE)

    def draw(self):
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
        self.sur = pygame.Surface((200, 200 - 1))
        self.image = self.sur
        self.white_border = pygame.Surface((202, 201))
        self.rect = self.sur.get_rect()
        self.Wrect = self.white_border.get_rect()

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

    def draw(self):
        screen.blit(self.image, (200, 200))

    def update(self):
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


drone = Drone()
asteroid = Asteroid()
purple_ship = Purple_ship()
yellow_ship = Yellow_ship()
grey_ship = Grey_ship()
red_ship = Red_ship()
player = Pilot()
planet_larger = Planet_larger()
planet_yellow = Planet_yellow()
LeftToolbar = LeftToolbar()
header = Header()
YanSan_window = YanSan_Window()
playerInfobox = PlayerInfobox()
photon_charger_window = Photon_Charger_Window()
Main_Menu = Main_Menu()
Menu_Box1 = Menu_Box1()
game_title = Title_text()
net_menu_sprite = Network_Map_Window()
net_menu.add(net_menu_sprite)
menu_group.add(header, game_title, photon_charger_window, YanSan_window, Menu_Box1)
battle_sprites.add(red_ship, yellow_ship, purple_ship)
menu_group.add(playerInfobox, photon_charger_window, YanSan_window, LeftToolbar)
all_sprites.add(planet_larger, planet_yellow, asteroid, drone, grey_ship, red_ship, purple_ship, yellow_ship, player)
grid_group.add(Main_Menu)
enemy_bullets = Enemy_Bullets(x, y)
bullet = Bullets(x, y)
bullets_group.add(enemy_bullets)

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

cockpit = Cockpit()
