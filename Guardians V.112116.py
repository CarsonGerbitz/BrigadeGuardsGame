def HG():
    '''Starts the Guardians TBB Game'''
    Char_Hth = 0
    Char_Agl = 0
    Char_Def = 0
    Hstl_Hth = 0
    Hstl_Def = 0
    Hstl_Agl = 0
    Btle_Trn = 0
    import random
    random = random.randint(1,3)
    def Char1():
        '''Wake'''
        Char_Hth = 50
        Char_Def = 25
        Char_Agl = 75
    def Char2():
        '''Dave'''
        Char_Hth = 50
        Char_Def = 25
        Char_Agl = 75
    def Char3():
        '''J'''
        Char_Hth = 50
        Char_Def = 25
        Char_Agl = 75
    def Hstl1():
        '''Amygdala'''
        Hstl_Hth = 100
        Hstl_Def = 75
        Hstl_Agl = 25
    def Hstl2():
        '''Paarl'''
        Hstl_Hth = 50
        Hstl_Def = 100
        Hstl_Agl = 50
    def Hstl3():
        '''Nightmare'''
        Hstl_Hth = 75
        Hstl_Def = 50
        Hstl_Agl = 75
    if random == 1:
        Hstl1()
    if random == 2:
        Hstl2()
    if random == 3:
        Hstl3()
    print("Who would you like to play as?")
    Char = input('Wake, Dave, J')
    if Char == 'Wake' or Char == 'wake':
        Char1()
    if Char == 'Dave' or Char == 'dave':
        Char2()
    if Char == 'J' or Char == 'j':
        Char3()