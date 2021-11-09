## Splashscreen Settings##################################
##
## A custom screen that allows players to set their accessibility settings the first
## time they launch the game. Borrows elements from the Preferences screen in
## screens.rpy, and will need to be manually adjusted.
## https://www.renpy.org/doc/html/splashscreen_presplash.html

screen splash_settings():
    
    frame:

        align 0.5, 0.5
        left_margin 200
        right_margin 200
        top_margin 150
        bottom_margin 150

        left_padding 100
        right_padding 100
        top_padding 50
        bottom_padding 50

        vbox:

            xalign 0.5
            spacing 30

            label _("Accessibility Settings") xalign 0.5
            label _("These options can be changed again at any time in the menu.") xalign 0.5

            hbox:

                # xfill True
                xalign 0.5

                vbox:

                    spacing 5

                    style_prefix "radio"
                    label _("Toggles") xalign 0.5

                    textbutton _("Audio Titles") action ToggleVariable("persistent.sound_captions") alt "Toggle Sound Captions" xalign 0.5
                    textbutton _("Image Descriptions") action ToggleVariable("persistent.image_captions") alt "Toggle Image Descriptions" xalign 0.5
                    textbutton _("Screenshake") action ToggleField(persistent,"screenshake",true_value=True,false_value=False) alt "Toggle Screen Shake" xalign 0.5

                    ## Self-voicing does not work on smartphone devices, so this option only shows if the user is playing on a PC.
                    if renpy.variant("pc"):

                        textbutton _("Self-Voicing") action Preference("self voicing", "toggle") alt "Toggle Self-Voicing" xalign 0.5

                vbox:

                    spacing 5

                    style_prefix "radio"
                    label _("Typeface") xalign 0.5

                    textbutton _("NotoSans") action [gui.SetPreference("font", "gui/fonts/NotoSans-Regular.ttf"), SetVariable("typeface", "NotoSans"), gui.SetPreference("dialogue_spacing", 2)] alt "Change to NotoSans" xalign 0.5

                    textbutton _("DejaVuSans") action [gui.SetPreference("font", "DejaVuSans.ttf"), SetVariable("typeface", "DejaVuSans"), gui.SetPreference("dialogue_spacing", 2.01)] alt "Change to DejaVuSans" xalign 0.5

                    textbutton _("OpenDyslexic") action [gui.SetPreference("font", "_OpenDyslexic3-Regular.ttf"), SetVariable("typeface", "OpenDyslexic"), gui.SetPreference("dialogue_spacing", -4)]  alt "Change to OpenDyslexic" xalign 0.5
                    ## Note: Having so many actions set to a single radio button
                    ## will cause some of the preferences in the same category to appear
                    ## to be all selected, causing players some confusion. Some numbers
                    ## have been set to 2.01 to prevent this from happening.

                vbox:

                    spacing 5

                    style_prefix "radio"
                    label _("Text Color") xalign 0.5
                    
                    textbutton _("White") action gui.SetPreference("color", "#ffffff") alt "Change to White Text" xalign 0.5
                    textbutton _("Cream") action gui.SetPreference("color", "#FBF0D9") alt "Change to Cream Text" xalign 0.5
                    textbutton _("Black") action gui.SetPreference("color", "#000000") alt "Change to Black Text" xalign 0.5

            hbox:

                #xfill True
                xalign 0.5

                vbox:

                    spacing 5

                    style_prefix "radio"
                    label _("Font Size") xalign 0.5

                    if renpy.variant("pc"):
                        textbutton _("Large") action gui.SetPreference("size", 33) alt "Change to Large Size Text" xalign 0.5
                        textbutton _("Regular") action gui.SetPreference("size", 31) alt "Change to Regular Size Text" xalign 0.5

                    elif renpy.variant("mobile"):

                        if typeface == "OpenDyslexic":
                            textbutton _("Large") action gui.SetPreference("phone_size", 32) xalign 0.5
                            textbutton _("Regular") action gui.SetPreference("phone_size", 30) xalign 0.5
                            ## Note: due to the unique nature of the OpenDyslexic font, it needs
                            ## to be just slightly smaller so as to not break the GUI

                        else:
                            textbutton _("Large") action gui.SetPreference("phone_size", 42) xalign 0.5
                            textbutton _("Regular") action gui.SetPreference("phone_size", 40) xalign 0.5
                
                vbox:

                    spacing 5

                    style_prefix "radio"
                    label _("Textbox") xalign 0.5

                    if renpy.variant("pc"):

                        textbutton _("Black") action [gui.SetPreference("ADVtextbox", "gui/textbox_1.png"), gui.SetPreference("NVLtextbox", "gui/nvl_1.png")] alt "Change to Black Textbox" xalign 0.5
                        textbutton _("White") action [gui.SetPreference("ADVtextbox", "gui/textbox_2.png"), gui.SetPreference("NVLtextbox", "gui/nvl_2.png")]  alt "Change to White Textbox" xalign 0.5

                    elif renpy.variant("mobile"):

                        textbutton _("Black") action [gui.SetPreference("m_ADVtextbox", "gui/phone/textbox_1.png"), gui.SetPreference("m_NVLtextbox", "gui/phone/nvl_1.png")] xalign 0.5
                        textbutton _("White") action [gui.SetPreference("m_ADVtextbox", "gui/phone/textbox_2.png"), gui.SetPreference("m_NVLtextbox", "gui/phone/nvl_2.png")] xalign 0.5
            
                vbox:

                    spacing 5

                    style_prefix "radio"
                    label _("Line Spacing") xalign 0.5

                    if typeface == "OpenDyslexic":

                        textbutton _("Taller") action gui.SetPreference("dialogue_spacing", -2) alt "Change the height of the space between lines of dialogue" xalign 0.5
                        textbutton _("Regular") action gui.SetPreference("dialogue_spacing", -4) alt "Change the height of the space between lines of dialogue" xalign 0.5

                    elif typeface == "DejaVuSans":

                        textbutton _("Taller") action gui.SetPreference("dialogue_spacing", 4.01) alt "Change the height of the space between lines of dialogue" xalign 0.5
                        textbutton _("Regular") action gui.SetPreference("dialogue_spacing", 2.01) alt "Change the height of the space between lines of dialogue" xalign 0.5

                    else:

                        textbutton _("Taller") action gui.SetPreference("dialogue_spacing", 4) alt "Change the height of the space between lines of dialogue" xalign 0.5
                        textbutton _("Regular") action gui.SetPreference("dialogue_spacing", 2) alt "Change the height of the space between lines of dialogue" xalign 0.5
 
            textbutton _("Confirm") action Return() xalign 0.5

