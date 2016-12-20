def Char():
    from Attack import Char_att_current
    from EvdCheck import HDC_Final_Check, CDC_Final_Check, Evade
    from Attack import Char_wep_current
    #from HstlSetup import Hstl_name, Hstl_hp_current, Hstl_hp_max, Hstl_buff_left, Hstl_buff_max, Hstl_ether_current
    from CharSetup import Char_name, Char_hp_current, Char_hp_max, Char_buff_left, Char_buff_max, Char_ether_current
    Char_Hit_Chance = 100
    if Char_att_current == 2:
        from Attack import Char_spell_current
        if Char_name.lower() == 'wake' and Char_spell_current.lower() == 'light heal':
            if Char_ether_current >= 10:
                if Char_hp_current <= Char_hp_max - 15:
                    Char_hp_current = Char_hp_max
                else:
                    Char_hp_current = Char_hp_current + 15
        elif Char_name.lower() == 'wake' and Char_spell_current.lower() == 'blood rush':
            if Char_ether_current >= 20:
                Char_buff_current = 'br'
                if Char_buff_left <= Char_buff_max - 3:
                    Char_buff_left = Char_buff_max
                else:
                    Char_buff_left = Char_buff_left + 3
        elif Char_name.lower() == 'wake' and Char_spell_current.lower() == 'mutilation':
            if Char_ether_current >= 20:
                Char_buff_current = 'm'
                if Char_buff_left <= Char_buff_max - 3:
                    Char_buff_left = Char_buff_max
                else:
                    Char_buff_left = Char_buff_left + 3
        elif Char_name.lower() == 'finrear' and Char_spell_current.lower() == 'heavy heal':
            if Char_ether_current >= 20:
                if Char_hp_current <= Char_hp_max - 25:
                    Char_hp_current = Char_hp_max
                else:
                    Char_hp_current = Char_hp_current + 25
        elif Char_name.lower() == 'finrear' and Char_spell_current.lower() == 'bolt strike':
            Char_Hit_Chance == 80
            if Char_ether_current >= 15:
                Evade()
                if HDC_Final_Check == 0:
                    Char_dmg_current = 20
                    print("You hit with " + str(Char_spell_current.lower()) + " for " + str(Char_dmg_current) + "!")
                else:
                    print("You missed.")
        elif Char_name.lower() == 'finrear' and Char_spell_current.lower() == 'buckle armor':
            if Char_ether_current >= 20:
                Char_buff_current = 'ba'
                if Char_buff_left <= Char_buff_max - 3:
                    Char_buff_left = Char_buff_max
                else:
                    Char_buff_left = Char_buff_left + 3
        elif Char_name.lower() == 'chrono' and Char_spell_current.lower() == 'mid heal':
            if Char_ether_current >= 15:
                if Char_hp_current <= Char_hp_max - 20:
                    Char_hp_current = Char_hp_max
                else:
                    Char_hp_current = Char_hp_current + 20
        elif Char_name.lower() == 'chrono' and Char_spell_current.lower() == 'barrel induction':
            Char_Hit_Chance == 100
            if Char_ether_current >= 15:
                Evade()
                if HDC_Final_Check == 0:
                    Char_dmg_current = 15
                    print("You hit with " + str(Char_spell_current.lower()) + " for " + str(Char_dmg_current) + "!")
                else:
                    print("You missed.")
        elif Char_name.lower() == 'chrono' and Char_spell_current.lower() == 'reinforced pellets':
            if Char_ether_current >= 20:
                Char_buff_current = 'rp'
                if Char_buff_left <= Char_buff_max - 3:
                    Char_buff_left = Char_buff_max
                else:
                    Char_buff_left = Char_buff_left + 3
    elif Char_att_current == 1:
        if Char_name.lower() == 'wake' and Char_wep_current.lower() == 'light attack':
            Evade()
            if HDC_Final_Check == 0:
                Char_dmg_current = 10
                print("You hit with " + str(Char_wep_current.lower()) + " for " + str(Char_dmg_current) + "!")
                if Char_buff_current == 'br' and Char_buff_left >= 1:
                    if Char_hp_current >= 40:
                        Char_dmg_current = Char_dmg_current + 0
                    elif 30 >= Char_hp_current > 40:
                        Char_dmg_current = Char_dmg_current + 5
                    elif 20 >= Char_hp_current > 30:
                        Char_dmg_current = Char_dmg_current + 10
                    elif 10 >= Char_hp_current > 20:
                        Char_dmg_current = Char_dmg_current + 15
                    elif Char_hp_current < 10:
                        Char_dmg_current = Char_dmg_current + 20
            else:
                print("You missed.")
        elif Char_name.lower() == 'wake' and Char_wep_current.lower() == 'heavy attack':
            Evade()
            if HDC_Final_Check == 0:
                Char_dmg_current = 20
                print("You hit with " + str(Char_wep_current.lower()) + " for " + str(Char_dmg_current) + "!")
                if Char_buff_current == 'br' and Char_buff_left >= 1:
                    if Char_hp_current >= 40:
                        Char_dmg_current = Char_dmg_current + 0
                    elif 30 >= Char_hp_current > 40:
                        Char_dmg_current = Char_dmg_current + 5
                    elif 20 >= Char_hp_current > 30:
                        Char_dmg_current = Char_dmg_current + 10
                    elif 10 >= Char_hp_current > 20:
                        Char_dmg_current = Char_dmg_current + 15
                    elif Char_hp_current < 10:
                        Char_dmg_current = Char_dmg_current + 20
            else:
                print("You missed.")
        elif Char_name.lower() == 'finrear' and Char_wep_current.lower() == 'heavy attack':
            Evade()
            if HDC_Final_Check == 0:
                Char_dmg_current = 20
                print("You hit with " + str(Char_wep_current.lower()) + " for " + str(Char_dmg_current) + "!")
            else:
                print("You missed.")
        elif Char_name.lower() == 'finrear' and Char_wep_current.lower() == 'medium attack':
            Evade()
            if HDC_Final_Check == 0:
                Char_dmg_current = 15
                print("You hit with " + str(Char_wep_current.lower()) + " for " + str(Char_dmg_current) + "!")
            else:
                print("You missed.")
        elif Char_name.lower() == 'chrono' and Char_wep_current.lower() == 'rapid fire':
            Evade()
            if HDC_Final_Check == 0:
                Char_dmg_current = 10
                Evade()
                if Char_buff_current == 'rp' and Char_buff_left >= 1:
                    Char_dmg_current = Char_dmg_current + 15
                elif HDC_Final_Check == 0:
                    Char_dmg_current = Char_dmg_current + 10
                    print("You hit with " + str(Char_wep_current.lower()) + " for " + str(Char_dmg_current) + "!")
                else:
                    print("You hit with " + str(Char_wep_current.lower()) + " for " + str(Char_dmg_current) + "!")
            else:
                print("You missed.")
        elif Char_name.lower() == 'chrono' and Char_wep_current.lower() == 'precise':
            Evade()
            if HDC_Final_Check == 0:
                Char_dmg_current = 10
                print("You hit with " + str(Char_wep_current.lower()) + " for " + str(Char_dmg_current) + "!")
            else:
                print("You missed.")
def Hstl():
    Hstl_dmg_current = 0
    #PLACEHOLDER
