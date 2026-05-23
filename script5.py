from tkinter import *



window=Tk()
window.geometry('420x420')
window.title("Tic-Tac-Toe")
icon=PhotoImage(file="icon.png")
def gamestart():
    for row in range(3):

        for col in range(3):
            button = Button(window,
                            text="",
                            font=("Arial", 30),
                            width=5,
                            height=2)

            button.config(command=lambda b=button: play(b))

            button.grid(row=row, column=col)

    display_board()
    game_label = Label(window,
                       text="Game Started",
                       font=("Arial",20,"bold"),
                        fg="pink",
                        bg="black",
                        padx=20,
                        pady=20,)
    game_label.pack()


def clickyes():
    label.destroy()
    button1.destroy()
    button2.destroy()
    gamestart()

def clickno():
    label.destroy()
    button1.destroy()
    button2.destroy()
    window.destroy()



window.iconphoto(True,icon)
photo=PhotoImage(file="game.png")
label=Label(window,text='Welcome!!\n Do you want to play Tic-Tac-Toe?',
            font=("Arial",40,"bold"),
            fg="yellow",bg="black",
            relief=RAISED,bd=10,
            padx=20,pady=20,
            image=photo,
            compound=TOP)
label.place(x=500,y=300)
button1=Button(window,
              text="Yes",
               font=("Arial",20,"bold"),
              fg="green",
              bg="black",
               padx=20,
               pady=20,
               command=clickyes,)
button1.place(x=700,y=870)
button2=Button(window,
               text="No",
               font=("Arial",20,"bold"),
               fg="red",
               bg="black",
               padx=20,
               pady=20,
               command=clickno,)
button2.place(x=1000,y=870)
window.mainloop()