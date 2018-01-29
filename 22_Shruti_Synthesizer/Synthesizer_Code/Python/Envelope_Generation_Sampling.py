# ##########################################################################
#
# scikit.audiolab installation Instruction :
#
# 1). sudo apt-get install python-dev python-numpy python-setuptools libsndfile-dev
# 2). sudo apt-get install libasound2-dev      # ALSA Header (Optional)
# 3). sudo pip install scikits.audiolab
# Homepage and Documentation : 1). http://cournape.github.io/audiolab/
#                              2). http://scikits.appspot.com/audiolab
#
############################################################################
#
# scikit.samplerate installation Instruction :
# Link : https://stackoverflow.com/a/38929336/4802474
#
# You first need to install the SRC library:
#
# sudo apt-get install libsamplerate0 libsamplerate0-dev
# This python package will probably be the most tricky to install. If you are lucky, you can just
#
# pip install scikits.samplerate
# On my Ubuntu 12.04, this results in an error because the SRC library path is not found. The reason is that the setup searches SRC in /usr/lib and not in /usr/lib/x86_64-linux-gnu where the library is actually present. To install, you need to download the archive from pypi and edit some configuration file:
#
# wget https://pypi.python.org/packages/source/s/scikits.samplerate/scikits.samplerate-0.3.3.tar.gz#md5=96c8d8ba3aa95a9db15994f78792efb4
# tar -xvf scikits.samplerate-0.3.3.tar.gz
# cd scikits.samplerate-0.3.3
# then edit the site.cfg example file and insert the following lines:
#
# [samplerate]
# library_dirs=/usr/lib/x86_64-linux-gnu
# include_dirs=/usr/include
# To know where the SRC library is on you machine:
#
# sudo dpkg -L libsamplerate0
# sudo dpkg -L libsamplerate0-dev
# then, build and install:
#
# python setup.py build
# python setup.py install
#
############################################################################

import numpy as np
from scikits.samplerate import resample
from scikits.audiolab import wavread


pi = 3.141592
bits = 16
max_sample = 2**(bits - 1) - 1

def Generate_Linespace(x1,x2,t):

    ln = np.linspace(x1, x2, t)

    return ln

def Generate_Time_Vector(t):

   ln = np.linspace(0, t, 2*22050*t)

   return ln


# f = Base Frequency
# s = Saptak
# n = Shruti from total 22 Shrutis
# d = Note Duration

def Generate_Sound(f,s,n,d):

    wav = "C4_Sa_Harmonium.wav"
    data, fs, enc = wavread(wav)

    # p1 = Ati Komal
    # p2 = Komal
    # p3 = Shuddh
    # p4 = Teevra

    bf = 261.2  # Base frequency of Note Sample

    p1 = 1+(5.35/100)
    p2 = 1+(6.66/100)
    p3 = 1+(11.11/100)
    p4 = 1+(12.5/100)

    # Saptak Selection
    if s==0:
        f = f/4 # Super Mandra

    elif s==1:
        f = f/2 # Mandra

    elif s==2:
        f = f   # Madhayam

    elif s==3:
        f = 2*f # Taar

    else:
        f = 4*f # Super Taar

    R2 = f*p4
    G2 = R2*p4
    P = 1.5*f
    D2 = P*p4

    # Note/Shrutis Selection

    if n == 1:
        f1 = f     # Sa                     - 1
    elif n == 2:
        f1 = f*p1  # Ati-Komal              - 2
    elif n == 3:
        f1 = f*p2  # Komal                  - 3
    elif n == 4:
        f1 = f*p3  # Shuddh Rishabha        - 4
    elif n == 5:
        f1 = f*p4  # Teevra Rishabha        - 5
    elif n == 6:
        f1 = R2*p1 # Ati-Komal Gandhar      - 6
    elif n == 7:
        f1 = R2*p2 # Komal Gandhar          - 7
    elif n == 8:
        f1 = R2*p3 # Shuddh Gandhar         - 8
    elif n == 9:
        f1 = R2*p4 # Teevra Gandhar         - 9
    elif n == 10:
        f1 = G2*p1 # Shuddh Madhyam         - 10
    elif n == 11:
        f1 = G2*p2 # Ek-Shruti Madhyam      - 11
    elif n == 12:
        f1 = G2*p3 # Teevra Madhyam         - 12
    elif n == 13:
        f1 = G2*p4 # Teevratama Madhyam     - 13
    elif n == 14:
        f1 = P     # Pancham                - 14
    elif n == 15:
        f1 = P*p1  # Ati-Komal Dhaivat      - 15
    elif n == 16:
        f1 = P*p2  # Komal Dhaivat          - 16
    elif n == 17:
        f1 = P*p3  # Shuddh Dhaivat         - 17
    elif n == 18:
        f1 = P*p4  # Teevra Dhaivat         - 18
    elif n == 19:
        f1 = D2*p1 # Ati-Komal Nishad       - 19
    elif n == 20:
        f1 = D2*p2 # Komal Nishad           - 20
    elif n == 21:
        f1 = D2*p3 # Shuddh Nishad          - 21
    elif n == 22:
        f1 = D2*p4 # Teevra Nishad          - 22

    resample_fraction = bf/f1

    if d == -1:
        d = 1000/f1    # d = -1 generates only 1000 cycle of the note
                       # Thus, now we need to loop that cycle for certain iterations to play note
                       # Use : To achieve better control over playing when key is pressed
    T = np.ceil(2*22050 * d); # Time Period

    final_tone = resample(data[:,0], resample_fraction, "sinc_fastest")

    final_tone = final_tone[0:int(T)]

    T1 = np.ceil(0.26 * T); # for linspace - Attack
    T2 = np.ceil(0.10 * T); # for linspace - Decay
    T3 = np.ceil(0.52 * T); # for linspace - Sustain
    T4 = np.ceil(0.12 * T); # for linspace - Release

    L1 = Generate_Linespace(0,0.80,T1)
    L2 = Generate_Linespace(0.80,0.80,T2)
    L3 = Generate_Linespace(0.80,0.80,T3)
    L4 = Generate_Linespace(0.80,0,T4)

    a = np.concatenate([L1, L2, L3, L4])
    ind1 = len(L1) + len(L2)  # Staring Index for Sustain part
    ind2  = len(L1) + len(L2) + len(L3)  # Starting Index for Release part

    if T>len(a):    # Appending zeros to a if necessary
        a = np.concatenate([a,np.zeros(T-len(a))])

    if len(final_tone)<len(a):
       a = a[0:len(final_tone)]

    final_tone = np.multiply(final_tone,a)

    final_tone = max_sample*final_tone # Normalizing for converting int16 from float 32 in future

    f = open('temp.txt', 'w')
    f.write(str(ind1)+'\n')
    f.write(str(ind2))
    f.close()

    return final_tone
