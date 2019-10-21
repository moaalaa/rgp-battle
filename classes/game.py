import random


# colors class is responsible for terminal background colors
class Color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Player Class Responsible for all players functions
class Player:

    # init method define instance property by using 'self'
    # if property nit found will serche class properties
    def __init__(self, hp, mp, attack, defence, magic):
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.attack_low = attack - 10
        self.attack_high = attack + 10
        self.defence = defence
        self.magic = magic
        self.actions = ['Attack', 'Magic']

    def generate_damage(self):
        return random.randrange(self.attack_low, self.attack_high)

    def generate_spell_damage(self, spell):
        magic_low = self.magic[spell]['damage'] - 5
        magic_high = self.magic[spell]['damage'] + 5

        return random.randrange(magic_low, magic_high)

    def take_damage(self, damage):
        self.hp -= damage

        if self.hp < 0:
            self.hp = 0

        return self.hp

    def heal(self, damage):
        self.hp += damage

        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.max_mp
    
    def reduce_mp(self, cost):
        self.mp -= cost

    def get_spell_name(self, spell):
        return self.magic[spell]['name']

    def get_spell_cost(self, spell):
        return self.magic[spell]['cost']

    def choose_actions(self):
        action = 1
        print(Color.OKBLUE + Color.BOLD + "Choose Action" + Color.ENDC)

        for item in self.actions:
            print(str(action) + ": " + item)
            action += 1
    
    def choose_spell(self):
        spell_index = 1 
        print(Color.OKBLUE + Color.BOLD + "Choose Magic Spell" + Color.ENDC)

        for spell in self.magic:
            print(str(spell_index) + ": " + spell['name'], "(cost: " + str(spell['cost']) + ")")
            spell_index += 1
