import  pygame

class units(pygame.sprite.Sprite):
    def __init__(self):
        super(units, self)
        self.image = []
        self.rect
        self.hp = 0
        self.cost = 0
        self.time= 0

    def yanSan_pilot(self):
        self.hp = 1080
        self.cost = 75000
        self.time = 100

    def resident(self):
        self.hp = 360
        self.cost = 24000
        self.time = 10

    def labor_droid(self):
        self.hp = 720
        self.cost = 50000
        self.time = 40

    def URA_pilot(self):
        self.hp = 1080
        self.cost = 0
        self.time = 0

    def URA_civilian(self):
        self.hp = 360
        self.cost = 0
        self.time = 0

    def URA_elite(self):
        self.hp = 720
        self.cost = 0
        self.time = 0


class Ships(pygame.sprite.Sprite):
    def __init__(self):
        super(Ships, self).__init__()
        self.image = []
        self.rect

    def fighter_drone(self):
        self.hp = 129600
        self.cost = 240000
        self.time = 100

    def mechanic_drone(self):
        self.hp =64800
        self.cost = 120000
        self.time = 250

    def explorer(self):
        self.hp = 32400
        self.cost =80000
        self.time = 75

    def rebel_fighter(self):
        self.hp = 129600
        self.cost = 0
        self.time = 0

    def rebel_cruiser(self):
        self.hp = 64800
        self.cost = 0
        self.time = 0

    def rebel_transport(self):
        self.hp = 32400
        self.cost = 0
        self.time = 0


class Structures(pygame.sprite.Sprite):
    def __init__(self):
        super(Structures, self).__init__()
        self.image = []
        self.rect

    def beacon(self):
        self.hp = 46656000
        self.cost = 24000000
        self.time = 2000

    def control_center(self):
        self.hp = 11664000
        self.cost = 12000000
        self.time = 1200

    def tactical_hub(self):
        self.hp = 15552000
        self.cost = 8500000
        self.time = 800

    def rebel_mil_outpost(self):
        self.hp = 46656000
        self.cost = 0
        self.time = 0

    def rebel_residence(self):
        self.hp = 11664000
        self.cost = 0
        self.time = 0

    def rebel_refinery(self):
        self.hp = 15552000
        self.cost = 0
        self.time = 0


class YanSan(pygame.sprite.Sprite):
    def __init__(self):
        super(YanSan, self).__init__()
#        self.icon = icon
        self.greeting = print(str("Hello Pilot"))
#        self.cycle =
#        self.update =
#        self.quit =
#        self.runserver =
        self.LOC = 0
        self.OUT = 0
        self.OBJ = 0
        self.loc_dic ={}
        self.OUT_dic = {}
        self.OBJ_dic = {}

    def location(self):
        self.gal = 0
        self.sec = 0
        self.reg = 0
        self.X = 0
        self.Y = 0
        self.Z = 0

    def output(self):
        self.x = 0
        self.t = 0
        self.m = 0

    def object(self):
        self.u = 0
        self.s = 0
        self.S = 0


def yan_san_beacon():
            pygame.image.load("images/ships/YanSan_BEACON_Eastern_Ridge_GAL1.sm.png")
            pygame.image.load("images/ships/YanSan_BEACON_Eastern_Ridge_GAL1.thm.png")