
from tkinter import *
import tic_tac_toe
import snake
import space_invader
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 900

def get_window_object():
    window = Tk()
    window.title("Games")
    window.geometry(str(WINDOW_WIDTH)+"x"+str(WINDOW_HEIGHT))
    window.resizable(False,False)
    window.config(background="Blue")
    window.eval('tk::PlaceWindow . center')
    return window


def draw_window(window):
    
    window.title("Games")
    master_frame = Frame(window,background="grey")
    master_frame.pack(fill="both",expand=True)
    choice_the_game_label = Label(master_frame,text="Choice the game",font=('consolas',40),fg="Red",pady=50,background="Grey")
    choice_the_game_label.pack()

    frame = Frame(master_frame,background="Grey")
    frame.pack()

    tic_tac_toe_button = Button(frame,text="Tic Tac Toe",width=20,height=10,background="Blue",activebackground="Blue",command= lambda :tic_tac_toe.draw(window,master_frame))
    tic_tac_toe_button.grid(row=0,column=0)

    snake_button = Button(frame,text="Snake",width=20,height=10,background="Green",activebackground="Green",command= lambda :snake.snake_game(window,master_frame))
    snake_button.grid(row=0,column=1)

    space_invaders_button = Button(frame,text="Space invider",width=20,height=10,background="Yellow",activebackground="Yellow",command= lambda :space_invader.snake_game(window,master_frame))
    space_invaders_button.grid(row=0,column=2)
    window.mainloop()

