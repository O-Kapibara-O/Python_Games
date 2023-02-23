
from random import randint, random
from tkinter import *
import random
from tic_tac_toe import exit_funct_button
GAME_WIDTH = 900
GAME_HEIGHT = 900
SPEED = 50
SPACE_SIZE = 50 
BODY_PARTS = 3
SNAKE_COLOR = "Green"
FOOD_COLLOR = "Red"
BACKGROUND_COLOR = "Black"
direction =""
score = 0
class Snake():

    def __init__(self,canvas):

        self.body_size = BODY_PARTS
        self.coordinates =[]
        self.squares =[]

        for i in range(0,BODY_PARTS):
            self.coordinates.append([0,0])

        for x,y in self.coordinates:
            square = canvas.create_rectangle(x,y, x + SPACE_SIZE, y + SPACE_SIZE,fill=SNAKE_COLOR, tags="snake")
            self.squares.append(square)
class Food():

    def __init__(self,canvas):


        x = randint(0, (GAME_WIDTH/SPACE_SIZE)-1)*SPACE_SIZE
        y = randint(0, (GAME_HEIGHT/SPACE_SIZE)-1)*SPACE_SIZE

        self.coordinates = [x,y]

        canvas.create_oval( x, y, x + SPACE_SIZE, y + SPACE_SIZE,fill=FOOD_COLLOR,tags="food")




def snake_game(window,master_frame):
    global direction
    master_frame.destroy()
    window.geometry(str(900)+"x"+str(970))
    window.title("Snake")
    window.resizable(True,True)
    bag_for_all_widgets = Canvas(window,background="Black")
    bag_for_all_widgets.pack(fill="both",expand=True)
    
    direction = "down"
    score = 0

    label = Label(bag_for_all_widgets,text="Score: "+str(score),font=('consolas',40),fg="Red",background="Black")
    label.pack()

    canvas = Canvas(bag_for_all_widgets,bg=BACKGROUND_COLOR,height=GAME_WIDTH,width=GAME_HEIGHT,highlightbackground="Red",bd=5)
    canvas.pack()

    window.bind("<Left>", lambda event: new_direction("left"))
    window.bind("<Up>", lambda event: new_direction("up"))
    window.bind("<Down>", lambda event: new_direction("down"))
    window.bind("<Right>", lambda event: new_direction("right"))

    snake = Snake(canvas)
    food = Food(canvas)

    move(snake,food,canvas,label,bag_for_all_widgets,window)
    
    window.mainloop()

def move(snake,food,canvas,label,bag_for_all_widgets,window):
    global score
    x = snake.coordinates[0][0]
    y = snake.coordinates[0][1]

    if direction == "down":
        y +=SPACE_SIZE
    elif direction == "up":
        y -=SPACE_SIZE
    elif direction == "right":
        x +=SPACE_SIZE
    elif direction == "left":
        x -=SPACE_SIZE

    snake.coordinates.insert(0,(x,y))
    square = canvas.create_rectangle(x,y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0,square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        score+=1
        label.config(text="Score: "+ str(score))
        canvas.delete("food")
        food = Food(canvas)
    else:
        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if collision(snake) is True:
        score =0
        gameover(canvas,bag_for_all_widgets,window)
    else:
        canvas.after(SPEED, move, snake, food, canvas,label,bag_for_all_widgets,window)

def new_direction(new_direction):
    global direction

    if new_direction =="left":
        if direction !="right":
            direction= new_direction
    elif new_direction =="up":
        if direction !="down":
            direction= new_direction
    elif new_direction =="right":
        if direction !="left":
            direction= new_direction
    elif new_direction =="down":
        if direction !="up":
            direction= new_direction


def collision(snake):
    
    x = snake.coordinates[0][0]
    y = snake.coordinates[0][1]

    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y<0 or y>=GAME_HEIGHT:
        return True
    
    for body_part in snake.coordinates[1:]:
        if body_part[0] == snake.coordinates[0][0] and body_part[1] == snake.coordinates[0][1]:
            return True
    else:
        return False

def gameover(canvas,bag_for_all_widgets,window):
    
    canvas.destroy()
    label_gameover = Label(bag_for_all_widgets,text="Game over",font=("consolas",40),fg="RED",anchor= CENTER,background="Black")
    label_gameover.pack(fill="both",expand=True)
    frame_over = Frame(bag_for_all_widgets,background="Black")
    frame_over.pack()
    
    exit_button = Button(frame_over,text="Exit",command= lambda : exit_funct_button(window,bag_for_all_widgets),font=("consolas",30),fg="Red",background="Black")
    exit_button.pack()

