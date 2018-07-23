# pyGame installation Instruction :
#
# 1). Install pyGame by running - "sudo pip install pygame"
#
#
# Homepage and Documentation : 1). http://www.pygame.org/docs/
#                              2). http://www.pygame.org
#
# Example:- Find examples in this directory in this PC

import numpy as np
import time
import pygame
from pygame.locals import *
import mido
import mido.backends.rtmidi

class Handler():

    def __init__(self):

        self.sample_rate = 44100
        self.bit_rate = -16
        self.channels = 1
        self.buff = 512
        self.frequency = 261.626    # Stores Base Frequency of the Scale. Default is C (261.626 Hz)
        self.ab = {}                # Dictionary that stores the tone waveform
        self.ind1 = {}              # Dictionary that stores index of Sustain part
        self.ind2 = {}              # Dictionary that stores index of Decay part
        self.NUM_SEC = -1           # NUM_SEC = -1 generates only 1000 cycle of the note OR NUM_SEC = t generates t seconds of note
        self.scale = 1 

        pygame.mixer.pre_init(self.sample_rate, self.bit_rate, self.channels, self.buff)
        pygame.sndarray.use_arraytype('numpy')

    def play_maxtime(self, sound, lo):
        sound.play(loops=lo)

    def check_midi_connection(self):  # Checks whether MIDI keyboard is connected. Returns 0 if connected
        while True:
            if len(mido.get_input_names()) == 2:
                return 0

    def frequency_selection(self): # Frequencies are in Hz

        f = 261.626             # Default

        if self.scale==1:
            f=261.626
        elif self.scale==2:
            f=277.183
        elif self.scale==3:
            f=293.665
        elif self.scale==4:
            f=311.127
        elif self.scale==5:
            f=329.628
        elif self.scale==6:
            f=349.228
        elif self.scale==7:
            f=369.994
        elif self.scale==8:
            f=391.995
        elif self.scale==9:
            f=415.305
        elif self.scale==10:
            f=440.00
        elif self.scale==11:
            f=466.164
        elif self.scale==12:
            f=493.883
        
        self.frequency = f  # Setting Frequency of the Scale

    def defaultNoteGeneration(self, env):

        Saptak = 0          # Super Mandra Saptak
        counter = 0

        while Saptak != 4:

            self.ab[counter] = [env.Generate_Sound_Western(self.frequency,Saptak,counter%12,self.NUM_SEC)]
            f = open('temp.txt','r')
            self.ind1[counter] = int(f.next())
            self.ind2[counter] = int(f.next())
            f.close()

            counter = counter + 1

            if counter%12 == 0:
                Saptak  = Saptak + 1
        
        # Mapping externally the last Sa of last Octave     
        
        self.ab[counter] = [env.Generate_Sound_Western(self.frequency,Saptak,counter%12,self.NUM_SEC)]
        f = open('temp.txt','r')
        self.ind1[counter] = int(f.next())
        self.ind2[counter] = int(f.next())
        f.close()

    def dynamicNoteGeneration(self, env, opt_str):

        Saptak = 0 # Super Mandra Saptak
        mp = opt_str

        counter = 0

        while Saptak != 4:

            # print str(counter) + "," + str(mp[(counter)%12]) + "," + str(counter%12) + "," + str(Saptak)

            self.ab[counter] = [env.Generate_Sound(self.frequency,Saptak,mp[counter%12],self.NUM_SEC)]
            f = open('temp.txt','r')
            self.ind1[counter] = int(f.next())
            self.ind2[counter] = int(f.next())
            f.close()

            counter = counter + 1

            if counter%12 == 0:
                Saptak  = Saptak + 1
        
        # Mapping externally the last Sa of last Octave     
        
        self.ab[counter] = [env.Generate_Sound(self.frequency,Saptak,mp[counter%12],self.NUM_SEC)]
        f = open('temp.txt','r')
        self.ind1[counter] = int(f.next())
        self.ind2[counter] = int(f.next())
        f.close()

    def ringing(self, key): # Returns 3 parts of wave in form of Attack-Decay, Sustain and Release
        wave = np.array(self.ab[key])
        wave = wave[0,:]

        wave = np.array(wave,"int16")

        ad = wave[0:self.ind1[key]]
        sust = wave[self.ind1[key]:self.ind2[key]]
        rel = wave[self.ind2[key] + 1:len(wave)]

        ad = pygame.sndarray.make_sound(ad) # Attack-Decay
        sust = pygame.sndarray.make_sound(sust) # Sustain
        rel = pygame.sndarray.make_sound(rel) # Release

        return (ad, sust, rel)

    def handling(self):
        
        tones = {}
        ret = {}      # Storing Keyboard keys. Dictionary lookup is faster than subtraction operation, thus making this dictionary
        base_key = 36 # Mandra Saptak Sa key on MIDI Keyboard value

        pygame.init()

        # Initializing Tone dictionary
        for i in range(len(self.ab)):
            tones[i] = {}
            (tones[i][0], tones[i][1], tones[i][2]) = self.ringing(i)
            ret[str(base_key + i)] = i

        def input(tones, ret):
            try:
                timeout = time.time() + 1
                _,out = mido.get_input_names()
                with mido.open_input(str(out)) as port:
                    while True:                         # Flush out junk message from MIDI Interface
                        msg = port.receive(block=False)
                        if time.time() > timeout:
                            break
                    for message in port:
                        msg = str(message)
                        if msg[6] == 'n':
                            self.play_maxtime(tones[ret[msg[23:25]]][1], -1)  # Sustain Part
                        elif msg[6] == 'f':
                            tones[ret[msg[24:26]]][1].stop() # Stop Play loop
            except Exception as e:
                print "\nWrong Key or MIDI Keyboard not connected... Try Again!"
                print e
                return 0
        
        while True:
            ret = input(tones, ret)
            pygame.quit()
            return 0