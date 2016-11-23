def Char():
    from Attack import Char_att_current
    if Char_att_current == 1:
        import random
        from Attack import Char_wep_current
        from HstlSetup import Hstl_hp_current
        from CharSetup import Char_name, Char_hp_current, Char_hp_max
        if Char_name.lower() == 'wake' and Char_wep_current.lower() == 'light attack':
            Hit_roll = random.randint(1,100)
            Hit_chance = 90
            if Hit_roll <= Hit_chance:
                Char_dmg_current = 10
                print("You hit with " + str(Char_wep_current.lower()) + " for " + str(Char_dmg_current) + "!")
            else:
                print("You missed.")
        elif Char_name.lower() == 'wake' and Char_wep_current.lower() == 'heavy attack':
            Hit_roll = random.randint(1,100)
            Hit_chance = 60
            if Hit_roll <= Hit_chance:
                Char_dmg_current = 20
                print("You hit with " + str(Char_wep_current.lower()) + " for " + str(Char_dmg_current) + "!")
            else:
                print("You missed.")
        elif Char_name.lower() == 'finrear' and Char_wep_current.lower() == 'heavy attack':
            Hit_roll = random.randint(1,100)
            Hit_chance = 60
            if Hit_roll <= Hit_chance:
                Char_dmg_current = 20
                print("You hit with " + str(Char_wep_current.lower()) + " for " + str(Char_dmg_current) + "!")
            else:
                print("You missed.")
        elif Char_name.lower() == 'finrear' and Char_wep_current.lower() == 'medium attack':
            Hit_roll = random.randint(1,100)
            Hit_chance = 75
            if Hit_roll <= Hit_chance:
                Char_dmg_current = 15
                print("You hit with " + str(Char_wep_current.lower()) + " for " + str(Char_dmg_current) + "!")
            else:
                print("You missed.")
        elif Char_name.lower() == 'chrono' and Char_wep_current.lower() == 'rapid fire':
            Hit_roll = random.randint(1,100)
            Hit_chance = 70
            if Hit_roll <= Hit_chance:
                Char_dmg_current = 10
                Hit_roll = random.randint(1,100)
                if Hit_roll <= Hit_chance:
                    Char_dmg_current = Char_dmg_current + 10
                    print("You hit with " + str(Char_wep_current.lower()) + " for " + str(Char_dmg_current) + "!")
                else:
                    print("You hit with " + str(Char_wep_current.lower()) + " for " + str(Char_dmg_current) + "!")
            else:
                print("You missed.")
        elif Char_name.lower() == 'chrono' and Char_wep_current.lower() == 'precise':
            Hit_roll = random.randint(1,100)
            Hit_chance = 90
            if Hit_roll <= Hit_chance:
                Char_dmg_current = 10
                print("You hit with " + str(Char_wep_current.lower()) + " for " + str(Char_dmg_current) + "!")
            else:
                print("You missed.")
    if Char_att_current == 2:
        from Attack import Char_spell_current
        if Char_name.lower() == 'wake' and Char_spell_current.lower() == 'light heal':
            if Char_hp_current <= Char_hp_max - 15:
                Char_hp_current = Char_hp_max
            else:
                Char_hp_current = Char_hp_current + 15
        elif Char_name.lower() == 'wake' and Char_spell_current.lower() == 'blood rush':
        elif Char_name.lower() == 'wake' and Char_spell_current.lower() == 'mutilation':
        elif Char_name.lower() == 'finrear' and Char_spell_current.lower() == 'heavy heal':
            if Char_hp_current <= Char_hp_max - 25:
                Char_hp_current = Char_hp_max
            else:
                Char_hp_current = Char_hp_current + 25
        elif Char_name.lower() == 'finrear' and Char_spell_current.lower() == 'bolt strike':
        elif Char_name.lower() == 'finrear' and Char_spell_current.lower() == 'buckle armor':
        elif Char_name.lower() == 'chrono' and Char_spell_current.lower() == 'mid heal':
            if Char_hp_current <= Char_hp_max - 20:
                Char_hp_current = Char_hp_max
            else:
                Char_hp_current = Char_hp_current + 20
        elif Char_name.lower() == 'chrono' and Char_spell_current.lower() == 'barrel induction':
        elif Char_name.lower() == 'chrono' and Char_spell_current.lower() == 'reinforced pellets':
def Hstl():
    #PLACEHOLDER
