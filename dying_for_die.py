import random


def dead():
    print("Everything goes dark, and you die.")
    exit()

def frank_regen():
    global san_max
    global hp_max
    global hp
    global sanity
    if hp < hp_max and day % 2 == 0:
        hp += 1
    if sanity < san_max:
        sanity += 1

def apply_passive_cb_s():
    global rocks
    global fruit
    global blood
    global meat
    global ins_max
    global insulation
    global thirst
    global trst_max
    global cb_s
    global sanity
    global san_max
    global day
    global time
    if 0 <= insulation <= ins_max and 1 in cb_s:
        insulation += 1
    if 0 <= thirst <= trst_max and 2 in cb_s:
        thirst += 1
    if 0 <= sanity <= san_max and 3 in cb_s:
        sanity += 1
    if 4 in cb_s and day == 1:
        rocks += 150
    if 11 in cb_s:
        a = random.randint(1,2)
        if a == 1:
            meat += 1
        else:
            blood += 15
    if 13 in cb_s and day == 1:
        blood += 200
    if 15 in cb_s and time == 1:
        fruit += 1


def craftable_cb_s(A):
    #twigs, grass, rocks, blood, meat, veggie, fruit, name of cb, effect of cb
    if A == 1:
        return [50, 10, 5, 0, 0, 0, 0, "sun", "makes you nearly immune to the cold"]
    elif A == 2:
        return [50, 10, 5, 20, 5, 1, 1, "rain clouds", "makes you less thirsty"]
    elif A == 3:
        return [0, 0, 50, 20, 1, 0, 0, "full moon", "passively gives off sanity"]
    elif A == 4:
        return [50, 50, 50, 0, 10, 10, 10, "mercury", "passively gives rocks at the end of season"]
    elif A == 5:
        return [20, 20, 20, 20, 20, 20, 20, "jupiter", "passively gives 4 extra die"]
    elif A == 6:
        return [25, 25, 5, 0, 0, 0, 5, "phobos", "passively provides 6 1's"]
    elif A == 7:
        return [0, 0, 0, 140, 0, 0, 0, "pandora", "passively gives 4 extra die"]
    elif A == 8:
        return [0, 0, 50, 0, 0, 0, 0, "pasiphae", "for every 10 rocks that you have, roll an extra die."]
    elif A == 9:
        return [0, 0, 0, 0, 0, 0, 0, "ananke", "when this celestial body is destroyed, gain 20 meat."]
    elif A == 10:
        return [50, 50, 10, 50, 10, 0, 0, "atlas", "gives 1 die for everytime you won a battle this run."]
    elif A == 11:
        return [20, 25, 15, 50, 15, 0, 0, "mars", "passively produces blood or meat"]
    elif A == 12:
        return [0, 0, 50, 50, 5, 0, 0, "titan","you roll 2 free sixes."]
    elif A == 13:
        return [10, 0, 3, 25, 1, 1, 0, "uranus","produces blood every season"]
    elif A == 14:
        return [0, 0 , 1, 0, 10, 10, 10, "venus", "roll double the dice if you have more than 1 meat"]
    elif A == 15:
        return [1, 1, 20, 1, 1, 1, 7, "earth", "passively provides fruit"]



def enemy_pool_fall():
    #odds(1 in (1-6), x times ex: need to roll a 6 twice), meat, blood, name
    a = random.randint(1,15)
    if a == 1:
        hungry_bear = [4, 4, 6, 12, "hungry bear"]
        return hungry_bear
    elif a == 2:
        hungry_wasp = [4, 1, 1, 0, "hungry wasp"]
        return hungry_wasp
    elif a == 3:
        red_squirrel = [1, 1, 3, 2, "red squirrel"]
        return red_squirrel
    elif a == 4:
        walnut_tree = [6, 5, 0, 16, "walnut tree"]
        return walnut_tree
    elif a == 5:
        forgetful_hound = [5, 3, 2, 14, "forgetful hound"]
        return forgetful_hound
    elif a == 6:
        water_elemental = [6, 1, 2, 0, "water elemental"]
        return water_elemental
    elif a == 7:
        wendigo = [3, 4, 10, 2, "wendigo?"]
        return wendigo
    elif a == 8:
        skin_walker = [6, 12, 20, 20, "skin walker"]
        return skin_walker
    elif a == 9:
        hungry_ant = [1, 1, 1, 1, "hungry ant"]
        return hungry_ant
    elif a == 10:
        mighty_eagle = [5, 2, 4, 2, "mighty eagle"]
        return mighty_eagle
    elif a == 11:
        migration = [3, 2, 5, 3, "migration"]
        return migration
    elif a == 12:
        mole_worm = [2, 2, 2, 2, "mole worm"]
        return mole_worm
    elif a == 13:
        crow = [2, 1, 1, 1, "crow"]
        return crow
    elif a == 14:
        sea_otter = [3, 3, 3, 2, "sea otter"]
        return sea_otter
    else:
        former_president = [1, 1, 2, 4, "former president"]
        return former_president

def enemy_pool_winter():
    #odds(1 in (1-6), x times ex: need to roll a 6 twice), meat, blood, name
    a = random.randint(1,10)
    if a == 1:
        wolf = [5, 3, 2, 3, "wolf"]
        return wolf
    elif a == 2:
        cold_owl = [6, 1, 3, 2, "cold owl"]
        return cold_owl
    elif a == 3:
        old_man = [6, 6, 1, 30, "old man"]
        return old_man
    elif a == 4:
        yeti = [6, 2, 10, 3, "yeti"]
        return yeti
    elif a == 5:
        elkclops = [3, 6, 8, 2, "elkclops"]
        return elkclops
    elif a == 6:
        white_fox = [2, 2, 2, 2, "white fox"]
        return white_fox
    elif a == 7:
        llama_tree = [1, 12, 9, 1, "llama tree"]
        return llama_tree
    elif a == 8:
        jack = [1, 1, 1, 1, "jack"]
        return jack
    elif a == 9:
        foursixsixsix = [6, 4, 5, 20, "scp 4666"]
        return foursixsixsix
    else:
        krampus = [3, 6, 8, 10, "krampus"]
        return krampus
