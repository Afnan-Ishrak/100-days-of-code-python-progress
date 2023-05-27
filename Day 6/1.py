'''USE THIS IN http://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json'''

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    if not front_is_clear():
        turn_left()
    elif not right_is_clear():
        move()
    else:
        turn_right()

while not at_goal():
    if not wall_in_front() and not right_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        move()
    elif not front_is_clear():
        jump()