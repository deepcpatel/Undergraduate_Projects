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

def defaultNoteGeneration():

    Frequency = 261.3   # Frequency of Middle C (C4) / Safed 1
    Saptak = 0          # Super Mandra Saptak

    NUM_SEC = -1        # NUM_SEC = -1 generates only 1000 cycle of the note OR NUM_SEC = t generates t seconds of note
    ab = {}
    ind1 = {}
    ind2 = {}
    mp = {}

    counter = 0

    mp[0] = 1
    mp[1] = 3
    mp[2] = 4
    mp[3] = 7
    mp[4] = 8
    mp[5] = 10
    mp[6] = 12
    mp[7] = 14
    mp[8] = 16
    mp[9] = 17
    mp[10] = 20
    mp[11] = 21

    while Saptak != 4:

        # print str(counter) + "," + str(mp[(counter)%12]) + "," + str(counter%12) + "," + str(Saptak)

        ab[counter] = [env.Generate_Sound(Frequency,Saptak,mp[counter%12],NUM_SEC)]
        f = open('temp.txt','r')
        ind1[counter] = int(f.next())
        ind2[counter] = int(f.next())
        f.close()

        counter = counter + 1

        if counter%12 == 0:
            Saptak  = Saptak + 1
    
    # Mapping externally the last Sa of last Octave     
    
    ab[counter] = [env.Generate_Sound(Frequency,Saptak,mp[counter%12],NUM_SEC)]
    f = open('temp.txt','r')
    ind1[counter] = int(f.next())
    ind2[counter] = int(f.next())
    f.close()

    return (ab, ind1, ind2)

def dynamicNoteGeneration():

    Frequency = 261.63 # Frequency of Middle C (C4) / Safed 1
    Saptak = 0 # Super Mandra Saptak

    NUM_SEC = -1  # NUM_SEC = -1 generates only 1000 cycle of the note OR NUM_SEC = t generates t seconds of note
    ab = {}
    ind1 = {}
    ind2 = {}
    mp = {}

    counter = 0

    # --------------------------Sa--------------------------------

    mp[0] = 1

    # --------------------------ReA-------------------------------

    print "\nChoose Komal Re:-"
    print "1).Ati Komal"
    print "2).Komal"
    selection = int(raw_input('Select:-'))

    mp[1] = 1+selection

    #---------------------------ReS--------------------------------

    print "\nChoose Shuddh Re:-"
    print "1).Shuddh"
    print "2).Teevra"
    selection = int(raw_input('Select:-'))

    mp[2] = 3+selection

    #-----------------------------GaA---------------------------------

    print "\nChoose Komal Ga:-"
    print "1).Ati Komal"
    print "2).Komal"
    selection = int(raw_input('Select:-'))

    mp[3] = 5+selection

    #-----------------------------GaS----------------------------------

    print "\nChoose Shuddh Ga:-"
    print "1).Shuddh"
    print "2).Teevra"
    selection = int(raw_input('Select:-'))

    mp[4] = 7+selection

    #-----------------------------MaS----------------------------------

    print "\nChoose Shuddh Ma:-"
    print "1).Shuddh Madhyam"
    print "2).Ek Shruti Madhyam"
    selection = int(raw_input('Select:-'))

    mp[5] = 9+selection

    #-----------------------------MaSh----------------------------------

    print "\nChoose Taar Ma:-"
    print "1).Teevra Madhyam"
    print "2).Teevratama Madhyam"
    selection = int(raw_input('Select:-'))

    mp[6] = 11+selection

    #------------------------------P-----------------------------------

    mp[7] = 14

    #-----------------------------DhA-----------------------------------

    print "\nChoose Komal Dh:-"
    print "1).Ati Komal"
    print "2).Komal"
    selection = int(raw_input('Select:-'))

    mp[8] = 14+selection

    #------------------------------DhS-----------------------------------

    print "\nChoose Shuddh Dh:-"
    print "1).Shuddh"
    print "2).Teevra"
    selection = int(raw_input('Select:-'))

    mp[9] = 16+selection

    #------------------------------NiA-----------------------------------

    print "\nChoose Komal Ni:-"
    print "1).Ati Komal"
    print "2).Komal"
    selection = int(raw_input('Select:-'))

    mp[10] = 18+selection

    #------------------------------NiS-----------------------------------

    print "\nChoose Shuddh Ni:-"
    print "1).Shuddh"
    print "2).Teevra"
    selection = int(raw_input('Select:-'))

    mp[11] = 20+selection

    while Saptak != 4:

        # print str(counter) + "," + str(mp[(counter)%12]) + "," + str(counter%12) + "," + str(Saptak)

        ab[counter] = [env.Generate_Sound(Frequency,Saptak,mp[counter%12],NUM_SEC)]
        f = open('temp.txt','r')
        ind1[counter] = int(f.next())
        ind2[counter] = int(f.next())
        f.close()

        counter = counter + 1

        if counter%12 == 0:
            Saptak  = Saptak + 1
    
    # Mapping externally the last Sa of last Octave     
    
    ab[counter] = [env.Generate_Sound(Frequency,Saptak,mp[counter%12],NUM_SEC)]
    f = open('temp.txt','r')
    ind1[counter] = int(f.next())
    ind2[counter] = int(f.next())
    f.close()

    return (ab, ind1, ind2)