def enemy_pool_spring():
    #odds(1 in (1-6), x times ex: need to roll a 6 twice), meat, blood, name
    a = random.randint(1,20)
    if a == 1:
        evil_bee = [1, 2, 1, 1, "evil bee"]
        return evil_bee
    elif a == 2:
        duck_elk = [4, 4, 8, 12, "duck elk"]
        return duck_elk
    elif a == 3:
        dyrad = [3, 3, 2, 5, "dyrad"]
        return dyrad
    elif a == 4:
        frog_rain = [1, 18, 18, 2, "frog rain"]
        return frog_rain
    elif a == 5:
        squid = [2, 2, 2, 4, "squid"]
        return squid
    elif a == 6:
        moss_witch = [6, 8, 2, 8, "moss witch"]
        return moss_witch
    elif a == 7:
        intimidating_horse = [2, 3, 6, 3, "intimidating horse"]
        return intimidating_horse
    elif a == 8:
        returning_aves = [1, 6, 6, 1, "returning aves"]
        return returning_aves
    elif a == 9:
        crocodile_or_possibly_alligator = [3, 3, 3, 3, "crocodile or possibly alligator"]
        return crocodile_or_possibly_alligator
    elif a == 10:
        hungry_worm = [1, 1, 3, 0, "hungry worm"]
        return hungry_worm
    elif a == 11:
        tamatoa = [6, 1, 5, 0, "tamatoa"]
        return tamatoa
    elif a == 12:
        elkling = [3, 1, 4, 1, "elkling"]
        return elkling
    elif a == 13:
        hammershark = [5, 2, 8, 2, "hammershark"]
        return hammershark
    elif a == 14:
        mighty_toad = [2, 1, 1, 0, "mighty toad"]
        return mighty_toad
    elif a == 15:
        thunder_eel = [5, 1, 2, 6, "thunder eel"]
        return thunder_eel
    elif a == 16:
        hawk = [5, 2, 3, 2, "hawk"]
        return hawk
    elif a == 17:
        just_a_cow = [5, 6, 20, 20, "just a cow"]
        return just_a_cow
    elif a == 18:
        capybara = [6, 6, 6, 6, "capybara"]
        return capybara
    elif a == 19:
        time_traveler = [6, 6, 10, 18, "time traveler"]
        return time_traveler
    else:
        great_whale = [6, 5, 20, 20, "great whale"]
        return great_whale

def enemy_pool_summer():
    # odds(1 in (1-6), x times ex: need to roll a 6 twice), meat, blood, name
    a = random.randint(1, 10)
    if a == 1:
        dragon_fly = [6, 2, 8, 3, "dragon fly"]
        return dragon_fly
    if a == 2:
        ant_lion = [5, 3, 8, 5, "ant lion"]
        return ant_lion
    if a == 3:
        stinking_rodent = [1, 1, 1, 1, "stinking rodent"]
        return stinking_rodent
    if a == 4:
        dragon = [6, 3, 9, 7, "dragon"]
        return dragon
    if a == 5:
        fire_fly = [1, 1, 1, 1, "fire fly"]
        return fire_fly
    if a == 6:
        tiger = [5, 2, 6, 2, "tiger"]
        return tiger
    if a == 7:
        shepeard = [6, 6, 6, 99, "shepeard"]
        return shepeard
    if a == 8:
        blood_spitter = [8, 10, 2, 100, "blood spitter"]
        return blood_spitter
    if a == 9:
        cactus_man = [4, 5, 8, 3, "cactus man"]
        return cactus_man
    else:
        fire_elemental = [3, 2, 5, 5, "fire elemental"]
        return fire_elemental

def enemy_pool_apocylapse():
    # odds(1 in (1-6), x times ex: need to roll a 6 twice), meat, blood, name
    a = random.randint(1, 5)
    if a == 1:
        unforgiving_hounds = [6, 2, 6, 2, "unforgiving hounds"]
        return unforgiving_hounds
    if a == 2:
        shepeard_again = [3, 15, 16, 23, "shepeard again"]
        return shepeard_again
    if a == 3:
        starer = [1, 11, 1, 11, "starer"]
        return starer
    if a == 4:
        the_mound = [2, 12, 1, 56, "the mound"]
        return the_mound
    else:
        rift = [6, 1, 0, 2, "rift"]
        return rift
        
def add_cb(A):
    global cb_max
    global cb_1
    global cb_2
    global cb_3
    global cb_4
    global cb_5
    global meat
    cb_slots = [cb_1, cb_2, cb_3, cb_4, cb_5]
    for i in range (len(cb_slots)):
        if cb_slots[i] == 0:
            cb_slots[i] = A
            break
        else:
            while True:
                print("your celestial bodies:")
                for idx, cb in enumerate(cb_slots, 1):
                    if cb != 0:
                        info = craftable_cb_s(cb)
                        print(f"{idx}: {info[7]} - {info[8]}")
                try:
                    removed =int(input("enter the number of the celestial body you would like to replace"))
                    if 1 <= removed <=5:
                        if cb_slots[removed - 1] == 9:
                            meat += 20
                        cb_slots[removed - 1] = A
                        break
                except ValueError:
                    pass



