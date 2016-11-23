print("Hello good Hunter.")
print("You have 3 Guaridans to choose from.")
Char = input("Wake, Dave, or Chrono? ")
if Char.lower() == 'wake' or Char.lower() == 'w':
    Char_name = 'Wake'
    Char_hp_current = 50
    Char_etr_max = 50
    Char_etr_current = 50
    Char_hp_max = 50
    Char_def = 25
    Char_agl = 75
    Char_alive = 1
    Char_buff_left = 0
    Char_buff_max = 6
    Turn = 0
if Char.lower() == 'finrear' or Char.lower() == 'f':
    Char_name = 'Finrear'
    Char_hp_current = 50
    Char_hp_max = 50
    Char_etr_max = 50
    Char_etr_current = 50
    Char_def = 75
    Char_agl = 25
    Char_alive = 1
    Char_buff_left = 0
    Char_buff_max = 6
    Turn = 0
if Char.lower() == 'chrono' or Char.lower() == 'c':
    Char_name = 'Chrono'
    Char_hp_current = 50
    Char_hp_max = 50
    Char_etr_max = 50
    Char_etr_current = 50
    Char_def = 50
    Char_agl = 50
    Char_alive = 1
    Char_buff_left = 0
    Char_buff_max = 6
    Turn = 0
