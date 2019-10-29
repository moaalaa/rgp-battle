import random

from classes.game import Color, Player
from classes.inventory import Item
from classes.magic import Spell

# Create Black Magic Spells
fire = Spell("Fire", 150, 1000, "black")
thunder = Spell("Thunder", 100, 600, "black")
blizzard = Spell("blizzard", 50, 200, "black")

# Create White Magic Spells
cure = Spell("Cure", 120, 420, "white")
cura = Spell("Cura", 180, 1000, "white")


# Create Inventory Items
potion = {"item": Item("Postion", 'potion', "Heals 50 HP", 50), "quantity": 5}
high_potion = {"item": Item("High Postion", 'potion', "Heals 100 HP", 100), "quantity": 3}
super_potion = {"item": Item("Super Postion", 'potion', "Heals 200 HP", 200), "quantity": 1}
elixir = {"item": Item("Elixir", 'elixir', "Fully Restores HP/MP of one party member", 9999), "quantity": 2} # no need for prop number here so give a high one
high_elixir = {"item": Item("High Elixir", 'elixir', "Fully Restores part's HP/MP", 9999), "quantity": 1} # no need for prop number here so give a high one

grenade = {"item": Item("Grenade", "attack", "Deals 500 Damage", 500), "quantity": 1}


# Players Instance
player_magic_list = [fire, thunder, blizzard, cure, cura]
player_items_list = [potion, high_potion, super_potion, elixir, high_elixir, grenade]
player1 = Player("Alaa", 3000, 1000, 320, 34, player_magic_list, player_items_list)
player2 = Player("Hamza", 2750, 1200, 120, 34, player_magic_list, player_items_list)
player3 = Player("Habiba", 4000, 1500, 500, 34, player_magic_list, player_items_list)

players = [player1, player2, player3]

enemy_magic_list = [fire, thunder, blizzard, cure]
enemy_items_list = [potion, high_potion, super_potion, elixir, high_elixir, grenade]
enemy1 = Player("Fire Dragon", 20200, 2200, 500, 25, enemy_magic_list, [])
enemy2 = Player("Dark Elf   ", 1500, 200, 800, 300, enemy_magic_list, [])
enemy3 = Player("Ghoul      ", 1300, 300, 900, 200, enemy_magic_list, [])

enemies = [enemy1, enemy2, enemy3]


running = True
i = 0

print(Color.FAIL + Color.BOLD + "An Enemy Attacks!" + Color.ENDC)

while running:
    print("===========================")

    # Print Members Hints
    print("\n\n")
    print("NAME                            HP                                                MP")
    
    # Print Members Stats
    for player in players:
        player.get_stats()

    print("\n")

    # Print Enemies Stats
    for enemy in enemies: 
        enemy.get_enemy_stats()
        
    print("\n")

    # Give Every Member A turn
    for player in players:
        
        # Player Turn
        player.choose_actions()
        player_choice = int(input("    Choose Action: ")) - 1

        # Normal Attack
        if player_choice == 0:
            damage = player.generate_damage()
            enemy = player.choose_target(enemies)
            
            if enemy == None:
                continue
            
            enemy.take_damage(damage)

            print(Color.OKBLUE + "\n You Attacked " + enemy.name + " For", damage, "Points of Damage. " + Color.ENDC)

        # Magic Attack
        elif player_choice == 1:
            player.choose_spell()
            spell_choice = int(input("    Choose Spell: ")) - 1
            
            if spell_choice == -1:
                continue

            spell = player.magic[spell_choice]
            spell_damage = spell.generate_damage()
            current_mp = player.get_mp()

            # If SpellCost Greater Than Player "MP" Return To Choose Action Menu 
            if spell.cost > current_mp :
                print(Color.FAIL + "\nNot Enough MP\n" + Color.ENDC)
                continue
            
            player.reduce_mp(spell.cost)        
            
            if spell.type == "white":
                player.heal(spell_damage)
                print(Color.OKGREEN + "\n" + spell.name + " Heals for", str(spell_damage), "HP. " + Color.ENDC)

            elif spell.type == "black":
                enemy = player.choose_target(enemies)

                if enemy == None:
                    continue

                enemy.take_damage(spell_damage)
                print(Color.OKBLUE + "\n" + spell.name + " Deals With", str(spell_damage), "Points of Damage to " + enemy.name + Color.ENDC)
        
        # Items Attack
        elif player_choice == 2:
            player.choose_item()
            item_choice = int(input("    Choose Item: ")) - 1
            
            if item_choice == -1:
                continue
            
            item = player.items[item_choice]["item"]
            
            if player.items[item_choice]["quantity"] == 0:
                print(Color.FAIL + "\n" + item.name + " Not Available in Stock" + Color.ENDC)
                continue

            player.items[item_choice]["quantity"] -= 1 # reduse the item quantity and save it in items object
            
            
            if item.type == "potion":
                player.heal(item.prop)
                print(Color.OKGREEN + "\n" + item.name + " Heals for", str(item.prop), "HP. " + Color.ENDC)

            elif item.type == "elixir":

                if item.name == "High Elixir":
                    for p in players:
                        p.hp = p.max_hp
                        p.mp = p.max_mp
                        print(Color.OKGREEN + "\n" + item.name + " Fully restors "+ p.name +" HP/MP." + Color.ENDC)
                
                else:
                    player.hp = player.max_hp
                    player.mp = player.max_mp
                    print(Color.OKGREEN + "\n" + item.name + " Fully restors HP/MP." + Color.ENDC)

            
            elif item.type == "attack":
                enemy = player.choose_target(enemies)
                
                if enemy == None:
                    continue

                enemy.take_damage(item.prop)
                print(Color.OKBLUE + "\n" + item.name + " Deals", str(item.prop), "Points of Damage to " + enemy.name + Color.ENDC)


    # game continues check
    defeated_enemies = 0
    defeated_players = 0
    
    # Check Defeated Enemies Count
    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1

    # Check Defeated Players Count
    for player in players:
        if player.get_hp() == 0:
            defeated_players += 1

    if defeated_enemies == 2:
        print(Color.OKGREEN + "You Win!" + Color.ENDC)
        running = False

    elif defeated_players == 2:
        print(Color.FAIL + "You Loose!" + Color.ENDC)
        running = False

    # Enemy Turn
    for enemy in enemies:
        enemy_choice = random.randrange(0, 2)

        if enemy_choice == 0:
            # Get Target Rand Start From 0 and end at 2 not 3 our limit is 3 
            target = random.randrange(0, 3)
            player_target = players[target]
            enemy_damage = enemy.generate_damage()
            
            player_target.take_damage(enemy_damage)
            print(Color.BOLD + Color.FAIL + "Enemy " + enemy.name.strip() + " Attacked "+ player_target.name +" For", enemy_damage, "Points of Damage. " + Color.ENDC)

        elif enemy_choice == 1: 
            spell, magic_damage = enemy.choose_enemy_spell()
            enemy.reduce_mp(spell.cost)
            
            if spell.type == "white":
                enemy.heal(magic_damage)
                print(Color.OKGREEN + "\n" + spell.name.strip() + " Heals " + enemy.name + " for", str(magic_damage), "HP. " + Color.ENDC)

            elif spell.type == "black":
                # Get Target Rand Start From 0 and end at 2 not 3 our limit is 3 
                target = random.randrange(0, 3)
                player_target = players[target]
                player_target.take_damage(magic_damage)
                print(Color.BOLD + Color.FAIL + "\n" + spell.name + " Deals With", str(magic_damage), "Points of Damage to " + player_target.name + Color.ENDC)
