from tkinter import *
#Importing tkinter module

'''Q1'''
#Creating new Interface
m = Tk()
#Creating Label
label = Label(m, text= "\nHello World\n")
label.pack()
#Creating EXIT button
button = Button(m,text = 'EXIT', width = 20, command = m.destroy)
button.pack()

'''Q2'''
#method to print text
def write_some():
    print("hi, you are talking to a brown kid")
#Creating Button
button1 = Button(m,text='Click to See Message',width=25,command = write_some)
button1.pack()

'''Q3'''
#Creating new Interface
r = Tk()
#method to change label
def change_label():
    label2["text"] = "My name is Chetan."
#Creating frame
frame = Frame(r)
frame.pack()
#Creating label
label2 = Label(r,text="\nCLICK ONE OF THE BUTTONS\n")
label2.pack()
bottomframe = Frame(r)
bottomframe.pack(side=BOTTOM)
stopbutton = Button(bottomframe, text='EXIT', width = 25, fg = 'green', command = r.destroy)
stopbutton.pack(side=LEFT)
printbutton = Button(bottomframe, text='Change Label', width = 25, fg = 'Blue', command=change_label)
printbutton.pack(side=LEFT)

'''Q4'''
tk = Tk()
def display():
    print("Your name is " +  e1.get())
Label(tk, text = "Enter your name: ").grid(row=0)
e1 = Entry(tk)
e1.grid(row=0,column=1)
button1 = Button(tk, text='PRINT',width=25,fg='Green',command=display)
button1.grid(row=4,column=1)

m.mainloop()
