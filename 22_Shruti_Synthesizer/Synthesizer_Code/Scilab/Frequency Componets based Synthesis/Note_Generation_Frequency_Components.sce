clear;
clc;
global r
r=1;
funcprot(0);

function [] = sound1(y)
  
  // play signal y at sample rate "rate"
  rate=22050;
  
  //y=resize_matrix(y,)
  savewave(TMPDIR+'/_playsnd_.wav', y, rate);   //Exporting the sound1 file to store temporarily
  //savewave("C:/Users/cmp/Deep/Semester 4/Project/Synthesizer/Testing/Synthetic Harmonium.wav", y, rate);   //Exporting the sound1 file to store temporarily
  PlaySound(TMPDIR+'/_playsnd_.wav');           //The inbuilt windows function plays the sound1
  
endfunction

function  tone  = noteG(f,s,n,d)
    //s denotes saptak (1,2,3)
    //n denotes the shruti and ranges from 1 to 22
    //f denotes the frecuency 
    //p1=ati komal
    //p2=komal
    //p3=shuddh
    //p4=teevra
    p1 = 1+(5.35/100); p2 = 1+(6.66/100);p3 = 1+(11.11/100);p4 = 1+(12.5/100);
    if s == 1  then                        
            f = f/2
        
    elseif s == 2 then 
            f = f;
            
    elseif s==3 then 
            f = 2*f;
            
    elseif s==4 then 
            f= 4*f;    
    end
    
    R2 = f*p4; G2 = R2*p4; P = 1.5*f ; D2 = P*p4;
    
    select n
        case 1 then
            f1 = f;      
        case 2 then
            f1 = f*p1;   
        case 3 then
            f1 = f*p2;   
        case 4 then
            f1 = f*p3;   
        case 5 then
            f1 = f*p4;  
        case 6 then 
            f1 = R2*p1;  
        case 7 then 
            f1 = R2*p2;
        case 8 then
            f1 = R2*p3;
        case 9 then 
            f1 = R2*p4;
        case 10 then
            f1 = G2*p1;
        case 11 then
            f1 = G2*p2;
        case 12 then
            f1 = G2*p3;
        case 13 then
            f1 = G2*p4;
        case 14 then 
            f1 = P;      
        case 15 then
            f1 = P*p1;
        case 16 then
            f1 = P*p2;
        case 17 then 
            f1 = P*p3;
        case 18 then 
            f1 = P*p4;
        case 19 then
            f1 = D2*p1;
        case 20 then
            f1 = D2*p2;
        case 21 then
            f1 = D2*p3;
        case 22 then 
            f1 = D2*p4;
    end   
    
t=soundsec(4);


T = length(t);
T1 = round(0.02*T);
T2 = round(0.26*T);
T3 =  round(0.08*T);
L1 = linspace(0,1,T1);
L2 = linspace(1,0.7,T2);
L3 = linspace(0.7,0.7,T2);
L4 = linspace(0.7,0,T3);
//L5 = linspace(0.45,0,T1);
a = [L1 L2 L3 L4];
A = length(a);
if T > A then
    diff = T-A;
    for i = 1:diff
        a = [a 0];
    end
    
elseif T < A then
        diff = A-T;
        for i = 1:diff
            t = {t 0};
        end        
end

S1 = 0.004058*cos(2*%pi*100.1*t)+0.004058*sin(2*%pi*100.1*t);
S2 = 0.04351*cos(2*%pi*f1*t)+0.04351*sin(2*%pi*f1*t);
S3 = 0.03106*cos(2*%pi*2*f1*t)+0.03106*sin(2*%pi*2*f1*t);
S4 = 0.02501*cos(2*%pi*3*f1*t)+0.02501*sin(2*%pi*3*f1*t);
S5 = 0.007601*cos(2*%pi*4*f1*t)+0.007601*sin(2*%pi*4*f1*t);
S6 = 0.03025*cos(2*%pi*5*f1*t)+0.03025*sin(2*%pi*5*f1*t);
S7 = 0.009108*cos(2*%pi*6*f1*t)+0.009108*sin(2*%pi*6*f1*t);
S8 = 0.0162*cos(2*%pi*7*f1*t)+0.0162*sin(2*%pi*7*f1*t);
S9 = 0.01177*cos(2*%pi*8*f1*t)+0.01177*sin(2*%pi*8*f1*t);
S10 = 0.008996*cos(2*%pi*9*f1*t)+0.008996*sin(2*%pi*9*f1*t);
S11 = 0.01075*cos(2*%pi*10*f1*t)+0.01075*sin(2*%pi*10*f1*t);
S12 = 0.01091*cos(2*%pi*11*f1*t)+0.01091*sin(2*%pi*11*f1*t);
S13 = 0.002159*cos(2*%pi*12*f1*t)+0.01091*sin(2*%pi*12*f1*t);
S14 = 0.002081*cos(2*%pi*13*f1*t)+0.01091*sin(2*%pi*13*f1*t);
S15 = 0.001304*cos(2*%pi*14*f1*t)+0.01091*sin(2*%pi*14*f1*t);
snd=S2+S3+S4+S5+S6+S7+S8+S9+S10+S11+S12+S13+S14+S15;

