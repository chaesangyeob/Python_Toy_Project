from tkinter import * 
from tkinter import ttk
from tkinter import messagebox as mb
from random import randint


#global Various
ActivePlayer = 1
p1 = []
p2 = []
winner=0
root = Tk()
style= ttk.Style()
style.theme_use('classic')
root.title('Tic Tac Toy Game:Player1 ')




#add Button
btn1 = ttk.Button(root,text='btn')
btn1.grid(row=0,column=0, sticky='snew', ipadx=40,ipady=40)
btn1.config(command=lambda: onBtnClick(1))

btn2 = ttk.Button(root,text='btn')
btn2.grid(row=0,column=1, sticky='snew', ipadx=40,ipady=40)
btn2.config(command=lambda: onBtnClick(2))

btn3 = ttk.Button(root,text='btn')
btn3.grid(row=0,column=2, sticky='snew', ipadx=40,ipady=40)
btn3.config(command=lambda: onBtnClick(3))

btn4 = ttk.Button(root,text='btn')
btn4.grid(row=1,column=0, sticky='snew', ipadx=40,ipady=40)
btn4.config(command=lambda: onBtnClick(4))

btn5 = ttk.Button(root,text='btn')
btn5.grid(row=1,column=1, sticky='snew', ipadx=40,ipady=40)
btn5.config(command=lambda: onBtnClick(5))

btn6 = ttk.Button(root,text='btn')
btn6.grid(row=1,column=2, sticky='snew', ipadx=40,ipady=40)
btn6.config(command=lambda: onBtnClick(6))

btn7 = ttk.Button(root,text='btn')
btn7.grid(row=2,column=0, sticky='snew', ipadx=40,ipady=40)
btn7.config(command=lambda: onBtnClick(7))

btn8 = ttk.Button(root,text='btn')
btn8.grid(row=2,column=1, sticky='snew', ipadx=40,ipady=40)
btn8.config(command=lambda: onBtnClick(8))

btn9 = ttk.Button(root,text='btn')
btn9.grid(row=2,column=2, sticky='snew', ipadx=40,ipady=40)
btn9.config(command=lambda: onBtnClick(9))

btnRest = ttk.Button(root, text='rest')
btnRest.grid(row=3,column=1, sticky='snew', ipadx=100,ipady=40)
btnRest.config(command=lambda: onClickReset())

def onClickReset():
        print('resetbtn clicked')

def onBtnClick(id):
        global p1
        global p2
        global winner
        global ActivePlayer
        print(winner)

        if(ActivePlayer ==1):          
            SetLayout(id,'x')
            p1.append(id)
            checkWinner()
            root.title('Tic Tac Toy Game:Player2')
            ActivePlayer=2
            if(winner ==0):
                    AutoPlay()
          

        elif(ActivePlayer ==2):
            SetLayout(id,'O')
            p2.append(id)
            checkWinner()
            root.title('Tic Tac Toy Game:Player1')
            ActivePlayer=1

           

        

def SetLayout(id, symbol):
        if id == 1:
                btn1.config(text=symbol)
                btn1.state(['disabled'])
        elif id == 2:
                btn2.config(text=symbol)
                btn2.state(['disabled'])
        elif id == 3:
                btn3.config(text=symbol)
                btn3.state(['disabled'])
        elif id == 4:
                btn4.config(text=symbol)
                btn4.state(['disabled'])
        elif id == 5:
                btn5.config(text=symbol)
                btn5.state(['disabled'])
        elif id == 6:
                btn6.config(text=symbol)
                btn6.state(['disabled'])
        elif id == 7:
                btn7.config(text=symbol)
                btn7.state(['disabled'])
        elif id == 8:
                btn8.config(text=symbol)
                btn8.state(['disabled'])
        elif id == 9:
                btn9.config(text=symbol)
                btn9.state(['disabled'])
        
