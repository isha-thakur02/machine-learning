import tkinter as tk
from tkinter import messagebox


def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    feedback = entry_feedback.get("1.0", tk.END).strip()



    if not name or not email or not feedback:
        messagebox.showerror("error", "all field is required")
    else:
        messagebox.showinfo("success","form submitted")
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_feedback.delete("1.0", tk.END)


root = tk.Tk()
root.title("feedback-form")
root.geometry("400x400")

label_name = tk.Label(root, text = "name", font = "Arial 12")
label_name.pack(pady = 5)
entry_name = tk.Entry(root, font = "Arial 12")
entry_name.pack(pady = 5 , padx = 20)


label_email = tk.Label(root, text = "email", font = "Arial 12")
label_email.pack(pady = 5)
entry_email = tk.Entry(root, font = "Arial 12")
entry_email.pack(pady = 5 , padx = 20)




label_feedback = tk.Label(root, text = "feedback", font = "Arial 12")
label_feedback.pack(pady = 5)
entry_feedback = tk.Text(root, font = "Arial 12", height = 4)
entry_feedback.pack(pady = 5 , padx = 20)



btn_submit = tk.Button(root, text = "submit", font = "Arial 12", command=submit_form)
btn_submit.pack(pady = 20)





root.mainloop()