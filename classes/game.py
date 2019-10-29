import random


# colors class is responsible for terminal background colors
class Color:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


# Player Class Responsible for all players functions
class Player:

    # init method define instance property by using "self"
    # if property init found will search class properties
    def __init__(self, name, hp, mp, attack, defence, magic, items):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.attack_low = attack - 10
        self.attack_high = attack + 10
        self.defence = defence
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]
        self.actions = ["Attack", "Magic", "Items"]

    def generate_damage(self):
        return random.randrange(self.attack_low, self.attack_high)

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

    def choose_actions(self):
        action_index = 1
        print("\n" + "-> " + Color.BOLD + Color.WARNING +self.name + Color.ENDC)
        print(Color.OKBLUE + Color.BOLD + "    Choose Action" + Color.ENDC)

        for action in self.actions:
            print("        " + str(action_index) + ": " + action)
            action_index += 1
    
    def choose_spell(self):
        spell_index = 1 
        print("\n" + Color.OKBLUE + Color.BOLD + "    Choose Magic Spell" + Color.ENDC)

        for spell in self.magic:
            print("        " + str(spell_index) + ": " + spell.name, "(cost: " + str(spell.cost) + ")", Color.WARNING + Color.BOLD + "(" + spell.type  + ")" + Color.ENDC)
            spell_index += 1

    def choose_item(self):
        item_index = 1 
        print("\n" + Color.OKBLUE + Color.BOLD + "    Choose Item" + Color.ENDC)

        for item_dictionary in self.items:
            print("        " + str(item_index) + ": " + item_dictionary["item"].name, Color.FAIL + Color.BOLD + "(x" + str(item_dictionary["quantity"])  + ")", Color.WARNING + Color.BOLD + "(" + item_dictionary["item"].description  + ")" + Color.ENDC)
            item_index += 1

    def choose_target(self, enemies):
        index = 1
        
        print("\n" + Color.FAIL + Color.BOLD + "    TARGET: " + Color.ENDC)

        for enemy in enemies:
            if enemy.get_hp() != 0:
                print("        " + str(index) + ":" + enemy.name)
                index += 1

        choice = int(input("    Choose Target: ")) - 1
        
        if enemies[choice].get_hp() == 0:
            print(Color.OKBLUE + Color.BOLD + " Enemy " + enemies[choice].name.strip() + " has Been Dead!")
            del enemies[choice]
            return None
        
        return enemies[choice]

    def get_enemy_stats(self):
        """
            Our HP bar Consists of 25 chars and if it's 100% so it can divided by 2 half
                
                HP  / Max HP    Get Result Percentage   Divide By 2 And Get Half Value
            Ex: (50 / 200 )      * 100                  / 2
        """
        hp_bar = ""
        hp_bar_ticks = (self.hp / self.max_hp) * 100 / 2

        # Generate HP Bar ticks
        while hp_bar_ticks > 0:
            hp_bar += "█"
            hp_bar_ticks -= 1
        
        # Generate HP Bar White Spaces
        while len(hp_bar) < 50:
            hp_bar += " "

        # Generate proper white spaces for enemy states
        hp_string = str(self.hp) + "/" + str(self.max_hp)
        current_hp = ""

        """
            11 stands for the complete 11 chars in HP status
            11200/11200
        """
        if len(hp_string) < 11:
            decreased = 11 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string
        
        # Print Stats
        print("\n")
        print(Color.BOLD + self.name + "                      " + 
                   current_hp + " |" + Color.FAIL + hp_bar + Color.ENDC +"|")

    def get_stats(self):
        """
            Our HP bar Consists of 25 chars and if it's 100% so it can divided by 4 quartes
                
                HP  / Max HP    Get Result Percentage   Divide By 4 And Get Quarter Value
            Ex: (50 / 200 )      * 100                  / 4
        """
        hp_bar = ""
        hp_bar_ticks = (self.hp / self.max_hp) * 100 / 4
        
        """
            Our MMP bar Consists of 10 chars and if it's 100% so it can divided by 10 pieces
                
                MP  / Max MP    Get Result Percentage   Divide By 10 And Get Piece Value
            Ex: (50 / 200 )      * 100                  / 10
        """
        mp_bar = ""
        mp_bar_ticks = (self.mp / self.max_mp) * 100 / 10

        # Generate HP Bar ticks
        while hp_bar_ticks > 0:
            hp_bar += "█"
            hp_bar_ticks -= 1
        
        # Generate HP Bar White Spaces
        while len(hp_bar) < 25:
            hp_bar += " "

        # Generate MP Bar Ticks
        while mp_bar_ticks > 0:
            mp_bar += "█"
            mp_bar_ticks -= 1
        
        # Generate MP Bar White Spaces
        while len(mp_bar) < 10:
            mp_bar += " "

        # Generate proper white spaces for player states
        hp_string = str(self.hp) + "/" + str(self.max_hp)
        current_hp = ""

        """
            9 stands for the complete 9 chars in HP status
            3000/3000
        """
        if len(hp_string) < 9:
            decreased = 9 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        mp_string = str(self.mp) + "/" + str(self.max_mp)
        current_mp = ""

        """
            9 stands for the complete 9 chars in MP status
            1000/1000
        """
        if len(mp_string) < 9:
            decreased = 9 - len(mp_string)

            while decreased > 0:
                current_mp += " "
                decreased -= 1

            current_mp += mp_string
        else:
            current_mp = mp_string

        # Print Stats
        print("\n")
        print(Color.BOLD + self.name[0:4] + "                      " + 
                   current_hp + " |" + Color.OKGREEN + hp_bar + Color.ENDC +"|                " + Color.BOLD +
                   current_mp + " |" + Color.OKBLUE  + mp_bar + Color.ENDC + "|")
    
    def choose_enemy_spell(self):
        magic_choice = random.randrange(0, len(self.magic))
        spell = self.magic[magic_choice]
        magic_damage = spell.generate_damage()

        # If Spell Cost Greater Than Player "MP" Return To Choose Action Menu 
        if spell.cost > self.mp:
            self.choose_enemy_spell()    
        else:
            return spell, magic_damage
