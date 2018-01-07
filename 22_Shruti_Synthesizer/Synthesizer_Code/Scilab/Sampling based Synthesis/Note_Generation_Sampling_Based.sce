clear;
clc;

global r

r=1;

stacksize('max');

funcprot(0);

disp("Select your instrument :- ");
disp('1-Harmonium');
disp('2-Paino');
disp('3-Harp');
disp('4-Syn-Str1');
disp('5-Strings 3');
disp('6-Violin');
disp('7-Flute');
disp('8-Alto Sax');
disp('9-Str.Guitar');
disp('10-Vibration Pad');
disp('11-Brass');
disp('12-SynLead 3');
disp('13-Bandneon ');
disp('14-Acous Guitar');
disp('15-Jazz Guitar');
disp('16-Electric Guitar');
disp('17-Mute Guitar');
disp('18-Dist Guitar');
disp('19-Wood bass');
disp('20-Banjo');
disp('21-Voice Ooh');
disp('22-Syn lead 2');
disp('Choice :- ');
choice5=input('');

if choice5==1 then
    [y1,Fs,bits] = wavread("3-Harmonium.wav");
elseif choice5==2 then
    [y1,Fs,bits] = wavread("4-Paino.wav");
elseif choice5==3 then
    [y1,Fs,bits] = wavread("5-Harp.wav");
elseif choice5==4 then
    [y1,Fs,bits] = wavread("6-Syn-Str1.wav");
elseif choice5==5 then
    [y1,Fs,bits] = wavread("7-Strings 3.wav");
elseif choice5==6 then
    [y1,Fs,bits] = wavread("8-Violin.wav");
elseif choice5==7 then
    [y1,Fs,bits] = wavread("9-Flute.wav");
elseif choice5==8 then
    [y1,Fs,bits] = wavread("10-Alto Sax.wav");
elseif choice5==9 then
    [y1,Fs,bits] = wavread("11-Str.Guitar.wav");
elseif choice5==10 then
    [y1,Fs,bits] = wavread("12-Vibration Pad.wav");
elseif choice5==11 then
    [y1,Fs,bits] = wavread("13-Brass.wav");
elseif choice5==12 then
    [y1,Fs,bits] = wavread("14-SynLead 3.wav");
elseif choice5==13 then
    [y1,Fs,bits] = wavread("15-Bandneon.wav");
elseif choice5==14 then
    [y1,Fs,bits] = wavread("16-Acous Guitar.wav");
elseif choice5==15 then
    [y1,Fs,bits] = wavread("17-Jazz Guitar.wav");
elseif choice5==16 then
    [y1,Fs,bits] = wavread("18-Electric Guitar.wav");
elseif choice5==17 then
    [y1,Fs,bits] = wavread("19-Mute Guitar.wav");
elseif choice5==18 then
    [y1,Fs,bits] = wavread("20-Dist Guitar.wav");
elseif choice5==19 then
    [y1,Fs,bits] = wavread("21-Wood Bass.wav");
elseif choice5==20 then
    [y1,Fs,bits] = wavread("22-Banjo.wav");
elseif choice5==21 then
    [y1,Fs,bits] = wavread("23-Voice Ooh.wav");
else
    [y1,Fs,bits] = wavread("24-Syn Lead 2.wav");
end


//-----------------------------------------------------------------------------------------------------
function [] = sound1(y)
  
  // play signal y at sample rate "rate"
  rate=22050;
  
  //y=resize_matrix(y,)
  savewave(TMPDIR+'/_playsnd_.wav', y, rate);   //Exporting the sound file to store temporarily
  //savewave('C:/Users/cmp/Deep/Semester 4/Project/Synthesizer/Synthesizer/Samples/1/cnt.wav', y, rate);   
  //Exporting the sound file to store temporarily
  PlaySound(TMPDIR+'/_playsnd_.wav');           //The inbuilt windows function plays the sound
  
endfunction
 
//-----------------------------------------------------------------------------------
function  tone  = noteG(p,s,n)
    p1 = 1+(5.35/100); p2 = 1+(6.66/100);p3 = 1+(11.11/100);p4 = 1+(12.5/100);
    if s == 1  then                       
           p = 2*p;
    elseif s == 2 then 
           p = p;
    elseif s==3 then
           p = p/2;
    else
           p = p/4;
    end
    
