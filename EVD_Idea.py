def Evade():
    from Damage import Char_Hit_chance, Hstl_Hit_chance
    import random
    random = random.randint(1,100)
    Char_Function = 6
    if Char_Function == 0:
        Func = .33
    if Char_Function == 1:
        Func = .375
    if Char_Function == 2:
        Func = .43
    if Char_Function == 3:
        Func = .5
    if Char_Function == 4:
        Func = .6
    if Char_Function == 5:
        Func = .75
    if Char_Function == 6:
        Func = 1
    if Char_Function == 7:
        Func = 1.33
    if Char_Function == 8:
        Func = 1.667
    if Char_Function == 9:
        Func = 2
    if Char_Function == 10:
        Func = 2.33
    if Char_Function == 11:
        Func = 2.667
    if Char_Function == 12:
        Func = 3
    HC = (HC*Func)
    if random < HC:
        print("hit")
        print(HC)
    else:
        print("miss")
        print(HC)