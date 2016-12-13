def evd(HC,Function):
    import random
    random = random.randint(1,100)
    if Function == 0:
        Func = .33
    if Function == 1:
        Func = .375
    if Function == 2:
        Func = .43
    if Function == 3:
        Func = .5
    if Function == 4:
        Func = .6
    if Function == 5:
        Func = .75
    if Function == 6:
        Func = 1
    if Function == 7:
        Func = 1.33
    if Function == 8:
        Func = 1.667
    if Function == 9:
        Func = 2
    if Function == 10:
        Func = 2.33
    if Function == 11:
        Func = 2.667
    if Function == 12:
        Func = 3
    HC = (HC*Func)
    if random < HC:
        print("hit")
        print(HC)
    else:
        print("miss")
        print(HC)