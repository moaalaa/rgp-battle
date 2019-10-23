import random


class Spell:
    def __init__(self, name, cost, damage, type):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.type = type
    
    def generate_damage(self):
        low_damage = self.damage - 15
        high_damage = self.damage + 15

        return random.randrange(low_damage, high_damage)
