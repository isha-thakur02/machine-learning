from tkinter import *

# Create the main window
root = Tk()
root.title("Tkinter Widgets Example")
root.geometry("600x700")  # Set the window size

# Label Widget
label = Label(root, text="This is a Label", font=("Arial", 14), fg="blue")
label.pack(pady=10)

# Button Widget
button = Button(root, text="Click Me", font=("Arial", 12))
button.pack(pady=10)

# Entry Widget
entry = Entry(root, width=30)
entry.pack(pady=10)

# Text Widget
text = Text(root, height=5, width=40)
text.pack(pady=10)


# Checkbutton Widget
check_var = IntVar()
checkbutton = Checkbutton(root, text="Check Me", variable=check_var)
checkbutton.pack(pady=10)

# Radiobutton Widget
radio_var = StringVar(value="Option 1")
radiobutton1 = Radiobutton(root, text="Option 1", variable=radio_var, value="Option 1")
radiobutton2 = Radiobutton(root, text="Option 2", variable=radio_var, value="Option 2")
radiobutton1.pack(pady=5)
radiobutton2.pack(pady=5)

# Listbox Widget
listbox = Listbox(root, height=5)
listbox.insert(1, "Item 1")
listbox.insert(2, "Item 2")
listbox.insert(3, "Item 3")
listbox.pack(pady=10)

# Scale Widget
scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, label="Scale")
scale.pack(pady=10)

# Spinbox Widget
spinbox = Spinbox(root, from_=0, to=10, width=10)
spinbox.pack(pady=10)


# Combobox (requires ttk)
from tkinter.ttk import Combobox
combobox = Combobox(root, values=["Option 1", "Option 2", "Option 3"])
combobox.set("Select an Option")
combobox.pack(pady=10)

# Messagebox (on button click)
from tkinter import messagebox
def show_message():
    messagebox.showinfo("Messagebox", "This is a message box!")

msg_button = Button(root, text="Show Messagebox", command=show_message)
msg_button.pack(pady=10)

# Progressbar (requires ttk)
from tkinter.ttk import Progressbar
progress = Progressbar(root, length=200, mode="determinate")
progress.pack(pady=10)
progress["value"] = 50  # Set progress to 50%


# # Run the application
root.mainloop()