//--------------------------------------------------------------------    
    select n
        case 1 then
             x1 = intdec(y1,p);    
        case 2 then
             x1 = intdec(y1,p/p1); 
        case 3 then
             x1 = intdec(y1,p/p2); 
        case 4 then
             x1 = intdec(y1,p/p3);
        case 5 then
             x1 = intdec(y1,p/p4);
        case 6 then 
             x1 = intdec(y1,p*0.843749);
        case 7 then 
             x1 = intdec(y1,p*0.83385);
        case 8 then
             x1 = intdec(y1,p*0.800008);
        case 9 then 
             x1 = intdec(y1,p*0.790124);
        case 10 then
             x1 = intdec(y1,p*0.749999);
        case 11 then
             x1 = intdec(y1,p*0.740787);
        case 12 then
             x1 = intdec(y1,p*0.711118);
        case 13 then
             x1 = intdec(y1,p*0.702332);
        case 14 then 
             x1 = intdec(y1,p*0.66667);    
        case 15 then
             x1 = intdec(y1,p*0.632811);
        case 16 then
             x1 = intdec(y1,p*0.625033);
        case 17 then 
             x1 = intdec(y1,p*0.600006);
        case 18 then 
             x1 = intdec(y1,p*0.592593);
        case 19 then
             x1 = intdec(y1,p*0.562499);
        case 20 then
             x1 = intdec(y1,p*0.55559);
        case 21 then
             x1 = intdec(y1,p*0.533339);
        case 22 then 
             x1 = intdec(y1,p*0.526749);
end     

tone = x1;

endfunction 

funcprot(0);

disp("Select from the Options Below:-");
disp("1 :- Ati Komal & Shudh");
disp("2 :- Choose Your Notes");
disp("3 :- Exit");
disp("Enter:- ");
choice=input('');

disp("Select from the Saptaks List below:-");
disp("1 :- Mandra");
disp("2 :- Madhya");
disp("3 :- Taar");
disp("4 :- Exit");
disp("Enter:- ");
choice_saptak=input('');

if choice==1 then
    
    disp("What is your Scale?");
    disp("1 :- C (Safed1)");
    disp("2 :- C# (Kali1)");
    disp("3 :- D (Safed2)");
    disp("4 :- D# (Kali2)");
    disp("5 :- E (Safed3)");
    disp("6 :- F (Safed4)");
    disp("7 :- F# (Kali3)");
    disp("8 :- G (Safed5)");
    disp("9 :- G# (Kali4)");
    disp("10 :- A (Safed6)");
    disp("11 :- A# (Kali5)");
    disp("12 :- B (Safed7)");
    disp("13 :- EXIT");
    disp("CHOICE :- ");
    key=input('');
    
        if key == 1 then
            p = 1.40274434;
          
        elseif key==2 then
            p = 1.32404935;
            
        elseif key==3 then 
            p = 1.2506815;
            
        elseif key==4 then 
            p = 1.1795712;
            
        elseif key==5 then 
            p = 1.113369535;            
        
        elseif key==6 then 
            p = 1.050883371;
        
        elseif key==7 then 
            p = 0.9919187005054;
        
        elseif key==8 then 
            p = 0.936224489795;

        elseif key==9 then 
            p = 0.883698531182;
        
        elseif key==10 then 
            p = 0.834090909090;
            
        elseif key==11 then 
            p = 0.787283336193;
            
        elseif key ==12 then  
            p = 0.74309548878270;
end
    Sa=noteG(p,choice_saptak,1); 
    ReA=noteG(p,choice_saptak,2);
    ReS=noteG(p,choice_saptak,4);
    GaA=noteG(p,choice_saptak,6);
    GaS=noteG(p,choice_saptak,8);
    MaS=noteG(p,choice_saptak,10);
    MaSh=noteG(p,choice_saptak,12);
    P=noteG(p,choice_saptak,14);
    DhA=noteG(p,choice_saptak,15);
    DhS=noteG(p,choice_saptak,17);
    NiA=noteG(p,choice_saptak,19);
    NiS=noteG(p,choice_saptak,21);
    Sa2=noteG(p,choice_saptak+1,1); 
    
