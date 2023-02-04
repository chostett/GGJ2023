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

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    {i}"Once upon a time, there lived a special little bunny."{/i}

    {i}"Why were they special?"{/i}

    {i}"Well...this bunny was a seed."{/i}

    {i}"And when they came of age, she would sink their roots into the ground..."{/i}

    {i}"...drink up a loooot of water..."{/i}

    {i}"And grow a beautiful flower."{/i}

    {i}"All the older rabbits had them. And the older they got, the more they asked..."{/i}

    {i}"Dad, what flower am I?"{/i}

    {i}"They asked their dad every day."{/i}

    {i}"And every day their dad told them the same thing..."{/i}

    s "You'll be the flower that you were meant to be, Hana."

    h "Daaaad."

    h "He's been saying that since you were a kid"

    s "What?"

    h "You've been saying that since I was a kid. Isn't it time you gave me a real answer?"

    s "That is the real answer."

    h "Daaaaaaaaaaad!"

    "Another rabbit emerges from the kitchen. He's chewing on some hay."

    l "Hana, is this man bothering you?"

    "Leo comes up behind Saku and gives him a squeeze. Saku looks mock-offended."

    s "I would never!"

    h "All my friends already have their flowers. Some of them say they're the same as their parents or their great-great-grandparents."

    h "You told me I was adopted. I was wondering..."

    h "Do you know who my real family is?"

    "Saku looks hurt."

    l "Honey, that hurts your dad and I. We're your real family."

    h "I-I'm sorry! But I've never met my bio parents or Saku's parents..."

    l "I don't think you want to meet his parents. They're...not very nice to me and your dad."

    h "But what if they like me??"

    "Both parents look like they are at a loss. They turn towards each other and discuss in hushed voices."

    {i}"It couldn't hurt..."{/i}

    {i}"Yes, it could..."{/i}

    {i}"They're an adult now..."{/i}

    {i}"I guess if we..."{/i}

    "They both turn back to Hana."

    l "Tell you what. We'll get in contact with the adoption agency and we can talk with them together."

    s "If you talk to my parents, I'd like to ask Haruka to join us."

    h "Oh sure. Why Haruka?"

    s "...you'll find out soon enough, I'm sure."

    h "Ok, then I'd like to..."

        menu: 
            "Contact the adoption agency"
            "Call Haruka and contact my grandparents"
            "Nevermind, I'll go to my room"

    # This ends the game.

    return