## Extras screens ###########################################
##
## Screens that includes Image Galleries, Music Room, Replay Room, and Dev Notes.
## https://www.renpy.org/doc/html/rooms.html

## We let Ren'Py resize our images so we don't have to make buttons in another
## program.

## These background buttons are 480x270
image room_button = im.FactorScale("bg/room.jpg", 0.25)
image office_button = im.FactorScale("bg/future_office.jpg", 0.25)
image beach_button = im.FactorScale("bg/sort_of_beautiful_beach_day.jpg", 0.25)
image bglock_button = "gui/button/bg_locked.jpg"

## These sprite buttons are 290x290
image ehappy_button = Crop((170, 245, 290, 290), "eileen happy")
image eneutral_button = Crop((170, 245, 290, 290), "eileen neutral")
image esurprised_button = Crop((170, 245, 290, 290), "eileen surprised")
image eupset_button = Crop((170, 245, 290, 290), "eileen upset")
image eangry_button = Crop((170, 245, 290, 290), "eileen angry")
image spritelock_button = "gui/button/sprite_locked.jpg"

init python:

    g_bg = Gallery()

    # Backgrounds for the BG Gallery
    g_bg.button("room")
    g_bg.unlock_image("room") 

    g_bg.button("office")
    g_bg.image("future_office")
    g_bg.unlock("future_office")

    g_bg.button("beach")
    g_bg.image("sort_of_beautiful_beach_day")
    g_bg.unlock("sort_of_beautiful_beach_day")

    # Sprites for the Sprite Gallery
    # We put a background in the first spot so Eileen isn't floating in a void.

    g_sprite = Gallery()

    g_sprite.button("eileen happy")
    g_sprite.unlock_image("room", "eileen happy")

    g_sprite.button("eileen neutral")
    g_sprite.unlock_image("room", "eileen neutral")

    g_sprite.button("eileen surprised")
    g_sprite.unlock_image("room", "eileen surprised")

    g_sprite.button("eileen upset")
    g_sprite.image("room", "eileen upset")
    g_sprite.unlock("room", "eileen upset")

    g_sprite.button("eileen angry")
    g_sprite.image("room", "eileen angry")
    g_sprite.unlock("room", "eileen angry")

    # The button used for locked images
    g_bg.locked_button = "bglock_button"
    g_sprite.locked_button = "spritelock_button"

    # The transition used when switching images.
    g_bg.transition = dissolve
    g_sprite.transition = dissolve

    # MusicRoom instance.
    mr = MusicRoom(fadeout=1.0)

    # Add music files.
    mr.add("audio/music/Careless-Summer_Looping.mp3", always_unlocked=True)
    mr.add("audio/music/Future-Business_v001.mp3")
    mr.add("audio/music/Sculpture-Garden_Looping.mp3")
    mr.add("audio/music/The-Concrete-Bakes_Looping.mp3")

