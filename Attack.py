def Attack():
    print("How will you attack?")
    action = input("With your Weapon or with Magic? ")
    if action.lower() == 'melee':
        from CharSetup import Char_name
        if Char_name.lower() == 'wake':
            print("You use the Scythe and you can do either a 'Light Attack' or a 'Precise Attack'")
        elif Char_name.lower() == 'finrear':
            print("You use the Great Hammer and you can do either a 'Heavy Attack' or a ' Medium Attack'")
        elif Char_name.lower() == 'chrono':
            print("You use Evelyn(musket) and you can either shoot 'Rapid Fire' or 'Precise'")
        elif Char_name.lower() == 'wake' or Char_name.lower == 'finrear':
            Char_wep_current = input("How do you want to swing? ")
            Char_att_current = 1
        elif Char_name.lower() == 'chrono':
            Char_wep_current = input("How do you want to shoot? ")
            Char_att_current = 1
    if action.lower() == 'magic':
        from CharSetup import Char_name
        if Char_name.lower() == 'wake':
            print("Your spells are 'Light Heal', 'Bloodtinge', and 'Swift Walk'")
        elif Char_name.lower() == 'finrear':
            print("Your spells are 'Heavy Heal', 'Bolt Strike', and 'Buckle Armour'")
        elif Char_name.lower() == 'chrono':
            print("Your spells are 'Mid Heal', 'Barrel Induction', and 'Reinforced Pellets'")
        Char_spell_current = input("What spell will you use? ")
        Char_att_current == 2
