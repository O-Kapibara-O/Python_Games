
import random
from utils import exit_funct_button
from tkinter import *
GAMEOVER = False
class Player:
    def __init__(self,canvas):
        self.health = 100
        self.size = 25
        self.coordinates =[450,800]
        self.direction ="stop"
        self.bulet_list =[]
        canvas.create_oval(self.coordinates[0],self.coordinates[1], self.coordinates[0]+self.size,self.coordinates[1]+self.size,fill="Cyan",tags="player")

    def shot(self):
        global key_space_counter
        self.bulet_list.append(Bulet(self.coordinates[0]+self.size/4,self.coordinates[1]+self.size/4,key_space_counter))
        key_space_counter+=1
        
    def move(self,direction):
        if direction =="left":
            self.direction = direction
        elif direction =="right":
            self.direction = direction

class Enemy:

    def __init__(self,canvas,x,y,id):

        self.id = id
        self.health  = 100
        self.size = 25
        self.coordinates = [x,y]
        self.bulet_list =[]
        canvas.create_rectangle(x,y,x+self.size,y+self.size,fill="Blue",tags=("enemy"+str(self.id)))

        self.number_of_shots =None
    def shot(self):
        if self.number_of_shots == None:
            self.number_of_shots = 0
        else:
            self.number_of_shots +=1
        self.bulet_list.append(Bulet(self.coordinates[0]+self.size/4,self.coordinates[1]+self.size/4,self.number_of_shots))

class Bulet:
    
    def __init__(self,x,y,id): 
        self.id =id
        self.size = 12
        self.coordinates =[x,y]
        self.damage = 10

def draw(window,canvas,player,enemy_list):
    
    if GAMEOVER == False:
        if player.direction =="left":
            player.coordinates[0] = player.coordinates[0]-player.size
            canvas.delete("player")
            canvas.create_oval(player.coordinates[0],player.coordinates[1], player.coordinates[0]+player.size,player.coordinates[1]+player.size,fill="Cyan",tags="player")
            player.direction ="stop"
        if player.direction =="right":
            player.coordinates[0] = player.coordinates[0]+player.size
            canvas.delete("player")
            canvas.create_oval(player.coordinates[0],player.coordinates[1], player.coordinates[0]+player.size,player.coordinates[1]+player.size,fill="Cyan",tags="player")
            player.direction ="stop"

        chance_to_shot(enemy_list)
        collision_detect(canvas,player,enemy_list)
        draw_all_bullets_on_canvas(canvas,player.bulet_list,enemy_list)

        
        canvas.after(20,draw,window,canvas,player,enemy_list)
    elif GAMEOVER =="win":
        game_over(2)
        BackToTheMenu(window,canvas,"win")
    else:
        game_over(2)
        BackToTheMenu(window,canvas,"Over")
        
def BackToTheMenu(window,canvas,result):

    canvas.destroy()
    if result == "win":
        statement = "Win"
    else:
        statement = "Game over"
    bag_for_all_widgets = Canvas(window,background="Black")
    bag_for_all_widgets.pack(fill="both",expand=True)
    label_gameover = Label(bag_for_all_widgets,text=statement,font=("consolas",40),fg="RED",anchor= CENTER,background="Black")
    label_gameover.pack(fill="both",expand=True)
    frame_over = Frame(bag_for_all_widgets,background="Black")
    frame_over.pack()
    
    exit_button = Button(frame_over,text="Exit",command= lambda : exit_funct_button(window,bag_for_all_widgets),font=("consolas",30),fg="Red",background="Black")
    exit_button.pack()


def draw_all_bullets_on_canvas(canvas,list_of_bulets,enemy_list):

    if len(list_of_bulets) !=0:
        for bulet in list_of_bulets:
            name = "id"+str(bulet.id)
            canvas.delete(name)
            bulet.coordinates[1] -=bulet.size
            canvas.create_oval(bulet.coordinates[0],bulet.coordinates[1], bulet.coordinates[0]+bulet.size,bulet.coordinates[1]+bulet.size,fill="Yellow",tags=name)
    if len(enemy_list) !=0:
        for enemy in enemy_list:
            if len(enemy.bulet_list) !=0:
                for bulet in enemy.bulet_list:
                    name = "e"+str(enemy.id)+"b"+str(bulet.id)
                    canvas.delete(name)
                    bulet.coordinates[1] +=bulet.size
                    canvas.create_oval(bulet.coordinates[0],bulet.coordinates[1], bulet.coordinates[0]+bulet.size,bulet.coordinates[1]+bulet.size,fill="Red",tags=name)   

