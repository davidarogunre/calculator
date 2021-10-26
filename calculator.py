import tkinter as tk
from tkinter import Button
from tkinter import Entry
from tkinter import Canvas
from tkinter import Frame

tk = tk.Tk()
tk.geometry("312x324") 
tk.resizable(0,0)
tk.title("Calculator")
height = 3
width =10
borderwidth = -1
input_frame = Frame(tk, width = 312, height=50, bd=0, highlightbackground="black",highlightcolor="black", highlightthickness = 2)
input_frame.pack(side='top')
btns_frame = Frame(tk, width=312, height=272.5)
btns_frame.pack()
entry = Entry(input_frame, font =('arial', 18, 'bold'),width=50, bg = "#eee", bd=0, justify='right') 
entry.grid(row=0, column=0)
entry.pack(ipady=10)
#first row 
clear= Button(btns_frame,text="C",fg = 'black', width= 32, height=height, cursor="hand2", background='white',borderwidth=borderwidth).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
divide= Button(btns_frame,text= '/',fg= "black", width=width,height=height, borderwidth=borderwidth, bd=0,  cursor="hand2").grid(row=0, column=3, padx = 1, pady=1)

#second row
seven= Button(btns_frame,text="7", fg = 'black', width= width, bd=0, cursor ="hand2", background='white',height=height, borderwidth=borderwidth).grid(row= 1, column = 0,padx=1, pady=1)
eight= Button(btns_frame, text = '8',fg="black", width= width, bd = 0, cursor ="hand2", background='white',height=height, borderwidth=borderwidth).grid(row= 1, column=1, padx=1, pady=1)
nine= Button(btns_frame,text="9", fg = "black", width= width, bd=0, cursor = "hand2", background='white',height=height, borderwidth=borderwidth).grid(row=1, column=2,padx=1,pady=1)
times= Button(btns_frame,text= 'x', fg = "black", bd = 0, cursor="hand2",  width= width, height=height, borderwidth=borderwidth).grid(row=1, column = 3, padx = 1, pady=1)

#third row
four= Button(btns_frame, text="4", fg="black", bd=0, cursor="hand2", width= width, height=height, background='white', borderwidth=borderwidth).grid(row=2, column=0, padx = 1, pady=1)
five= Button(btns_frame, text="5", fg= "black", bd=0, cursor="hand2", width= width, background='white', height=height, borderwidth=borderwidth).grid(row = 2, column = 1, padx = 1, pady = 1)
six= Button(btns_frame, text="6",fg = "black", bd=0, cursor = "hand2", width= width, background='white',height=height, borderwidth=borderwidth).grid(row=2, column = 2, padx= 1, pady = 1)
minus= Button(btns_frame, text= '-', fg = "black", bd=0, cursor = "hand2", width= width, height=height, borderwidth=borderwidth).grid(row=2, column =3, padx =1, pady=1)

#fourth row
one= Button(btns_frame, text="1", fg = "black", bd =0, cursor = "hand2", width= width, background='white', height=height, borderwidth=borderwidth).grid(row=3,column = 0, padx =1, pady=1)
two= Button(btns_frame, text="2",fg = "black", bd=0, cursor = "hand2", width= width, background='white',height=height, borderwidth=borderwidth).grid(row=3, column =1 , padx =1, pady =1)
three= Button(btns_frame, text='3',fg = "black", bd = 0, cursor="hand2", width= width, background='white',height=height, borderwidth=borderwidth).grid(row=3, column =2, padx = 1, pady =1)
plus= Button(btns_frame, text= '+', fg ="black", bd = 0, cursor = "hand2", width= width, height=height, borderwidth=borderwidth).grid(row = 3, column=3, padx = 1, pady =1)

#fifth row
zero= Button(btns_frame, text= '0', fg = "black", bd =0, cursor = "hand2", width= 21, background='white',height = height, borderwidth=borderwidth).grid(row= 4, column = 0, columnspan=2, padx = 1, pady=1)
point= Button(btns_frame, text= '.', fg = "black", bd =0, cursor = "hand2", width= width, height = height, borderwidth=borderwidth).grid(row = 4, column = 2, padx=1, pady=1)
equals= Button(btns_frame,text= '=', fg = "black", bd = 0, cursor="hand2",width=width, height = height, borderwidth=borderwidth).grid(row = 4, column = 3, padx = 1, pady = 1)









tk.mainloop()
