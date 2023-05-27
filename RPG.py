import random

# Variables


maxhp = 2
hp = maxhp
lvl = 1
x = 0.5
invent = []
maxxp = lvl * 5 + 10
enemy_lvl = lvl
firstinvent = ranint = xp = y = 0
g = 0
hotelgreetings = ("Hello", "Hey", "Good evening", "Welcome to my hotel", "Good to see you")
moved_already = activated = False


# Functions


def save():
    gold = str(g)
    shp = str(int(hp))
    if int(hp) < hp:
        shp = str(int(shp) + 1)

    def savecodeprint(savecode):
        print('Write down this save code:')
        print(f"    {savecode}")

    length_invent = len(invent)
    if length_invent >= 1:
        saveinvent0 = invent[0]
        if 'b' in saveinvent0:
            saveinvent0 = '!'
        elif 'sa' in saveinvent0:
            saveinvent0 = '@'
        elif 'goat' in saveinvent0:
            saveinvent0 = '#'
    else:
        saveinvent0 = ''
    if length_invent >= 2:
        saveinvent1 = invent[1]
        if 'b' in saveinvent1:
            saveinvent1 = 'q'
        elif 'sa' in saveinvent1:
            saveinvent1 = 'w'
        elif 'goat' in saveinvent1:
            saveinvent1 = 'e'
    else:
        saveinvent1 = ''
    if length_invent >= 3:
        saveinvent2 = invent[2]
        if 'b' in saveinvent2:
            saveinvent2 = '1'
        elif 'sa' in saveinvent2:
            saveinvent2 = '2'
        elif 'goat' in saveinvent2:
            saveinvent2 = '3'
    else:
        saveinvent2 = ''
    if length_invent >= 4:
        saveinvent3 = invent[3]
        if 'b' in saveinvent3:
            saveinvent3 = '4'
        elif 'sa' in saveinvent3:
            saveinvent3 = '5'
        elif 'goat' in saveinvent3:
            saveinvent3 = '6'
    else:
        saveinvent3 = ''
    if length_invent >= 5:
        saveinvent4 = invent[4]
        if 'b' in saveinvent4:
            saveinvent4 = 'r'
        elif 'sa' in saveinvent4:
            saveinvent4 = 't'
        elif 'goat' in saveinvent2:
            saveinvent2 = 'y'
    else:
        saveinvent4 = ''
    if xp == 10:
        save_xp = '~'
    elif xp == 11:
        save_xp = '!'
    elif xp == 12:
        save_xp = '@'
    elif xp == 13:
        save_xp = '#'
    elif xp == 14:
        save_xp = '$'
    elif xp == 15:
        save_xp = '%'
    elif xp == 16:
        save_xp = '^'
    elif xp == 17:
        save_xp = '&'
    elif xp == 18:
        save_xp = '*'
    elif xp == 19:
        save_xp = '('
    elif xp >= 20:
        save_xp = ')'
    else:
        save_xp = str(xp)

    if g > 9:
        if x < 0 and y < 0:
            savecodeprint(f'${shp + str(maxhp) + str(lvl) + str(firstinvent) + str(x * -1) + str(y * -1) + gold[0] + gold[1]}~{save_xp + saveinvent0 + saveinvent1 + saveinvent2 + saveinvent3 + saveinvent4}')
        elif y < 0:
            savecodeprint(f'${shp + str(maxhp) + str(lvl) + str(firstinvent) + str(x) + str(y * -1) + gold[0] + gold[1]};{save_xp + saveinvent0 + saveinvent1 + saveinvent2 + saveinvent3 + saveinvent4}')
        elif x < 0:
            savecodeprint(f'${shp + str(maxhp) + str(lvl) + str(firstinvent) + str(x * -1) + str(y) + gold[0] + gold[1]}?{save_xp + saveinvent0 + saveinvent1 + saveinvent2 + saveinvent3 + saveinvent4}')
        else:
            savecodeprint(f'${shp + str(maxhp) + str(lvl) + str(firstinvent) + str(x) + str(y) + gold[0] + gold[1] + save_xp + saveinvent0 + saveinvent1 + saveinvent2 + saveinvent3 + saveinvent4}')
    elif g < 10:
        if x < 0 and y < 0:
            savecodeprint(f'{shp + str(maxhp) + str(lvl) + str(x * -1) + str(y * -1) + str(firstinvent) + gold + save_xp}~{saveinvent0 + saveinvent1 + saveinvent2 + saveinvent3 + saveinvent4}')
        elif y < 0:
            savecodeprint(f'{shp + str(maxhp) + str(lvl) + str(firstinvent) + str(x) + str(y * -1) + gold + save_xp};{saveinvent0 + saveinvent1 + saveinvent2 + saveinvent3 + saveinvent4}')
        elif x < 0:
            savecodeprint(f'{shp + str(maxhp) + str(lvl) + str(firstinvent) + str(x * -1) + str(y) +  gold + save_xp}?{saveinvent0 + saveinvent1 + saveinvent2 + saveinvent3 + saveinvent4}')
        else:
            savecodeprint(shp + str(maxhp) + str(lvl) + str(firstinvent) + str(x) + str(y) + str(firstinvent) + gold + save_xp + saveinvent0 + saveinvent1 + saveinvent2 + saveinvent3 + saveinvent4)