def game_over(num):
    
    global GAMEOVER
    if num == 0:
        GAMEOVER = True
    elif num =="win":
        GAMEOVER ="win"
    else:
        GAMEOVER = False

            
def collision_detect(canvas,player,enemy_list):
    #---------------------------------------------
    list=[]
    list_of_enemy_to_delate =[]
    if len(player.bulet_list) !=0:
        for bulet in player.bulet_list:
            if bulet.coordinates[1]<0:
                list.append(bulet)
                canvas.delete("id"+str(bulet.id))   # ----------- Removing player's bullet, collision with border
            
            if len(enemy_list) !=0:
                for enemy in enemy_list:
                        if bulet.coordinates[0] >= enemy.coordinates[0] and bulet.coordinates[0] + bulet.size <= enemy.coordinates[0] + enemy.size:
                            if bulet.coordinates[1] >= enemy.coordinates[1] and bulet.coordinates[1] + bulet.size <= enemy.coordinates[1] + enemy.size:
                                
                                list_of_enemy_to_delate.append(enemy)
                                for enemy_bulet in enemy.bulet_list:
                                    canvas.delete("e"+str(enemy.id)+"b"+str(enemy_bulet.id))
                                enemy.bulet_list.clear()
                                canvas.delete("enemy"+str(enemy.id))
                                list.append(bulet)
                                canvas.delete("id"+str(bulet.id))

            
        if len(list) !=0:    
            for x in list:
                if x in player.bulet_list:
                    player.bulet_list.remove(x)
            list.clear()
        if len(list_of_enemy_to_delate) !=0:
            for x in list_of_enemy_to_delate:
                if x in enemy_list:
                    enemy_list.remove(x)
            list_of_enemy_to_delate.clear()
    #----------------------------------------------
    enemy_bulet_list =[]
    if len(enemy_list) !=0:
        for enemy in enemy_list:
            if len(enemy.bulet_list) !=0:
                for bulet in enemy.bulet_list:
                    if bulet.coordinates[1]>900:
                        name = "e"+str(enemy.id)+"b"+str(bulet.id)          # Removing enemy's bullet, collision with border
                        enemy_bulet_list.append(bulet)
                        canvas.delete(name)

                    if bulet.coordinates[0] >= player.coordinates[0] and bulet.coordinates[0] + bulet.size <= player.coordinates[0] + player.size:
                        if bulet.coordinates[1] >= player.coordinates[1] and bulet.coordinates[1] + bulet.size <= player.coordinates[1] + player.size:
                            game_over(0)
                            
        if len(enemy_bulet_list) !=0:
            for enemy in enemy_list:
                if len(enemy.bulet_list) !=0:
                    for x in enemy_bulet_list:
                        if x in enemy.bulet_list:          
                            enemy.bulet_list.remove(x)
            enemy_bulet_list.clear()
    else:
        game_over("win")

    #-----------------------------------------------

def create_enemy_list(canvas):
    
    copy_enemy_list =[]
    for row in range(10):
        for column in range(36):
            copy_enemy_list.append(Enemy(canvas,column*25,100+(row*25)+ row*15,column+row*36))
    
    return copy_enemy_list

def chance_to_shot(enemy_list):
    if len(enemy_list) !=0:
        for enemy in enemy_list:
            if random.randint(0,400)== 2:
                enemy.shot()


def snake_game(window,master_frame):
    global key_space_counter
    key_space_counter = 0
    master_frame.destroy()

    window.title("Space invider")

    bag_for_all_widgets = Canvas(window,background="Green")
    bag_for_all_widgets.pack(fill="both",expand=True)

    player = Player(bag_for_all_widgets)
    enemy_list = create_enemy_list(bag_for_all_widgets)
    window.bind("<Left>",lambda event : player.move("left"))
    window.bind("<Right>",lambda event : player.move("right"))
    window.bind("<space>",lambda event : player.shot())
    
    draw(window,bag_for_all_widgets,player,enemy_list)
    
    window.update()

    window.mainloop()

