import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from time import sleep
import comp

def check_winner(str): #To check if anyone win or draw
    global winner
    for i in conditions:
        if buttons[i[0]].cget("text") == buttons[i[1]].cget("text") == buttons[i[2]].cget("text") != " ":
            messagebox.showinfo("Winner",str+" wins!")
            set_board_and_difficulty(False," ")
            winner = True
            return
    winner=True
    for button in buttons:
        if button.cget("text") == " ":
            winner=False
            break
    if winner:
        set_board_and_difficulty(False," ")
        messagebox.showinfo("Tie", "It's a tie!")

def button_click(idx): #Actions to be taken after grid button click by user
    global turn, winner
    if buttons[idx].cget("text") == " " and not winner:
        if turn:
            buttons[idx].config(text="X", state="disabled")
        else:
            buttons[idx].config(text="O", state="disabled")
        if comp_difficulty==" " and turn:
            check_winner("X")
            turns.config(text="O Pick")
        elif comp_difficulty==" " and not turn:
            check_winner("O")
            turns.config(text="X Pick")
        else:
            check_winner("You")
        turn = not turn
        if comp_difficulty!=" " and not winner:
            comp_pick(comp_difficulty)
def reset_game(): #reset the game like grid buttons or default setting
    mode.configure(text="")
    play_with_computer_label.place(x=160,y=90)
    computer_button.config(state="normal")
    computer_button.place(x=90,y=170)
    multiplayer_button.config(state="normal")
    multiplayer_button.place(x=250,y=170)
    global turn, winner,middle,turns
    turns.configure(text="")
    middle=True
    set_board_and_difficulty(True," ")
    turn = True
    winner = False

root = tk.Tk()
root.title("Tic Tac Toe")
root.maxsize(1366,768)
root.minsize(1366,768)
root.maxsize(width=1366, height=786)
root.resizable(0,0)

def play_with_computer(): # when user want to play with computer
    computer_button.config(state=tk.DISABLED)
    multiplayer_button.config(state=tk.DISABLED)
    easy_button.place(x=100,y=260)
    medium_button.place(x=200,y=260)
    hard_button.place(x=330,y=260)

def set_board_and_difficulty(x,difficulty=" "):#Enable or disable the grid/board and also take action by difficulty
    global comp_difficulty
    comp_difficulty=difficulty
    for button in buttons:
        if x:
            button.config(text=" ",state="normal")
        else:
            button.config(state="disabled")
    if  comp_difficulty=="Hard" or comp_difficulty=="Easy" or comp_difficulty=="Medium":
        easy_button.place_forget()
        medium_button.place_forget()
        hard_button.place_forget()
        play_with_computer_label.place_forget()
        computer_button.place_forget()
        multiplayer_button.place_forget()
        mode.configure(state="normal",text=comp_difficulty)
        turns.configure(text="Your Pick")

def multiplayer_configration(): #set grid and other settings according to multiplayer
    for button in buttons:
        button.config(text=" ",state="normal")
    turns.configure(text="X Pick")
    play_with_computer_label.place_forget()
    computer_button.place_forget()
    multiplayer_button.place_forget()
    mode.configure(state="normal",text="Multiplayer")
def comp_pick(difficulty): #Get the computer pick
    global turn,buttons
    global middle
    turns.config(text="Computer's Pick")
    x=comp.comp_pick(buttons, difficulty, middle)# calling a function from user defined library
    buttons[x].config(text="O", state="disabled")
    middle=False
    sleep(1)
    check_winner("Computer")
    turns.config(text="Your Pick")
    turn = not turn

# Load background image
bg_image = Image.open(r'D:\IOT-Project\bg1.png')
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

buttons = []
turn = True
winner = False
middle=True
conditions=[(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
comp_difficulty=" "
turns = tk.Label(root, text="",background="#B06C48", font=("Consolas", 25))
turns.place(x=850, y=670)

for i in range(9): #Initiallizing board buttons
    button = tk.Button(root, text=" ", font=("Helvetica", 22),foreground="#B06C48", width=7, height=3, command=lambda idx=i: button_click(idx))
    button.place(x=710 + (i % 3) * 145, y=233 + (i // 3) * 140)
    button.config(state="disabled")
    buttons.append(button)


reset_button = tk.Button(root, text="Reset",background="#B06C48", font=("Consolas", 30), command=reset_game)
reset_button.place(x=120, y=520)

exit_button = tk.Button(root, text="Exit",background="#B06C48", font=("Consolas", 30), command=root.destroy)
exit_button.place(x=280, y=520)


play_with_computer_label = tk.Label(root, text="Play with", background="#B06C48", font=("Consolas", 35))
play_with_computer_label.place(x=165,y=90)

mode = tk.Label(root, text="", background="#B06C48", font=("Consolas", 50),state="disabled")
mode.place(x=160,y=160)

computer_button = tk.Button(root, text="Computer",background="#B06C48", font=("Consolas", 20), command=play_with_computer)
computer_button.place(x=90,y=170)

multiplayer_button = tk.Button(root, text="Multiplayer",background="#B06C48", font=("Consolas", 20),command=multiplayer_configration)
multiplayer_button.place(x=250,y=170)

easy_button = tk.Button(root, text="Easy",background="#B06C48", font=("Consolas", 20), command=lambda: set_board_and_difficulty(True,"Easy"))
medium_button = tk.Button(root, text="Medium",background="#B06C48", font=("Consolas", 20), command=lambda: set_board_and_difficulty(True,"Medium"))
hard_button = tk.Button(root, text="Hard", background="#B06C48",font=("Consolas", 20),command=lambda: set_board_and_difficulty(True,"Hard"))


root.mainloop()