def load():
    info = tuple(input("Input save code(Don't mess up, if you do it'll crash): "))
    infolen = len(info)

    def loading(twodigit, subx, suby, loadinvent, align, alignxp):
        global hp
        global maxhp
        global lvl
        global x
        global y
        global firstinvent
        global g
        global xp
        global maxxp
        hp = int(info[1 + align])
        maxhp = int(info[2 + align])
        lvl = int(info[3 + align])
        maxxp = 5 * lvl + 5
        firstinvent = int(info[4 + align])
        x = int(info[5 + alignxp]) * subx
        y = int(info[6 + alignxp]) * suby
        g = int(info[7 + align])
        if twodigit:
            gold = (info[7], info[8])
            g = int(''.join(gold))
        if str(info[9 + alignxp]) in '1234567890':
            xp = int(info[9 + alignxp])
        elif str(info[9 + alignxp]) == '~':
            xp = 10
        elif str(info[9 + alignxp]) == '!':
            xp = 11
        elif str(info[9 + alignxp]) == '@':
            xp = 12
        elif str(info[9 + alignxp]) == '#':
            xp = 13
        elif str(info[9 + alignxp]) == "$":
            xp = 14
        elif str(info[9 + alignxp]) == '%':
            xp = 15
        elif str(info[9 + alignxp]) == '^':
            xp = 16
        elif str(info[9 + alignxp]) == '&':
            xp = 17
        elif str(info[9 + alignxp]) == '*':
            xp = 18
        elif str(info[9 + alignxp]) == '(':
            xp = 19
        elif str(info[9 + alignxp]) == ')':
            xp = 20
        invent.clear()
        if infolen >= loadinvent:
            if '!' in info[loadinvent - 1]:
                invent.append('berries')
            elif '@' in info[loadinvent - 1]:
                invent.append('sand')
            elif '#' in info[loadinvent - 1]:
                invent.append('goat horn')
        if infolen >= loadinvent + 1:
            if 'q' in info[loadinvent]:
                invent.append('berries')
            elif 'w' in info[loadinvent]:
                invent.append('sand')
            elif 'e' in info[loadinvent]:
                invent.append('goat horn')
        if infolen >= loadinvent + 2:
            if '1' in info[loadinvent + 1]:
                invent.append('berries')
            elif '2' in info[loadinvent + 1]:
                invent.append('sand')
            elif '3' in info[loadinvent + 1]:
                invent.append('goat horn')
        if infolen >= loadinvent + 3:
            if '4' in info[loadinvent + 2]:
                invent.append('berries')
            elif '5' in info[loadinvent + 2]:
                invent.append('sand')
            elif '6' in info[loadinvent + 2]:
                invent.append('goat horn')
        if infolen >= loadinvent + 4:
            if 'r' in info[loadinvent + 3]:
                invent.append('berries')
            elif 't' in info[loadinvent + 3]:
                invent.append('sand')
            elif 'y' in info[loadinvent + 3]:
                invent.append('goat horn')

    if '$' in str(info[0]):
        if info[9] == ';':
            loading(True, 1, -1, 12, 0, 1)
        elif info[9] == '?':
            loading(True, -1, 1, 12, 0, 1)
        elif info[9] == '~':
            loading(True, -1, -1, 12, 0, 1)
        else:
            loading(True, 1, 1, 11, 0, 0)
    if str(info[0]) in '1234567890':
        if info[8] == ';':
            loading(False, 1, -1, 10, -1, -2)
        elif info[8] == '?':
            loading(False, -1, 1, 10, -1, -2)
        elif info[8] == '~':
            loading(False, -1, -1, 10, -1, -2)
        else:
            loading(False, 1, 1, 9, 0, -1)