function piano(win, x, y, ibut)
   if ibut == 115 & r=1 then
        sound1(Sa);
        clearglobal r
   elseif ibut == -115 then 
         global r
         r=1;   
   elseif ibut == 100 & r=1 then
        sound1(ReS);
        clearglobal r
   elseif ibut == -100 then 
         global r
         r=1;       
   elseif ibut == 102 & r=1 then
        sound1(GaS);
        clearglobal r
   elseif ibut == -102 then 
         global r
         r=1;        
   elseif ibut == 103 & r=1 then
        sound1(MaS);
        clearglobal r
   elseif ibut == -103 then
        global r
        r=1;    
   elseif ibut == 104 & r=1 then
        sound1(P); 
        clearglobal r
   elseif ibut == -104 then 
         global r
         r=1;    
   elseif ibut == 106 & r=1 then
        sound1(DhS); 
        clearglobal r
   elseif ibut == -106 then 
         global r
         r=1;    
   elseif ibut == 107 & r=1 then
        sound1(NiS); 
        clearglobal r
   elseif ibut == -107 then 
         global r
         r=1;   
   elseif ibut == 101 & r=1 then
        sound1(ReA);
       clearglobal r 
   elseif ibut == -101 then 
         global r
         r=1;  
   elseif ibut == 114 & r=1 then
        sound1(GaA);
        clearglobal r
   elseif ibut == -114 then 
         global r
         r=1;    
   elseif ibut == 117 & r=1 then
        sound1(MaSh); 
        clearglobal r
   elseif ibut == -117 then 
         global r
         r=1;    
   elseif ibut == 105 & r=1 then
        sound1(DhA);
        clearglobal r
   elseif ibut == -105 then 
         global r
         r=1;    
   elseif ibut == 111 & r=1 then
        sound1(NiA); 
        clearglobal r
    elseif ibut == -111 then 
         global r
         r=1;    
   elseif ibut == 108 & r=1 then
        sound1(Sa2);  
        clearglobal r
   elseif ibut ==-108  then
         global r
         r=1;    
   end     
   endfunction
seteventhandler('piano')
  
elseif choice==2 then
   
    disp("What is your Scale?");
    disp("1 :- C (Safed1)");
    disp("2 :- C# (Kali1)");
    disp("3 :- D (Safed2)");
    disp("4 :- D# (Kali2)");
    disp("5 :- E (Safed3)");
    disp("6 :- F (Safed4)");
    disp("7 :- F# (Kali3)");
    disp("8 :- G (Safed5)");
    disp("9 :- G# (Kali4)");
    disp("10 :- A (Safed6)");
    disp("11 :- A# (Kali5)");
    disp("12 :- B (Safed7)");
    disp("13 :- EXIT");
    disp("CHOICE :- ");
    key=input('');
    
        if key == 1 then
            p = 1.40274434;
          
        elseif key==2 then
            p = 1.32404935;
            
        elseif key==3 then 
            p = 1.2506815;
            
        elseif key==4 then 
            p = 1.1795712;
            
        elseif key==5 then 
            p = 1.113369535;            
        
        elseif key==6 then 
            p = 1.050883371;
        
        elseif key==7 then 
            p = 0.9919187005054;
        
        elseif key==8 then 
            p = 0.936224489795;

        elseif key==9 then 
            p = 0.883698531182;
        
        elseif key==10 then 
            p = 0.834090909090;
            
        elseif key==11 then 
            p = 0.787283336193;
            
        elseif key ==12 then  
            p = 0.74309548878270;
