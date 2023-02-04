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
image ikebunny01 = im.Scale("01_ikebunny-a.png", 1920, 1080)
image ikebunny02 = im.Scale("01_ikebunny-b.png", 1920, 1080)
image roots01 = im.Scale("02_roots-a.png", 1920, 1080)
image roots02 = im.Scale("02_roots-b.png", 1920, 1080)
image roots03 = im.Scale("02_roots-c.png", 1920, 1080)


# The game starts here.

label start:

    define persistent.paradiseEnd = False
    define persistent.basilDaisyEnd = False
    define persistent.harukaEnd = False

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image ikebunny01atl:
        "ikebunny01"
        pause 0.5
        "ikebunny02"
        pause 0.5
        repeat
    
    image ikebunny02atl:
        "roots01"
        pause 0.5
        "roots02"
        pause 0.5
        "roots03"
        pause 0.5
        repeat

    show ikebunny01atl


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    "{i}An ikebunny is a very special creature.{/i}"

    "{i}Why are they special?{/i}"

    show ikebunny02atl

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

    "His name is Leo. He's from the U.S. He met Saku while studying abroad in Japan and they fell in love."

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

    if (persistent.paradiseEnd == True) and (persistent.basilDaisyEnd == True) and (persistent.harukaEnd == True):

        jump hiddenEnding

    else:
        "{i}There are still more endings to explore! Help Hana expand her roots to help her grow.{/i}"
    
    return
return

# The game ends here

label paradise: 

    $ persistent.paradiseEnd = True

    h "I'm sorry. I think I said something bad..."

    "Saku nudges Leo."

    s "Leo, I think this could be a good moment to talk about what family means to us."

    "Leo nods. Saku turns to you."

    s "Hana, your know Uncle Paradise."

    h "Of course. He's dad's brother. He took care of me from when I was a kid."

    h "Ooh, maybe I'll have a Bird of Paradise flower like him!"

    l "Hana, Uncle Paradise isn't related to me."

    h "?! But you look like brothers!"

    "Leo laughs."

    l "I know. Everyone says so. But Uncle Paradise is actually one of Saku's old work colleagues."

    l "When Saku came out and you were born, he was there for all the rough times."

    s "He took me in after my parents kicked me out."

    s "And when we were overwhelmed with your dirty diapers."

    l "And so we asked him to be your uncle."

    s "He's a good uncle."

    h "He's a great uncle. But why tell me that?"

    l "I guess I wanted you to know that society can be really focused on 'blood' relatives."

    s "But sometimes the family that sticks around the longest isn't necessarily related to us."

    h "Is there a word for that?"

    "Saku smiles."

    s "Yeah. It's called 'chosen family.'"

    "You fall asleep that night thinking of birds of paradise."

    "You wish you could be like Uncle Paradise."

    "You hope one day you'll find an ikebunny family."

    "You want to be someone's aunt someday."

    "You wake up the next morning for school and check the mirror."

    "Your flower still hasn't bloomed."

    "You dial the number for Uncle Paradise. Maybe he'll know how to make it grow faster...?"

    "{i}{b}Paradise Ending: The Family You Choose{/b}{/i}"

    return

label basilAndDaisy:

    $ persistent.basilDaisyEnd = True

    h "I asked who my real dad is. Why is that a problem?"

    l "We're your parents. We raised you."

    h "No, I mean...whoever is my real dad I'll inherit their flower, right?"

    l "The word you're looking for is birth parent."

    h "Why does it matter?"

    l "Let me get Grandma Daisy and Grandpa Basil on the phone."

    "Just like their namesakes, Grandma Daisy has a field of daisies on her back, and Grandpa Basil has basil leaves sprouting from his ears."

    b "LEO! SAKU! HARU! HOW ARE YOU??"

    d "Grandpa, you don't need to shout for them to hear you..."

    b "Eh??"

    l "Hi dad. Hi mom. Can you explain to Hana the difference between a 'real' parent and a birth parent?"

    "Grandma Daisy looks a bit serious."

    d "Hana, where did you first hear that word?"

    menu:
        "My classmates at school...":
            call classmates
        "My teachers...":
            call teachers
        
    "Grandpa Basil chuckles."

    b "Little sprout, did you know I was adopted?"

    "You didn't know that. You shake your head."

    d "It's true. And maybe back in Grandpa's day, they'd use words like that..."

    d "But times are changing. Your Grandpa's parents are his parents. He has birth parents, but..."

    b "If you say things like 'real,' that means you think there are 'fake' parents!"

    "Now you realize why your dads were so hurt by you saying real parents."

    h "That's not what I was trying to say...!"

    b "But intent isn't magic, little sprout. You're old enough to know that."

    l "I'm your birth parent, Hana. But Saku isn't any less of a parent to you than I am."

    s "That's right."

    l "We both wanted to understand this before we told you."

    "You feel really, really bad."

    h "...I'm sorry."

    "Saku gives you a big squeeze."

    s "Maybe you'll be a handsome sunflower like Leo. Or a daisy like Grandma or a basil like Grandpa."

    h "If I become a basil, promise you won't eat me?"

    s "Only a little."

    s "As a snack."

    "Your family laughs, and you do, too."

    "You fall asleep that night feeling grateful."

    "You wake up the next morning for school and check the mirror, even for a little sprout."

    "No sprout."

    "You sigh. You hope you'll bloom soon. You're looking forward to seeing what you become."

    "{i}{b}Daisy and Basil Ending: Little Sprout Grows Up{/b}{/i}"

