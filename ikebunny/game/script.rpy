# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Hana")
# はな
define s = Character("Saku", color = "#d77dc4")
# 桜
define l = Character("Leo", color = "#e7b80c")
define b = Character("Basil", color = "#2c6a2e")
define d = Character("Daisy", color = "#b628e1")
define r = Character("Haruka", color="#8533ae")
# 紫陽花
define p = Character("Paradise", color="#1596a2")

# The game starts here.

label start:

    $ endings = 0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    
label start2:

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    "{i}An ikebunny is a very special creature.{/i}"

    "{i}Why are they special?{/i}"

    "{i}When an ikebunny comes of age, they sink their roots into the ground...{/i}"

    "{i}...drink up a loooot of water...{/i}"

    "{i}And grow a beautiful flower.{/i}"

    "{i}Somebunnies' flowers are the same as their mother. Or father. And somebunnies' flowers are the same as other relatives, like their aunties or cousins.{/i}"

    "{i}You are an ikebunny named Hana. You want to know what your beautiful flower will be.{/i}"

    "{i}So you ask your dads.{/i}"

    h "Hey dad, do you think I'll be a sakura flower like you?"

    "One of your dads is named Saku. He was born and raised in Japan."

    s "You'll be the flower that you were meant to be, Hana."

    h "Daaaad."

    "You groan. He's been saying vague stuff like that since you were a kid."

    h "I mean, I know I came from Auntie Haruka."

    "Haruka has been your dad's best friend since forever. She was also the person who gave birth to you. She comes over every week for dinner."

    h "But like...who is my real dad?"

    "Saku suddenly goes quiet. Then he looks very, very sad. You get the sense you said something bad. You start to panic."

    "Another rabbit comes up behind your dad and gives him a hug. He has a big, cheerful sunflower sprouting from his back."

    l "Saku, is this lady bothering you?"

    s "..."

    "Leo's smile drops when he sees the tears in Saku's eyes. His flower wilts a bit."

    l "Saku, what happened?"

    h "Uh..."

    "Oh no. You messed up. Your dads are going to be mad at you...! What are you supposed to say?!"

    menu: 
            "I'm sorry. I think I said something bad...":
                call paradise
            "I asked who my real dad is. Why is that a problem?":
                call basilAndDaisy
            "Um...can I go over to Auntie Haruka's house?":
                call auntHaruka

    if endings >= 3:

        jump hiddenEnding

    else:

        h "It's a normal ending of the game."

        jump start2
        
return

return

# The game ends here

label paradise: 

    p "This is the ending with Paradise"

    $ endings += 1

    return

label basilAndDaisy:
    b "I'm Basil!"

    d "I'm Daisy."

    h "This is the Basil and Daisy Ending."

    $ endings += 1

    return

label auntHaruka:
    h "Um...can I go over to Auntie Haruka's house?"

    l "What's this all of the sudden?"

    "Leo looks confused. Saku puts a hand on his shoulder."

    s "It's okay. Let her go."

    "Before Leo can say anything, you grab your bike and leave in a panic. What did you do!? You're scared to ask either of them."

    "Maybe Auntie Haruka has answers."

    "Auntie Haruka's house is a ten minute bike ride. You practically toss the bike down to get to her door."

    h "Auntie...!"

    "She opens the door. She's dressed sharply and the hydrangea on her back is perfectly quaffed. She always looks so put together."

    h "Auuuunnntiiiiiieeee!"

    "Auntie Haruka gives you a big hug."

    r "Oh, Haru! What's wrong?!"

    h "*sniff* I think I said something bad...I asked my dad about my flower and who my real dad was..."

    r "Aw honey. Don't stand outside. Come in, come in."

    "She invites you in for lavender tea. The words come spilling out of you."

    h "All my friends already have their flowers. Some of them say they're the same as their parents or their great-great-grandparents."

    h "And like, I know you and one of my dads made me. But they never told me which one."

    h "And then I asked...and dad..."

    $ endings += 1

    return

label hiddenEnding:

    h "Congratulations! You found the hidden ending."

    return
