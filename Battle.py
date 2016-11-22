def Battle():
    from HstlSetup import Hstl_name, Hstl_alive
    from CharSetup import Char_alive
    import Act
    print("Something dark approches!")
    print("You should probably fight them.")
    while Hstl_alive == 1 and Char_alive == 1:
        Act.act() 
    if Hstl_alive == 1 and Char_alive == 0:
        print("GAME OVER!!!")
    elif Hstl_alive == 0 and Char_alive == 1:
        print("You have defeated " + Hstl_name)
    else:
        print("How did you get here?")