## Extras Navigation screen ############################################################
##
## This is the same as the Game Menu Navigation screen, but just for the Extras.

screen extras_navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        textbutton _("Achievements") action ShowMenu("achievements") alt "Achievements"

        textbutton _("Sprite Gallery") action ShowMenu("sprite_gallery") alt "Sprite Gallery"

        textbutton _("Background Gallery") action ShowMenu("bg_gallery") alt "Background Gallery"

        textbutton _("Music Room") action ShowMenu("music_gallery") alt "Music Room"

        textbutton _("Replay Room") action ShowMenu("replay_gallery") alt "Replay Room"

        if persistent.game_clear:

            textbutton _("Developer Notes") action ShowMenu("dev_notes") alt "Developer Notes"

        else:

            textbutton _("???") action None alt ":Locked Option"

        textbutton _("Return") action Return() alt "Return"

## Extras Menu screen #######################################
##
## This is the same as the Game Menu screen, but just for the Extras.

screen extras_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    label title

    use extras_navigation

## Sprite Gallery screen ######################################
##
## This is a simple screen that shows buttons that display a sprite imposed on a
## background.

screen sprite_gallery():

    tag menu

    ## This use statement includes the extras_menu screen inside this one.
    use extras_menu("Sprite Gallery"):

        grid 5 1:

            xfill True
            yfill True

            ## Call make_button to show a particular button.
            # add g_sprite.make_button("sprite", "sprite_button")

            add g_sprite.make_button("eileen happy", "ehappy_button")
            add g_sprite.make_button("eileen neutral", "eneutral_button")
            add g_sprite.make_button("eileen surprised", "esurprised_button")
            add g_sprite.make_button("eileen upset", "eupset_button")
            add g_sprite.make_button("eileen angry", "eangry_button")

## Background Gallery screen ############################################################
##
## This is a simple screen that shows buttons that display a background.
## You can easily adapt this screen to make a CG or concept art screen.

screen bg_gallery():

    tag menu

    ## This use statement includes the extras_menu screen inside this one.
    use extras_menu("Background Gallery"):

        grid 1 3:

            xfill True
            yfill True

            ## Call make_button to show a particular button.
            # add g_bg.make_button("background", "bg_button")

            add g_bg.make_button("room", "room_button", xalign=0.5, yalign=0.5)
            add g_bg.make_button("office", "office_button", xalign=0.5, yalign=0.5)
            add g_bg.make_button("beach", "beach_button", xalign=0.5, yalign=0.5)

## Music Gallery screen ############################################################
##
## This is a simple screen that shows buttons that play a music track.

screen music_gallery():

    tag menu

    ## This use statement includes the extras_menu screen inside this one.
    use extras_menu("Music Room"):

        vbox:

            xalign 0.5
            yalign 0.5

            # The buttons that play each track.
            textbutton "The Concrete Brakes" action mr.Play("audio/music/The-Concrete-Bakes_Looping.mp3")
            textbutton "Sculpture Garden" action mr.Play("audio/music/Sculpture-Garden_Looping.mp3")
            textbutton "Future Business" action mr.Play("audio/music/Future-Business_v001.mp3")
            textbutton "Careless Summer" action mr.Play("audio/music/Careless-Summer_Looping.mp3")

            null height 20

            hbox:
            # Buttons that let us advance through tracks.
                textbutton "Previous" action mr.Previous() alt "Previous Song"
                textbutton "Next" action mr.Next() alt "Next Song"

            null height 20

        # Start the music playing on entry to the music room.
        on "replace" action mr.Play()

        ## Restore the main menu music upon leaving.
        ## You can actually comment this out if you want to let players enjoy the music
        ## while looking at the other screens.
        on "replaced" action Play("music", "audio/The-Concrete-Bakes_Looping.mp3")

