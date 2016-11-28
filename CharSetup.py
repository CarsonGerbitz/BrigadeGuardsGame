def CharSelect():
    print("Hello Young Hunter.")
    print("You have 4 Guaridans to choose from.")
    Char = input("Wake, Finrear, Viktor, or Chrono? ")
    global Char_alive, Turn, Char_name, Char_hp_current, Char_etr_max, Char_hp_max, Char_etr_current, Char_def, Char_agl, Char_buff_left, Char_buff_max
    if Char.lower() == 'wake' or Char.lower() == 'w':
        Char_name = 'Wake'
        Char_hp_current = 50
        Char_etr_max = 50
        Char_etr_current = 50
        Char_hp_max = 50
        Char_def = 25
        Char_agl = 75
        Char_alive = 1
        Turn = 0
        Char_buff_left = 0
        Char_buff_max = 6
    elif Char.lower() == 'finrear' or Char.lower() == 'f':
        Char_name = 'Finrear'
        Char_hp_current = 50
        Char_hp_max = 50
        Char_etr_max = 50
        Char_etr_current = 50
        Char_def = 75
        Char_agl = 25
        Char_alive = 1
        Turn = 0
        Char_buff_left = 0
        Char_buff_max = 6
    elif Char.lower() == 'chrono' or Char.lower() == 'c':
        Char_name = 'Chrono'
        Char_hp_current = 50
        Char_hp_max = 50
        Char_etr_max = 50
        Char_etr_current = 50
        Char_def = 50
        Char_agl = 50
        Char_alive = 1
        Turn = 0
        Char_buff_left = 0
        Char_buff_max = 6
    elif Char.lower() == 'viktor' or Char.lower() == 'v':
        Char_name = 'Viktor'
        Char_hp_current = 75
        Char_hp_max = 75
        Char_etr_max = 50
        Char_etr_current = 50
        Char_def = 25
        Char_agl = 50
        Char_alive = 1
        Turn = 0
        Char_buff_left = 0
        Char_buff_max = 6
    else:
        print("That is not a valid choice.")
        print("Please try again.")
        CharSelect()
