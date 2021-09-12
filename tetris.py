import random
import time
import os
import keyboard
#AREJ KOJI NAM DRZI TETROMINOSE
piece_dict={
    "T":[[["*","0","*","*"],
         ["0","0","0","*"],
         ["*","*","*","*"],
         ["*","*","*","*"]],
        [["*","*","0","*"],
         ["*","*","0","0"],
         ["*","*","0","*"],
         ["*","*","*","*"]],
        [["*","*","*","*"],
         ["*","*","*","*"],
         ["*","0","0","0"],
         ["*","*","0","*"]],
        [["*","*","*","*"],
         ["*","0","*","*"],
         ["0","0","*","*"],
         ["*","0","*","*"]]]
}

#print(piece_dict["T"])

#AREJ KOJI DRZI "IMENA" TETROMINOSA

pieces=list(piece_dict.keys())
#print(pieces)




#AREJ KOJI DRZI TABLU
table=[["#","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","#"],
       ["#","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","#"],
       ["#","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","#"],
       ["#","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","#"],
       ["#","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","#"],
       ["#","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","#"],
       ["#","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","#"],
       ["#","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","#"],
       ["#","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","#"],
       ["#","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","#"],
       ["#","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","#"],
       ["#","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","#"],
       ["#","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","#"],
       ["#","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","#"],
       ["#","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","#"],
       ["#","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","#"],
       ["#","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","#"],
       ["#","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","#"],
       ["#","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","#"],
       ["#","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","#"],
       ["#","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","#"],
       ["#","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","#"],
       ["#","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","#"],
       ["#","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","#"],
       ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]]



#FUNKCIJA KOJA CE PRINTATI TABLU
def print_table(table):
    for y in range(len(table)):
        for x in range(len(table[0])):
            print(table[y][x],end="")
        print()

#print_table(table)

#FUNKCIJA KOJA CE BIRATI TETROMINO
def choose_piece(pieces):
    return "T"

#FUNKCIJA KOJA CE BIRATI ROTACIJU
def choose_rotation(pieces,piece,rot_index):
    t=pieces[piece]
    return t[rot_index]

#FUNKCIJA KOJA CE PROVJERAVATI DA LI MOZEMO DOLE
def check_down(table,piece,origin):
    for i in range(4):
        for k in range(4):
            if piece[i][k]=="0":
                if table[origin[0]+i+1][origin[1]+k]=="@" or table[origin[0]+i+1][origin[1]+k]=="#":
                    return False
    return True



#FUNKCIJA KOJA CE NAS POMJERATI DOLE
def move_down(table,piece,origin):
    if check_down(table,piece,origin):
        origin[0]+=1
        switch=False
        t=[]
        for i in range(4):
            for k in range(4):
                if piece[i][k]=="0":
                    t.append([origin[0]+i,origin[1]+k])
                    table[origin[0]+i-1][origin[1]+k]="*"
        for i in t:
            table[i[0]][i[1]]="0"
    else:
        for i in range(4):
            for k in range(4):
                if piece[i][k]=="0":
                    table[origin[0]+i][origin[1]+k]="@"
        switch=True
    return [table,switch]



#FUNKCIJA KOJA CE PROVJERAVATI DA LI SMO IZGUBILI
def check_lost(table,origin):
    for i in table[0]:
        if i=="@":
            return True
    return False



#FUNKCIJA ZA POMJERANJE DESNO
def check_right(table,piece,origin):
    for i in range(4):
        for k in range(4):
            if piece[i][k]=="0":
                if table[origin[0]+i][origin[1]+k+1]=="@" or table[origin[0]+i][origin[1]+k+1]=="#":
                    return False
    return True



#FUNKCIJA KOJA CE NAS POMJERATI DESNO
def move_right(table,piece,origin):
    if check_right(table,piece,origin):
        origin[1]+=1
        t=[]
        for i in range(4):
            for k in range(4):
                if piece[i][k]=="0":
                    t.append([origin[0]+i,origin[1]+k])
                    table[origin[0]+i][origin[1]+k-1]="*"
        for i in t:
            table[i[0]][i[1]]="0"
    return table



#FUNKCIJA ZA POMJERANJE LIJEVO
def check_left(table,piece,origin):
    for i in range(4):
        for k in range(4):
            if piece[i][k]=="0":
                if table[origin[0]+i][origin[1]+k-1]=="@" or table[origin[0]+i][origin[1]+k-1]=="#":
                    return False
    return True



#FUNKCIJA KOJA CE NAS POMJERATI LIJEVO
def move_left(table,piece,origin):
    if check_left(table,piece,origin):
        origin[1]-=1
        t=[]
        for i in range(4):
            for k in range(4):
                if piece[i][k]=="0":
                    t.append([origin[0]+i,origin[1]+k])
                    table[origin[0]+i][origin[1]+k+1]="*"
        for i in t:
            table[i[0]][i[1]]="0"
    return table


#FUNKCIJA KOJA CE U STVARI PREDSTAVLJATI GLAVNI LOOP IGRE
def game(table,pieces):
    curr_origin=[0,6]#y,x
    rot=0
    piece=choose_piece(pieces)
    curr_piece=choose_rotation(pieces,piece,rot)
    while not check_lost(table,curr_origin):
        if keyboard.is_pressed("a"):
            i="l"
        elif keyboard.is_pressed("d"):
            i="r"
        else:
            i=""
        if i=="r":
            table=move_right(table,curr_piece,curr_origin)
        elif i=="l":
            table=move_left(table,curr_piece,curr_origin)
        table,switch=move_down(table,curr_piece,curr_origin)
        if switch:
            curr_origin=[0,6]
            curr_piece=choose_rotation(pieces,choose_piece(pieces),rot)
        os.system("clear")
        print_table(table)
        time.sleep(.05)
    table[8][8]="Y"
    table[8][9]="O"
    table[8][10]="U"
    table[8][11]=" "
    table[8][12]=" "
    table[8][13]=" "
    table[8][14]="L"
    table[8][15]="O"
    table[8][16]="S"
    table[8][17]="T"
    os.system("clear")
    print_table(table)
game(table,piece_dict)
        