def move_logic():
    global x
    global y
    global moved_already
    def move(value, change):
        global x
        global y
        global ranint
        ranint = random.randint(1, 100)
        if value == 'x':
            x += change
        else:
            y += change
    moving = input('North, East, South, or West: ').upper()
    if x == -1 and y == 1 and not moved_already:
        print("As you start walking away you hear a loud rumbling sound behind you.")
        enemy_fight(f'A massive lvl.{lvl} boulder has awakened behind you!', 'boulder', 500, 950, 1400, 1900, 900, 20, 25, 70, 'Boulder rolled into you', 20, 25, True, 5, 9, 20)
        moved_already = True
    elif 'SO' in moving:
        if lvl < 2:
            if y == 0:
                if x == 0:
                    print("     Your level isn't high enough! Get to level 2 and then you can enter this area.")
                    return
                elif x == 1:
                    print("     Your level isn't high enough! Get to level 2 and then you can enter this area.")
                    return
                elif x == -1:
                    print("     Your level isn't high enough! Get to level 2 and then you can enter this area.")
                    return
        move('y', -1)
    elif 'NO' in moving:
        if lvl < 5:
            if x == -1 and y == 0:
                print("     Your level isn't high enough! Get to level 5 and then you can enter this area.")
                return
        move('y', 1)
    elif 'WE' in moving:
        if lvl < 5:
            if x == 0 and y == 1:
                print("     Your level isn't high enough! Get to level 5 and then you can enter this area.")
                return
        move('x', -1)
    elif 'EA' in moving:
        move('x', 1)
    else:
        print('     That is not a valid input.')
        move_logic()


def stat():
    print(f"{int(round(hp, 1) * 50)}/{maxhp * 50} hp")
    print(f"lvl {lvl}")
    print(f"{xp}/{maxxp} xp")


def forage():
    activate()
    value = random.randint(0, 100)
    if value >= 41 and len(invent) < 5:
        print("     You found some berries!")
        invent.append("berries")
    elif value >= 41 and len(invent) > 4:
        print("You can not pickup any berries because your inventory is full.")
    elif value <= 40:
        enemy_fight(f'A lvl.{enemy_lvl} squirrel attacks you!', 'squirrel', 50, 90, 135, 180, 40, 25, 25, 15,'Squirrel bit you', 1, 1)


def dig():
    activate()
    if len(invent) < 5:
        print('     You got some sand!')
        invent.append('sand')
    elif len(invent) > 4:
        print("You can not pickup any sand because your inventory is full.")
    value = random.randint(0, 100)
    if value > 60:
        enemy_fight(f"A lvl.{enemy_lvl} snake attacks you!.", "snake", 75, 140, 210, 275, 60, 15, 25, 15,'Snake bit you', 2, 2)


def level_up():
    global xp
    global lvl
    global enemy_lvl
    global maxhp
    global hp
    global maxxp
    while xp >= maxxp:
        xp -= maxxp
        lvl += 1
        enemy_lvl = lvl
        maxhp += 1
        hp = maxhp
        maxxp += 5
        print(f"         LEVEL UP! You're now on lvl {lvl}!")


