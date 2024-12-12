"""
pack()  
grid()  
place()

"""
# pack
# from tkinter import *

# a = Tk()
# a.title("pack method")
# a.geometry(("500x300"))
# rb = Button(a,text = "button", fg = "red", bg = "blue")
# rb.pack(side=RIGHT)

# a.mainloop()

# grid

# from tkinter import *

# a = Tk()
# a.title("grid method")
# nm = Label(a, text="name").grid(rows = 1, column = 1)
# el = Entry(a).grid(row = 1,column = 2)
# e2 = Label(a, text = "class").grid(row = 2,column = 1)

# re = Label()
# a.mainloop()


# place

from tkinter import *

a = Tk()
nm = Label(a, text = "name")
nm.place(x = 10, y = 0)

el = Entry(a).place(x = 50,y = 95)

vb = Canvas()

a.mainloop()
