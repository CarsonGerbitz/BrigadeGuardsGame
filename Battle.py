def Battle():
    print(Hstl_name +" approches you!")
    print("You should probably fight them.")
    while Hstl_alive == 1 and Char_alive == 1:
        act() 
    if Hstl_alive == 1 and Char_alive == 0:
        print("GAME OVER!!!")
    elif Hstl_alive == 0 and Char_alive == 1:
        print("You have defeated " + Hstl_name)
    else:
        print("How did you get here?")
