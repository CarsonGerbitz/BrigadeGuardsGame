def Act():
    if turn %2==0: 
        action = input("What shall you do? ")
        if (action).lowercase == 'help':
            Help()
        elif (action).lowercase == 'check':
            Check()
        elif (action).lowercase == 'attack':
            Attack()
        elif (action).lowercase == 'defend':
            Defend()
        elif (action).lowercase == 'wait':
            Wait()
        else:
            print("Please try that again")
            Act()
    else:
        Enemy_Act()
