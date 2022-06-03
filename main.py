#######################
# Number Tic Tac Toe
# Created by Cera W., Jennifer L., Anika S., Jana H.
# Additional enhancements done on 05/23/2021 by Anika S. 
# JAMHacks V
#######################

#imports and initializing variables
from tkinter import *
from tkinter import messagebox
from random import randint
count=0
player = ''
colour = ''
mtrx=[[[0 for i in range(3)] for j in range(3)] for k in range(3)]

#randomizing the number placement with 1 or more winning combos
while True:
  b1t = randint(1,9)
  b2t = randint(1,9)
  b3t = randint(1,9)
  b4t = randint(1,9)
  b5t = randint(1,9)
  b6t = randint(1,9)
  b7t = randint(1,9)
  b8t = randint(1,9) 
  b9t = randint(1,9)

  if b1t+b2t+b3t==15 or b1t+b4t+b7t==15 or b1t+b5t+b9t==15 or b2t+b5t+b8t==15 or b3t+b6t+b9t==15 or b4t+b5t+b6t==15 or b7t+b8t+b9t==15 or b3t+b5t+b7t==15:
    break
  
  else:
    continue

#Displaying the winner window
def displayWinner(last_person):
    global t,winnerWindow,ID   
    winnerWindow=Tk() 
    winnerWindow.title("Winner Window")
    winnerWindow.configure(bg='purple')

    l1=Label(winnerWindow,text="THE WINNER IS: ",font=("COMIC SANS MS",15,'bold'),bg='purple',fg=colour)
    l1.pack()
    
    l2=Label(winnerWindow,text=last_person,font=("COMIC SANS MS",15,'bold'),bg= 'purple',fg=colour)
    l2.pack()

#Checks for the winner        
def checkWinner():
  if mtrx[0][0][0]+mtrx[0][1][0]+mtrx[0][2][0]==15 and mtrx[0][0][1]==mtrx[0][1][1]==mtrx[0][2][1]:
    displayWinner(last_person)

  elif mtrx[1][0][0]+mtrx[1][1][0]+mtrx[1][2][0]==15 and mtrx[1][0][1]==mtrx[1][1][1]==mtrx[1][2][1]:
    displayWinner(last_person)
    
  elif mtrx[2][0][0]+mtrx[2][1][0]+mtrx[2][2][0]==15 and mtrx[2][0][1]==mtrx[2][1][1]==mtrx[2][2][1]:
    displayWinner(last_person)

  elif mtrx[0][0][0]+mtrx[1][1][0]+mtrx[2][2][0]==15 and mtrx[0][0][1]==mtrx[1][1][1]==mtrx[2][2][1]:
    displayWinner(last_person)
  
  elif mtrx[0][2][0]+mtrx[1][1][0]+mtrx[2][0][0]==15 and mtrx[0][2][1]==mtrx[1][1][1]==mtrx[2][0][1]:
    displayWinner(last_person)

  elif mtrx[0][0][0]+mtrx[1][0][0]+mtrx[2][0][0]==15 and mtrx[0][0][1]==mtrx[1][0][1]==mtrx[2][0][1]:
    displayWinner(last_person)

  elif mtrx[0][1][0]+mtrx[1][1][0]+mtrx[2][1][0]==15 and mtrx[0][1][1]==mtrx[1][1][1]==mtrx[2][1][1]:
    displayWinner(last_person)

  elif mtrx[0][2][0]+mtrx[1][2][0]+mtrx[2][2][0]==15 and mtrx[0][2][1]==mtrx[1][2][1]==mtrx[2][2][1]:
    displayWinner(last_person)
    
