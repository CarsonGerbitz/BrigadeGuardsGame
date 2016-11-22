def act():
    from CharSetup import Turn
    import Check, Help, Attack  #, Defend, Wait
    if Turn %2==0:
        action = input("What shall you do? ")
        if action.lowercase() == 'help':
            Help.Help()
            turn = turn + 1
            act()
        elif action.lowercase() == 'check':
            Check.Check()
            turn = turn + 1
            act()
        elif action.lowercase() == 'attack':
            Attack.Attack()
            turn = turn + 1
            act()
        elif (action).lowercase == 'defend':
            Defend.Defend()
            turn = turn + 1
            act()
        elif (action).lowercase == 'wait':
            Wait.Wait()
            turn = turn + 1
            act()
        else:
            print("Please try that again")
            act()
    else:
        Enemy_act()
        turn = turn + 1
