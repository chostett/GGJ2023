﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Hana")
define t = Character("Mirabel", color = "#ffa200")
define s = Character("Saku", color = "#d77dc4")
define l = Character("Leo", color = "#e7b80c")
define g = Character("Ginger", color = "#2c6a2e")
define f = Character("Fennel", color = "#b628e1")
define r = Character("Haruka", color="#8533ae")
define p = Character("Paradise", color="#1596a2")

image main_menu_animated:
    "gui/main_menu.png"
    pause 1.0
    "gui/main_menu_2.png"
    pause 1.0
    "gui/main_menu_3.png"
    pause 1.0
    repeat

# Initializing Universal Ikebunny images for animation (first animation)
image ikebunnyCenter = im.Scale("ikebunny-center.png", 1920, 1080)
image ikebunnyRight = im.Scale("ikebunny-right.png", 1920, 1080)
image ikebunnyLeft = im.Scale("ikebunny-left.png", 1920, 1080)

# Initializing Tree and Roots images for animation (second and third animation)
image tree01 = im.Scale("tree-1.png", 1920, 1080)
image tree02 = im.Scale("tree-2.png", 1920, 1080)
image tree03 = im.Scale("tree-3.png", 1920, 1080)
image tree04 = im.Scale("tree-4.png", 1920, 1080)
image tree05 = im.Scale("tree-5.png", 1920, 1080)
image tree06 = im.Scale("tree-6.png", 1920, 1080)
image tree07 = im.Scale("tree-7.png", 1920, 1080)
image tree08 = im.Scale("tree-8.png", 1920, 1080)
image tree09 = im.Scale("tree-9.png", 1920, 1080)
image tree10 = im.Scale("tree-10.png", 1920, 1080)
image tree11 = im.Scale("tree-11.png", 1920, 1080)
image tree12 = im.Scale("tree-12.png", 1920, 1080)
image tree13 = im.Scale("tree-13.png", 1920, 1080)
image tree14 = im.Scale("tree-14.png", 1920, 1080)
image tree15 = im.Scale("tree-15.png", 1920, 1080)
image tree16 = im.Scale("tree-16.png", 1920, 1080)
image tree17 = im.Scale("tree-17.png", 1920, 1080)
image tree18 = im.Scale("tree-18.png", 1920, 1080)
image tree19 = im.Scale("tree-19.png", 1920, 1080)
image tree20 = im.Scale("tree-20.png", 1920, 1080)
image tree21 = im.Scale("tree-21.png", 1920, 1080)
image tree22 = im.Scale("tree-22.png", 1920, 1080)
image tree23 = im.Scale("tree-23.png", 1920, 1080)
image tree24 = im.Scale("tree-24.png", 1920, 1080)
image tree25 = im.Scale("tree-25.png", 1920, 1080)
image tree26 = im.Scale("tree-26.png", 1920, 1080)
image tree27 = im.Scale("tree-27.png", 1920, 1080)
image tree28 = im.Scale("tree-28.png", 1920, 1080)
image tree29 = im.Scale("tree-29.png", 1920, 1080)
image tree30 = im.Scale("tree-30.png", 1920, 1080)

# Solid Color Backgrounds Used in the Game
image bgBlack = Solid("#1c1a27")
image bgpink = Solid("#f2ddf1")

# Original sizing for Hana: 435px x 360
image hana angry = im.Scale("hana-angry.png", 652, 540)
image hana happy = im.Scale("hana-happy.png", 652, 540)
image hana sad = im.Scale("hana-sad.png", 652, 540)
image hana shock = im.Scale("hana-shock.png", 652, 540)
image hana smile = im.Scale("hana-smile.png", 652, 540)
image hana talk = im.Scale("hana-talk.png", 652, 540)
# Original sizing for Saku: 575px x 560px
image saku smile = im.Scale("saku-smile.png", 1150, 1120)
image saku happy = im.Scale("saku-happy.png", 1150, 1120)
image saku worried = im.Scale("saku-worried.png", 1150, 1120)
image saku sad = im.Scale("saku-sad.png", 1150, 1120)

