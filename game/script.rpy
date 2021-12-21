# The script of the game goes in this file.



## Splashscreen ############################################################
## A portion of the game that plays at launch, before the main menu is shown.
## https://www.renpy.org/doc/html/splashscreen_presplash.html

## The animation is boring so I recommend using something else.
## ATL documentation: https://www.renpy.org/doc/html/atl.html

image splash_anim_1:

    "gui/renpy-logo.png"
    xalign 0.5 yalign 0.5 alpha 0.0
    ease_quad 7.0 alpha 1.0 zoom 2.0

label splashscreen:
    $ preferences.set_volume("music", 0.30)
    $ preferences.set_volume("sfx", 0.40)
    scene black

    $_dismiss_pause = False
    scene black
    with fade

    scene black
    with Pause(1)

    show logo_company with dissolve
    with Pause(2)

    scene black with dissolve
    with Pause(1)
 
    pass

    scene black

    play sound "audio/flash.mp3"

    show menu1 at truecenter with zoomin

    show white at truecenter
    with dissolve

    hide white at truecenter
    with dissolve

    play sound "audio/openings.mp3"

    # RESET ALL

    
    # $ achievement.clear_all()
    # $ persistent.unlockJeep = False
    # $ persistent.unlockroom = False
    # $ persistent.unlockroom = False
    # $ persistent.unlockTrain = False
    # $ persistent.unlockJeep = False
    # $ persistent.unlockHallway = False
    # $ persistent.unlockTrain2 = False
    # $ persistent.unlockWalk = False
    # $ persistent.unlockCafeteria = False
    # $ persistent.unlockClass = False
    # $ persistent.unlockYui = False
    # $ persistent.unlockKurtney = False
    # $ readtotal = 0
    # $ persistent.achievementList = [False, False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False, False]
    # $ persistent.completed = False
    return

## The game starts here

label start:

    # START HERE!
    
    jump starting
    
    return