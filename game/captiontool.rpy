## Original file by npckc - https://npckc.site or https://npckc.itch.io
## Download at https://npckc.itch.io/caption-tool-for-renpy

## With an additional Screenshake setting by TheoMinute - https://twitter.com/theominute
## Download at https://minute.itch.io/renpy-accessibility

################################################################################
## Caption Tool
################################################################################

# Hello! This is Caption Tool, a simple tool for adding image and sound captions to your Ren'Py game, made by npckc (https://npckc.site)!

# Lines that begin with TODO: are sections where you may be required to do something with the code, so you can Ctrl+F TODO: to make sure you haven't missed anything.

# TODO: Please copy this file (captiontool.rpy) to the "game" folder of your game. As well, please add the following textbutton to a screen somewhere, like the Preferences screen in your screens.rpy file.

# textbutton _("Accessibility") action ShowMenu("accessibility")
# TODO: Remove the # when pasting in the preferences screen. You can also use the code in the screens.rpy file of this tool instead.

# Once you've done that, you're OK! Just edit captiontool.rpy to work with your game (e.g., add your own sound captions, change the image caption character name if necessary).

# You can take a look at script.rpy for an example of the code.

# If you use this tool, I would appreciate it if you can credit npckc (https://npckc.site or https://npckc.itch.io) or the tool in some way, but it isn't required.

################################################################################
## Table of Contents
################################################################################

# C1: Initialisation
# C2: Sound Captions
# C3: Image Captions
# C4: Accessibility Menu
# C5: Initialising Sound Captions for Translations
# C6: npckc Licence

################################################################################
## C1: Initialization
################################################################################

# This asks the user whether they want to use image or sound captions the first time they boot the game. It uses Ren'Py's splashscreen function - you can add your own splashscreen to this label as well.
init -1:
    default persistent.sound_captions = True
    default persistent.image_captions = True
    default self.voicing = False

# label splashscreen:

#     scene black
#     if not persistent.caption:
#         menu:
#             "Do you want sound captions on? They describe music and sound effects in text.{fast}"
#             "On":
#                 $ persistent.sound_captions = True
#             "Off":
#                 pass
#         menu:
#             "Do you want image captions on? They describe game visuals in text.{fast}"
#             "On":
#                 $ persistent.image_captions = True
#             "Off":
#                 pass
#         "These options can be changed at any time in the menu.{fast}"
#         $ persistent.caption = True
#     return

################################################################################
## C2: Sound Captions
################################################################################

# These are the commands for playing music and sounds, as well as where sound captions are defined. Please change the text to fit your own

init python:

# This is the text that will show whenever you play a sound. The sound description will follow.

    soundtext = _("Sound: ")

# This is the text that will show whenever you play music. The music description will follow.
    musictext = _("Music: ")

# This is where you define the names for the sound files you will be using in the game.

# TODO: Add your own sound files.

    # example = "audio/examplefile.ogg"
    door = "audio/sfx/Interior-Door_Close.mp3"
    drawer_close = "audio/sfx/Chest-Drawer_Close.mp3"
    drawer_open = "audio/sfx/Chest-Drawer_Open.mp3"
    ocean = "audio/sfx/Edge-of-Ocean.mp3"
    phone = "audio/sfx/iphone.ogg"
    addPoints = "audio/sfx/addPoints.mp3"
    paper = "audio/sfx/newspaper.wav"
    bell = "audio/sfx/bell.mp3"
    tv = "audio/sfx/tv.wav"
    doorknock = "audio/sfx/doorknock.mp3"
    yawn = "audio/sfx/yawn.wav"
    eat = "audio/sfx/eat.ogg"
    flip = "audio/sfx/newspaper.wav"
    people = "audio/sfx/peopletalk.wav"
    carleave = "audio/sfx/carleaving.ogg"
    subPoints = "audio/sfx/subPoints.wav"
    punch = "audio/sfx/punch.wav"
    running = "audio/sfx/running.mp3"
    walking = "audio/sfx/walking.ogg"
    trainambience = "audio/sfx/trainambience.mp3"
    operator = "audio/sfx/operator.mp3"
    trainpass = "audio/sfx/trainpass.wav"
    speaker = "audio/sfx/speaker.wav"
    clap = "audio/sfx/clap.wav"
    doorcreak = "audio/sfx/doorcreak.wav"
    siren = "audio/sfx/siren_1.ogg"
    radio = "audio/sfx/radio.ogg"
    crowdlaugh = "audio/sfx/crowdlaugh.mp3"
    pervlaugh = "audio/sfx/pervlaugh.wav"