## Replay Gallery screen ######################################
##
## This is a simple screen that shows buttons that replay a scene from the game.

screen replay_gallery():

    tag menu

    ## This use statement includes the extras_menu screen inside this one.
    use extras_menu("Replay Room"):

        vbox:

            xalign 0.5
            yalign 0.5

            # The buttons that play each section.
            textbutton "The Beginning" action Replay("start")
            textbutton "The Office" action Replay("office")
            textbutton "The Beach" action Replay("beach")

            null height 20

## Dev Notes screen ########################################
##
## This screen contains a message for players after they beat the entire game.
## We borrowed the base of this screen from the About screen.

screen dev_notes():

    tag menu

    ## This use statement includes the extras_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the extras_menu
    ## screen.
    use extras_menu(_("Developer's Notes"), scroll="viewport"):

        style_prefix "about"

        vbox:

            ## gui.dev_notes is usually set in options.rpy.
            if gui.dev_notes:
                text "[gui.dev_notes!t]\n"

## Type your special message here.
define gui.dev_notes = _p("""Hello, this is BáiYù of tofurocks here. I want to thank
    you for downloading this All-In-One GUI template to use in your own game. As
    someone who has received support from the visual novel community in the past,
    I wanted to give back something that will benefit other developers for no
    charge neccessary. While the code provided here is almost a straight copy
    from the official documentation for the most part, I purposely kept it very bare-bones so that
    you can customize the GUI yourself. I hope that by sharing this with others, the overall quality of all Ren'Py games will improve.
    \n
    Thank you for taking the time to read this, and I wish you the best on your
    development adventures to come.""")

## Achievements screen ######################################
##
## This custom screen contains a list of achievements for the game.
## Official Documentation: https://www.renpy.org/doc/html/achievement.html
## Additional writeup by bobcgames:
## Part 1: http://bobcgames.com/blog/archives/48/
## Part 2: http://bobcgames.com/blog/archives/54/
## Roselia Achievements Module: https://github.com/OlegWock/Roselia-achievements/

## List achievements that are either True or False here
python early:
    simple_achievement_list = (
        # ("Achievement Name", "Description when not unlocked", "Description when unlocked"),
        ("Beginning", "???", "Started a new game"),
        ("Office", "???", "Went to the office"),
        ("Beach", "???", "Went to the beach"),
        ("Completionist", "???", "Read all of the game")
    )

## Registers your achievements to work on backend systems such as Steam
## Be sure to match the name of the achievement in achievement_list and
## the corresponding achievement.grant or achievement.progress in the script.
## Notes for testing: you need at least 2 achievements for it to work

init python:

    for a, lockdesc, unlockdesc in simple_achievement_list:

        ## This auto-populates the achievements to register on the backend
        achievement.register(a)

        ## This Achievement is based on an integer, and must be defined manually
        achievement.register("Point Collector", stat_max=100, stat_modulo=0)
        ## TODO: Simplify achievements that are integer-based
        ## to update in a bar directly tied to achievement.progress

## For our Point Collector Achievement
default persistent.points = 0

## Our actual achievements screen
screen achievements():

    tag menu

    ## This use statement includes the extras_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the extras_menu
    ## screen.
    use extras_menu(_("Achievements"), scroll="viewport"):

        ## This screen doesn't need anything fancy, so we borrow the style
        ## from the About screen, which just displays text.
        style_prefix "about"

        vbox:

            ## This auto-populates our list of simple achievements that will appear
            ## in the screen, so we don't have to manually type each one out.
            for aname, lockdesc, unlockdesc in simple_achievement_list:

                if achievement.has(aname):

                    text "[aname]: [unlockdesc]"

                else:

                    text "[aname]: [lockdesc]"

            ## We have to type each integer based achievement however
            hbox:
                text "Point Collector:"

                null width 10

                bar value persistent.points range 100 xsize 525

            text "[persistent.readtotal]% of the game read"

## End Credits Scroll ############################################################
## ATL for scrolling screen object. In this case, credits roll.
## Speed is the time for object to move up from initial ypos to finish ypos.

## Code Source: https://lemmasoft.renai.us/forums/viewtopic.php?t=42667

transform credits_scroll(speed):
    ypos 3500
    linear speed ypos -3500
    ## Adjust these numbers to be the height of your end credits. Both numbers
    ## should be the same.

