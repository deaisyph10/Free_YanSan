import pygame
import random
import sys
import os
from Colors import *

pygame.init()
pygame.font.init()
cell_pxl_size = 70
cell_count = 10
screen = pygame.display.set_mode((cell_pxl_size * cell_count, cell_pxl_size * cell_count))
pygame.display.set_caption("FREE_YanSan")
clock = pygame.time.Clock()
back_round = pygame.image.load("Stars.png")
music = pygame.mixer.Sound("monkeys wedding_low.wav")
game_font = pygame.font.Font("freesansbold.ttf", 42)

score_text = str("FREE YanSan")
score_surface = game_font.render(score_text, True, white)
score_x = int(cell_pxl_size * 5)
score_y = 22
score_rect = score_surface.get_rect(center=(score_x, score_y))


class Player(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        img = pygame.image.load(os.path.join('', '')).convert()
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()


box_1 = pygame.Rect(1, 1, 698, 40)
box_1_w = pygame.Rect(0, 0, 700, 42)

box_2 = pygame.Rect((1, 620, (cell_pxl_size * 3), int(cell_pxl_size)))
box_2_w = pygame.Rect((0, 620-1, (cell_pxl_size * 3)+2, int(cell_pxl_size)+2))

box_3 = pygame.Rect(330, 620, (cell_pxl_size * 3)-2, int(cell_pxl_size))
box_3_w = pygame.Rect(330-1, 620-1, (cell_pxl_size * 3), int(cell_pxl_size)+2)

box_icon = pygame.Rect(550, 620, (cell_pxl_size * 2), int(cell_pxl_size))
box_icon_w = pygame.Rect(550-1, 620-1, (cell_pxl_size * 2)+2, int(cell_pxl_size)+2)

message_box = pygame.Rect(480, 60, 200, 300-1)
message_box_w = pygame.Rect(480-1, 60-1, 200+2, 300+1)

dream_logic_icon = pygame.image.load("Yan_San_rainbow_phaser.png")
dream_logic_icon_surface = dream_logic_icon
dream_logic_icon_rect = dream_logic_icon.get_rect()
dream_logic_icon_rect.x = 190
dream_logic_icon_rect.y = 630

planet_2_icon = pygame.image.load("planet7.png")
planet_2_icon_surface = planet_2_icon
planet_2_icon_rect = planet_2_icon.get_rect()
planet_2_icon_rect.x = 480
planet_2_icon_rect.y = 100

planet_icon = pygame.image.load("planet1.png")
planet_icon_surface = planet_icon
planet_icon_rect = planet_icon.get_rect()
planet_icon_rect.x = 155
planet_icon_rect.y = 630

purple_ship = pygame.image.load("large_purp.png")
purple_ship_surface = purple_ship
purple_ship_rect = purple_ship.get_rect()
purple_ship_rect.x = 150
purple_ship_rect.y = 400

red_ship = pygame.image.load("red_ship.png")
red_ship_surface = red_ship
red_ship_rect = purple_ship.get_rect()
red_ship_rect.x = 100
red_ship_rect.y = 260

yellow_ship = pygame.image.load("blue_ship.png")
yellow_ship_surface = yellow_ship
yellow_ship_rect = yellow_ship.get_rect()
yellow_ship_rect.x = 340
yellow_ship_rect.y = 310

player = Player()   # spawn player
player.rect.x = 0   # go to x
player.rect.y = 0   # go to y
player_list = pygame.sprite.Group()
player_list.add(player)
snow_list = []
for i in range(1000):
    x = random.randrange(0, 700)
    y = random.randrange(0, 700)
    snow_list.append([x, y])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for i in range(len(snow_list)):
        pygame.draw.circle(screen, white, snow_list[i], 1)
        snow_list[i][1] += 1
        if snow_list[i][1] > 600:
            y = random.randrange(-550, -360)
            snow_list[i][1] = y
            x = random.randrange(0, 700)
            snow_list[i][0] = x
    screen.blit(red_ship_surface, red_ship_rect)
    screen.blit(yellow_ship_surface, yellow_ship_rect)
    screen.blit(purple_ship_surface, purple_ship_rect)
    pygame.draw.rect(screen, white, box_1_w)
    pygame.draw.rect(screen, white, box_2_w)
    pygame.draw.rect(screen, white, box_3_w)
    pygame.draw.rect(screen, white, box_icon_w)
    pygame.draw.rect(screen, grey, box_1)
    pygame.draw.rect(screen, grey, box_2)
    pygame.draw.rect(screen, black, box_3)
    pygame.draw.rect(screen, black, box_icon)
    screen.blit(dream_logic_icon_surface, dream_logic_icon_rect)
    screen.blit(score_surface, score_rect)
    screen.blit(planet_icon_surface, planet_icon_rect)
    screen.blit(back_round, (0, 0))
    pygame.draw.rect(screen, white, message_box_w)
    pygame.draw.rect(screen, black, message_box)
    screen.blit(planet_2_icon_surface, planet_2_icon_rect)
    player_list.draw(screen)  # draw player
    pygame.display.update()
    screen.fill(black)
    music.play()
    clock.tick(72)