# This is where you define the sound captions for each sound file you will be using in the game. Please make sure the names of the sounds defined above match the ones used for the captions below.

# TODO: Add your own sound captions.

    sound_list = {
    # example: _("Example text here"),
    door : _("A door closes"),
    drawer_close : _("A drawer closes"),
    drawer_open : _("A drawer opens"),
    ocean : _("Ocean waves hit the shore"),
    phone : _("A phone alarm rings"),
    addPoints: _("Points have been added!"),
    paper : _("A newspaper gets opened"),
    bell : _("The school bell rings"),
    tv : _("Television turns on"),
    doorknock : _("Knocking on the door"),
    yawn : _("Yawns"),
    eat : _("Eating food"),
    flip : _("Flipping pages"),
    people : _("People talking"),
    carleave : _("Vehicles passing by"),
    subPoints: _("Points have been deducted!"),
    punch : _("A strong punch"),
    running : _("Running footsteps"),
    walking : _("Walking footsteps"),
    trainambience : _("Train ambience"),
    operator : _("Train operator announcement"),
    trainpass : _("Incoming train"),
    speaker : _("Loud microphone speaker"),
    clap : _("Clapping of students"),
    doorcreak : _("The door opens"),
    siren : _("Police siren in the distance"),
    radio : _("Police radio echo"),
    crowdlaugh : _("People laughing"),
    pervlaugh : _("Perverted laughter"),
    
    }

# This is where you define the names for the music files you will be using in the game. It is recommended to define the main menu BGM as well.

# TODO: Add your own music files.

    # example = "audio/examplefile.ogg"
    business = "audio/music/Future-Business_v001.mp3"
    concrete = "audio/music/The-Concrete-Bakes_Looping.mp3"
    garden = "audio/music/Sculpture-Garden_Looping.mp3"
    summer = "audio/music/Careless-Summer_Looping.mp3"
    tutorial = "audio/music/Shenanigans!.ogg"
    rest = "audio/music/Time_for_Rest.ogg"
    magical ="audio/music/Magical.ogg"
    poppy = "audio/music/PoppyShop.ogg"
    evans = "audio/music/Evans.ogg"
    quirky = "audio/music/QuirckyShop.ogg"
    jazzy = "audio/music/JazzyShop.ogg"
    relax = "audio/music/Relax.ogg"
    Lurking = "audio/music/Lurking.ogg"
    legends = "audio/music/In_Legends.ogg"
    doll = "audio/music/Doll_Dance.ogg"
    fight = "audio/music/Fight.ogg"
    everyone = "audio/music/Everyone.ogg"
    
    

# This is where you define the music captions for each music file you will be using in the game. Please make sure the names of the music defined above match the ones used for the captions below.

# TODO: Add your own music captions.

    music_list = {
    # example: _("Example text here"),
    business : _("Future Business"),
    concrete : _("The Concrete Bakes"),
    garden : _("Sculpture Garden"),
    summer : _("Careless Summer"),
    tutorial : _("Shenanigans!"),
    rest : _("Time for Rest"),
    magical : _("Magical"),
    poppy : _("Poppy Shop"),
    quirky : _("Quircky Shop"),
    evans : _("Evans"),
    jazzy : _("Jazzy Shop"),
    relax : _("Relax"),
    Lurking: _("Lurking"),
    legends : _("In Legends"),
    doll : _("Doll Dance"),
    fight : _("Fight On"),
    everyone : _("Everyone"),
    
    }

# This is the sound command. It functions the same way as "play sound" normally does. You can change the fadein, fadeout and loop values when you invoke the command. If you do not change the values, the default values are 0.0 fadein, 0.0 fadeout, and no loop. If you change the values below, that will change the default values for every time you invoke the command.

    def play_sound(file, channel='sound', fadein=0.0, fadeout=0.0, loop=False):
        renpy.sound.play(file, channel=channel, fadein=fadein, fadeout=fadeout, loop=loop)
        if persistent.sound_captions:
            renpy.notify(soundtext + sound_list[file])

# Here are some examples of how to use the play_sound command in your game.
# Put the name for the file that you defined above in the (brackets).
# Add additional values afterwards if you want to change them from the default.
#(Remove the # when using it.)