# Original sizing for Leo: 455px x 320px
image leo angry = im.Scale("leo-angry.png", 910, 640)
image leo happy = im.Scale("leo-happy.png", 910, 640)
image leo sad = im.Scale("leo-sad.png", 910, 640)
image leo smile = im.Scale("leo-smile.png", 910, 640)
image leo talk = im.Scale("leo-talk.png", 910, 640)
# Original sizing for Haruka: 350px x 325px
image haruka happy = im.Scale("haruka-happy.png", 700, 650)
image haruka smile = im.Scale("haruka-smile.png", 700, 650)
image haruka talk = im.Scale("haruka-talk.png", 700, 650)
image haruka worried = im.Scale("haruka-worried.png", 700, 650)

# The game starts here.

label start:

    define persistent.paradiseEnd = False
    define persistent.gingerFennelEnd = False
    define persistent.harukaEnd = False

    define fennelConvo = False
    define gingerConvo = False

    define date = 0

    $ leftAlign = Position(xpos=0.20, ypos=0.9)
    $ rightAlign = Position(xpos=0.75, ypos=0.9)
    $ rightAlignTop = Position(xpos=0.8, ypos=0.9)

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # Universal Ikebunny, First animation: setup
    image universe:
        "ikebunnyCenter"
        pause 0.5
        "ikebunnyRight"
        pause 0.5
        "ikebunnyCenter"
        pause 0.5
        "ikebunnyLeft"
        pause 0.5
        repeat

    # Roots, Second animation: setup
    image roots:
        "tree01"
        pause 0.5
        "tree02"
        pause 0.5
        "tree03"
        pause 0.5
        "tree04"
        pause 0.5
        "tree05"
        pause 0.5
        "tree06"
        pause 0.5
        "tree07"
        pause 0.5
        "tree08"
        pause 0.5
    
    image tree:
        "tree09"
        pause 0.5
        "tree10"
        pause 0.5
        "tree11"
        pause 0.5
        "tree12"
        pause 0.5
        "tree13"
        pause 0.5
        "tree14"
        pause 0.5
        "tree15"
        pause 0.5
        "tree16"
        pause 0.5
        "tree17"
        pause 0.5
        "tree18"
        pause 0.5
        "tree19"
        pause 0.5
        "tree20"
        pause 0.5
        "tree21"
        pause 0.5
        "tree22"
        pause 0.5
        "tree23"
        pause 0.5
        "tree24"
        pause 0.5
        "tree25"
        pause 0.5
        "tree26"
        pause 0.5
        "tree27"
        pause 0.2
        "tree28"
        pause 0.5
        "tree29"
        pause 0.5

    # Initialize First Animation
    show universe

    # Initialize Dialogue
    "{i}We ikebunnies are very special.{/i}"

    "{i}Why are we special?{/i}"

    # Initialize Second Animation
    show roots
    with fade
    hide universe

    "{i}When we get to be a certain age, we sink our roots into the ground...{/i}"

    "{i}...drink up a loooot of water...{/i}"

    # Initialize Third Animation
    show tree
    hide roots

    "{i}And grow a beautiful garden atop our backs.{/i}"

    "{i}'What kind of garden will I grow?' you might ask yourself.{/i}"

    "{i}Well, that depends...{/i}"

    "{i}Somebunnies' will grow herbs like their mother. Others will bloom flowers like their father. And somebunnies' gardens will have blooms like their aunties or cousins.{/i}"

    "{i}What determines your garden is a mystery.{/i}"

    "{i}But all we know is that we only grow seeds that were planted with love.{/i}"

    show bgBlack 
    with fade
    hide tree

    "Teacher Mirabel looks around the room. Some ikebunnies are picking their noses. Others are falling asleep."

    "But not you. You are staring at her intensely. Your hand is raised."

    t "Yes, Hana?"

    h "But I wanna know what my flower is going to be right now. How do I find out?"

    "Teacher Mirabel smiles. There's always one in every class."

    t "Your assignment this week is to interview your family members about their gardens."

    t "You will prepare a short presentation on your unique family to share with the class on Friday."

    "She winks at Hana."

    t "Maybe you will get some clues."

    "You're so excited to get started you almost forget your school notebook."

    "You can't wait to find out what you will be!"

    "You run home and burst through the door. You almost make it to the dining table when your dad stops you."

    scene bgpink

    show hana smile at leftAlign
    show saku smile at rightAlign

    s "Hey! Shoes off, little lady!"

    h "Sorry!"

    "You take your shoes off."

    h "Hey dad, do you think I'll become a cherry blossom like you?"

    "Your dad is named Saku. He was born and raised in Japan."

    s "You'll be the garden that you were meant to be."

    show hana angry at leftAlign

    h "Daaaad."

    "You groan. He's been saying vague stuff like that since you were a kid."

    show hana smile at leftAlign

    h "I have a school project to interview my family."

    h "I wanna interview you and Auntie Haruka."

    "Haruka has been your dad's best friend since forever. She was also the person who gave birth to you."
    
    "And she's not your mom, but she's your family."

    s "Me? Sure. I'm sure Auntie Haruka can tell you more about family than me..."

    "Come to think of it, dad never talks about his family. You've heard of Grandma and Grandpa before, but never met them."

    show hana talk at leftAlign

    h "Why don't you talk about your family, dad?"

    show saku worried at rightAlign

    "Saku suddenly goes quiet. Then he looks very, very sad."
    
    "You get the sense you said something bad. You start to panic."

    show leo smile at rightAlignTop

    "Your pops comes up behind your dad and squeezes his shoulder. Pops has a big, cheerful sunflower sprouting from his back."

    "His name is Leo. He's from the U.S. He met Saku while studying abroad in Japan and fell in love."

    "They wanted to get married, but because same-sex marriage is illegal in Japan, they only recently were able to get a partnership."
    
    l "What's up?"

    show saku sad at rightAlign

    s "..."

    show leo sad at rightAlignTop

    "Leo's smile drops when he sees the tears in Saku's eyes. His flower wilts a bit."

    l "Hey, what happened?"

    show hana shock at leftAlign

    h "Uh..."

    "Oh no. You messed up. Your dads are going to be mad at you...! What are you supposed to say?!"

    menu family: 
            "I want to interview dad's family.":
                call paradise from _call_paradise
            "Pops, how about I interview your family?":
                call gingerAndFennel from _call_gingerAndFennel
            "Um...can I go to Auntie Haruka's house?":
                call auntHaruka from _call_auntHaruka
            "I...think I have all the information I need." if (persistent.paradiseEnd == True) and (persistent.gingerFennelEnd == True) and (persistent.harukaEnd == True):
                jump hiddenEnding
    
    return
