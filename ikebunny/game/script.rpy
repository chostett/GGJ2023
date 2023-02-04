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
define paradiseEnd = False
define basilDaisyEnd = False
define harukaEnd = False


# The game starts here.

label start:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

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

    if (paradiseEnd == True) and (basilDaisyEnd == True) and (harukaEnd == True):

        jump hiddenEnding

    else:

        "This is a normal ending."
        
return

return

# The game ends here

label paradise: 

    $ paradiseEnd = True

    p "This is the ending with Paradise"

    return

label basilAndDaisy:

    $ basilDaisyEnd = True

    b "I'm Basil!"

    d "I'm Daisy."

    h "This is the Basil and Daisy Ending."

    return

label auntHaruka:
    h "Um...can I go over to Auntie Haruka's house?"

    "Leo looks confused. Saku puts a hand on his shoulder."

    s "It's okay. Let her go."

    "Before your dads can say anything, you grab your bike and leave in a panic. What did you do!? You're scared to ask."

    h "Maybe Auntie Haruka can tell me."

    "Auntie Haruka's house is a ten minute bike ride. You toss your bike down and run to her door."

    h "Auntie...!"

    "Auntie Haruka opens the door. She's dressed sharply and the hydrangea on her back is perfectly quaffed."

    h "Auuuunnntiiiiiieeee!"

    "Auntie Haruka gives you a big hug."

    r "Oh, little bean! What's wrong?!"

    h "*sniff* I think I said something bad...I asked my dad about my flower and...and who my real dad was..."

    r "Aw honey."

    "She invites you in for lavender tea. The words come spilling out of you."

    menu:
        "All my friends already have their flowers.":
            call flowers
        "Why is my dad so sad?":
            call sadDad
    
    r "Oh little bean. Family doesn't always work that way."

    h "It doesn't?"

    r "Sometimes you inherit stuff from your family, sure. But sometimes you grow your own stuff."

    "Haruka grabs a photo album off the shelf."
    
    r "Do you want to see some photos of me and my parents?"

    h "Sure!"

    "The album has photos ikebunnies in full bloom; violets, hydrangea, and lilac."

    r "My family tends to grow blue and purple flowers."

    h "But your hydrangea isn't blue. It's pink."

    r "Did you know that based on what you eat, hydrangeas can change colors?"

    r "My family gave me some things, but other things I grew myself."

    "You come back from Auntie Haruka's house not having a clear answer to your question, but you do feel better about yourself."

    "You wonder if you'll have a hydrangea like Auntie Haruka."

    "Saku is waiting for you when you get home. You can't avoid him so you stand awkwardly in front of him."

    s "How was your trip?"

    h "Good... Auntie Haruka said some stuff I didn't completely get."

    s "Like what?"

    h "{i}Family can give you some things, but other things you have to grow yourself.{/i}"

    "To your surprise, your dad smiles."

    s "A wise one, that Haruka."

    "He leans over to kiss you on the forehead."

    h "I'm sorry dad."

    s "Thanks, sweetie."

    "You fall asleep that night thinking of blooms."

    "You wake up the next morning for school and check the mirror."

    "Your flower still hasn't bloomed."

    "You sigh. You were hoping for a {b}hydrangea.{/b}"

    "Maybe one day, you'll figure out who you'll be."

    "{i}{b}Haruka Ending: Some Things You Grow Yourself{/b}{/i}"

    "{i}There's still more to explore! Try out different options and see how Hana grows.{/i}"

    $ harukaEnd = True

return

label flowers:
    h "All my friends already have their flowers."
    
    h "Some say they're the same as their parents or their great-great-grandparents."

    h "They told me if I knew who my family was..."

    h "I'd know what I'd grow up to be."

    "Haruka puts a hand on your paw."
    
    return

label sadDad:
    h "Why is my dad so sad?"
    
    "Haruka considers."

    r "Well, I think it's because he wants you to be happy with the family you have."

    h "That doesn't make any sense. I mean, I have family, but like..."

    h "What about my biological family? Aren't they the bunnies I'll grow up to be?"

    "Haruka chuckles."
    
    return

label hiddenEnding:

    h "Congratulations! You found the hidden ending."

    return
