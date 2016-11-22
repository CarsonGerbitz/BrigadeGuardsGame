def act():
    from CharSetup import Turn
    import Check, Help  #, Attack, Defend, Wait
    if Turn %2==0:
        action = input("What shall you do? ")
        if (action).lowercase == 'help':
            Help.Help()
            act()
        elif (action).lowercase == 'check':
            Check.Check()
            act()
        elif (action).lowercase == 'attack':
            Attack.Attack()
        #elif (action).lowercase == 'defend':
        #    Defend()
        #elif (action).lowercase == 'wait':
        #    Wait()
        else:
            print("Please try that again")
            act()
    #else:
    #    Enemy_act()
