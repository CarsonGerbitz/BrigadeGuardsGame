def Attack():
    print("How will you attack?")
    action = input("Melee or Magic? ")
    if action.lower() == 'melee':
        from CharSetup import Char_name
        if Char_name.lower == 'wake':
            print("You use the Scythe and you can do either a 'Light Attack' or a 'Precise Attack'")
        if Char_name.lower == 'finrear':
            print("You use the Great Hammer and you can do either a 'Heavy Attack' or a ' Medium Attack'")
        if Char_name.lower == 'chrono':
            print("You use Evelyn(musket) and you can either shoot 'Rapid Fire' or 'Precise'")
        if Char_name.lower == 'wake' or Char_name.lower == 'dave':
            action = input("How do you want to swing? ")
        if Char_name.lower == 'chrono':
            action = input("How do you want to shoot? ")
    if action.lower() == 'magic':
        from CharSetup import Char_name
        if Char_name.lower == 'wake':
            print("Your spells are 'Light Heal', 'Bloodtinge', and 'Swift Walk'")
        if Char_name.lower == 'finrear':
            print("Your spells are 'Heavy Heal', 'Bolt Strike', and 'Buckle Armour'")
        if Char_name.lower == 'chrono':
            print("Your spells are 'Mid Heal', 'Barrel Induction', and 'Reinforced Pellets'")
        action = input("What spell will you use? ")
