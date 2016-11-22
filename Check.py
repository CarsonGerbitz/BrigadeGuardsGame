def Check():
    print("Who shall we check?")
    action = input(Char_name + " or " + Hstl_name + "?")
    if (action).lowercase == Char_name or (action).lowercase == 'me':
        print(Char_hp_current + "/" + Char_hp_max)
    if (action).lowercase == Hstl_name or (action).lowercase == 'them':
        print(Hstl_hp_current + "/" + Hstl_hp_max)
    else:
        print("You can CHECK " + Char_name + " or " + Hstl_name)
        check()
