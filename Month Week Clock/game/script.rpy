# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:
    call variables
    $ gameRunning = True
    while gameRunning:
        "Hello!"

# Runs property addTime, which is in events.rpy
        $ calendar.AddTime(1)
        $ Output = calendar.Output

# This calls our event.  

    # call eventCheck
    return
    
# This defines all the pieces of our clock. (in Python)
label variables:
    $ calendar = Calendar(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31], 0, 0, 0, 0, 0)
    return

# This shows what our event should be checking for in order to run (see Ren'Py notes for a one-line solution)
label eventCheck:

    return