## Credits screen.

screen credits():

    ## Ensure that the game_menu screens don't appear and interrupt the credits.
    key "K_ESCAPE" action NullAction()
    key "K_MENU" action NullAction()
    key "mouseup_3" action NullAction()

    style_prefix "credits"

    ## If a player has seen the end credits before, this button appears.
    if persistent.credits_seen:

        textbutton _("Skip End Credits") action Jump("skip_credits") xalign 1.0 yalign 1.0

    timer 15.0 action Return()
    ## Adjust this number to control when the Credits screen is hidden and the game
    ## returns to its normal flow.
    ## Ideally, there is some wait time after the the credits reaches the end.

    frame at credits_scroll(10.0):
        ## Adjust this number to control the speed at which the credits scroll.
        background None
        xalign 0.5

        vbox:
            label "Credits" xalign 0.5

            null height 300

            text "Producer" size 100
            null height 50
            text "BáiYù"

            #null height 200

            # text "Logo" size 100
            # null height 50
            # text "Lorem Ipsum"

            #null height 200

            # text "Script" size 100
            # null height 50
            # text "Lorem Ipsum"

            null height 200
            
            text "Art" size 100
            null height 50

            text "Mannequin by HelloAR14"

            null height 50

            text "Uncle Mugen" 

            null height 200

            text "Soundtrack" size 100
            null height 50 

            text "Eric Matyas"

            null height 200

            # text "GUI Template" size 100
            text "Programming" size 100
            null height 50

            hbox:

                xalign 0.5
                spacing 200

                text "BáiYù"

                text "bobcgames"

            null height 50

            hbox:

                xalign 0.5
                spacing 200

                text "minute" 

                text "npckc" 

            null height 200

            text "Special Thanks" size 100
            null height 50 

            text "Renall"

            null height 50 

            text "tofurocks Patrons"

            null height 200

            # text "Trailer" size 100
            # null height 50
            # text "Lorem Ipsum"

            # null height 200

            # text "Voiceover" size 100
            # null height 50 

            # hbox:
            #     xalign 0.5
            #     spacing 250

            #     vbox:

            #         text "Lorem Ipsum"

            #     vbox:

            #         text "Lorem Ipsum"

            # null height 200

            # text "Backers" size 100
            # null height 50

            # hbox:

            #     xalign 0.5
            #     spacing 100
            #     style_prefix "backercredits"

            #     vbox:

            #         text "Lorem Ipsum"

            #     vbox:

            #         text "Lorem Ipsum"

            #     vbox:

            #         text "Lorem Ipsum"

            text "Made with Ren'Py [renpy.version_only]." size 100

            null height 450

            text "Thanks for Playing!" size 100

style credits_hbox:
    spacing 40
    ysize 30

style credits_label_text:
    xalign 0.5
    size 200
    text_align 0.5

style credits_text:
    xalign 0.5
    size 80
    justify True
    text_align 0.5
    color "#ffffff"

style backercredits_text:
    xalign 0.5
    size 50
    justify True
    text_align 0.5
    color "#ffffff"


## Results Screen ############################################################
## A screen that displays how much of the game the player has seen.

## Code Source: https://lemmasoft.renai.us/forums/viewtopic.php?t=39859
## Official Documentation of function: https://www.renpy.org/doc/html/other.html#renpy.count_dialogue_blocks

# This creates a percentage based on how much of the game the player has seen. 
init python:

    numblocks = renpy.count_dialogue_blocks()

    def percent():

        global readtotal
        readtotal = renpy.count_seen_dialogue_blocks()* 100 / numblocks
        persistent.readtotal = readtotal
        ## This is displayed in our Achievements screen.

default readtotal = 0

screen results():
    
    zorder 200

    vbox:
        xalign .5
        yalign .2
        spacing 45

        text "Script Seen: [readtotal]%" color "#fff"

## TODO: Figure out how to get total game time working properly
## https://lemmasoft.renai.us/forums/viewtopic.php?t=40407
## Official Documentation of function: https://www.renpy.org/doc/html/other.html#renpy.get_game_runtime

# default playtime = 0

# init 2 python:

#     def total_playtime(d):
#         renpy.store.playtime += renpy.get_game_runtime()
#         #renpy.clear_game_runtime()
#         d["playtime"] = renpy.store.playtime

    # config.save_json_callbacks = [total_playtime]