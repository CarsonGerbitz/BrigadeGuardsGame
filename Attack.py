def Attack():
    print("How will you attack?")
    action = input("With your Weapon or with Ether? ")
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
    if action.lower() == 'Ether':
        from CharSetup import Char_name
        if Char_name.lower() == 'wake':
            print("Your spells are 'Light Heal', 'Blood Rush', and 'Mutilation'")
            '''Light heal heals for 15.
    Blood Rush makes it where the less health you have, the more damage you do and the more Agl you have.
    Mutilation is a next attack Large Damage boost for a bit of your health'''
        elif Char_name.lower() == 'finrear':
            print("Your spells are 'Heavy Heal', 'Bolt Strike', and 'Buckle Armor'")
            '''Heavy Heal heals for 25.
    Bolt Strike is a Large ammount of Bolt damage.
    Buckle Armor increases defence for 3 rounds.'''
        elif Char_name.lower() == 'chrono':
            print("Your spells are 'Mid Heal', 'Barrel Induction', and 'Reinforced Pellets'")
            '''Mid Heal heals for 20.
    Barrel Induction does a large ammount of fire damage.
    Reinforced Pellits increases your damage for 5 rounds.'''
        Char_spell_current = input("What spell will you use? ")
        Char_att_current == 2