label endGame:
return

# The game ends here

label paradise: 

    show hana sad at leftAlign
    show saku sad at rightAlign
    show leo sad at rightAlignTop

    h "I want to interview dad's family."

    h "I know about grandma and grandpa, but I don't even know what kinds of gardens they have."

    # Saku Worried

    "Though your dad's expression hasn't changed, he is nodding."

    s "It's a fair question, Hana. It was a little silly of me to not bring this up sooner."
    
    s "Hana, do you know what the word 'disown' means?"

    menu: 
            "You bought something and then sold it?":
                call soldSomething
            "Someone who doesn't like you?":
                call dontLike
            "Am I going to be disowned?":
                call question

    label soldSomething:
        h "You bought something and then sold it?"

        "Saku considers."

        s "Not quite."

        s "Things can be bought and sold. People can disowned."

        jump chosenFamily
    
    label dontLike:
        h "Someone who doesn't like you?"

        s "It's more like...someone who doesn't want to be associated with you anymore."

        h "Like they avoid you and never talk to you?"

        s "Yes, like that..."

        h "That sounds terrible."

        s "It is."

        jump chosenFamily

    label question:
        h "Am I going to be disowned?"

        "Your pops jumps in."

        l "No way, Hana. We won't disown you."

        h "Whew. It doesn't sound like a good thing."

        s "You're right..."

        jump chosenFamily
    
    label chosenFamily:

    s "You see, when I met your Pops and we fell in love, my family wasn't supportive."

    s "They told me if I wanted to marry a man, that they did not want to be my family anymore."

    s "That's what 'disowned' means."
    
    s "Because I was not family, they told me I couldn't live with them."

    l "And I was finishing up my degree in the U.S. so I was far away..."

    h "Why would they say something like that? They're your family!"

    s "They're not my family anymore. They disowned me."
    
    s "Family loves us, no matter what shape we are or garden we grow. They said they loved me, but only if I would be something different."

    "Your eyes fill with tears."

    "Just then, you hear a knock on the door. Your dad goes to get it. It's your Uncle Paradise."

    "He takes one look at the situation and, just like always, gets at the heart of the problem. He turns towards your dad."

    p "Let me guess. Talking about your parents?"

    "Saku nods."

    h "Uncle, I hate Grandma and Grandpa! How could they be so mean to dad?"

    p "Hanabean. It's okay to be angry at people. Heck, I was really angry at Saku's family for kicking him out."

    p "But the opposite of hate ain't more hate."

    "He smiles at you, and you feel calmness spread over you like a warm chamomile tea."

    p "We were coworkers. Your dad came into work crying something fierce. He had all his things in a backpack."

    s "It was awful."

    p "And I made him a promise then that whatever happened, I wouldn't let him leave work and sleep on the streets. That we would be there for each other."
    
    p "And here we are."

    "Saku smiles."

    s "And here we are."

    p "And we won in the end. But it wasn't by marching over to their house and calling them bigots."

    l "But it would have felt good."

    p "We won because we supported and loved one another."

    h "Family loves us, no matter what shape we are or garden we grow."

    l "That's right. He's family."

    s "Sometimes the family that sticks around isn't related to us."

    show hana smile at leftAlign

    h "Is there a word for that?"

    # Saku Happy

    "Saku smiles."

    s "Yes. It's called 'chosen family.'"

    hide hana smile
    #Hide Saku and Leo

    "You fall asleep that night thinking of birds of paradise."

    "You wish you could be like Uncle Paradise."

    "His words could calm an ocean."

    "You hope that one day, you can be someone's chosen family, too."

    "You wake up the next morning for school and excitedly check the mirror."

    "Now that you've learned about chosen family, maybe your garden has grown a little."

    "But you find nothing. Not even a sprout."

    "You text Uncle Paradise. Maybe he'll know how to make it grow faster...?"

    "{i}{b}Paradise Ending: The Family You Choose{/b}{/i}"

    $ persistent.paradiseEnd = True
    $ date += 1

    "{i}There are still more endings to explore!{/i}"

    "{i}When you advance to the next day, you'll have the choice to do more interviews.{/i}"

    "{i}Help Hana expand her roots to help her grow.{/i}"

    menu:
        "Go to the next day":
            jump nextDay1

    label nextDay1:

    "The next day you return home from school. Your dads are waiting for you."

    l "Hey! Shoes, young lady!"

    h "Ah! Sorry, pops!"

    "As soon as you kick your shoes off, you grab your trusty notepad."

    h "Ok, now I want to ask about..."
    
    jump family

