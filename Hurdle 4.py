def turnright():
    turn_left()
    turn_left()
    turn_left()
def repeat():
    turn_left()
    while wall_on_right():
        move()
    turnright()
    move()
    turnright()
    while front_is_clear():
        move()
    turn_left()
while not at_goal():
    if wall_in_front():
        repeat()
    else:
        move()
        
        

    

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
