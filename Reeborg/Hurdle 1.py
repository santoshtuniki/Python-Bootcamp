def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_round():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for i in range(1,7):
    turn_round()


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
