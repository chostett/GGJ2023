# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Crystal")
define s = Character("Sapphire", color = "#1b53e7")
image shop = im.Scale("GaoGaoBanana.png", 1920, 1080)
image crystal = "crystal-happy.png"
image sapphire = "sapphire-happy.png"
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    show shop

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show crystal

    # These display lines of dialogue.

    c "This was the choco banana place I was telling you about."

    show sapphire

    s "It's amazing!"

    c "Right!?"

    c "If you grab us a seat I'll get you something."

    c "What do you want?"

    menu:
        "Classic chocolate banana":
            call chocoBanana
        "Strawberry and rainbow sprinkle banana":
            call strawBanana
        "Wasabi banana":
            call wasabiBanana

    # This ends the game.

    return

label chocoBanana:
    c "Gotta love a good classic."

    c "One chocolate banana coming right up!"

    return
label strawBanana:
    "Crystal looks surprised."

    s "What?"

    c "I was gonna order the same one!"

    s "Great minds think alike."

    c "Haha, they do!"

    return
label wasabiBanana:
    c "Isn't that the menu item for dudes to impress their dates?"

    s "I'm not a dude."

    c "Are you trying to impress me?"

    s "{i}Maybe.{/i}"

    "Crystal blushes."

    return
