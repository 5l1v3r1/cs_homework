import random

#Load 'random' library

#Print starting message
print("Welcome to Tic Tac Toe\nGame manual:\nYou play against the computer. Computer's choises are random!\nYou must give coordinates like A1 OR B3 OR C2!\nPLAY SAFE, GOOD LUCK!")

##DEFINE FUNCTIONS##
#Define portal function (check cordinates)
def portal(f, ashenone, round):
    if((round=="A1")or(round==0)):
        f[0]=ashenone[1]
        portal=True
    elif((round=="A2")or(round==1)):
        f[1]=ashenone[1]
        portal=True
    elif((round=="A3")or(round==2)):
        f[2]=ashenone[1]
        portal=True
    elif((round=="B1")or(round==3)):
        f[3]=ashenone[1]
        portal=True
    elif((round=="B2")or(round==4)):
        f[4]=ashenone[1]
        portal=True
    elif((round=="B3")or(round==5)):
        f[5]=ashenone[1]
        portal=True
    elif((round=="C1")or(round==6)):
        f[6]=ashenone[1]
        portal=True
    elif((round=="C2")or(round==7)):
        f[7]=ashenone[1]
        portal=True
    elif((round=="C3")or(round==8)):
        f[8]=ashenone[1]
        portal=True
    else:
        portal=False
    return portal

#d-and-d function for command-line graphics
def dandd(f):
    print("",f[0],"|",f[1],"|",f[2])
    print("",f[3],"|",f[4],"|",f[5])
    print("",f[6],"|",f[7],"|",f[8])

#Random generator/picker
def rdlist(f, ashenone):
    emlist=[""]
    for i in range(8):
        if(i==0):
            if((emlist[0]=="") and (f[i]=="")):
              emlist[0]=i
            elif (f[i]==""):
                emlist.append(i)

    round=(random.choice(emlist))
    portal(f, ashenone, round)

#Define check function
def check(f, ashenone1, ashenone2):
    #Check H(orizontal) lines
    for i in range(0, 8, 3):
        if((f[i]==f[i+1]) and (f[i]==f[i+2])):
            if(f[i]==ashenone1[0]):
                ashenone1[1]=ashenone1[1]+1
            else:
                ashenone2[1]=ashenone2[1]+1

    #Check V(ertical) lines
    for i in range(2):
        if((f[i]==f[i+3]) and (f[i]==f[i+6])):
            if(f[i]==ashenone1[0]):
                ashenone1[1]=ashenone1[1]+1
            else:
                ashenone2[1]=ashenone2[1]+1

    #First
    if((f[0]==f[4]) and (f[0]==f[8])):
            if(f[i]==ashenone1[0]):
                ashenone1[1]=ashenone1[1]+1
            else:
                ashenone2[1]=ashenone2[1]+1
    #Second
    if((f[2]==f[4]) and (f[2]==f[6])):
            if(f[i]==ashenone1[0]):
                ashenone1[1]=ashenone1[1]+1
            else:
                ashenone2[1]=ashenone2[1]+1

#Cells ashenone: choosen symbol & score
round="yes"
f=["","","","","","","","",""]
ans=["A1","A2","A3","B1","B2","B3","C1","C2","C3"]


flag=True
#Play again until False
while(flag):
    #Run one time/allow player to choose his character (X/0)
    flag=True
    while(flag):
        round=input("Player one symbol: [X or 0]: ")
        if((round=="X") or (round=="0")):
            ashenone1=[round, 0]
            #computer symbol
            if (round=="X"):
                ashenone2=["0", 0]
                flag=False
            else:
                ashenone2=["X", 0]
                flag=False
        else:
            round=input("Try again please.")
            flag=True

    #Main part
    flag=True
    while(flag):
        flag=True
        while(flag):
            #Check cordinates
            round=input("Please input cordinates: ")
            flag=portal(f, ashenone1, round)
            if(flag):
                flag=False
                print("ok")
            else:#Check cordinates
                print("Invalid cordinates - please try again.")
                flag=True
            print("OK!")
        #computer's move
        rdlist(f, ashenone2)
        dandd(f)
        check(f, ashenone1, ashenone2)
        if((ashenone1[1]==1)or(ashenone2[1]==1)):
            flag=False
        else:
            flag=True

    #Print score
    if(ashenone1[1]>ashenone2[1]):
        print("YOU HAVE WON!\nWell done!")
    elif(ashenone1[1]<ashenone2[1]):
        print("YOU HAVE LOST!")
    else:
        print("DRAW!")

    ans=input("Do you want to play again? [yes/no]: ")
    if(ans=="no"):
        flag=False
    else:
        flag=True
