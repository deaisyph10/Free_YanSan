import sys
from manage import *
from YanSan_Network import *


class Main:
    def __init__(self):
        update()
        clock.tick(FPS)

# ................................................. {Game Loop} ...................................................

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    Main()
    pygame.display.update()
