from tkinter import *

root = Tk()

top1 = Frame(root)

bottom1 = Frame(root)
top1.pack(fill=X)
bottom1.pack(side="bottom")

label1 = Label(top1, text="label1", fg="red", bg="yellow")
label1.pack(fill=X)

label2 = Label(top1, text="label2")
label2.pack(side=LEFT, fill=Y)

label3 = Label(bottom1, text="label3")
label3.pack(side=TOP)

button1 = Button(bottom1, text='Close', fg="red")
button1.pack(side=BOTTOM)

root.mainloop()
