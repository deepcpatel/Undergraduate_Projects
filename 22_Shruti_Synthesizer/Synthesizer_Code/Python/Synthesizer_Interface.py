# pyGame installation Instruction :
#
# 1). Install pyGame by running - "sudo pip install pygame"
#
#
# Homepage and Documentation : 1). http://www.pygame.org/docs/
#                              2). http://www.pygame.org
#
# Example:- Find examples in this directory in this PC


import sys
import os
import numpy as np
import Envelope_Generation_Sampling as env  # For Sampling based, call : import Envelope_Generation_Sampling as env
                                            # For Fourier based, call : import Envelope_Generation_Fourier as env
# import matplotlib.pyplot as plt
import time
import pygame
from pygame.locals import *
# import datetime
import mido
# from scikits.audiolab import play

# Two different methods for playing the sound.
def play_maxtime(sound, lo):
    sound.play(loops=lo)

def play_loops(sound, duration, lo):
    sound.play(loops=lo)
    pygame.time.delay(duration)
    sound.stop()

def defaultNoteGeneration(Frequency,Saptak):

    NUM_SEC = -1  # NUM_SEC = -1 generates only 1000 cycle of the note OR NUM_SEC = t generates t seconds of note
    ab = {}
    ind1 = {}
    ind2 = {}

    ab[0] = [env.Generate_Sound(Frequency,Saptak,1,NUM_SEC)]
    f = open('temp.txt','r')
    ind1[0] = int(f.next())
    ind2[0] = int(f.next())
    f.close()
    ab[1] = [env.Generate_Sound(Frequency,Saptak,2,NUM_SEC)]
    f = open('temp.txt','r')
    ind1[1] = int(f.next())
    ind2[1] = int(f.next())
    f.close()
    ab[2] = [env.Generate_Sound(Frequency,Saptak,4,NUM_SEC)]
    f = open('temp.txt','r')
    ind1[2] = int(f.next())
    ind2[2] = int(f.next())
    f.close()
    ab[3] = [env.Generate_Sound(Frequency,Saptak,6,NUM_SEC)]
    f = open('temp.txt','r')
    ind1[3] = int(f.next())
    ind2[3] = int(f.next())
    f.close()
    ab[4] = [env.Generate_Sound(Frequency,Saptak,8,NUM_SEC)]
    f = open('temp.txt','r')
    ind1[4] = int(f.next())
    ind2[4] = int(f.next())
    f.close()
    ab[5] = [env.Generate_Sound(Frequency,Saptak,10,NUM_SEC)]
    f = open('temp.txt','r')
    ind1[5] = int(f.next())
    ind2[5] = int(f.next())
    f.close()
    ab[6] = [env.Generate_Sound(Frequency,Saptak,12,NUM_SEC)]
    f = open('temp.txt','r')
    ind1[6] = int(f.next())
    ind2[6] = int(f.next())
    f.close()
    ab[7] = [env.Generate_Sound(Frequency,Saptak,14,NUM_SEC)]
    f = open('temp.txt','r')
    ind1[7] = int(f.next())
    ind2[7] = int(f.next())
    f.close()
    ab[8] = [env.Generate_Sound(Frequency,Saptak,15,NUM_SEC)]
    f = open('temp.txt','r')
    ind1[8] = int(f.next())
    ind2[8] = int(f.next())
    f.close()
    ab[9] = [env.Generate_Sound(Frequency,Saptak,17,NUM_SEC)]
    f = open('temp.txt','r')
    ind1[9] = int(f.next())
    ind2[9] = int(f.next())
    f.close()
    ab[10] = [env.Generate_Sound(Frequency,Saptak,19,NUM_SEC)]
    f = open('temp.txt','r')
    ind1[10] = int(f.next())
    ind2[10] = int(f.next())
    f.close()
    ab[11] = [env.Generate_Sound(Frequency,Saptak,21,NUM_SEC)]
    f = open('temp.txt','r')
    ind1[11] = int(f.next())
    ind2[11] = int(f.next())
    f.close()
    ab[12] = [env.Generate_Sound(Frequency,Saptak+1,1,NUM_SEC)]
    f = open('temp.txt','r')
    ind1[12] = int(f.next())
    ind2[12] = int(f.next())
    f.close()

    return (ab, ind1, ind2)

