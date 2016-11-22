from CharSetup import Turn, Char_alive
from HstlSetup import Hstl_alive
def act():
    global Turn, Char_alive, Hstl_alive
    import Check, Help, Attack  #, Defend, Wait
    while Char_alive == 1 and Hstl_alive == 1:
        if Turn %2==0:
            action = input("What shall you do? ")
            if action.lower() == 'help':
                Help.Help()
                act()
            elif action.lower() == 'check':
                Check.Check()
                Turn = Turn + 1
                act()
            elif action.lower() == 'attack':
                Attack.Attack()
                Turn = Turn + 1
                from Damage import Char
                Damage.Char()
                act()
            elif action.lower() == 'defend':
                Defend.Defend()
                Turn = Turn + 1
                act()
            elif action.lower() == 'wait':
                Wait.Wait()
                Turn = Turn + 1
                act()
            else:
                print("Please try that again")
                act()
        if Char_alive == 0 or Hstl_alive == 0:
            break
        else:
            Enemy_act()
            turn = turn + 1