def checkWinner():
        global winner
        
        if(( 1 in p1) and (2 in p1) and (3 in p1)):
                winner=1
        if(( 1 in p2) and (2 in p2) and (3 in p2)):
                winner=2
        
        if(( 1 in p1) and (4 in p1) and (7 in p1)):
                winner=1
        if(( 1 in p2) and (4 in p2) and (7 in p2)):
                winner=2

        if(( 1 in p1) and (5 in p1) and (9 in p1)):
                winner=1
        if(( 1 in p2) and (5 in p2) and (9 in p2)):
                winner=2

        if(( 4 in p1) and (5 in p1) and (6 in p1)):
                winner=1
        if(( 4 in p2) and (5 in p2) and (6 in p2)):
                winner=2

        if(( 7 in p1) and (8 in p1) and (9 in p1)):
                winner=1
        if(( 7 in p2) and (8 in p2) and (9 in p2)):
                winner=2

        if(( 2 in p1) and (5 in p1) and (8 in p1)):
                winner=1
        if(( 2 in p2) and (5 in p2) and (8 in p2)):
                winner=2

        if(( 3 in p1) and (6 in p1) and (9 in p1)):
                winner=1
        if(( 3 in p2) and (6 in p2) and (9 in p2)):
                winner=2

        if(( 3 in p1) and (5 in p1) and (7 in p1)):
                winner=1
        if(( 3 in p2) and (5 in p2) and (7 in p2)):
                winner=2

        if(winner ==1):
                mb.showinfo(title='Congrat.', message='Player1 is the winner')
                btn1.config(command=lambda: mb.showinfo(title='Congrat.', message='Player1 is the winner'))
                btn2.config(command=lambda: mb.showinfo(title='Congrat.', message='Player1 is the winner'))
                btn3.config(command=lambda: mb.showinfo(title='Congrat.', message='Player1 is the winner'))
                btn4.config(command=lambda: mb.showinfo(title='Congrat.', message='Player1 is the winner'))
                btn5.config(command=lambda: mb.showinfo(title='Congrat.', message='Player1 is the winner'))
                btn6.config(command=lambda: mb.showinfo(title='Congrat.', message='Player1 is the winner'))
                btn7.config(command=lambda: mb.showinfo(title='Congrat.', message='Player1 is the winner'))
                btn8.config(command=lambda: mb.showinfo(title='Congrat.', message='Player1 is the winner'))
                btn9.config(command=lambda: mb.showinfo(title='Congrat.', message='Player1 is the winner'))
        if(winner ==2):
                mb.showinfo(title='Congrat.', message='Player2 is the winner')
                btn1.config(command=lambda: mb.showinfo(title='Congrat.', message='Player1 is the winner'))
                btn2.config(command=lambda: mb.showinfo(title='Congrat.', message='Player1 is the winner'))
                btn3.config(command=lambda: mb.showinfo(title='Congrat.', message='Player1 is the winner'))
                btn4.config(command=lambda: mb.showinfo(title='Congrat.', message='Player1 is the winner'))
                btn5.config(command=lambda: mb.showinfo(title='Congrat.', message='Player1 is the winner'))
                btn6.config(command=lambda: mb.showinfo(title='Congrat.', message='Player1 is the winner'))
                btn7.config(command=lambda: mb.showinfo(title='Congrat.', message='Player1 is the winner'))
                btn8.config(command=lambda: mb.showinfo(title='Congrat.', message='Player1 is the winner'))
                btn9.config(command=lambda: mb.showinfo(title='Congrat.', message='Player1 is the winner'))


def AutoPlay():
        global p1
        global p2
        EmptyCell = []
        for i in range(1,10):
                if(not((i in p1 ) or ( i in p2))):
                        EmptyCell.append(i)

        RandomIndex = randint(0,len(EmptyCell)-1)
        onBtnClick(EmptyCell[RandomIndex])

                     


print(randint(0,9))
  


root.mainloop()
