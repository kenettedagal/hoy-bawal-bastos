#Check if special route unlocked

label Mall_End:

        # 3 endings below 10 is bad ending, 11 to 16 is ending, 17 to 20 good ending
        
        if hbbpoints >=20:
        #block of code to run
                jump Mall_EndG
        
        elif badending1:
                
                if hbbpoints >10:

                centered "You have chosen the bad ending."
                
                        menu:
                        
                                "Try Again":
                                #block of code to run
                                        jump Act_2_School
                                "See the ending":
                                #block of code to run
                                        jump Mall_EndB
        elif mending:

                centered "You got the ending."
                jump Mall_EndM
        



    