label gingerAndFennel:

    show hana angry at leftAlign

    h "Pops, how about I interview your family?"

    l "Grandma Fennel and Grandpa Ginger? I can ask them if they're free..."

    h "Hooray!"

    "Grandma Fennel and Grandpa Ginger live far away. They like to travel a lot, so you often talk to them by video call."

    "Just like their namesakes, Grandma Fennel has a field of fennel on her back, with a few big sunflowers waving tall, just like pops. Grandpa Ginger has big magenta flowers sprouting from his ears."

    g "LEO! SAKU! HARU! HOW ARE YOU??"

    f "Grandpa, you don't need to shout for them to hear you..."

    g "Eh??"

    l "Hi dad, Hi mom!"

    f "Hi sweetie! Where's Saku and Haru?"

    s "I'm right here."

    f "Oooh, look at those blooms! Such a handsome boy."

    l "I swear, if she could reach through the Internet and pinch your cheeks, she would."

    f "I would!"

    "Your dad blushes."

    l "Dad, mom, Haru is doing a school project on family."

    g "You don't say!"

    "Who will you ask?"

    menu grandparentsChoose:
            "Ask Grandma Fennel about her garden":
                jump fennel
            "Ask Grandpa Ginger about his garden":
                jump ginger
            "Thanks, Grandma and Grandpa!" if fennelConvo == True and gingerConvo ==True:

                h "Thanks, Grandma and Grandpa!"

                h "Soooo...If I become a fennel, promise you won't eat me?"

                s "Only a little."

                s "As a snack."

                h "Noooo!"

                show hana happy at leftAlign

                "Your family laughs, and you do, too."

                hide hana happy

                "You fall asleep that night feeling grateful."

                "Grateful for Grandma and Grandpa and your dads."

                "Will you grow a big garden to become a world star chef?"

                "Travel the world like Grandma Fennel?"

                "You fall asleep dreaming of travel and cooking."

                "You wake up the next morning for school and check the mirror, even for a little sprout."

                "No sprout."

                "You sigh. You hope you'll bloom soon. You're looking forward to seeing what you become."

                "{i}{b}Daisy and Basil Ending: Little Sprout Grows Up{/b}{/i}"

                $ persistent.gingerFennelEnd = True
                $ date += 1

                "{i}There are still more endings to explore!{/i}"

                "{i}When you advance to the next day, you'll have the choice to do more interviews.{/i}"

                "{i}Help Hana expand her roots to help her grow.{/i}"

                menu:
                    "Go to the next day":
                        jump nextDay2

                label nextDay2:
                "The next day you return home from school."

                "You remember your shoes this time."

                h "Dad! Pops! Can I do more interviews?"

                l "Sure, ask away."

                h "Ok, now I want to ask about..."

                jump family
    
    label fennel:

        show hana talk at leftAlign

        $ fennelConvo = True

        h "Grandma, can you tell me what your family was like? What kinds of blooms did everybunny have?"

        "Grandma Fennel looks overjoyed."

        f "We come from a family of tough flowers and herbs, and we're proud of it!"

        f "When I was a little girl, I used to dream about fields of daisies..."

        f "I was so sure I was going to grow a field of daisies! But I got fennel."

        h "Were you disappointed when you found out?"

        f "A little, at first. But then I found out how useful fennel is."

        "You lean closer to the screen."

        "Grandma Fennel takes some small shears and snips a leaf off her plant."

        f "You can eat them raw, sautée them, and they're really tasty!"

        f "Your grandpa and I, we love traveling the world for new ingredients. There's nothing better than something you can grow yourself."

        h "Wow! So I could have a salad on my back!?"

        f "Maybe!"
        
        jump grandparentsChoose
    
    label ginger:

        show hana talk at leftAlign

        $ gingerConvo = True

        h "Grandpa, what was your family like?"

        "Grandpa Ginger chuckles."

        g "Little sprout, did you know I was adopted?"

        "You shake your head."

        g "It was a closed adoption, which means I never met my birth parents."

        g "My parents were a lavender bush and a beetroot. They always smelled so good."

        g "I wondered about my birth parents a lot in my youth, before I sprouted."

        h "I would too!"

        g "My parents were really supportive. They told me whatever I chose they would support me."

        g "I ended up not meeting them."

        h "Are you happy you made that choice?"

        "Grandpa Ginger smiles."

        g "I am. Maybe another person would have made a different choice than me, but I'm happy with the one I made."

        g "And I promised my parents that when I had a kid, I would support them in making their own decisions."

        g "And my goodness, look at me now! Our little Leo is all grown up and I've supported him all the way."

        l "Dad...you're gonna make me cry."

        "Saku dabs at his eyes."

        s "Too late!"

        h "Your flowers are so pretty, Grandpa!"

        h "What are they?"

        g "They're ginger root!"

        h "Ginger roots have flowers?"

        g "They sure do."

        jump grandparentsChoose