'''
def saptak_selection():

    print "\nSelect your Saptak/Octave:-"
    print "1).Mandra"
    print "2).Madhya"
    print "3).Taar"
    print "4).Exit"
    selection = int(raw_input('Select:-'))

    return selection
'''
'''
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
'''
'''
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
'''

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
    # mapping = {} # Doing mapping for Recording in the file
    ret = {}
    base_key = 36 # Mandra Saptak Sa key on MIDI Keyboard value
    
    '''
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
    '''

    # Creating Directory and file for Recording

    # if not os.path.exists('Record'):
    #    os.makedirs('Record')

    # timestamp = "{:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now())

    # f = open('Record/Record_' + timestamp + '.txt', 'w')

    # Initializing Tone dictionary
    for i in range(len(tone_dict)):
        tones[i] = {}
        (tones[i][0], tones[i][1], tones[i][2]) = ringing(tone_dict, ind1, ind2, i)


    for i in range(len(tone_dict)):  
        ret[str(base_key + i)] = i # S

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
            with mido.open_input('Samson Carbon49:Samson Carbon49 MIDI 1 24:0') as port: # 'VMPK Output:VMPK Output 128:0' , 'Samson Carbon49:Samson Carbon49 MIDI 1 24:0', 'VMPK Output:VMPK Output 129:0'

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

    sample_rate, bit_rate, channels, buff = 2*22050, -16, 1, 512
    pygame.mixer.pre_init(sample_rate, bit_rate, channels, buff)

    os.system('clear') # Clear screen for Linux. In Windows use 'cls' instead of 'clear'

    print "------------------------------------------------------"
    print "-------Welcome to 22 Shruti Synthesizer Program-------"
    print "------------------------------------------------------"
    
    '''
    res = scale_selection()

    if res == 13:
        answer = 2
    else:
        f = frequency_selection(res)
    '''
    
    while answer == 1:

        os.system('clear') # Clear screen for Linux. In Windows use 'cls' instead of 'clear'

        pygame.init()
        # sample_rate, bit_rate, channels = pygame.mixer.get_init()
        pygame.sndarray.use_arraytype('numpy')

        print "\nChoose from the options below:-"
        print "1).Western Scale"
        print "2).Notes of your choice"
        print "3).Exit"
        selection = int(raw_input('Select:-'))

        if selection == 1:

            (tone_dict, ind1, ind2) = defaultNoteGeneration()
            os.system('clear')
            print "\nPlay!"
            
            handling(tone_dict, ind1, ind2)
            pygame.quit()

        elif selection == 2:
            
            (tone_dict, ind1, ind2) = dynamicNoteGeneration()
            os.system('clear')
            print "\nPlay!"

            handling(tone_dict, ind1, ind2)
            pygame.quit()

        else:
            answer = 2

    print "\nBye!"

if __name__ == "__main__":
    main()