def dynamicNoteGeneration(Frequency,Saptak):

    NUM_SEC = -1    # NUM_SEC = -1 generates only 1000 cycle of the note OR NUM_SEC = t generates t seconds of note
    ab = {}
    ind1 = {}
    ind2 = {}

    # --------------------------Sa--------------------------------

    ab[0] = [env.Generate_Sound(Frequency,Saptak,1,NUM_SEC)]
    f = open('temp.txt','r')
    ind1[0] = int(f.next())
    ind2[0] = int(f.next())

    # --------------------------ReA-------------------------------

    print "\nChoose Komal Re:-"
    print "1).Ati Komal"
    print "2).Komal"
    selection = int(raw_input('Select:-'))

    ab[1] = [env.Generate_Sound(Frequency,Saptak,1+selection,NUM_SEC)]
    f = open('temp.txt','r')
    ind1[1] = int(f.next())
    ind2[1] = int(f.next())

    #---------------------------ReS--------------------------------

    print "\nChoose Shuddh Re:-"
    print "1).Shuddh"
    print "2).Teevra"
    selection = int(raw_input('Select:-'))

    ab[2] = [env.Generate_Sound(Frequency,Saptak,3+selection,NUM_SEC)]
    f = open('temp.txt','r')
    ind1[2] = int(f.next())
    ind2[2] = int(f.next())

    #-----------------------------GaA---------------------------------

    print "\nChoose Komal Ga:-"
    print "1).Ati Komal"
    print "2).Komal"
    selection = int(raw_input('Select:-'))

    ab[3] = [env.Generate_Sound(Frequency,Saptak,5+selection,NUM_SEC)]
    f = open('temp.txt','r')
    ind1[3] = int(f.next())
    ind2[3] = int(f.next())
    #-----------------------------GaS----------------------------------

    print "\nChoose Shuddh Ga:-"
    print "1).Shuddh"
    print "2).Teevra"
    selection = int(raw_input('Select:-'))

    ab[4] = [env.Generate_Sound(Frequency,Saptak,7+selection,NUM_SEC)]
    f = open('temp.txt','r')
    ind1[4] = int(f.next())
    ind2[4] = int(f.next())

    #-----------------------------MaS----------------------------------

    print "\nChoose Shuddh Ma:-"
    print "1).Shuddh Lower Pitch Madhyam"
    print "2).Ek Shruti Madhyam"
    selection = int(raw_input('Select:-'))

    ab[5] = [env.Generate_Sound(Frequency,Saptak,9+selection,NUM_SEC)]
    f = open('temp.txt','r')
    ind1[5] = int(f.next())
    ind2[5] = int(f.next())

    #-----------------------------MaSh----------------------------------

    print "\nChoose Taar Ma:-"
    print "1).Shuddh Madhyam"
    print "2).Teevra Madhyam Higher Pitch"
    selection = int(raw_input('Select:-'))

    ab[6] = [env.Generate_Sound(Frequency,Saptak,11+selection,NUM_SEC)]
    f = open('temp.txt','r')
    ind1[6] = int(f.next())
    ind2[6] = int(f.next())

    #------------------------------P-----------------------------------

    ab[7] = [env.Generate_Sound(Frequency,Saptak,14,NUM_SEC)]
    f = open('temp.txt','r')
    ind1[7] = int(f.next())
    ind2[7] = int(f.next())

    #-----------------------------DhA-----------------------------------

    print "\nChoose Komal Dh:-"
    print "1).Ati Komal"
    print "2).Komal"
    selection = int(raw_input('Select:-'))

    ab[8] = [env.Generate_Sound(Frequency,Saptak,14+selection,NUM_SEC)]
    f = open('temp.txt','r')
    ind1[8] = int(f.next())
    ind2[8] = int(f.next())

    #------------------------------DhS-----------------------------------

    print "\nChoose Shuddh Dh:-"
    print "1).Shuddh"
    print "2).Teevra"
    selection = int(raw_input('Select:-'))

    ab[9] = [env.Generate_Sound(Frequency,Saptak,16+selection,NUM_SEC)]
    f = open('temp.txt','r')
    ind1[9] = int(f.next())
    ind2[9] = int(f.next())

    #------------------------------NiA-----------------------------------

    print "\nChoose Komal Ni:-"
    print "1).Ati Komal"
    print "2).Komal"
    selection = int(raw_input('Select:-'))

    ab[10] = [env.Generate_Sound(Frequency,Saptak,18+selection,NUM_SEC)]
    f = open('temp.txt','r')
    ind1[10] = int(f.next())
    ind2[10] = int(f.next())

    #------------------------------NiS-----------------------------------

    print "\nChoose Shuddh Ni:-"
    print "1).Shuddh"
    print "2).Teevra"
    selection = int(raw_input('Select:-'))

    ab[11] = [env.Generate_Sound(Frequency,Saptak,20+selection,NUM_SEC)]
    f = open('temp.txt','r')
    ind1[11] = int(f.next())
    ind2[11] = int(f.next())

    #------------------------------Sa2-----------------------------------

    ab[12] = [env.Generate_Sound(Frequency,Saptak+1,1,NUM_SEC)]
    f = open('temp.txt','r')
    ind1[12] = int(f.next())
    ind2[12] = int(f.next())

    return (ab, ind1, ind2)