label auntHaruka:

    $ persistent.harukaEnd = True

    show hana shock at leftAlign
    show saku worried at rightAlign
    show leo talk at rightAlignTop

    h "Um...can I go over to Auntie Haruka's house?"

    "Leo looks confused. Saku puts a paw on his shoulder."

    "Before your dads can say anything, you grab your bike and leave in a panic. What did you do!? You're scared to ask."

    hide saku worried
    hide leo talk
    
    "Auntie Haruka's house is a ten minute bike ride. You toss your bike down and run to her door."

    "Auntie Haruka opens the door. She's dressed sharply and the hydrangea on her back is perfectly quaffed."

    show hana sad at leftAlign

    h "Auuuunnntiiiiiieeee!"

    show haruka worried at rightAlign

    "Auntie Haruka gives you a big hug."

    r "Oh, little bean! What's wrong?"

    h "*sniff* I think I said something bad...I asked my dad about my flower and...and who my real dad was..."

    show haruka smile at rightAlign
    
    r "Come in, come in."

    "She invites you in for lavender tea. The words come spilling out of you."

    menu:
        "All my friends already have their flowers.":
            call flowers from _call_flowers
        "Why is my dad so sad?":
            call sadDad from _call_sadDad
    
    show haruka happy at rightAlign
    
    r "Little bean, family doesn't always work that way."

    show hana shock at leftAlign

    h "It doesn't?"

    show haruka talk at rightAlign

    r "Sometimes you inherit stuff from your family, sure. But sometimes you grow your own stuff."

    show hana smile at leftAlign
    show haruka smile at rightAlign

    "Haruka grabs a photo album off the shelf."
    
    "In it are what you assume are Haruka, her brothers and and her parents."
    
    "They are in in full bloom; violets, hydrangea, and lilac."

    show haruka talk at rightAlign

    r "My family tends to grow blue and purple flowers."

    show hana talk at leftAlign

    h "But your hydrangea isn't blue. It's pink."

    show haruka smile at rightAlign

    r "Did you know that based on what you eat, hydrangeas can change colors?"

    show hana shock at leftAlign

    "You shake your head."

    show hana smile at leftAlign
    show haruka happy at rightAlign

    r "My family gave me some things, but other things I grew myself."

    hide haruka happy at rightAlign

    "You come back from Auntie Haruka's house not having clear answers, but feeling better."

    show hana happy at leftAlign

    "You wonder if you'll grow a hydrangea. What color would it be?"

    "Saku is waiting for you when you get home. You can't avoid him so you stand awkwardly at the door."

    show saku worried at rightAlign

    s "How was your trip?"

    show hana smile at leftAlign

    h "Good... Auntie Haruka said some stuff I didn't completely get."

    show saku smile at rightAlign

    s "Like what?"

    show hana talk at leftAlign

    h "{i}Family can give you some things, but other things you have to grow yourself.{/i}"

    "To your surprise, your dad smiles."

    show saku happy at rightAlign

    s "A wise one, that Haruka."

    show saku smile at rightAlign

    "He leans over to kiss you on the forehead."

    show hana sad at leftAlign

    h "I'm sorry dad."

    s "Thanks, sweetie. I love you."

    show hana happy at leftAlign
    show saku happy at rightAlign

    h "Love you too, dad."

    hide hana happy
    hide saku happy

    "You fall asleep that night thinking of hydrangeas."

    "You wake up the next morning for school and check the mirror."

    "Your flower still hasn't bloomed."

    "You sigh. Maybe one day, you'll figure out who you'll become."

    "{i}{b}Haruka Ending: Some Things You Grow Yourself{/b}{/i}"


