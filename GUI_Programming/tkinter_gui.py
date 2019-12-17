import tkinter

from tkinter import Tk
from tkinter import ttk
from tkinter import *

root = Tk()

# button
'''
root.title('GUI Using Python')
ttk.Button(root, text='Hello Pratik').grid()
root.mainloop()

# frame

frame = Frame(root)
labelText = StringVar()

label = Label(frame, textvariable = labelText)
button = Button(frame, text = 'I am Button')

labelText.set('Hey!!')
label.pack()
button.pack()
frame.pack()

root.mainloop()


frame = Frame(root)
Label(frame, text='Hey').pack()
Button(frame, text = 'B1').pack(side=LEFT, fill = Y)
Button(frame, text = 'B2').pack(side=RIGHT, fill = X)
Button(frame, text = 'B3').pack(side=TOP, fill = Y)
Button(frame, text = 'B4').pack(side=LEFT, fill = X)

frame.pack()
root.mainloop()

'''

Label(root, text='Name').grid(row=0, column=0, sticky=N)
Entry(root, width=50).grid(row=0, column=1)

Button(root, text = 'Submit').grid(row=0, column=5)

Label(root, text='Name').grid(row=0, column=0, sticky=N)
Radiobutton(root, text='F', value=1).grid(row=1, column=1, sticky=N)
Radiobutton(root, text='M', value=2).grid(row=1, column=2, sticky=N)

Label(root, text='cources').grid(row=2, column=0, sticky=N)
Checkbutton(root, text='Python').grid(row=3, column=1, sticky=N)
Checkbutton(root, text='Django').grid(row=4, column=1, sticky=N)
Checkbutton(root, text='Flask').grid(row=5, column=1, sticky=N)


root.mainloop()
