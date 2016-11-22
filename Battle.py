def Battle():
    from HstlSetup import Hstl_name, Hstl_hp_current, Hstl_hp_max, Hstl_def, Hstl_agl, Hstl_alive
    from CharSetup import Char_name, Char_hp_current, Char_hp_max, Char_def, Char_agl, Char_alive
    import Act
    print(Hstl_name +" approches you!")
    print("You should probably fight them.")
    while Hstl_alive == 1 and Char_alive == 1:
        Act.act() 
    if Hstl_alive == 1 and Char_alive == 0:
        print("GAME OVER!!!")
    elif Hstl_alive == 0 and Char_alive == 1:
        print("You have defeated " + Hstl_name)
    else:
        print("How did you get here?")
