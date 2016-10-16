#A list for payouts to chosen spots

def matchPayout(spots, matches):
    if spots == 1:
        if matches == 1:
            return 2.5
        else:
            return 0.0
    elif spots == 2:
        if matches == 1:
            return 1.0
        elif matches == 2:
            return 5.0
        else:
            return 0.0
    elif spots == 3:
        if matches == 2:
            return 2.5
        elif matches == 3:
            return 25.0
        else:
            return 0.0
    elif spots == 4:
        if matches == 2:
            return 1.0
        elif matches == 3:
            return 4.0
        elif matches == 4:
            return 100.0
        else:
            return 0.0
    elif spots == 5:
        if matches == 3:
            return 2.0
        elif matches == 4:
            return 20.0
        elif matches == 5:
            return 450.0
        else:
            return 0.0
    else:
        print("Invalid chosen spots")
        return
