def Char_setup():
    print("Who do you want to play as?")
    Char = input("Wake, Dave, or J? ")
    if (Char).lowercase == 'wake':
        Char_name = 'Wake'
        Char_hp_current = 50
        Char_hp_max = 50
        Char_def = 25
        Char_agl = 75
        Char_alive = 1
    if (Char).lowercase == 'dave':
        Char_name = 'Dave'
        Char_hp_current = 50
        Char_hp_max = 50
        Char_def = 75
        Char_agl = 25
        Char_alive = 1
    if (Char).lowercase == 'j':
        Char_name = 'J'
        Char_hp_current = 50
        Char_hp_max = 50
        Char_def = 50
        Char_agl = 50
        Char_alive = 1