return

label flowers:
    show hana talk at leftAlign

    h "All my friends already have their flowers."
    
    h "Some say they're the same as their parents or their great-great-grandparents."

    h "They told me if I knew who my family was..."

    h "I'd know what I'd grow up to be."

    show haruka worried at rightAlign

    "Haruka puts a hand on your paw."
    
    return

label sadDad:
    show hana sad at leftAlign

    h "Why is my dad so sad?"

    show haruka worried at rightAlign
    
    "Haruka considers."

    show haruka talk at rightAlign

    r "Well, I think it's because he wants you to be happy with the family you have."

    h "That doesn't make any sense. I mean, I have family, but like..."

    show hana smile at leftAlign

    h "What about my biological family? Aren't they the ikebunnies I'll grow up to be?"

    show haruka happy at rightAlign

    "Haruka chuckles."
    
    return

label hiddenEnding:

    "One week later..."

    "You awake from your bed, feeling groggy."

    "Something feels...different."

    "You take a look at yourself in the mirror."

    show hana shock at leftAlign

    h "What!!!"

    h "DAAAAAAAD!"

    show saku worried at rightAlign

    s "What is it!?"

    show leo talk at rightAlignTop

    l "Coming honey!"

    show hana happy at leftAlign

    h "I...! I bloomed!"

    "Your dads burst into your room to see you standing in front of the mirror, wide-eyed."

    "You..."

    show saku happy at rightAlign
    show leo happy at rightAlignTop

    "Are so beautiful!"

    "You're a flower you've never seen before. Something that is majestic and gigantic. Your dads' eyes go wide."

    show hana shock at leftAlign

    h "What is it?"

    l "It's a..."

    show hana happy at leftAlign

    s "Chrysanthemum!"

    hide hana happy
    hide saku happy
    hide leo happy

    "{i}{b}Hana Ending: In Full Bloom{/b}{/i}"

    "{i}You have now acheived all endings in the game. You can choose to either reset the game entirely or keep your save.{/i}"

    menu:
        "Reset the game entirely. You will have to replay the game to get to this ending.":
            call resetGame from _call_resetGame
        "Keep my save. You will jump straight to this ending upon loading the game.":
            pass

    return

label resetGame: 

    $ persistent._clear()
    $ renpy.full_restart()

    return
