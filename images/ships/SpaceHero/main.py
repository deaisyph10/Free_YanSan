# import pygame
# import sys
# import random

# pygame.init()
battle_screen_width = 400
battle_screen_height = 400
battle_screen = (battle_screen_width, battle_screen_height)
# pygame.display.set_caption("Maze_World")
# pygame.display.get_surface()
# clock = pygame.time.Clock()
# FPS = 160


class Red_ship(pygame.sprite.Sprite):
    def __init__(self):
        super(Red_ship, self).__init__()
        self.image = pygame.image.load("red_ship_micro.png")
        self.im2 = pygame.image.load("red_ship_micro_hit.png")
        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 325
        self.movex = 0  # move along X
        self.movey = 0  # move along Y

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
        screen.blit(self.image, (self.rect.x, self.rect.y))


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
        if self.rect.colliderect(cl1_rect):
            self.kill()


class Purple_ship(pygame.sprite.Sprite):
    def __init__(self):
        super(Purple_ship, self).__init__()
        self.image = pygame.image.load("purple_ship_micro.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 400)
        self.rect.y = random.randint(0, 200)
        self.movex = 0  # move along X
        self.movey = 0  # move along Y

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
        self.image.fill((255, 255, 255))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        self.rect.y += 1
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
        self.image = pygame.image.load("yellow_ship_micro.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 400)
        self.rect.y = random.randint(0, 200)
        self.movex = 0  # move along X
        self.movey = 0  # move along Y

    def move(self):
        self.rect.x += 0
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
        screen.blit(self.image, (self.rect.x, self.rect.y))


class Grey_ship(pygame.sprite.Sprite):
    def __init__(self):
        super(Grey_ship, self).__init__()
        self.image = pygame.image.load("grey_ship_micro.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 400)
        self.rect.y = random.randint(0, 200)
        self.movex = 0  # move along X
        self.movey = 0  # move along Y

    def move(self):
        self.rect.x += random.randint(-3, 3)
        self.rect.y += random.randint(-3, 3)
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
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def check_collision(self):
        if self.rect.colliderect(bullets):
            return self.kill()


drone_pos = []
drone_rect = []

x = 0
y = 0
steps = 2
purple_ship = Purple_ship()
yellow_ship = Yellow_ship()
grey_ship = Grey_ship()
red_ship = Red_ship()
bullets = Bullet(x, y)
enemy_bullets = Enemy_Bullets(x, y)
All_sprites = pygame.sprite
All_sprites.add(red_ship, yellow_ship, purple_ship)
Draw_group = pygame.sprite
bullets_group = pygame.sprite
bullets_group.add(bullets, enemy_bullets)
cl1_rect = grey_ship
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                cl1 = Draw_group.add(grey_ship.create_clone())
                drone_pos.append(cl1)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                red_ship.control(-steps, 0)
            if event.key == pygame.K_RIGHT:
                red_ship.control(steps, 0)
            if event.key == pygame.K_UP:
                bullets_group.add(red_ship.create_bullet())
                bullets_group.add(red_ship.sec_bullet())
            if event.key == pygame.K_SPACE:
                purple_ship.attack()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                red_ship.control(steps, 0)
            if event.key == pygame.K_RIGHT:
                red_ship.control(-steps, 0)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0, 0, 0))
    bullets_group.draw(screen)
    All_sprites.update()
    Draw_group.update()
    bullets_group.update()
    # pygame.display.update()
    # clock.tick(FPS)