return

label classmates:

    h "My classmates at school. We were talking about what kind of ikebunnies we'd be."

    h "I told them I'd probably either be a sakura blossom or a sunflower and they laughed at me."

    h "They told me that's not possible because both of of my parents are male. One of them had to be the 'real' one."

    return

label teachers:

    h "My teachers. We were studying genetics and my teachers told me that by looking at an ikebunny's genetics..."

    h "You could find out who the 'real' parent was."

    h "Then I thought...what does that mean for me?"

    return

label auntHaruka:

    $ persistent.harukaEnd = True

    h "Um...can I go over to Auntie Haruka's house?"

    "Leo looks confused. Saku puts a paw on his shoulder."

    "Before your dads can say anything, you grab your bike and leave in a panic. What did you do!? You're scared to ask."

    "Auntie Haruka's house is a ten minute bike ride. You toss your bike down and run to her door."

    "Auntie Haruka opens the door. She's dressed sharply and the hydrangea on her back is perfectly quaffed."

    h "Auuuunnntiiiiiieeee!"

    "Auntie Haruka gives you a big hug."

    r "Oh, little bean! What's wrong?"

    h "*sniff* I think I said something bad...I asked my dad about my flower and...and who my real dad was..."

    r "Come in, come in."

    "She invites you in for lavender tea. The words come spilling out of you."

    menu:
        "All my friends already have their flowers.":
            call flowers
        "Why is my dad so sad?":
            call sadDad
    
    r "Little bean, family doesn't always work that way."

    h "It doesn't?"

    r "Sometimes you inherit stuff from your family, sure. But sometimes you grow your own stuff."

    "Haruka grabs a photo album off the shelf."
    
    "In it are what you assume are Haruka, her brothers and and her parents."
    
    "They are in in full bloom; violets, hydrangea, and lilac."

    r "My family tends to grow blue and purple flowers."

    h "But your hydrangea isn't blue. It's pink."

    r "Did you know that based on what you eat, hydrangeas can change colors?"

    "You shake your head."

    r "My family gave me some things, but other things I grew myself."

    "You come back from Auntie Haruka's house not having clear answers, but feeling better."

    "You wonder if you'll grow a hydrangea. What color would it be?"

    "Saku is waiting for you when you get home. You can't avoid him so you stand awkwardly at the door."

    s "How was your trip?"

    h "Good... Auntie Haruka said some stuff I didn't completely get."

    s "Like what?"

    h "{i}Family can give you some things, but other things you have to grow yourself.{/i}"

    "To your surprise, your dad smiles."

    s "A wise one, that Haruka."

    "He leans over to kiss you on the forehead."

    h "I'm sorry dad."

    s "Thanks, sweetie. I love you."

    h "Love you too, dad."

    "You fall asleep that night thinking of hydrangeas."

    "You wake up the next morning for school and check the mirror."

    "Your flower still hasn't bloomed."

    "You sigh. Maybe one day, you'll figure out who you'll become."

    "{i}{b}Haruka Ending: Some Things You Grow Yourself{/b}{/i}"


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

    h "What about my biological family? Aren't they the ikebunnies I'll grow up to be?"

    "Haruka chuckles."
    
    return

label hiddenEnding:

    "One week later..."

    "You awake from your bed, feeling groggy."

    "Something feels...different."

    "You take a look at yourself in the mirror."

    h "What!!!"

    h "DAAAAAAAD!"

    s "What is it!?"

    l "Coming honey!"

    h "I...! I bloomed!"

    "Your dads burst into your room to see you standing in front of the mirror, wide-eyed."

    "You..."

    "Are so beautiful!"

    "You're a flower you've never seen before. Something that is majestic and gigantic. Your dads' eyes go wide."

    h "What is it?"

    l "It's a..."

    s "Chrysanthemum!"

    "{i}{b}Hana Ending: In Full Bloom{/b}{/i}"

    "{i}You have now acheived all endings in the game. You can choose to either reset the game entirely or keep your save.{/i}"

    menu:
        "Reset the game entirely. You will have to replay the game to get to this ending.":
            call resetGame
        "Keep my save. You will jump straight to this ending upon loading the game.":
            pass

    return

label resetGame: 

    $ persistent._clear()
    $ renpy.full_restart()

    return