tone = a.*snd;

//n = length(tone);
//disp(n);
//t=1:1:n;

//plot(t,tone);
    
endfunction 

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
    d1=2.17;
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
            f=261.63;
          
        elseif key==2 then
            f=277.18;
            
        elseif key==3 then 
            f=293.44;
            
        elseif key==4 then 
            f=311.13;
            
        elseif key==5 then 
            f=329.63;            
        
        elseif key==6 then 
            f=349.23;
        
        elseif key==7 then 
            f=369.99;
        
        elseif key==8 then 
            f=392.00;
        
        elseif key==9 then 
            f=415.30;
        
        elseif key==10 then 
            f=440.00;
            
        elseif key==11 then 
            f=466.16;
            
        elseif key ==12 then  
            f=493.88;
end
    Sa=noteG(f,choice_saptak,1,d1);
    ReA=noteG(f,choice_saptak,2,d1);
    ReS=noteG(f,choice_saptak,4,d1);
    GaA=noteG(f,choice_saptak,6,d1);
    GaS=noteG(f,choice_saptak,8,d1);
    MaS=noteG(f,choice_saptak,10,d1);
    MaSh=noteG(f,choice_saptak,12,d1);
    P=noteG(f,choice_saptak,14,d1);
    DhA=noteG(f,choice_saptak,15,d1);
    DhS=noteG(f,choice_saptak,17,d1);
    NiA=noteG(f,choice_saptak,19,d1);
    NiS=noteG(f,choice_saptak,21,d1);
    Sa2=noteG(f,choice_saptak+1,1,d1);
    
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
    
    d1=2.17;
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
            f=261.63;
          
        elseif key==2 then
            f=277.18;
            
        elseif key==3 then 
            f=293.44;
            
        elseif key==4 then 
            f=311.13;
            
        elseif key==5 then 
            f=329.63;            
        
        elseif key==6 then 
            f=349.23;
        
        elseif key==7 then 
            f=369.99;
        
        elseif key==8 then 
            f=392.00;
        
        elseif key==9 then 
            f=415.30;
        
        elseif key==10 then 
            f=440.00;
            
        elseif key==11 then 
            f=466.16;
            
        elseif key ==12 then  
            f=493.88;
end 

    Sa=noteG(f,choice_saptak,1,d1);
    
    disp("Choose Komal Re:-");
    disp("2 :- Ati Komal");
    disp("3 :- Komal");
    choice_1=input('');
    
    ReA=noteG(f,choice_saptak,choice_1,d1);    //Ati komal-komal   //komal
    
    disp("Choose Shuddh Re:-");
    disp("4 :- Shudh");
    disp("5 :- Teevra");
    choice_1=input('');
    
    ReS=noteG(f,choice_saptak,choice_1,d1);    //Shudh-Teevra      //Teevra
    
    disp("Choose Komal Ga:-");
    disp("6 :- Ati Komal");
    disp("7 :- Komal");
    choice_1=input('');
    
    GaA=noteG(f,choice_saptak,choice_1,d1);    //Ati komal-komal
    
    disp("Choose Shuddh Ga:-");
    disp("8 :- Shudh");
    disp("9 :- Teevra");
    choice_1=input('');
    
    GaS=noteG(f,choice_saptak,choice_1,d1);    //Shudh-Teevra
    
    disp("Choose Shuddh Ma:-");
    disp("10 :- Shudh Lower Pitch Madhyam");
    disp("11 :- Ek Shruti Madhyam ");
    choice_1=input('');
    
    MaS=noteG(f,choice_saptak,choice_1,d1);
    
    disp("Choose Taar Ma:-");
    disp("12 :- Shudh Madhyam");
    disp("13 :- Teevra Madhyam Higher Pitch");
    choice_1=input('');
    
    MaSh=noteG(f,choice_saptak,choice_1,d1);
    
    P=noteG(f,choice_saptak,14,d1);
    
    disp("Choose Komal Dh:-");
    disp("15 :- Ati Komal");
    disp("16 :- Komal");
    choice_1=input('');
    
    DhA=noteG(f,choice_saptak,choice_1,d1);   //Ati komal-komal
    
    disp("Choose Shudh Dh:-");
    disp("17 :- Shudh");
    disp("18 :- Teevra");
    choice_1=input('');
    
    DhS=noteG(f,choice_saptak,choice_1,d1);   //Shudh-Teevra
    
    disp("Choose Komal Ni:-");
    disp("19 :- Ati Komal");
    disp("20 :- Komal");
    choice_1=input('');
    
    NiA=noteG(f,choice_saptak,choice_1,d1);   //Ati komal-komal
    
    disp("Choose Shudh Ni:-");
    disp("21 :- Shudh");
    disp("22 :- Teevra");
    choice_1=input('');
    
    NiS=noteG(f,choice_saptak,choice_1,d1);    //Shudh-Teevra
    
    Sa2=noteG(f,choice_saptak+1,1,d1);
    
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

