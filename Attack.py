def Attack():
    print("How will you attack?")
    action = input("With your Weapon or with Ether? ")
    if action.lower() == 'melee':
        from CharSetup import Char_name
        if Char_name.lower() == 'wake':
            print("You use the Scythe and you can do either a 'Light Attack' or a 'Heavy Attack'")
            Char_wep_current = input("How do you want to swing? ")
            Char_att_current = 1
            if Char_wep_current.lower() == 'la' or Char_wep_current.lower() == 'light attack':
                Char_wep_current = 'light attack'
            elif Char_wep_current.lower() == 'ha' or Char_wep_current.lower() == 'heavy attack':
                Char_wep_current = 'heavy attack'
            else:
                print("That is not an attack you can use, please try again.")
                Attack()
        elif Char_name.lower() == 'finrear':
            print("You use the Great Hammer and you can do either a 'Heavy Attack' or a ' Medium Attack'")
            Char_wep_current = input("How do you want to swing? ")
            Char_att_current = 1
            if Char_wep_current.lower() == 'ma' or Char_wep_current.lower() == 'medium attack':
                Char_wep_current = 'medium attack'
            elif Char_wep_current.lower() == 'ha' or Char_wep_current.lower() == 'heavy attack':
                Char_wep_current = 'heavy attack'
            else:
                print("That is not an attack you can use, please try again.")
                Attack()
        elif Char_name.lower() == 'chrono':
            print("You use Evelyn(Repeating Musket) and you can either shoot 'Rapid Fire' or 'Precise'")
            Char_wep_current = input("How do you want to shoot? ")
            Char_att_current = 1
            if Char_wep_current.lower() == 'rf' or Char_wep_current.lower() == 'rapid fire':
                Char_wep_current = 'rapid fire'
            elif Char_wep_current.lower() == 'p' or Char_wep_current.lower() == 'precise':
                Char_wep_current = 'precise'
            else:
                print("That is not an attack you can use, please try again.")
                Attack()
        elif Char_name.lower() == 'viktor':
            print("You use a Bearded Axe and you can do either a 'Light Attack' or a 'Heavy Attack'")
            Char_wep_current = input("How do you want to swing? ")
            Char_att_current = 1
            if Char_wep_current.lower() == 'la' or Char_wep_current.lower() == 'light attack':
                Char_wep_current = 'light attack'
            elif Char_wep_current.lower() == 'ha' or Char_wep_current.lower() == 'heavy attack':
                Char_wep_current = 'heavy attack'
            else:
                print("That is not an attack you can use, please try again.")
                Attack()
    if action.lower() == 'Ether':
        from CharSetup import Char_name
        if Char_name.lower() == 'wake':
            print("Your spells are 'Light Heal', 'Blood Rush', and 'Mutilation'")
            Char_spell_current = input("What spell will you use? ")
            Char_att_current == 2
            if Char_spell_current.lower() == 'lh' or Char_spell_current.lower() == 'light heal':
                Char_spell_current = 'light heal'
            elif Char_spell_current.lower() == 'br' or Char_spell_current.lower() == 'blood rush':
                Char_spell_current = 'blood rush'
            elif Char_spell_current.lower() == 'm' or Char_spell_current.lower() == 'mutilation':
                Char_spell_current = 'mutilation'
            else:
                print("That is not an attack you can use, please try again.")
        elif Char_name.lower() == 'finrear':
            print("Your spells are 'Heavy Heal', 'Bolt Strike', and 'Buckle Armor'")
            Char_spell_current = input("What spell will you use? ")
            Char_att_current == 2
            if Char_spell_current.lower() == 'hh' or Char_spell_current.lower() == 'heavy heal':
                Char_spell_current = 'heavy heal'
            elif Char_spell_current.lower() == 'ba' or Char_spell_current.lower() == 'buckle armor':
                Char_spell_current = 'buckle armor'
            elif Char_spell_current.lower() == 'bs' or Char_spell_current.lower() == 'bolt strike':
                Char_spell_current = 'bolt strike'
            else:
                print("That is not an attack you can use, please try again.")
        elif Char_name.lower() == 'chrono':
            print("Your spells are 'Mid Heal', 'Barrel Induction', and 'Reinforced Pellets'")
            Char_spell_current = input("What spell will you use? ")
            Char_att_current == 2
            if Char_spell_current.lower() == 'mh' or Char_spell_current.lower() == 'mid heal':
                Char_spell_current = 'mid heal'
            elif Char_spell_current.lower() == 'bi' or Char_spell_current.lower() == 'barrel induction':
                Char_spell_current = 'barrel induction'
            elif Char_spell_current.lower() == 'rp' or Char_spell_current.lower() == 'reinforced pellets':
                Char_spell_current = 'reinforced pellets'
            else:
                print("That is not an attack you can use, please try again.")
        elif Char_name.lower() == 'viktor':
            print("Your spells are 'Mid Heal', 'Soul Fracture', and 'Wrath'")
            Char_spell_current = input("What spell will you use? ")
            Char_att_current == 2
            if Char_spell_current.lower() == 'mh' or Char_spell_current.lower() == 'mid heal':
                Char_spell_current = 'mid heal'
            elif Char_spell_current.lower() == 'sf' or Char_spell_current.lower() == 'soul fracture':
                Char_spell_current = 'soul fracture'
            elif Char_spell_current.lower() == 'w' or Char_spell_current.lower() == 'wrath':
                Char_spell_current = 'wrath'
            else:
                print("That is not an attack you can use, please try again.")
