def Evade():
    from HstlSetup import Hstl_agl
    from CharSetup import Char_agl
    from Act import Turn
    from Damage import Char_Hit_chance, Hstl_Hit_chance
    import random
    Evd_Final_Check = 0
    '''1 is miss, 0 is hit'''
    if Turn %2==0:
        CHC_Final_Check = 0
        CHC_random = random.randint(1,100)
        Char_Hit_Function = 6
        if Char_Hit_Function == 0:
            Char_Hit_Func = .33
        if Char_Hit_Function == 1:
            Char_Hit_Func = .375
        if Char_Hit_Function == 2:
            Char_Hit_Func = .43
        if Char_Hit_Function == 3:
            Char_Hit_Func = .5
        if Char_Hit_Function == 4:
            Char_Hit_Func = .6
        if Char_Hit_Function == 5:
            Char_Hit_Func = .75
        if Char_Hit_Function == 6:
            Char_Hit_Func = 1
        if Char_Hit_Function == 7:
            Char_Hit_Func = 1.33
        if Char_Hit_Function == 8:
            Char_Hit_Func = 1.667
        if Char_Hit_Function == 9:
            Char_Hit_Func = 2
        if Char_Hit_Function == 10:
            Char_Hit_Func = 2.33
        if Char_Hit_Function == 11:
            Char_Hit_Func = 2.667
        if Char_Hit_Function == 12:
            Char_Hit_Func = 3
        HC = (Char_Hit_chance*Char_Hit_Func)
        if CHC_random < HC:
            CHC_Final_Check = 0
        else:
            CHC_Final_Check = 1
        HDC_Final_Check = 0
        HDC_random = random.randint(1,100)
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
        HC = (Hstl_agl*Hstl_Dge_Func)
        if HDC_random < HC:
            HDC_Final_Check = 0
        else:
            HDC_Final_Check = 1
        if CHC_Final_Check > HDC_Final_Check:
            Evd_Final_Check = 0
        if CHC_Final_Check < HDC_Final_Check:
            Evd_Final_Check = 1
        else:
            Evd_Final_Check = 0