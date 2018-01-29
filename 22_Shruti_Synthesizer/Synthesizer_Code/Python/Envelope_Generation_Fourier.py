import numpy as np

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

    # p1 = Ati Komal
    # p2 = Komal
    # p3 = Shuddh
    # p4 = Teevra

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
        f1 = f
    elif n == 2:
        f1 = f*p1
    elif n == 3:
        f1 = f*p2
    elif n == 4:
        f1 = f*p3
    elif n == 5:
        f1 = f*p4
    elif n == 6:
        f1 = R2*p1
    elif n == 7:
        f1 = R2*p2
    elif n == 8:
        f1 = R2*p3
    elif n == 9:
        f1 = R2*p4
    elif n == 10:
        f1 = G2*p1
    elif n == 11:
        f1 = G2*p2
    elif n == 12:
        f1 = G2*p3
    elif n == 13:
        f1 = G2*p4
    elif n == 14:
        f1 = P
    elif n == 15:
        f1 = P*p1
    elif n == 16:
        f1 = P*p2
    elif n == 17:
        f1 = P*p3
    elif n == 18:
        f1 = P*p4
    elif n == 19:
        f1 = D2*p1
    elif n == 20:
        f1 = D2*p2
    elif n == 21:
        f1 = D2*p3
    elif n == 22:
        f1 = D2*p4

    if d == -1:
        d = 1000/f1    # d = -1 generates only 1000 cycle of the note
                       # Thus, now we need to loop that cycle for certain iterations to play note
                       # Use : To achieve better control over playing when key is pressed
    T = np.ceil(2*22050 * d); # Time Period

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

    t = Generate_Time_Vector(d)

    S1 = 0.004058*np.cos(2*pi*100.1*t) + 0.004058*np.sin(2*pi*100.1*t)
    S2 = 0.04351*np.cos(2*pi*f1*t) + 0.04351*np.sin(2*pi*f1*t)
    S3 = 0.03106*np.cos(2*pi*2*f1*t) + 0.03106*np.sin(2*pi*2*f1*t)
    S4 = 0.02501*np.cos(2*pi*3*f1*t) + 0.02501*np.sin(2*pi*3*f1*t)
    S5=  0.007601*np.cos(2*pi*4*f1*t) + 0.007601*np.sin(2*pi*4*f1*t)
    S6 = 0.03025*np.cos(2*pi*5*f1*t) + 0.03025*np.sin(2*pi*5*f1*t)
    S7 = 0.009108*np.cos(2*pi*6*f1*t) + 0.009108*np.sin(2*pi*6*f1*t)
    S8 = 0.0162*np.cos(2*pi*7*f1*t) + 0.0162*np.sin(2*pi*7*f1*t)
    S9 = 0.01177*np.cos(2*pi*8*f1*t) + 0.01177*np.sin(2*pi*8*f1*t)
    S10 = 0.008996*np.cos(2*pi*9*f1*t) + 0.008996*np.sin(2*pi*9*f1*t)
    S11 = 0.01075*np.cos(2*pi*10*f1*t) + 0.01075*np.sin(2*pi*10*f1*t)
    S12 = 0.01091*np.cos(2*pi*11*f1*t) + 0.01091*np.sin(2*pi*11*f1*t)
    S13 = 0.002159*np.cos(2*pi*12*f1*t) + 0.002159*np.sin(2*pi*12*f1*t)
    S14 = 0.002081*np.cos(2*pi*13*f1*t) + 0.002081*np.sin(2*pi*13*f1*t)
    S15 = 0.001304*np.cos(2*pi*14*f1*t) + 0.001304*np.sin(2*pi*14*f1*t)

    final_tone = S1 + S2 + S3 + S4 + S5 + S6 + S7 + S8 + S9 + S10 + S11 + S12 + S13 + S14 + S15

    if len(final_tone)<len(a):
       a = a[0:len(final_tone)]

    final_tone = np.multiply(final_tone,a)

    final_tone = max_sample*final_tone # Normalizing for converting int16 from float 32 in future

    f = open('temp.txt', 'w')
    f.write(str(ind1)+'\n')
    f.write(str(ind2))
    f.close()

    return final_tone