def goat():
    activate()
    print("You approach a single goat. It is very large, white, and shaggy. Large horns protrude from its head.")
    inputs = input("Do you fight the goat?(yes or no): ")
    if 'YE' in inputs.upper():
        enemy_fight(f'You attack a lvl.{enemy_lvl} goat!', 'goat', 200, 350, 525, 700, 150, 20, 15, 30,'Goat rammed you', 3, 3, False, 2, 5)
    elif 'N' in inputs.upper():
        print("You decide not to attack the goat.")
    else:
        print('     That is not a valid input.')


def enemy_fight(enemy_intro, enemy, hp1, hp2, hp3, hp4, hp_increment, punch_damage, kick_damage, enemy_damage,enemy_attack_parameters, gain_xp, gain_gold, hard=False, lvl_start=1, lvl_end=4, increment=1):
    global hp
    enemy_hp = hp1
    if enemy_lvl == lvl_start + 1:
        enemy_hp = hp2
    elif enemy_lvl == lvl_start + 2:
        enemy_hp = hp3
    elif enemy_lvl >= lvl_start + 3:
        enemy_hp = hp4 + (hp_increment * (enemy_lvl - lvl_end))
    enemy_max = enemy_hp
    print(f'{enemy_intro} {enemy.capitalize()} has {enemy_hp} hp.')
    while enemy_hp > 0 and hp > 0:
        attack = input('Choose an attack(Punch or Kick): ').upper()
        if "PU" in attack:
            print(f'You punched the {enemy}!')
            if not hard:
                print(f"     {enemy.capitalize()} lost {punch_damage * lvl} hp. {enemy.capitalize()} has {enemy_hp - punch_damage * lvl}/{enemy_max} hp.")
            elif hard:
                print(f"     {enemy.capitalize()} lost {punch_damage * lvl} hp and you lost 10 hp. {enemy.capitalize()} has {enemy_hp - 5 * lvl}/{enemy_max} hp and you have {int(round(hp, 1) * 50) - 10}/{maxhp * 50} hp.")
                hp -= 10 * 0.02
            enemy_hp -= punch_damage * lvl
        elif 'KI' in attack:
            print(f'You kicked the {enemy}!')
            print(f"     {enemy.capitalize()} lost {kick_damage * lvl} hp. {enemy.capitalize()} has {enemy_hp - kick_damage * lvl}/{enemy_max} hp.")
            enemy_hp -= kick_damage * lvl
        if attack not in 'PUNCHKICK':
            print("     That is not a valid input.")
        elif enemy_attack(enemy_attack_parameters, enemy_damage):
            return
    enemy_kill(enemy, gain_xp - 1, gain_gold - 1, increment)


def enemy_attack(attack, attack_damage):
    global hp
    hp -= attack_damage * 0.02
    print(f"{attack}. You lost {attack_damage}. You have {int(round(hp, 1) * 50)}/{maxhp * 50} hp.")
    return death()


def enemy_kill(enemy, gain_xp, gain_gold, increment=1):
    global xp
    global g
    if enemy == 'boulder':
        xp += gain_xp + (enemy_lvl - 5) * increment
        xp += gain_xp + (enemy_lvl - 5) * increment
    else:
        xp += gain_xp + enemy_lvl * increment
        g += gain_gold + enemy_lvl * increment
    success = f"         You killed the {enemy}! You gained {increment * enemy_lvl + gain_xp} xp and {enemy_lvl * increment + gain_gold} gold."
    if enemy == 'goat':
        invent.append("goat horn")
        success += " You also got a goat horn!"
    print(success)
    level_up()


def death():
    global x
    global y
    global hp
    if hp <= 0:
        print('         GAME OVER')
        print('         You died')
        inputs = input('Title Screen or Respawn: ')
        y = 0
        if 'TIT' in inputs.upper():
            hp = maxhp
            x = 0.5
        elif 'RES' in inputs.upper():
            hp = maxhp
            x = 0
        else:
            print("     That is not a valid input.")
            death()
        return True
    return False


