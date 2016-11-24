from HstlSetup import Hstl_name, Hstl_alive
from CharSetup import Char_alive
import Act
print("A Vileblood approches!")
print("You should probably fight them.")
while Hstl_alive == 1 and Char_alive == 1:
    Act.act() 
if Hstl_alive == 1 and Char_alive == 0:
    print("You have failed Young Hunter.")
    print("The Vilebloods have succesfully summoned the Harbingers.")
elif Hstl_alive == 0 and Char_alive == 1:
    print("You have defeated the Vileblood.")
    print("Its Dark Beast burst into a a brightlight and faded away.")
    print("You have succesfully prevented the summoning of the Harbingers")
    print("Good job Young Hunter.")
else:
    print("How did you get here?")
    print("I mean honestly... how did you get here.")
    print("From what we (the Devs) know of, there really isn't any way to get here.")
    print("So... you messed up in some way shape or form.")
    print("So... good job...")