if __name__ == "__main__":
    character_info = int(input("Would you like to get info on the characters? Press 0 for yes."))
    if character_info == 0:
        print("Frank:")
        print("health: 10 - sanity: 15 - hunger: 20 - thirst: 10 - insulation: 10")
        print("quirks: regenerates sanity and health slowly, starts days bright")

        #More may get added
    character_picked = int(input("press 0 to pick Frank."))
    if character_picked == 0:
        character = 0
        hp_max = 10
        san_max = 15
        hun_max = 20
        trst_max = 10
        ins_max = 10
        cb_max = 5
        current_cb_count = 0
        cb_1 = 0
        cb_2 = 0
        cb_3 = 0
        cb_4 = 0
        cb_5 = 0
        add_cb(1)
    else:
        exit()
    hp = hp_max
    sanity = san_max
    hunger = hun_max
    thirst = trst_max
    insulation = ins_max
    day = 1
    season = 0
    twigs = 10
    grass = 10
    rocks = 10
    blood = 0
    meat = 2
    veggie = 2
    fruit = 2
    atlas = 0
    year = 0
    cb_s = [cb_1, cb_2, cb_3, cb_4, cb_5]

        ####################### F A L L ###############################

    # 0 is fall 1 is winter 2 is spring 3 is summer 4 is apocylpse
    while True:
        #The year loop
        day = 0
        year += 1
        while day < 31:
            day += 1
            #the fall loop
            if True:
                apply_passive_cb_s()
                for time in range(0,3,1):
                    hunger -= 1
                    if time != 1:
                        sanity -= 1
                    if sanity < 0:
                        hp -= 1
                    if hunger < 0:
                        hp -= 1
                    print("hp:", hp, "hunger:", hunger, "sanity:", sanity)
                    while True:
                        activity = int(input("What would you like to do for the day? 0 -> gather materials 1 -> gather food 2 -> craft 3 -> combat"))
                        if activity == 0 or activity == 1 or activity == 2 or activity == 3 or activity == 4:
                            break
                    if activity == 0:
                        a = random.randint(1,5)
                        b = random.randint(1,5)
                        if a == 1 or b == 1:
                            twigs += 20
                            print("you have obtained some twigs!")
                        if a == 2 or b == 2:
                            grass += 20
                            print("you have obtained some grass!")
                        if a == 3 or b == 3:
                            rocks += 10
                            print("you have obtained some rocks!")
                        if a == 4 or b == 4:
                            veggie+= 5
                            print("you have obtained some veggies!")
                        if a == 5 or b == 5:
                            fruit += 5
                            print("you have obtained some fruit!")
                    elif activity == 1:
                        veggie += 5
                        fruit += 5
                        print("you have gathered some fruit and veggies.")
                    elif activity == 2:
                        #select 2 variables between 1 and the number of cb's craftable
                        a = random.randint(1, 15)
                        b = random.randint(1, 15)
                        c = craftable_cb_s(a)
                        d = craftable_cb_s(b)
                        print("first celestial body you may craft is", c[7], "its effect are:", c[8], "its costs this much twigs, grass, rocks, blood, meat, veggies and fruit respectively.", c[0], c[1], c[2], c[3], c[4], c[5], c[6])
                        print("second celestial body you may craft is", d[7], "its effect are:", d[8], "its costs this much twigs, grass, rocks, blood, meat, veggies and fruit respectively.", d[0], d[1], d[2], d[3], d[4], d[5], d[6])
                        e = int(input("type 1 for the first, 2 for the second, 0 to ignore."))
                        if e == 1:
                            if twigs >= c[0] and grass >= c[1] and rocks >= c[2] and blood >= c[3] and meat >= c[4] and veggie >= c[5] and fruit >= c[6]:
                                twigs -= c[0]
                                grass -= c[1]
                                rocks -= c[2]
                                blood -= c[3]
                                meat -= c[4]
                                veggie -= c[5]
                                fruit -= c[6]
                                add_cb(a)

                            elif twigs >= d[0] and grass >= d[1] and rocks >= d[2] and blood >= d[3] and meat >= d[4] and veggie >= d[5] and fruit >= d[6]:
                                twigs -= d[0]
                                grass -= d[1]
                                rocks -= d[2]
                                blood -= d[3]
                                meat -= d[4]
                                veggie -= d[5]
                                fruit -= d[6]
                                add_cb(b)
                            cb_s = [cb_1, cb_2, cb_3, cb_4, cb_5]


                    elif activity == 3:
                        #combat
                        print("select an enemy.")
                        a = enemy_pool_fall()
                        print(a[4], a[2], "meat", a[3], "blood, and you need to roll a", a[0], a[1], "times")
                        b = enemy_pool_fall()
                        print(b[4], b[2], "meat", b[3], "blood, and you need to roll a", b[0], b[1], "times")
                        c = int(input("1 to choose one, 2 to choose 2"))
                        #main combat loop, you add dice rolls in a list and do an "if" for every cb
                        #remember to put a event in BOTH the loops, or not
                        dice_rolls = []
                        if 6 in cb_s:
                            dice_rolls += [1] * 6
                        x = 3
                        if cb_1 == 5:
                            x += 4
                        elif cb_2 == 5:
                            x += 4
                        elif cb_3 == 5:
                            x += 4
                        elif cb_4 == 5:
                            x += 4
                        elif cb_5 == 5:
                            x += 4
                        if cb_1 == 7:
                            x += 4
                        elif cb_2 == 7:
                            x += 4
                        elif cb_3 == 7:
                            x += 4
                        elif cb_4 == 7:
                            x += 4
                        elif cb_5 == 7:
                            x += 4
                        if cb_1 == 8:
                            for i in range(0,rocks,10):
                                x += 1
                        elif cb_2 == 8:
                            for i in range(0, rocks, 10):
                                x += 1
                        elif cb_3 == 8:
                            for i in range(0, rocks, 10):
                                x += 1
                        elif cb_4 == 8:
                            for i in range(0, rocks, 10):
                                x += 1
                        elif cb_5 == 8:
                            for i in range(0, rocks, 10):
                                x += 1
                        if cb_1 == 10:
                            for i in range (0,atlas,1):
                                x += 1
                        if cb_2 == 10:
                            for i in range (0,atlas,1):
                                x += 1
                        if cb_3 == 10:
                            for i in range (0,atlas,1):
                                x += 1
                        if cb_4 == 10:
                            for i in range (0,atlas,1):
                                x += 1
                        if cb_5 == 10:
                            for i in range (0,atlas,1):
                                x += 1
                        if cb_s.count(14) >= 1 and meat > 1:
                            x *= 2
                        if cb_s.count(12) >= 1:
                            dice_rolls.append(6)
                            dice_rolls.append(6)
                        for i in range(0,x,1):
                            d = (random.randint(1, 6))
                            print("you rolled a", d)
                            dice_rolls.append(d)
                        if c == 1:
                            if dice_rolls.count(a[0]) >= a[1]:
                                meat += a[2]
                                blood += a[3]
                                print("you won!")
                                atlas += 1
                            else:
                                hp -= 5
                                print("you lost.")
                        else:
                            if dice_rolls.count(b[0]) >= b[1]:
                                meat += b[2]
                                blood += b[3]
                                print("you won!")
                                atlas += 1
                            else:
                                hp -= 5
                                print("you lost.")


                print("you have", twigs, "twigs,", grass, "grass,", rocks,"rocks,", blood, "blood,", meat, "meat,", veggie, "veggie,", fruit, ",fruit")
                a = int(input("what would you like to eat? 1 = meat, 2 = veggie, 3 = fruit."))
                if a == 1 and meat > 0:
                    meat -= 1
                    hunger += 2
                    hunger = min(hunger, hun_max)
                elif a == 2 and veggie > 0:
                    veggie -= 1
                    hunger += 1
                    hp += 1
                    hp = min(hp, hp_max)
                    hunger = min(hunger, hun_max)
                elif a == 3 and fruit > 0:
                    fruit -= 1
                    hunger += 1
                    sanity += 2
                    hunger = min(hunger, hun_max)
                    sanity = min(sanity, san_max)
                if hp < 1:
                    dead()


                                    
                            
                    
            ############################# W İ N T E R ################################
                

        while True:
            day = 0
            #the winter loop
            if day < 31:
                if cb_s.count(15) >= 1:
                    fruit += 1
                day += 1
                apply_passive_cb_s()
                for time in range(0, 3, 1):
                    hunger -= 1
                    if time == 1:
                        sanity -= 1
                    if sanity < 0:
                        hp -= 1
                    if hunger < 0:
                        hp -= 1
                    if insulation < 1:
                        hp -= 1
                    # full moon
                    insulation -= 1
                    print("hp:", hp, "hunger:", hunger, "sanity:", sanity, "insulation:", insulation)
                    while True:
                        activity = int(input(
                            "What would you like to do for the day? 0 -> gather materials 1 -> gather food 2 -> craft 3 -> combat"))
                        if activity == 0 or activity == 1 or activity == 2 or activity == 3 or activity == 4:
                            break
                    if activity == 0:
                        a = random.randint(1, 5)
                        b = random.randint(1, 5)
                        if a == 1 or b == 1:
                            twigs += 30
                            print("you have obtained some twigs!")
                        if a == 2 or b == 2:
                            grass += 5
                            print("you have obtained some grass!")
                        if a == 3 or b == 3:
                            rocks += 20
                            print("you have obtained some rocks!")
                        if a == 4 or b == 4:
                            veggie += 1
                            print("you have obtained some veggies!")
                        if a == 5 or b == 5:
                            fruit += 1
                            print("you have obtained some fruit!")
                    elif activity == 1:
                        veggie += 1
                        fruit += 1
                        print("you have gathered some fruit and veggies.")
                    elif activity == 2:
                        # select 2 variables between 1 and the number of cb's craftable
                        a = random.randint(1, 15)
                        b = random.randint(1, 15)
                        c = craftable_cb_s(a)
                        d = craftable_cb_s(b)
                        print("first celestial body you may craft is", c[7], "its effect are:", c[8],
                              "its costs this much twigs, grass, rocks, blood, meat, veggies and fruit respectively.", c[0],
                              c[1], c[2], c[3], c[4], c[5], c[6])
                        print("second celestial body you may craft is", d[7], "its effect are:", d[8],
                              "its costs this much twigs, grass, rocks, blood, meat, veggies and fruit respectively.", d[0],
                              d[1], d[2], d[3], d[4], d[5], d[6])
                        e = int(input("type 1 for the first, 2 for the second, 0 to ignore."))
                        if e == 1:
                            if twigs >= c[0] and grass >= c[1] and rocks >= c[2] and blood >= c[3] and meat >= c[4] and veggie >= c[5] and fruit >= c[6]:
                                twigs -= c[0]
                                grass -= c[1]
                                rocks -= c[2]
                                blood -= c[3]
                                meat -= c[4]
                                veggie -= c[5]
                                fruit -= c[6]
                                add_cb(a)

                            elif twigs >= d[0] and grass >= d[1] and rocks >= d[2] and blood >= d[3] and meat >= d[4] and veggie >= d[5] and fruit >= d[6]:
                                twigs -= d[0]
                                grass -= d[1]
                                rocks -= d[2]
                                blood -= d[3]
                                meat -= d[4]
                                veggie -= d[5]
                                fruit -= d[6]
                                add_cb(b)

                            cb_s = [cb_1, cb_2, cb_3, cb_4, cb_5]
                    elif activity == 3:
                        # combat
                        print("select an enemy.")
                        a = enemy_pool_winter()
                        print(a[4], a[2], "meat", a[3], "blood, and you need to roll a", a[0], a[1], "times")
                        b = enemy_pool_winter()
                        print(b[4], b[2], "meat", b[3], "blood, and you need to roll a", b[0], b[1], "times")
                        c = int(input("1 to choose one, 2 to choose 2"))
                        # main combat loop, you add dice rolls in a list and do an "if" for every cb
                        # remember to put a event in BOTH the loops, or not
                        dice_rolls = []
                        if 6 in cb_s:
                            dice_rolls += [1] * 6
                        x = 3
                        if cb_1 == 5:
                            x += 4
                        elif cb_2 == 5:
                            x += 4
                        elif cb_3 == 5:
                            x += 4
                        elif cb_4 == 5:
                            x += 4
                        elif cb_5 == 5:
                            x += 4
                        if cb_1 == 7:
                            x += 4
                        elif cb_2 == 7:
                            x += 4
                        elif cb_3 == 7:
                            x += 4
                        elif cb_4 == 7:
                            x += 4
                        elif cb_5 == 7:
                            x += 4
                        if cb_1 == 8:
                            for i in range(0, rocks, 10):
                                x += 1
                        elif cb_2 == 8:
                            for i in range(0, rocks, 10):
                                x += 1
                        elif cb_3 == 8:
                            for i in range(0, rocks, 10):
                                x += 1
                        elif cb_4 == 8:
                            for i in range(0, rocks, 10):
                                x += 1
                        elif cb_5 == 8:
                            for i in range(0, rocks, 10):
                                x += 1
                        if cb_1 == 10:
                            for i in range (0,atlas,1):
                                x += 1
                        if cb_2 == 10:
                            for i in range (0,atlas,1):
                                x += 1
                        if cb_3 == 10:
                            for i in range (0,atlas,1):
                                x += 1
                        if cb_4 == 10:
                            for i in range (0,atlas,1):
                                x += 1
                        if cb_5 == 10:
                            for i in range (0,atlas,1):
                                x += 1
                        if cb_s.count(14) >= 1 and meat > 1:
                            x *= 2
                        if cb_s.count(12) >= 1:
                            dice_rolls.append(6)
                            dice_rolls.append(6)
                        for i in range(0, x, 1):
                            d = (random.randint(1, 6))
                            print("you rolled a", d)
                            dice_rolls.append(d)
                        if c == 1:
                            if dice_rolls.count(a[0]) >= a[1]:
                                meat += a[2]
                                blood += a[3]
                                print("you won!")
                                atlas += 1
                            else:
                                hp -= 5
                                print("you lost.")
                        else:
                            if dice_rolls.count(b[0]) >= b[1]:
                                meat += b[2]
                                blood += b[3]
                                print("you won!")
                                atlas += 1
                            else:
                                hp -= 5
                                print("you lost.")
                    else:
                        pass
                print("you have", twigs, "twigs,", grass, "grass,", rocks, "rocks,", blood, "blood,", meat, "meat,",veggie, "veggie,", fruit, ",fruit")
                a = int(input("what would you like to eat? 1 = meat, 2 = veggie, 3 = fruit."))
                if a == 1 and meat > 0:
                    meat -= 1
                    hunger += 2
                    hunger = min(hunger, hun_max)
                elif a == 2 and veggie > 0:
                    veggie -= 1
                    hunger += 1
                    hp += 1
                    hp = min(hp, hp_max)
                    hunger = min(hunger, hun_max)
                elif a == 3 and fruit > 0:
                    fruit -= 1
                    hunger += 1
                    sanity += 2
                    hunger = min(hunger, hun_max)
                    sanity = min(sanity, san_max)
                if hp < 1:
                    dead()
            day = 0
    ########################### S P R İ N G #####################
        while day < 31:
            #the spring loop
            apply_passive_cb_s()
            if True:
                if cb_s.count(11) >= 1:
                    a = random.randint(1, 2)
                    if a == 1:
                        meat += 1
                    else:
                        blood += 10
                for time in range(0, 3, 1):
                    hunger -= 1
                    sanity -= 1
                    if sanity < 0:
                        hp -= 1
                    if hunger < 0:
                        hp -= 1
                    insulation -= 1
                    # full moon
                    if 3 in cb_s:
                        sanity += 1
                    print("hp:", hp, "hunger:", hunger, "sanity:", sanity, "insulation:", insulation)
                    while True:
                        activity = int(input(
                            "What would you like to do for the day? 0 -> gather materials 1 -> gather food 2 -> craft 3 -> combat"))
                        if activity == 0 or activity == 1 or activity == 2 or activity == 3 or activity == 4:
                            break
                    if activity == 0:
                        a = random.randint(1, 5)
                        b = random.randint(1, 5)
                        if a == 1 or b == 1:
                            twigs += 20
                            print("you have obtained some twigs!")
                        if a == 2 or b == 2:
                            grass += 50
                            print("you have obtained some grass!")
                        if a == 3 or b == 3:
                            rocks += 5
                            print("you have obtained some rocks!")
                        if a == 4 or b == 4:
                            veggie += 15
                            print("you have obtained some veggies!")
                        if a == 5 or b == 5:
                            fruit += 30
                            print("you have obtained some fruit!")
                    elif activity == 1:
                        veggie += 15
                        fruit += 30
                        print("you have gathered some fruit and veggies.")
                    elif activity == 2:
                        # select 2 variables between 1 and the number of cb's craftable
                        a = random.randint(1, 15)
                        b = random.randint(1, 15)
                        c = craftable_cb_s(a)
                        d = craftable_cb_s(b)
                        print("first celestial body you may craft is", c[7], "its effect are:", c[8],
                              "its costs this much twigs, grass, rocks, blood, meat, veggies and fruit respectively.",
                              c[0],
                              c[1], c[2], c[3], c[4], c[5], c[6])
                        print("second celestial body you may craft is", d[7], "its effect are:", d[8],
                              "its costs this much twigs, grass, rocks, blood, meat, veggies and fruit respectively.",
                              d[0],
                              d[1], d[2], d[3], d[4], d[5], d[6])
                        e = int(input("type 1 for the first, 2 for the second, 0 to ignore."))
                        if e == 1:
                            if twigs >= c[0] and grass >= c[1] and rocks >= c[2] and blood >= c[3] and meat >= c[4] and veggie >= c[5] and fruit >= c[6]:
                                twigs -= c[0]
                                grass -= c[1]
                                rocks -= c[2]
                                blood -= c[3]
                                meat -= c[4]
                                veggie -= c[5]
                                fruit -= c[6]
                                add_cb(a)

                            elif twigs >= d[0] and grass >= d[1] and rocks >= d[2] and blood >= d[3] and meat >= d[4] and veggie <= d[5] and fruit >= d[6]:
                                twigs -= d[0]
                                grass -= d[1]
                                rocks -= d[2]
                                blood -= d[3]
                                meat -= d[4]
                                veggie -= d[5]
                                fruit -= d[6]
                                add_cb(b)

                            cb_s = [cb_1, cb_2, cb_3, cb_4, cb_5]
                    elif activity == 3:
                        # combat
                        print("select an enemy.")
                        a = enemy_pool_spring()
                        print(a[4], a[2], "meat", a[3], "blood, and you need to roll a", a[0], a[1], "times")
                        b = enemy_pool_spring()
                        print(b[4], b[2], "meat", b[3], "blood, and you need to roll a", b[0], b[1], "times")
                        c = int(input("1 to choose one, 2 to choose 2"))
                        # main combat loop, you add dice rolls in a list and do an "if" for every cb
                        # remember to put a event in BOTH the loops, or not
                        dice_rolls = []
                        if 6 in cb_s:
                            dice_rolls += [1] * 6
                        x = 3
                        if cb_1 == 5:
                            x += 4
                        elif cb_2 == 5:
                            x += 4
                        elif cb_3 == 5:
                            x += 4
                        elif cb_4 == 5:
                            x += 4
                        elif cb_5 == 5:
                            x += 4
                        if cb_1 == 7:
                            x += 4
                        elif cb_2 == 7:
                            x += 4
                        elif cb_3 == 7:
                            x += 4
                        elif cb_4 == 7:
                            x += 4
                        elif cb_5 == 7:
                            x += 4
                        if cb_1 == 8:
                            for i in range(0, rocks, 10):
                                x += 1
                        elif cb_2 == 8:
                            for i in range(0, rocks, 10):
                                x += 1
                        elif cb_3 == 8:
                            for i in range(0, rocks, 10):
                                x += 1
                        elif cb_4 == 8:
                            for i in range(0, rocks, 10):
                                x += 1
                        elif cb_5 == 8:
                            for i in range(0, rocks, 10):
                                x += 1
                        if cb_1 == 10:
                            for i in range(0, atlas, 1):
                                x += 1
                        if cb_2 == 10:
                            for i in range(0, atlas, 1):
                                x += 1
                        if cb_3 == 10:
                            for i in range(0, atlas, 1):
                                x += 1
                        if cb_4 == 10:
                            for i in range(0, atlas, 1):
                                x += 1
                        if cb_5 == 10:
                            for i in range(0, atlas, 1):
                                x += 1
                        if cb_s.count(14) >= 1 and meat > 1:
                            x *= 2
                        if cb_s.count(12) >= 1:
                            dice_rolls.append(6)
                            dice_rolls.append(6)
                        for i in range(0, x, 1):
                            d = (random.randint(1, 6))
                            print("you rolled a", a)
                            dice_rolls.append(d)
                        if c == 1:
                            if dice_rolls.count(a[0]) >= a[1]:
                                meat += a[2]
                                blood += a[3]
                                print("you won!")
                                atlas += 1
                            else:
                                hp -= 5
                                print("you lost.")
                        else:
                            if dice_rolls.count(b[0]) >= b[1]:
                                meat += b[2]
                                blood += b[3]
                                print("you won!")
                                atlas += 1
                            else:
                                hp -= 5
                                print("you lost.")
                print("you have", twigs, "twigs,", grass, "grass,", rocks, "rocks,", blood, "blood,", meat, "meat,",
                      veggie, "veggie,", fruit, ",fruit")
                a = int(input("what would you like to eat? 1 = meat, 2 = veggie, 3 = fruit."))
                if a == 1 and meat > 0:
                    meat -= 1
                    hunger += 2
                    hunger = min(hunger, hun_max)
                elif a == 2 and veggie > 0:
                    veggie -= 1
                    hunger += 1
                    hp += 1
                    hp = min(hp, hp_max)
                    hunger = min(hunger, hun_max)
                elif a == 3 and fruit > 0:
                    fruit -= 1
                    hunger += 1
                    sanity += 2
                    hunger = min(hunger, hun_max)
                    sanity = min(sanity, san_max)

            day = 0
            ##################### S U M M E R ############
        while day < 31:
            #the summer loop
            apply_passive_cb_s()
            if True:
                day += 1
                if cb_s.count(15) >= 1:
                    fruit += 1
                if cb_s.count(11) >= 1:
                    a = random.randint(1, 2)
                    if a == 1:
                        meat += 1
                    else:
                        blood += 10
                        day += 1
                for time in range(0, 3, 1):
                    hunger -= 1
                    # full moon
                    if 3 in cb_s:
                        sanity += 1
                    if thirst == 0:
                        hp -= 1
                    thirst -= 1
                    if sanity < 0:
                        hp -= 1
                    if hunger < 0:
                        hp -= 1
                    if cb_1 == 2:
                        thirst += 1
                    #rainclouds
                    elif cb_2  == 2:
                        thirst += 1
                    elif cb_3 == 2:
                        thirst += 1
                    elif cb_4 == 2:
                        thirst += 1
                    elif cb_5 == 2:
                        thirst += 2
                    #end of rainclouds
                    print("hp:", hp, "hunger:", hunger, "sanity:", sanity, "insulation:", insulation)
                    while True:
                        activity = int(input(
                            "What would you like to do for the day? 0 -> gather materials 1 -> gather food 2 -> craft 3 -> combat"))
                        if activity == 0 or activity == 1 or activity == 2 or activity == 3 or activity == 4:
                            break
                    if activity == 0:
                        a = random.randint(1, 5)
                        b = random.randint(1, 5)
                        if a == 1 or b == 1:
                            twigs += 10
                            print("you have obtained some twigs!")
                        if a == 2 or b == 2:
                            grass += 10
                            print("you have obtained some grass!")
                        if a == 3 or b == 3:
                            rocks += 20
                            print("you have obtained some rocks!")
                        if a == 4 or b == 4:
                            veggie += 10
                            print("you have obtained some veggies!")
                        if a == 5 or b == 5:
                            fruit += 5
                            print("you have obtained some fruit!")
                    elif activity == 1:
                        veggie += 10
                        fruit += 5
                        print("you have gathered some fruit and veggies.")
                    elif activity == 2:
                        # select 2 variables between 1 and the number of cb's craftable
                        a = random.randint(1, 15)
                        b = random.randint(1, 15)
                        c = craftable_cb_s(a)
                        d = craftable_cb_s(b)
                        print("first celestial body you may craft is", c[7], "its effect are:", c[8],
                              "its costs this much twigs, grass, rocks, blood, meat, veggies and fruit respectively.",
                              c[0],
                              c[1], c[2], c[3], c[4], c[5], c[6])
                        print("second celestial body you may craft is", d[7], "its effect are:", d[8],
                              "its costs this much twigs, grass, rocks, blood, meat, veggies and fruit respectively.",
                              d[0],
                              d[1], d[2], d[3], d[4], d[5], d[6])
                        e = int(input("type 1 for the first, 2 for the second, 0 to ignore."))
                        if e == 1:
                            if twigs >= c[0] and grass >= c[1] and rocks >= c[2] and blood >= c[3] and meat >= c[4] and veggie >= c[5] and fruit >= c[6]:
                                twigs -= c[0]
                                grass -= c[1]
                                rocks -= c[2]
                                blood -= c[3]
                                meat -= c[4]
                                veggie -= c[5]
                                fruit -= c[6]
                                add_cb(a)

                            elif twigs >= d[0] and grass >= d[1] and rocks >= d[2] and blood >= d[3] and meat >= d[4] and veggie >= d[5] and fruit >= d[6]:
                                twigs -= d[0]
                                grass -= d[1]
                                rocks -= d[2]
                                blood -= d[3]
                                meat -= d[4]
                                veggie -= d[5]
                                fruit -= d[6]
                                add_cb(b)

                            cb_s = [cb_1, cb_2, cb_3, cb_4, cb_5]
                    elif activity == 3:
                        # combat
                        print("select an enemy.")
                        a = enemy_pool_summer()
                        print(a[4], a[2], "meat", a[3], "blood, and you need to roll a", a[0], a[1], "times")
                        b = enemy_pool_summer()
                        print(b[4], b[2], "meat", b[3], "blood, and you need to roll a", b[0], b[1], "times")
                        c = int(input("1 to choose one, 2 to choose 2"))
                        # main combat loop, you add dice rolls in a list and do an "if" for every cb
                        # remember to put a event in BOTH the loops, or not
                        dice_rolls = []
                        if 6 in cb_s:
                            dice_rolls += [1] * 6
                        x = 3
                        if cb_1 == 5:
                            x += 4
                        elif cb_2 == 5:
                            x += 4
                        elif cb_3 == 5:
                            x += 4
                        elif cb_4 == 5:
                            x += 4
                        elif cb_5 == 5:
                            x += 4
                        if cb_1 == 7:
                            x += 4
                        elif cb_2 == 7:
                            x += 4
                        elif cb_3 == 7:
                            x += 4
                        elif cb_4 == 7:
                            x += 4
                        elif cb_5 == 7:
                            x += 4
                        if cb_1 == 8:
                            for i in range(0, rocks, 10):
                                x += 1
                        elif cb_2 == 8:
                            for i in range(0, rocks, 10):
                                x += 1
                        elif cb_3 == 8:
                            for i in range(0, rocks, 10):
                                x += 1
                        elif cb_4 == 8:
                            for i in range(0, rocks, 10):
                                x += 1
                        elif cb_5 == 8:
                            for i in range(0, rocks, 10):
                                x += 1
                        if cb_1 == 10:
                            for i in range(0, atlas, 1):
                                x += 1
                        if cb_2 == 10:
                            for i in range(0, atlas, 1):
                                x += 1
                        if cb_3 == 10:
                            for i in range(0, atlas, 1):
                                x += 1
                        if cb_4 == 10:
                            for i in range(0, atlas, 1):
                                x += 1
                        if cb_5 == 10:
                            for i in range(0, atlas, 1):
                                x += 1
                        if cb_s.count(12) >= 1:
                            dice_rolls.append(6)
                            dice_rolls.append(6)
                        if cb_s.count(14) >= 1 and meat > 1:
                            x *= 2
                        for i in range(0, x, 1):
                            d = (random.randint(1, 6))
                            print("you rolled a", a)
                            dice_rolls.append(d)
                        if c == 1:
                            if dice_rolls.count(a[0]) >= a[1]:
                                meat += a[2]
                                blood += a[3]
                                print("you won!")
                                atlas += 1
                            else:
                                hp -= 5
                                print("you lost.")
                        else:
                            if dice_rolls.count(b[0]) >= b[1]:
                                meat += b[2]
                                blood += b[3]
                                print("you won!")
                                atlas += 1
                            else:
                                hp -= 5
                                print("you lost.")
                print("you have", twigs, "twigs,", grass, "grass,", rocks, "rocks,", blood, "blood,", meat, "meat,",veggie, "veggie,", fruit, ",fruit")
                a = int(input("what would you like to eat? 1 = meat, 2 = veggie, 3 = fruit."))
                if a == 1 and meat > 0:
                    meat -= 1
                    hunger += 2
                    hunger = min(hunger, hun_max)
                elif a == 2 and veggie > 0:
                    veggie -= 1
                    hunger += 1
                    hp += 1
                    hp = min(hp, hp_max)
                    hunger = min(hunger, hun_max)
                elif a == 3 and fruit > 0:
                    fruit -= 1
                    hunger += 1
                    sanity += 2
                    hunger = min(hunger, hun_max)
                    sanity = min(sanity, san_max)
                if hp < 1:
                    dead()

                else:
                    break

        day = 0
            ########### A P O C Y L P S E ##################
        while day < 31:
            #the apocylpse loop
            if True:
                apply_passive_cb_s()
                for time in range(0, 3, 1):
                    hunger -= 1
                    # full moon
                    if 3 in cb_s:
                        sanity += 1
                    sanity -= 1
                    if sanity < 0:
                        hp -= 1
                    if hunger < 0:
                        hp -= 1
                    insulation -= 1
                    print("hp:", hp, "hunger:", hunger, "sanity:", sanity, "insulation:", insulation)
                    while True:
                        activity = int(input(
                            "What would you like to do for the day? 0 -> gather materials 1 -> gather food 2 -> craft 3 -> combat"))
                        if activity == 0 or activity == 1 or activity == 2 or activity == 3 or activity == 4:
                            break
                    if activity == 0:
                        a = random.randint(1, 5)
                        b = random.randint(1, 5)
                        if a == 1 or b == 1:
                            twigs += 30
                            print("you have obtained some twigs!")
                        if a == 2 or b == 2:
                            grass += 15
                            print("you have obtained some grass!")
                        if a == 3 or b == 3:
                            rocks += 50
                            print("you have obtained some rocks!")
                        if a == 4 or b == 4:
                            veggie += 1
                            print("you have obtained some veggies!")
                        if a == 5 or b == 5:
                            fruit += 1
                            print("you have obtained some fruit!")
                    elif activity == 1:
                        veggie += 1
                        fruit += 1
                        print("you have gathered some fruit and veggies.")
                    elif activity == 2:
                        # select 2 variables between 1 and the number of cb's craftable
                        a = random.randint(1, 15)
                        b = random.randint(1, 15)
                        c = craftable_cb_s(a)
                        d = craftable_cb_s(b)
                        print("first celestial body you may craft is", c[7], "its effect are:", c[8],
                              "its costs this much twigs, grass, rocks, blood, meat, veggies and fruit respectively.",
                              c[0],
                              c[1], c[2], c[3], c[4], c[5], c[6])
                        print("second celestial body you may craft is", d[7], "its effect are:", d[8],
                              "its costs this much twigs, grass, rocks, blood, meat, veggies and fruit respectively.",
                              d[0],
                              d[1], d[2], d[3], d[4], d[5], d[6])
                        e = int(input("type 1 for the first, 2 for the second, 0 to ignore."))
                        if e == 1:
                            if twigs >= c[0] and grass >= c[1] and rocks >= c[2] and blood >= c[3] and meat >= c[4] and veggie >= c[5] and fruit >= c[6]:
                                twigs -= c[0]
                                grass -= c[1]
                                rocks -= c[2]
                                blood -= c[3]
                                meat -= c[4]
                                veggie -= c[5]
                                fruit -= c[6]
                                add_cb(a)

                            elif twigs >= d[0] and grass >= d[1] and rocks >= d[2] and blood >= d[3] and meat >= d[4] and veggie >= d[5] and fruit >= d[6]:
                                twigs -= d[0]
                                grass -= d[1]
                                rocks -= d[2]
                                blood -= d[3]
                                meat -= d[4]
                                veggie -= d[5]
                                fruit -= d[6]
                                add_cb(b)

                            cb_s = [cb_1, cb_2, cb_3, cb_4, cb_5]
                    elif activity == 3:
                        # combat
                        print("select an enemy.")
                        a = enemy_pool_apocylpse()
                        print(a[4], a[2], "meat", a[3], "blood, and you need to roll a", a[0], a[1], "times")
                        b = enemy_pool_apocylpse()
                        print(b[4], b[2], "meat", b[3], "blood, and you need to roll a", b[0], b[1], "times")
                        c = int(input("1 to choose one, 2 to choose 2"))
                        # main combat loop, you add dice rolls in a list and do an "if" for every cb
                        # remember to put a event in BOTH the loops, or not
                        dice_rolls = []
                        if 6 in cb_s:
                            dice_rolls += [1] * 6
                        x = 3
                        if cb_1 == 5:
                            x += 4
                        elif cb_2 == 5:
                            x += 4
                        elif cb_3 == 5:
                            x += 4
                        elif cb_4 == 5:
                            x += 4
                        elif cb_5 == 5:
                            x += 4
                        if cb_1 == 7:
                            x += 4
                        elif cb_2 == 7:
                            x += 4
                        elif cb_3 == 7:
                            x += 4
                        elif cb_4 == 7:
                            x += 4
                        elif cb_5 == 7:
                            x += 4
                        if cb_1 == 8:
                            for i in range(0, rocks, 10):
                                x += 1
                        elif cb_2 == 8:
                            for i in range(0, rocks, 10):
                                x += 1
                        elif cb_3 == 8:
                            for i in range(0, rocks, 10):
                                x += 1
                        elif cb_4 == 8:
                            for i in range(0, rocks, 10):
                                x += 1
                        elif cb_5 == 8:
                            for i in range(0, rocks, 10):
                                x += 1
                        if cb_1 == 10:
                            for i in range(0, atlas, 1):
                                x += 1
                        if cb_2 == 10:
                            for i in range(0, atlas, 1):
                                x += 1
                        if cb_3 == 10:
                            for i in range(0, atlas, 1):
                                x += 1
                        if cb_4 == 10:
                            for i in range(0, atlas, 1):
                                x += 1
                        if cb_5 == 10:
                            for i in range(0, atlas, 1):
                                x += 1
                        if cb_s.count(14) >= 1 and meat > 1:
                            x *= 2
                        if cb_s.count(12) >= 1:
                            dice_rolls.append(6)
                            dice_rolls.append(6)
                        for i in range(0, x, 1):
                            d = (random.randint(1, 6))
                            print("you rolled a", a)
                            dice_rolls.append(d)
                        if c == 1:
                            if dice_rolls.count(a[0]) >= a[1]:
                                meat += a[2]
                                blood += a[3]
                                print("you won!")
                                atlas += 1
                            else:
                                hp -= 5
                                print("you lost.")
                        else:
                            if dice_rolls.count(b[0]) >= b[1]:
                                meat += b[2]
                                blood += b[3]
                                print("you won!")
                                atlas += 1
                            else:
                                hp -= 5
                                print("you lost.")
                print("you have", twigs, "twigs,", grass, "grass,", rocks, "rocks,", blood, "blood,", meat, "meat,",
                        veggie, "veggie,", fruit, ",fruit")
                a = int(input("what would you like to eat? 1 = meat, 2 = veggie, 3 = fruit."))
                if a == 1 and meat > 0:
                    meat -= 1
                    hunger += 2
                    hunger = min(hunger, hun_max)
                elif a == 2 and veggie > 0:
                    veggie -= 1
                    hunger += 1
                    hp += 1
                    hp = min(hp, hp_max)
                    hunger = min(hunger, hun_max)
                elif a == 3 and fruit > 0:
                    fruit -= 1
                    hunger += 1
                    sanity += 2
                    hunger = min(hunger, hun_max)
                    sanity = min(sanity, san_max)
                if hp < 1:
                    dead()

                else:
                    break


        
    
