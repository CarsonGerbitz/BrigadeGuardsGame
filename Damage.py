def Char():
    from Attack import Char_att_current
    if Char_att_current == 1:
        from Attack import Char_wep_current
        from HstlSetup import Hstl_hp_current
        from CharSetup import Char_name, Char_hp_current
        if Char_name.lower() == 'wake' and Char_wep_current.lower() == 'light attack':
            Char_dmg_current = 50
        if Char_name.lower() == 'wake' and Char_wep_current.lower() == 'precise attack':
            Char_dmg_current = 50
        if Char_name.lower() == 'finrear' and Char_wep_current.lower() == 'heavy attack':
            Char_dmg_current = 50
        if Char_name.lower() == 'finrear' and Char_wep_current.lower() == 'medium attack':
            Char_dmg_current = 50
        if Char_name.lower() == 'chrono' and Char_wep_current.lower() == 'rapid fire':
            Char_dmg_current = 50
        if Char_name.lower() == 'chrono' and Char_wep_current.lower() == 'precise':
            Char_dmg_current = 50
    if Char_att_current == 2:
        from Attack import Char_spell_current
        if Char_name.lower() == 'wake' and Char_spell_current.lower() == 'light heal':
            if Char_hp_current <= Char_hp_max - 15:
                Char_hp_current = Char_hp_max
            else:
                Char_hp_current = Char_hp_current + 15
        if Char_name.lower() == 'wake' and Char_spell_current.lower() == 'blood rush':
        if Char_name.lower() == 'wake' and Char_spell_current.lower() == 'mutilation':
        if Char_name.lower() == 'finrear' and Char_spell_current.lower() == 'heavy heal':
        if Char_name.lower() == 'finrear' and Char_spell_current.lower() == 'bolt strike':
        if Char_name.lower() == 'finrear' and Char_spell_current.lower() == 'buckle armour':
        if Char_name.lower() == 'chrono' and Char_spell_current.lower() == 'mid heal':
        if Char_name.lower() == 'chrono' and Char_spell_current.lower() == 'barrel induction':
        if Char_name.lower() == 'chrono' and Char_spell_current.lower() == 'reinforced pellets':
def Hstl():
    #PLACEHOLDER