def saptak_selection():

    print "\nSelect your Saptak/Octave:-"
    print "1).Mandra"
    print "2).Madhya"
    print "3).Taar"
    print "4).Exit"
    selection = int(raw_input('Select:-'))

    return selection

def scale_selection():

    print "Select Scale:-"
    print "1).C (Safed1)"
    print "2).C# (Kali1)"
    print "3).D (Safed2)"
    print "4).D# (Kali2)"
    print "5).E (Safed3)"
    print "6).F (Safed4)"
    print "7).F# (Kali3)"
    print "8).G (Safed5)"
    print "9).G# (Kali4)"
    print "10).A (Safed6)"
    print "11).A# (Kali5)"
    print "12).B (Safed7)"
    print "13).Exit"
    selection = int(raw_input('Select:-'))
    return selection

def frequency_selection(Option3):

    f = 0

    if Option3==1:
        f=261.63
    elif Option3==2:
        f=277.18
    elif Option3==3:
        f=293.44
    elif Option3==4:
        f=311.13
    elif Option3==5:
        f=329.63
    elif Option3==6:
        f=349.23
    elif Option3==7:
        f=369.99
    elif Option3==8:
        f=392.00
    elif Option3==9:
        f=415.30
    elif Option3==10:
        f=440.00
    elif Option3==11:
        f=466.16
    elif Option3==12:
        f=493.88
    return f

def ringing(tone_dict, ind1, ind2, key): # Returns 3 parts of wave in form of Attack-Decay, Sustain and Release
    wave = np.array(tone_dict[key])
    wave = wave[0,:]

    wave = np.array(wave,"int16")

    ad = wave[0:ind1[key]]
    sust = wave[ind1[key]:ind2[key]]
    rel = wave[ind2[key] + 1:len(wave)]

    ad = pygame.sndarray.make_sound(ad) # Attack-Decay
    sust = pygame.sndarray.make_sound(sust) # Sustain
    rel = pygame.sndarray.make_sound(rel) # Release

    return (ad, sust, rel)