def inventory():
    global hp
    global maxhp
    global firstinvent
    iinv_is_int = False
    if firstinvent < 3:
        print('NOTE: INVENTORY LIMIT IS 5 ITEMS, ALL ITEMS OBTAINED AFTER THIS LIMIT IS REACHED WILL BE DELETED')
        firstinvent += 1
    print(f"These are the items you have: {invent} and you have {g} gold.")
    ext = input("Select item number to interact with(1-5, left to right) or EXIT: ")
    if ext in '1234567890' and ext != "":
        iinv = int(ext) - 1
        iinv_is_int = True
    if 'EX' not in ext.upper() and iinv_is_int:
        if len(invent) > iinv and iinv >= 0:
            item = invent[iinv]
            if item == 'berries':
                berries(iinv)
            elif item == 'sand':
                sand(iinv)
            elif item == 'goat horn':
                goat_horn(iinv)
            elif item == 'apple':
                apple(iinv)
        elif len(invent) == 0:
            print("     Your inventory is empty, exiting inventory.")
        else:
            print("     There isn't anything in that slot")
            inventory()
    elif 'EX' in ext.upper():
        print('  Exiting inventory.')
    else:
        print("     That is not a valid input.")
        inventory()


def sand(iinv):
    print("     A simple pile of sand.")
    inputs = input('Throw away the sand?(Yes or No): ')
    if 'Y' in inputs.upper():
        confirmation('sand', iinv)
    elif 'N' in inputs.upper():
        inventory()
    elif inputs.upper() == 'EAT':
        print("     You ate the sand.")
        print("                     CARTERISM +100.")
        invent.remove(invent[iinv])
        inventory()
    else:
        print("     That is not a valid inupt.")
        sand(iinv)


def berries(iinv):
    print('     A cluster of red berries of unknown species. They look good enough to eat.')
    inputs = input("Eat the Berries?(Yes or No): ")
    if 'Y' in inputs.upper():
        health_gain(10)
        invent.remove(invent[iinv])
        print(f'The berries were very tasty, +10 hp, you now have {int(hp * 50)}/{maxhp * 50} hp.')
        inventory()
    elif 'N' in inputs.upper():
        inventory()
    else:
        print("     That is not a valid input.")
        berries(iinv)


def goat_horn(iinv):
    print("     A single spiral shaped horn, it's as hard as a rock.")
    inputs = input("Blow the horn?(Yes or No or Throw away):")
    if 'YE' in inputs.upper():
        print("     You blew the horn. It made a very loud horn noise, other than that nothing happened. ")
        inventory()
    elif 'NO' in inputs.upper():
        inventory()
    elif 'TH' in inputs.upper():
        confirmation('goat horn', iinv)
    else:
        print("     That is not a valid input.")
        goat_horn(iinv)


def apple(iinv):
    activate()
    print("     A single red apple. It shines in the sunlight.")
    inputs = input("Eat the apple?(Yes or No)")
    if 'YE' in inputs.upper():
        invent.remove(invent[iinv])
        health_gain(15)
        print(f'The apple was very sweet, +15 hp, you now have {int(hp * 50)}/{maxhp * 50} hp.')
    elif 'N' in inputs.upper():
        inventory()
    else:
        print("     That is not a valid input.")
        apple(iinv)


def health_gain(health_gain_amount):
    global hp
    hp += health_gain_amount * 0.02
    if hp > maxhp:
        hp = maxhp


def confirmation(item, iinv):
    confirm = input("Are you sure?(yes or no): ")
    if 'NO' in confirm.upper():
        print(f"You decided against throwing the {item} away.")
        if invent[iinv] == 'sand':
            sand(iinv)
        elif invent[iinv] == 'goat horn':
            goat_horn(iinv)
    elif 'YES' in confirm.upper():
        print(f"     You threw away the {item}.")
        invent.remove(invent[iinv])
        inventory()
    else:
        print("     That is not a valid input.")
        confirmation(item, iinv)


def people():
    person = input("Who would you like to talk to?(Options: Farmer or go Back): ")
    if 'FA' in person.upper():
        farmer(True)
    elif 'BA' in person.upper():
        print("Guess you didn't feel like talking.")
    else:
        print("     That is not a valid input.")
        people()


def buying_stuff(price, object_thing, object):
    global g
    if g >= price:
        print(f"     You bought {object_thing} {object}.")
        invent.append(object)
        g -= price
    else:
        print(f"     You do not have enough money to buy {object}.")


