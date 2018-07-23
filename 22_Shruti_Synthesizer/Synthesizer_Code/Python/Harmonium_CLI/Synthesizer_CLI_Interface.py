import os
import Envelope_Generation_Sampling as env
import Handler as handle

def main():

    answer = 1
    tone_filename = "C4_Sa_Harmonium_VST.wav"
    e = env.Envelope_Generation_Sampling(filename = tone_filename)
    h = handle.Handler()

    os.system('clear') # Clear screen for Linux. In Windows use 'cls' instead of 'clear'

    print "------------------------------------------------------"
    print "-------Welcome to 22 Shruti Synthesizer Program-------"
    print "------------------------------------------------------"

    while answer == 1:

        os.system('clear') # Clear screen for Linux. In Windows use 'cls' instead of 'clear'

        print "\nChoose from the options below:-"
        print "1).Western Scale"
        print "2).Notes of your choice"
        print "3).Exit"
        selection = int(raw_input('Select:-'))

        if selection != 3:

            os.system('clear')
            option = h.scale_selection()

            if option == 13:
                selection = 3
            else:
                h.frequency_selection(option)

        if selection == 1:

            h.defaultNoteGeneration(env = e)
            os.system('clear')
            print "\nPlay!"
            print "(Press \"Panic\" button or move \"Wheel\" to stop playing)"
            h.handling()

        elif selection == 2:
            
            h.dynamicNoteGeneration(env = e)
            os.system('clear')
            print "\nPlay!"
            h.handling()

        else:
            answer = 2

    print "\nBye!"

if __name__== "__main__":
    main()