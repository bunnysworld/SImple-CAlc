from tkinter import *


def click(event):
    global value
    text=event.widget.cget("text")
    if text == "=":
        if value.get().isdigit():
            v=int(value.get())
        else:
            v=eval(screen.get())
        value.set(v)
        screen.update()
    elif text == "c":
        value.set("")
        screen.update()
    else:
        value.set(value.get()+text)
        screen.update()

root=Tk()

root.geometry("600x900")

root.title("Simple calculator")
value=StringVar()
value.set("")
screen=Entry(root,textvar=value,font="lucida 40 bold")
screen.pack(fill=X,padx=8,pady=8)

frame=Frame(root,bg="red")
frame.pack()
button=Button(frame,text="9",padx=20,pady=2,font="lucida 35 bold")
button.pack(side=LEFT,padx=10,pady=3)
button.bind("<Button-1>",click)

button=Button(frame,text="8",padx=20,pady=2,font="lucida 35 bold")
button.pack(side=LEFT,padx=10,pady=3)
button.bind("<Button-1>",click)

button=Button(frame,text="7",padx=20,pady=2,font="lucida 35 bold")
button.pack(side=LEFT,padx=10,pady=3)
button.bind("<Button-1>",click)

# ************
# SECOND FRAME
# ************


frame=Frame(root,bg="blue")
frame.pack()
button=Button(frame,text="6",padx=20,pady=2,font="lucida 35 bold")
button.pack(side=LEFT,padx=10,pady=3)
button.bind("<Button-1>",click)

button=Button(frame,text="5",padx=20,pady=2,font="lucida 35 bold")
button.pack(side=LEFT,padx=10,pady=3)
button.bind("<Button-1>",click)

button=Button(frame,text="4",padx=20,pady=2,font="lucida 35 bold")
button.pack(side=LEFT,padx=10,pady=3)
button.bind("<Button-1>",click)

# ***********
# THIRD FRAME
# ***********

frame=Frame(root,bg="green")
frame.pack()
button=Button(frame,text="3",padx=20,pady=2,font="lucida 35 bold")
button.pack(side=LEFT,padx=10,pady=3)
button.bind("<Button-1>",click)

button=Button(frame,text="2",padx=20,pady=2,font="lucida 35 bold")
button.pack(side=LEFT,padx=10,pady=3)
button.bind("<Button-1>",click)

button=Button(frame,text="1",padx=20,pady=2,font="lucida 35 bold")
button.pack(side=LEFT,padx=10,pady=3)
button.bind("<Button-1>",click)

# ************
# FOURTH FRAME
# ************
frame=Frame(root,bg="black")
frame.pack()
button=Button(frame,text="0",padx=20,pady=2,font="lucida 35 bold")
button.pack(side=LEFT,padx=10,pady=3)
button.bind("<Button-1>",click)

button=Button(frame,text="-",padx=20,pady=2,font="lucida 40 bold")
button.pack(side=LEFT,padx=10,pady=3)
button.bind("<Button-1>",click)

button=Button(frame,text="*",padx=20,pady=2,font="lucida 40 bold")
button.pack(side=LEFT,padx=10,pady=3)
button.bind("<Button-1>",click)

# ***********
# FIFTH FRAME
# ***********

frame=Frame(root,bg="orange")
frame.pack()
button=Button(frame,text="/",padx=20,pady=2,font="lucida 35 bold")
button.pack(side=LEFT,padx=10,pady=3)
button.bind("<Button-1>",click)

button=Button(frame,text="%",padx=20,pady=2,font="lucida 35 bold")
button.pack(side=LEFT,padx=10,pady=3)
button.bind("<Button-1>",click)

button=Button(frame,text="=",padx=20,pady=2,font="lucida 35 bold")
button.pack(side=LEFT,padx=10,pady=3)
button.bind("<Button-1>",click)

# **********
#SIXTH FRAME
# **********

frame=Frame(root,bg="purple")
frame.pack()
button=Button(frame,text="c",padx=20,pady=2,font="lucida 35 bold")
button.pack(side=LEFT,padx=10,pady=3)
button.bind("<Button-1>",click)

button=Button(frame,text="8",padx=20,pady=2,font="lucida 35 bold")
button.pack(side=LEFT,padx=10,pady=3)
button.bind("<Button-1>",click)

button=Button(frame,text="7",padx=20,pady=2,font="lucida 35 bold")
button.pack(side=LEFT,padx=10,pady=3)
button.bind("<Button-1>",click)

root.mainloop()