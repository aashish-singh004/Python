#visit reeborg's World and select python and then maze problem.
def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
#it was kinda confusing at first and took me so much time but its still worth it and gonna help me build strong foundation haha.
