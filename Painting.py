from tkinter import*

canvas_width=600
canvas_height=450

color = 'black'

def paint (event):
    x1, y1=(event.x-1), (event.y-1) 
    x2, y2=(event.x+1), (event.y+1)
    c.create_oval (x1, y1, x2, y2, fill=color, outline=color)

master=Tk()
master.title('Python Paint')
c=Canvas (master, width=canvas_width, height=canvas_height,bg='White')
master.iconbitmap('black-snake-python-with-floral-rainbow-painting-vector.ico')

c.pack(expand=YES, fill=BOTH) 
c.bind('<B1-Motion>', paint)
def Green(event):
    global color
    color ='green'
myButton=Button(master, text="Green")
myButton.bind("<Button>", Green)
myButton.pack(pady=2)

def Red(event):
    global color
    color ='Red'
myButton=Button(master, text="Red")
myButton.bind("<Button>", Red)
myButton.pack(pady=2)

def Orange(event):
    global color
    color ='Orange'
myButton=Button(master, text="Orange")
myButton.bind("<Button>", Orange)
myButton.pack(pady=2)

def Yellow(event):
    global color
    color ='Yellow'
myButton=Button(master, text="Yellow")
myButton.bind("<Button>", Yellow)
myButton.pack(pady=2)

def Purple(event):
    global color
    color ='Purple'
myButton=Button(master, text="Purple")
myButton.bind("<Button>", Purple)
myButton.pack(pady=2)

def Pink(event):
    global color
    color ='Pink'
myButton=Button(master, text="Pink")
myButton.bind("<Button>", Pink)
myButton.pack(pady=2)

def Black(event):
    global color
    color ='Black' 
myButton=Button(master, text="Black")
myButton.bind("<Button>", Black)
myButton.pack(pady=2)

def Erase_all(event):
    c.delete('all')
myButton=Button(master, text="Erase all")
myButton.bind("<Button>", Erase_all)
myButton.pack(pady=2)
master.mainloop()