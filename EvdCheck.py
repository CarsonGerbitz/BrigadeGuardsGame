def Evade():
    from HstlSetup import Hstl_agl
    from CharSetup import Char_agl
    from Damage import Char_Hit_Chance, Hstl_Hit_Chance
    from Act import Turn
    '''1 is miss, 0 is hit'''
    if Turn %2==0:
        HDC_Final_Check = 0
        Hstl_Dge_Function = 6
        if Hstl_Dge_Function == 0:
            Hstl_Dge_Func = .33
        if Hstl_Dge_Function == 1:
            Hstl_Dge_Func = .375
        if Hstl_Dge_Function == 2:
            Hstl_Dge_Func = .43
        if Hstl_Dge_Function == 3:
            Hstl_Dge_Func = .5
        if Hstl_Dge_Function == 4:
            Hstl_Dge_Func = .6
        if Hstl_Dge_Function == 5:
            Hstl_Dge_Func = .75
        if Hstl_Dge_Function == 6:
            Hstl_Dge_Func = 1
        if Hstl_Dge_Function == 7:
            Hstl_Dge_Func = 1.33
        if Hstl_Dge_Function == 8:
            Hstl_Dge_Func = 1.667
        if Hstl_Dge_Function == 9:
            Hstl_Dge_Func = 2
        if Hstl_Dge_Function == 10:
            Hstl_Dge_Func = 2.33
        if Hstl_Dge_Function == 11:
            Hstl_Dge_Func = 2.667
        if Hstl_Dge_Function == 12:
            Hstl_Dge_Func = 3
        HDC = (Hstl_agl*Hstl_Dge_Func)
        if Char_Hit_Chance < HDC:
            HDC_Final_Check == 0
        else:
            HDC_Final_Check == 1
    else:
        CDC_Final_Check = 0
        Char_Dge_Function = 6
        if Char_Dge_Function == 0:
            Char_Dge_Func = .33
        if Char_Dge_Function == 1:
            Char_Dge_Func = .375
        if Char_Dge_Function == 2:
            Char_Dge_Func = .43
        if Char_Dge_Function == 3:
            Char_Dge_Func = .5
        if Char_Dge_Function == 4:
            Char_Dge_Func = .6
        if Char_Dge_Function == 5:
            Char_Dge_Func = .75
        if Char_Dge_Function == 6:
            Char_Dge_Func = 1
        if Char_Dge_Function == 7:
            Char_Dge_Func = 1.33
        if Char_Dge_Function == 8:
            Char_Dge_Func = 1.667
        if Char_Dge_Function == 9:
            Char_Dge_Func = 2
        if Char_Dge_Function == 10:
            Char_Dge_Func = 2.33
        if Char_Dge_Function == 11:
            Char_Dge_Func = 2.667
        if Char_Dge_Function == 12:
            Char_Dge_Func = 3
        CDC = (Char_agl*Char_Dge_Func)
        if Hstl_Hit_Chance < CDC:
            CDC_Final_Check == 0
        else:
            CDC_Final_Check == 1