# $ play_sound(beepbeep)
# $ play_sound(phone, loop=True)

# You can use "stop sound" to stop the sound, just as you would normally.

# This is the music command. It functions the same way as "play music" normally does. You can change the fadein and fadeout values when you invoke the command. If you do not change the values, the default values are 0.0 fadein and 0.0 fadeout. If you change the values below, that will change the default values for every time you invoke the command.

    def play_music(file, channel='music', fadein=0.0, fadeout=0.0):
        renpy.music.play(file, fadein=fadein, fadeout=fadeout)
        if persistent.sound_captions:
            renpy.notify (musictext + music_list[file])

# Here are some examples of how to use the play_music command in your game.
# Put the name for the file that you defined above in the (brackets).
# Add additional values afterwards if you want to change them from the default.
#(Remove the # when using it.)

# $ play_music(cake)
# $ play_music(cake,fadein=2.0,fadeout=2.0)

# You can use "stop music" to stop the sound, just as you would normally.

# Note: By default, the play_sound command will play on the sound channel, and the play_music command will play on the music channel, but if you have custom channels, you can specify the channel in your command.

# Example:
# $ play_sound(ambientsound, channel='ambient')
# $ play_music(rainybgm, channel='weathermusic')

################################################################################
## C3: Image Captions
################################################################################

# This character will speak if image captions or self-voicing is on. Ren'Py also has "alt" (or "sv" in previous versions of Ren'Py), a built-in character that can be used for self-voicing, but the following character, "ic", will be displayed even if self-voicing if off as long as image captions are set to On in Preferences. The default character name is None - that is, there is no name, like a narrator - but that can be changed.

define ic = Character(_(None),condition="persistent.image_captions or _preferences.self_voicing")

# You can read more about Ren'Py's built-in self-voicing options here: https://www.renpy.org/doc/html/self_voicing.html

################################################################################
## C4: Accessibility Menu
################################################################################

# This can be used if you want a menu ONLY for accessibility options. You can also copy and paste the buttons into the default Ren'Py preferences screen.

# screen accessibility():

#     tag menu

#     use game_menu(_("Preferences"), scroll="viewport"):
#         vbox:
#             style_prefix "check"
#             label _("Accessibility")
#             textbutton _("Sound Captions") action ToggleVariable("persistent.sound_captions")
#             textbutton _("Image Captions") action ToggleVariable("persistent.image_captions")
#             # Self-voicing does not work on smartphone devices, so this option only shows if the user is playing on a PC.
#             if renpy.variant("pc"):
#                 textbutton _("Self-Voicing") action Preference("self voicing", "toggle")
#             # This shows Ren'Py's built-in accessibility menu, added to Ren'Py in Ren'Py 7.2.2. This can also be displayed by pressing "A" on the keyboard when playing on a PC. As this option can break the way the game is displayed and also does not support translation as of Ren'Py build 7.3.2, you may want to hide the option. The button should also be removed if your version of Ren'Py is under 7.2.2, as the menu does not exist in previous versions.
#             textbutton _("More Options...") action Show("_accessibility")
#             textbutton ("") #Adds space between accessibility options and return button
#             # The Return button will return the user to the Preferences menu. It can be removed if it isn't necessary.

#             textbutton _("Return") action ShowMenu("preferences")

################################################################################
## C5: Initialising Sound Captions for Translations
################################################################################

# If you are translating your game, adding the following will make sure that sound captions are properly initialised when starting a new game or loading a save file.

# TODO: Add this to the beginning of your start label:

# $ renpy.change_language(_preferences.language, force=True)
# Remove the # when copying and pasting.

# You can see an example in script.rpy.

# TODO: If you are using the Ren'Py after_load label elsewhere, you can just include the code from here into your label

# label after_load:

#     $ renpy.change_language(_preferences.language, force=True)

#     return

# Please refer to script.rpy for an example of how to translate sound captions for a different language.

################################################################################
## C6: Licence
################################################################################

# Copyright 2020 npckc

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

################################################################################
## C7: Screenshake
################################################################################

default screenshake = True

init python:
    # Shakes the screen. To use, put
    # $ shake()
    # inline. For other uses, simply do a check inline for ATL statements, or a ConditionSwitch for shaky images.

    def shake():

        if persistent.screenshake:
            
            renpy.with_statement(hpunch)

        else:

            renpy.with_statement(fade)
            ### OPTIONAL: Show a different effect if screenshake is turned off.
