
from cgitb import text
import random
from tkinter import *
import menu
player = ""
players = ["X","O"]
buttons  =  [[0,0,0],
            [0,0,0],
            [0,0,0]]

def draw(window,master_frame):
    window.geometry(str(820)+"x"+str(820))
    global player,palyers,buttons
    master_frame.destroy()

    window.title("Tic Tac Toe")
    canvas = Canvas(window, background="Grey")
    canvas.pack(fill="both",expand= True)

    players = ["X","O"]
    player = random.choice(players)
    
    whose_turn_label = Label(canvas,text="Turn : "+str(player),font=("consolas",30),background="Grey",pady=30,bd=0, highlightthickness=0, relief='ridge')
    whose_turn_label.pack(side=TOP)

    frame = Frame(canvas)
    frame.pack(anchor="center",)



    restart_button = Button(canvas,text="Restart",font=("consolas",15),width=20,height=4,command= lambda :new_game(whose_turn_label))
    restart_button.pack()

    exit_button = Button(canvas,text="Exit",width=10,height=3,command= lambda :exit_funct_button(window,canvas))
    exit_button.pack(side=RIGHT,anchor=S + E)


    for row in range(3):
        for column in range(3):
            buttons[row][column] = Button(frame,text="",width=20,height=10,command= lambda row=row,column=column :move(row,column,whose_turn_label))
            buttons[row][column].grid(row = row+1, column = column+1)

def exit_funct_button(window,somthing_whats_gona_be_destroy):
    somthing_whats_gona_be_destroy.destroy()
    menu.draw_window(window)

def move(row,column,label):

    global player,players
    if buttons[row][column]['text'] == "" and check_winner() is False:
        if player == players[0]:
            buttons[row][column]['text'] = player
            if check_winner() is False:
                player = players[1]
                label.config(text=("Turn: "+str(players[1])))
            elif check_winner() is True:
                label.config(text="Player: "+str(player)+ " win")
            elif check_winner() =="Draw":
                label.config(text="Draw")
        else:
            buttons[row][column]['text'] = player
            if check_winner() is False:
                player = players[0]
                label.config(text="Turn: "+str(players[0]))
            elif check_winner() is True:
                label.config(text="Player: "+str(player)+" win")
            elif check_winner() =="Draw":
                label.config(text="Draw")


def check_winner():
    
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="Green",activebackground="Green")
            buttons[row][1].config(bg="Green",activebackground="Green")
            buttons[row][2].config(bg="Green",activebackground="Green")
            return True
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="Green",activebackground="Green")
            buttons[1][column].config(bg="Green",activebackground="Green")
            buttons[2][column].config(bg="Green",activebackground="Green")
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] ==buttons[2][2]['text'] !="":
        buttons[0][0].config(bg="Green",activebackground="Green")
        buttons[1][1].config(bg="Green",activebackground="Green")
        buttons[2][2].config(bg="Green",activebackground="Green")
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] ==buttons[2][0]['text'] !="":
        buttons[0][2].config(bg="Green",activebackground="Green")
        buttons[1][1].config(bg="Green",activebackground="Green")
        buttons[2][0].config(bg="Green",activebackground="Green")
        return True
    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                if buttons[row][column]['text'] == players[0]:
                    buttons[row][column].config(bg="Green",activebackground="Green")
                else:
                    buttons[row][column].config(bg="Red",activebackground="Red")
        return "Draw"
    else:
        return False

def new_game(label):
    global player,players
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0",activebackground="#F0F0F0")
    player = random.choice(players)
    label.config(text="Turn: "+str(player))

def empty_spaces():

    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] !="":
                spaces -=1
    if spaces ==0:
        return False
    else:
        return True