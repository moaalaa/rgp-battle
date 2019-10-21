from classes.game import Color, Player

magic = [
    {"name": "fire", "cost": 100, "damage": 80},
    {"name": "thunder", "cost": 90, "damage": 60},
    {"name": "blizzard", "cost": 5, "damage": 40},
]

player = Player(460, 56, 60, 34, magic)
enemy = Player(1200, 65, 45, 25, magic)

running = True
i = 0

print(Color.FAIL + Color.BOLD + "An Enemy Attacks!" + Color.ENDC)

while running:
    print("===========================")
    
    # Player Turn
    player.choose_actions()
    choice = input("Choose Action: ")
    player_choice = int(choice) - 1

    if player_choice == 0:
        damage = player.generate_damage()
        enemy.take_damage(damage)
        print("You Attacked For", damage, "Points of Damage.")
    elif player_choice == 1:
        player.choose_spell()
        spell_choice = int(input("Choose Spell: ")) - 1
        magic_damage = player.generate_spell_damage(spell_choice)
        spell = player.get_spell_name(spell_choice)
        spell_cost = player.get_spell_cost(spell_choice)
        current_mp = player.get_mp()

        if spell_cost > current_mp :
            print(Color.FAIL + "\nNot Enough MP\n" + Color.ENDC)
            continue

        player.reduce_mp(spell_cost)
        enemy.take_damage(magic_damage)
        print(Color.OKBLUE + "\n" + spell + " Deals", str(magic_damage), "Points of Damage. " + Color.ENDC)

    # Enemy Turn
    enemy_choice = 1
    enemy_damage = enemy.generate_damage()
    player.take_damage(enemy_damage)
    print("Enemy Attacked For", enemy_damage, "Points of Damage. ")

    print('------------------------------------')
    print("Enemy HP: " + Color.FAIL + str(enemy.get_hp()) + '/' + str(enemy.get_max_hp()) + Color.ENDC + "\n")
    print("Player HP: " + Color.OKGREEN + str(player.get_hp()) + '/' + str(player.get_max_hp()) + Color.ENDC + "\n")
    print("Player MP: " + Color.OKBLUE + str(player.get_mp()) + '/' + str(player.get_max_mp()) + Color.ENDC + "\n")

    # game continues check
    if enemy.get_hp() == 0:
        print(Color.OKGREEN + "You Win!" + Color.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(Color.FAIL + "You Loose!" + Color.ENDC)
        running = False