def farmer(first=False):
    if first:
        print('Farmer: Hey there! I buy and sell anything and everything that can be farmed!')
    purchase = input("Farmer: Would you like to buy or sell?(or go Back): ")
    if 'BU' in purchase.upper():
        farmerbuy()
    elif 'SE' in purchase.upper():
        farmersell()
    elif 'BA' in purchase.upper():
        people()
    elif purchase.upper() not in 'BUYSELL':
        print("     That is not a valid input.")
        farmer()


def farmerbuy():
    print("Farmer: What would you like to buy?")
    buy = input("Options: Berries(2 gold), Apple(3 gold) or go Back: ").upper()
    if len(invent) < 5:
        if 'BA' in buy:
            print("Farmer: Ok then.")
            farmer()
        elif "BE" in buy:
                buying_stuff(2, 'some', 'berries')
        elif 'AP' in buy:
            buying_stuff(3, 'an', 'apple')
        else:
            print("That is not valid input.")
        farmerbuy()
    else:
        print("     You do not have enough inventory space to buy this item.")
        farmer()


def farmersell():
    global g
    print(f"These are the items you have {invent}")
    i = input("Select item number to sell(1-5, left to right) or go Back: ").upper()
    if 'BA' in i:
        print("Farmer: Ok then.")
        farmer()
    elif i == '':
        print("     That is not a valid input.")
    elif len(invent) == 0:
        print("     You have nothing to sell, GOING BACK.")
        farmer()
    elif i in '1234567890':
        i = int(i)
        if len(invent) > i - 1 and i > 0:
            item = invent[i - 1]
            if 'berries' in item:
                invent.remove(item)
                g += 1
                print('You sold your berries. +1 gold.')
            elif 'apple' in item:
                invent.remove(item)
                g += 2
                print('You sold your apple. +2 gold.')
            else:
                print("Farmer: Sorry, but I don't buy that kind of item.")
        else:
            print("     There isn't anything in that slot")
    else:
        print("     That is not a valid input.")
    farmersell()

def apples():
    activate()
    inputs = input("Would you like to pick an apple?(yes or no): ").upper()
    oof = len(invent) == 5
    if 'Y' in inputs:
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        answer = input(f"What's {a}x{b}?: ").strip()
        if answer == str(a * b):
            print('Correct! You got an apple.' + ' Unfortunately you do not have enough inventory space to hold it.' * oof)
            if not oof:
                invent.append('apple')
        else:
            print("That's not correct")
    elif 'N' in inputs:
        print("The apples didn't look tasty enough to you.")
    else:
        print("     That is not a valid input.")
        apples()


def hotel(valid=True):
    greeting_value = random.choice(hotelgreetings)
    if valid:
        print("     You enter a small hotel. A person approaches you.")
    inputs = input(f"Hotel Owner: {greeting_value}, how can I help you today?(Stay a night or leave): ").upper()
    if "ST" in inputs:
        hotel_price()
    elif 'LE' in inputs:
        print("     You decided to leave the hotel.")
    else:
        print("     That is not a valid input.")
        hotel(False)


def hotel_price():
    global g
    inputs = input("Hotel Owner: Staying a night will cost you 5 gold, are you sure?(yes or no): ").upper()
    if 'Y' in inputs:
        if g < 5:
            print("     You do not have enough gold, leaving hotel.")
        else:
            health_gain(maxhp)
            g -= 5
            print(f"     You wake up the next night feeling well rested. You are now at {hp}/{maxhp} hp.")
    elif 'N' in inputs:
        print("     You left the hotel.")
    else:
        print("     That is not a valid input.")
        hotel_price()


# Areas


def basic_options(basic_input):
    global activated
    activated = True
    if 'MO' in basic_input:
        move_logic()
    elif 'ST' in basic_input:
        stat()
    elif 'SA' in basic_input:
        save()
    elif 'IN' in basic_input:
        inventory()
    elif 'LO' in basic_input:
        load()
    else:
        activated = False