end 

    Sa=noteG(p,choice_saptak,1);
    
    disp("Choose Komal Re:-");
    disp("2 :- Ati Komal");
    disp("3 :- Komal");
    choice_1=input('');
    
    ReA=noteG(p,choice_saptak,choice_1);    //Ati komal-komal   //komal
    
    disp("Choose Shuddh Re:-");
    disp("4 :- Shudh");
    disp("5 :- Teevra");
    choice_1=input('');
    
    ReS=noteG(p,choice_saptak,choice_1);    //Shudh-Teevra      //Teevra
    
    disp("Choose Komal Ga:-");
    disp("6 :- Ati Komal");
    disp("7 :- Komal");
    choice_1=input('');
    
    GaA=noteG(p,choice_saptak,choice_1);    //Ati komal-komal
    
    disp("Choose Shuddh Ga:-");
    disp("8 :- Shudh");
    disp("9 :- Teevra");
    choice_1=input('');
    
    GaS=noteG(p,choice_saptak,choice_1);    //Shudh-Teevra
    
    disp("Choose Shuddh Ma:-");
    disp("10 :- Shudh Lower Pitch Madhyam");
    disp("11 :- Ek Shruti Madhyam ");
    choice_1=input('');
    
    MaS=noteG(p,choice_saptak,choice_1);
    
    disp("Choose Taar Ma:-");
    disp("12 :- Shudh Madhyam");
    disp("13 :- Teevra Madhyam Higher Pitch");
    choice_1=input('');
    
    MaSh=noteG(p,choice_saptak,choice_1);
    
    P=noteG(p,choice_saptak,14);
    
    disp("Choose Komal Dh:-");
    disp("15 :- Ati Komal");
    disp("16 :- Komal");
    choice_1=input('');
    
    DhA=noteG(p,choice_saptak,choice_1);   //Ati komal-komal
    
    disp("Choose Shudh Dh:-");
    disp("17 :- Shudh");
    disp("18 :- Teevra");
    choice_1=input('');
    
    DhS=noteG(p,choice_saptak,choice_1);   //Shudh-Teevra
    
    disp("Choose Komal Ni:-");
    disp("19 :- Ati Komal");
    disp("20 :- Komal");
    choice_1=input('');
    
    NiA=noteG(p,choice_saptak,choice_1);   //Ati komal-komal
    
    disp("Choose Shudh Ni:-");
    disp("21 :- Shudh");
    disp("22 :- Teevra");
    choice_1=input('');
    
    NiS=noteG(p,choice_saptak,choice_1);    //Shudh-Teevra
    
    Sa2=noteG(p,choice_saptak+1,1);
    
function piano(win, x, y, ibut)
    
    if ibut == 115 & r=1 then
        sound1(Sa);
        clearglobal r 
   elseif ibut == -115 then 
         global r
         r=1;
   elseif ibut == 100 & r=1 then
        sound1(ReS);
        clearglobal r
   elseif ibut == -100 then 
         global r
         r=1;    
   elseif ibut == 102 & r=1 then
        sound1(GaS);
        clearglobal r
   elseif ibut == -102 then 
         global r
         r=1;        
   elseif ibut == 103 & r=1 then
        sound1(MaS);
        clearglobal r
   elseif ibut == -103 then 
        global r
        r=1;    
   elseif ibut == 104 & r=1 then
        sound1(P); 
        clearglobal r
   elseif ibut == -104 then 
         global r
         r=1;    
   elseif ibut == 106 & r=1 then
        sound1(DhS); 
        clearglobal r
   elseif ibut == -106 then 
         global r
         r=1;    
   elseif ibut == 107 & r=1 then
        sound1(NiS); 
        clearglobal r
   elseif ibut == -107 then 
         global r
         r=1;    
   elseif ibut == 101 & r=1 then
        sound1(ReA);
       clearglobal r 
   elseif ibut == -101 then 
         global r
         r=1;    
   elseif ibut == 114 & r=1 then
        sound1(GaA);
        clearglobal r
   elseif ibut == -114 then 
         global r
         r=1;    
   elseif ibut == 117 & r=1 then
        sound1(MaSh); 
        clearglobal r
   elseif ibut == -117 then 
         global r
         r=1;    
   elseif ibut == 105 & r=1 then
        sound1(DhA);
        clearglobal r
   elseif ibut == -105 then 
         global r
         r=1;    
   elseif ibut == 111 & r=1 then
        sound1(NiA); 
        clearglobal r
   elseif ibut == -111 then 
         global r
         r=1;    
   elseif ibut == 108 & r=1 then
        sound1(Sa2);  
        clearglobal r
   elseif ibut ==-108  then
         global r
         r=1;    
   end       
   endfunction

seteventhandler('piano')
end 