def handling(tone_dict, ind1, ind2):

    tones = {}
    mapping = {} # Doing mapping for Recording
    ret = {}

    mapping[0] = ' Sa '
    mapping[1] = ' ReK '
    mapping[2] = ' ReS '
    mapping[3] = ' GaK '
    mapping[4] = ' GaS '
    mapping[5] = ' MaS '
    mapping[6] = ' MaT '
    mapping[7] = ' P '
    mapping[8] = ' DhK '
    mapping[9] = ' DhS '
    mapping[10] = ' NiK '
    mapping[11] = ' NiS '
    mapping[12] = ' Sa2 '

    # Creating Directory and file for Recording

    # if not os.path.exists('Record'):
    #    os.makedirs('Record')

    # timestamp = "{:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now())

    # f = open('Record/Record_' + timestamp + '.txt', 'w')

    # Initializing Tone dictionary
    for i in range(13):
        tones[i] = {}

    (tones[0][0], tones[0][1], tones[0][2]) = ringing(tone_dict, ind1, ind2, 0)
    (tones[2][0], tones[2][1], tones[2][2]) = ringing(tone_dict, ind1, ind2, 2)
    (tones[4][0], tones[4][1], tones[4][2]) = ringing(tone_dict, ind1, ind2, 4)
    (tones[5][0], tones[5][1], tones[5][2]) = ringing(tone_dict, ind1, ind2, 5)
    (tones[7][0], tones[7][1], tones[7][2]) = ringing(tone_dict, ind1, ind2, 7)
    (tones[9][0], tones[9][1], tones[9][2]) = ringing(tone_dict, ind1, ind2, 9)
    (tones[11][0], tones[11][1], tones[11][2]) = ringing(tone_dict, ind1, ind2, 11)
    (tones[12][0], tones[12][1], tones[12][2]) = ringing(tone_dict, ind1, ind2, 12)
    (tones[1][0], tones[1][1], tones[1][2]) = ringing(tone_dict, ind1, ind2, 1)
    (tones[3][0], tones[3][1], tones[3][2]) = ringing(tone_dict, ind1, ind2, 3)
    (tones[6][0], tones[6][1], tones[6][2]) = ringing(tone_dict, ind1, ind2, 6)
    (tones[8][0], tones[8][1], tones[8][2]) = ringing(tone_dict, ind1, ind2, 8)
    (tones[10][0], tones[10][1], tones[10][2]) = ringing(tone_dict, ind1, ind2, 10)

    ret['37'] = 0 # S
    ret['39'] = 2 # D
    ret['41'] = 4 # F
    ret['42'] = 5 # G
    ret['44'] = 7 # H
    ret['46'] = 9 # J
    ret['48'] = 11 # K
    ret['49'] = 12 # L
    ret['38'] = 1 # E
    ret['40'] = 3 # R
    ret['43'] = 6 # U
    ret['45'] = 8 # I
    ret['47'] = 10 # O

    '''
    # Window initialization
    screen=pygame.display.set_mode((800,600))
    pygame.display.set_caption("Virtual Piano")

    # Background text layer initialization
    background = pygame.Surface(screen.get_size())
    background = background.convert()

    # Text information to go to background
    if pygame.font:
        font = pygame.font.Font(None, 36)
        title = font.render("Virtual Piano", 1, (255, 255, 255))
        instructions = font.render("Each note corresponds to the following computer keys:", 1, (255,255,255))
        note = font.render("Note: C  C# D  D# E  F  F# G  G# A  A# B  C(high)", 1, (255,255,255))
        key =  font.render("Key:   S  E  D  R   F  G  U   H   I   J  O   K   L   ---Z(to Quit)---", 1, (255,255,255))
        textpos = title.get_rect(top=410, left=10)
        instpos = instructions.get_rect(top=440, left=10)
        notepos = note.get_rect(top=470, left=10)
        keypos = key.get_rect(top=500, left=10)
        background.blit(title, textpos)
        background.blit(instructions, instpos)
        background.blit(note, notepos)

        background.blit(key, keypos)

    # Add background to screen. Added to hear to load before images.
    screen.blit(background, (0,0))
    pygame.display.flip()
    '''
    def input(tones, ret):
        try:
            timeout = time.time() + 1 # See this in RaspberryPi
            input_port = 'VMPK Output:VMPK Output 129:0' # Use "print mido.get_input_names()" to get input ports
            with mido.open_input(input_port) as port:

                while True:      # Flush out junk message
                    msg = port.receive(block=False)
                    if time.time() > timeout:
                        break

                for message in port:
                    if str(message)[6] == 'n':

                        # f.write(mapping[ret[str(message)[24:26]]])
                        # play_maxtime(tones[ret[str(message)[23:25]]][0], 0) # Attack and Decay Part
                        play_maxtime(tones[ret[str(message)[23:25]]][1], -1) # Sustain Part

                    elif str(message)[6] == 'f':  # Release part during key release

                        # f.write("|") # Separator in Recording file
                        tones[ret[str(message)[24:26]]][1].stop() # Stop Play loop
                        # play_maxtime(tones[ret[str(message)[24:26]]][2], 0) # Release Part

                    elif str(message)[6] == 'l':
                        return 0
        except:
            print "\n Wrong Key... Try Again!"
            return 0
        return -1

    while True:
        ret = input(tones, ret)
        if ret == 0:
            # f.close()
            return 0


def main():

    answer = 1

    sample_rate, bit_rate, channels, buff = 22050, -16, 1, 512
    pygame.mixer.pre_init(sample_rate, bit_rate, channels, buff)

    os.system('clear') # Clear screen for Linux. In Windows use 'cls' instead of 'clear'

    print "------------------------------------------------------"
    print "-------Welcome to 22 Shruti Synthesizer Program-------"
    print "------------------------------------------------------"

    res = scale_selection()

    if res == 13:
        answer = 2
    else:
        f = frequency_selection(res)

    while answer == 1:

        os.system('clear') # Clear screen for Linux. In Windows use 'cls' instead of 'clear'

        pygame.init()
        # sample_rate, bit_rate, channels = pygame.mixer.get_init()
        pygame.sndarray.use_arraytype('numpy')

        print "\nChoose from the options below:-"
        print "1).Ati komal & Shuddh Notes"
        print "2).Notes of your choice"
        print "3).Exit"
        selection = int(raw_input('Select:-'))

        if selection == 1:

            selection_2 = saptak_selection()

            if selection_2 >= 4 or selection_2 <= 0:
                answer = 2
            else:
                (tone_dict, ind1, ind2) = defaultNoteGeneration(f,selection_2) # Left for ADSR
                print "\nPlay!"

                handling(tone_dict, ind1, ind2)
                pygame.quit()

        elif selection == 2:

            selection_2 = saptak_selection()

            if selection_2 >= 4 or selection_2 <=0:
                answer = 2
            else:
                (tone_dict, ind1, ind2) = dynamicNoteGeneration(f,selection_2)
                print "\nPlay!"

                handling(tone_dict, ind1, ind2)
                pygame.quit()
        else:
            answer = 2

    print "\nBye!"

if __name__ == "__main__":
    main()