#When button is clicked, changes the value of the button, updates matrix
def changeVal(button,boardValRow,boardValCol):
  global count,last_person,b_val, colour
                      
  #if button doesn't have a value
  if button['text']== '':
    
    #keeps track of the player 
    #player 1
    if count%2==0:
      last_person="Player 1"
      l1=Label(t,text="Player 2",height=3,font=("COMIC SANS MS",10,"bold"),bg="#f5d5c6").grid(row=0,column=0)
      player = 'p1'
      colour = '#bed9d4'

    #player 2
    else:
      last_person="Player 2"
      l1=Label(t,text="Player 1",height=3,font=("COMIC SANS MS",10,"bold"),bg="#bed9d4").grid(row=0,column=0)
      player = 'p2'
      colour = '#f5d5c6'
  
  #if button does have a value
  else:
    messagebox.showerror("Error","This box already has a value!")

  #update mtrx
  if boardValRow==0 and boardValCol==0:
    b_val=b1t
    mtrx[0][0]=[b_val,player,colour]
  if boardValRow==0 and boardValCol==1:
    b_val=b2t
    mtrx[0][1]=[b_val,player,colour]
  if boardValRow==0 and boardValCol==2:
    b_val=b3t
    mtrx[0][2]=[b_val,player,colour]
  if boardValRow==1 and boardValCol==0:
    b_val=b4t
    mtrx[1][0]=[b_val,player,colour]
  if boardValRow==1 and boardValCol==1:
    b_val=b5t
    mtrx[1][1]=[b_val,player,colour]
  if boardValRow==1 and boardValCol==2:
    b_val=b6t
    mtrx[1][2]=[b_val,player,colour]
  if boardValRow==2 and boardValCol==0:
    b_val=b7t
    mtrx[2][0]=[b_val,player,colour]
  if boardValRow==2 and boardValCol==1:
    b_val=b8t
    mtrx[2][1]=[b_val,player,colour]
  if boardValRow==2 and boardValCol==2:
    b_val=b9t
    mtrx[2][2]=[b_val,player,colour]
  
  #assigning values and colours based on player
  button["text"]=b_val
  button['bg']=colour
  button['activebackground']=colour

  #increment count and check for winner each time
  count+=1 
  checkWinner()
  
  #if all squares have been clicked and no winner
  if count==9:
    displayWinner("NOBODY!")

#Displays the GUI 
def NumberTicTacToe():
    global t
    t=Tk()
    t.title("Number Tic Tac Toe")
    t.configure(bg="white") 

    #Displaying the player
    l1=Label(t,text= "Player 1",height=3,font=("COMIC SANS MS",10,"bold"),bg="#bed9d4")
    l1.grid(row=0,column=0)
    
    #Grid buttons{}
    b1_grid=Button(t,text= '',height=2,width=4,bg="#FFF5AB",activebackground="#FFF5AB",fg="#C449C2",activeforeground = '#C449C2',font="Times 15 bold",command=lambda: changeVal(b1_grid,0,0))

    b2_grid=Button(t,text='',height=2,width=4,bg="#FFF5AB",activebackground="#FFF5AB",fg="#C449C2",activeforeground = '#C449C2',font="Times 15 bold",command=lambda: changeVal(b2_grid,0,1))
    
    b3_grid=Button(t,text='',height=2,width=4,bg="#FFF5AB",activebackground="#FFF5AB",fg="#C449C2",activeforeground = '#C449C2',font="Times 15 bold",command=lambda: changeVal(b3_grid,0,2))
    
    b4_grid=Button(t,text='',height=2,width=4,bg="#FFF5AB",activebackground="#FFF5AB",fg="#C449C2",activeforeground = '#C449C2',font="Times 15 bold",command=lambda: changeVal(b4_grid,1,0))
    
    b5_grid=Button(t,text='',height=2,width=4,bg="#FFF5AB",activebackground="#FFF5AB",fg="#C449C2",activeforeground = '#C449C2',font="Times 15 bold",command=lambda: changeVal(b5_grid,1,1))
    
    b6_grid=Button(t,text='',height=2,width=4,bg="#FFF5AB",activebackground="#FFF5AB",fg="#C449C2",activeforeground = '#C449C2',font="Times 15 bold",command=lambda: changeVal(b6_grid,1,2))
    
    b7_grid=Button(t,text='',height=2,width=4,bg="#FFF5AB",activebackground="#FFF5AB",fg="#C449C2",activeforeground = '#C449C2',font="Times 15 bold",command=lambda: changeVal(b7_grid,2,0))
    
    b8_grid=Button(t,text='',height=2,width=4,bg="#FFF5AB",activebackground="#FFF5AB",fg="#C449C2",activeforeground = '#C449C2',font="Times 15 bold",command=lambda: changeVal(b8_grid,2,1))
    
    b9_grid=Button(t,text='',height=2,width=4,bg="#FFF5AB",activebackground="#FFF5AB",fg="#C449C2",activeforeground = '#C449C2',font="Times 15 bold",command=lambda: changeVal(b9_grid,2,2))

    b1_grid.grid(row=2,column=0)
    b2_grid.grid(row=2,column=1)
    b3_grid.grid(row=2,column=2)

    b4_grid.grid(row=3,column=0)
    b5_grid.grid(row=3,column=1)
    b6_grid.grid(row=3,column=2)

    b7_grid.grid(row=4,column=0)
    b8_grid.grid(row=4,column=1)
    b9_grid.grid(row=4,column=2)

#Calls the function
NumberTicTacToe()