def goat_mountain_options():
    inputs = input("Move, Goats, Stats, Inventory, Load, or Save: ").upper()
    basic_options(inputs)
    if 'GO' in inputs:
        goat()
    not_valid()


def not_valid():
    if not activated:
        print('     That is not a valid input.')


def activate():
    global activated
    activated = True


while True:

    # Title Screen
    if x == 0.5 and y == 0:
        hp = maxhp
        inputs = input('New game or Load game: ').upper()
        if 'NE' in inputs:
            x = 0
        elif 'LO' in inputs:
            load()
        else:
            print('     That is not a valid input.')


    # Start Area
    elif x == 0 and y == 0:
        print('You are in an spruce forest.')
        inputs = input("Move, Forage, Inventory, Stats, Load or Save: ").upper()
        if 'FO' in inputs:
            forage()
        else:
            basic_options(inputs)
        not_valid()


    # Northern Desert
    elif x == 0 and y == 2:
        hp -= 10 * 0.02
        print('You have entered a vast desert. You also lost 10 hp due to dehydration.')
        death()
        inputs = input("Move, Dig, Stats, Inventory, Load, or Save: ").upper()
        basic_options(inputs)
        if 'DI' in inputs:
            dig()
        not_valid()


    # Morecambe
    elif x == 1 and y == 0:
        print('You enter a small village. A sign near the entrance says "Morecombe Village".')
        inputs = input("Move, People, Hotel, Stats, Inventory, Load, or Save: ").upper()
        basic_options(inputs)
        if 'PE' in inputs:
            people()
        elif 'HO' in inputs:
            hotel()
        not_valid()


    # Apple Orchard
    elif x == 1 and y == 1:
        print("You walk into a apple orchard, there are no people to found though.")
        inputs = input("Move, Apples, Stats, Inventory, Load, or Save: ").upper()
        basic_options(inputs)
        if 'AP' in inputs:
            apples()
        not_valid()


    # Plains
    elif x == 0 and y == 1:
        if ranint > 50:
            ranint = 0
            enemy_fight(f'A lvl.{enemy_lvl} rock pops out of the ground and attacks you!', 'rock', 25, 45, 65, 90, 20,5, 10, 10, 'Rock smacked you', 2, 3, True)
        print("You enter a vast expanse of grassy plains with very few trees. Mountains can be seen in the distace in the west.")
        inputs = input("Move, Stats, Inventory, Load, or Save: ").upper()
        basic_options(inputs)
        not_valid()

    elif x == -1 and y == 0:
        if ranint > 50:
            ranint = 0
            enemy_fight(f'A lvl.{enemy_lvl} rock pops out of the ground and attacks you!', 'rock', 25, 45, 65, 90, 20,5, 10, 10, 'Rock smacked you', 2, 3, True)
        print("You enter a vast expanse of grassy plains with very few trees. Mountains can be seen in the distance to the north and south.")
        inputs = input("Move, Stats, Inventory, Load, or Save: ").upper()
        basic_options(inputs)
        not_valid()


    # Southern Mountains
    elif x == -1 and y == -1:
        print("You have entered an area of massive, snowcapped mountains. You're just south of some plains. They're some goats on the mountains.")
        goat_mountain_options()

    elif x == 0 and y == -1:
        print("You have entered an area of massive, snowcapped mountains. You're just south of spawn. They're some goats on the mountains.")
        goat_mountain_options()

    elif x == 1 and y == -1:
        print("You have entered an area of massive, snowcapped mountains. You're just south of Morecambe. They're some goats on the mountains.")
        inputs = input("Move, Goats, Stats, Inventory, Load, or Save: ")
        goat_mountain_options()


    # Northern Mountain
    elif x == -1 and y == 1:
        print("You have entered an area of massive, snowcapped mountains. You're just north of some plains. There are boulders on the mountains.")
        inputs = input("Move, Stats, Inventory, Load, or Save: ").upper()
        basic_options(inputs)
        not_valid()


    # LMAO Unfinished
    else:
        print("The creator isn't finished with the game so there is nothing here.")
        print("             You should probably leave while you can, go along now.")
        print(f"You are at ({x},{y})")
        move_logic()