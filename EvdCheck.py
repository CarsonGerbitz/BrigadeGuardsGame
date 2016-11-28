def Evade():
    from HstlSetup import Hstl_agl
    from CharSetup import Char_agl
    from Act import Turn
    from Damage import Char_Hit_chance, Hstl_Hit_chance
    import random
    random_evade = random.randint(1,100)
    random_hit = random.randint(1,100)
    random_TB = random.randint(1,100)
    Hit_check = 0
    '''1 is hit, 0 is miss'''
    Evd_check = 0
    '''1 is miss, 0 is hit'''
    if Turn %2==0:
        if random_evade > Hstl_agl:
            Evd_check == 1
        if random_evade < Hstl_agl:
            Evd_check == 0
    if not Turn %2==0:
        if random_evade > Char_agl:
            Evd_check == 1
        if random_evade < Char_agl:
            Evd_check == 0
    if Turn %2==0:
        if random_hit > Hstl_Hit_chance:
            Hit_check == 0
        if random_hit < Hstl_Hit_chance:
            Hit_check == 1
    if not Turn %2==0:
        if random_hit > Char_Hit_chance:
            Hit_check == 0
        if random_hit < Char_Hit_chance:
            Hit_check == 1
    if Hit_check > Evd_check:
        '''The attack hit'''
    if Hit_check < Evd_check:
        '''The attack missed'''
    if Hit_check == Evd_check:
        if random_TB > 50:
            '''The attack hit'''
        else:
            '''The attack missed'''
        