from tkinter import *  #1 
from PIL import ImageTk,Image #9 if not install in terminal 
# pip install pillow

root = Tk()     #2

root.title("Login Form") #4
# root.minsize(400,400)#5set default window size 
# root.maxsize(1000,1000)#6 set default max size
root.geometry("500x600")  #7 particular size window(wXh)
root.configure(background="skyblue")#8 background colour


#9 add image install library
img = Image.open("gui_image1.png")
resized_img = img.resize((70,70))
img = ImageTk.PhotoImage(resized_img)

# 10 place img in gui window use label(print text) but we 
# can print image also
img_label = Label(root, image=img)


# 11 gemoetry manager(pack)---decide where any ui element 
# place in screen
img_label.pack(pady = (10,10))# pady move image
#12 add text
text_label = Label(root, text = "photos", fg = "white",bg = "skyblue")
text_label.pack()
text_label.config(font = ("verdana", 24, "bold"))
#13 email
email_label = Label(root,text='Enter Email',fg='white',bg='skyblue')
email_label.pack(padx=(20,5))
email_label.config(font=('verdana',12))
#14 entry box
email_input = Entry(root,width=50)
email_input.pack(ipady=6,pady=(1,15))

# 15 16 password entry box
password_label = Label(root,text='Enter Password',fg='white',bg='skyblue')
password_label.pack(pady=(20,5))
password_label.config(font=('verdana',12))
password_input = Entry(root,width=50)
password_input.pack(ipady=6,pady=(1,15))
# 17 button
login_btn = Button(root,text='Login Here',bg='white',fg='black',width=20,height=2)
login_btn.pack(pady=(10,20))
login_btn.config(font=('verdana',10))

root.mainloop()   #3