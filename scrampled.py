#---------------------SAVING THE RECORD------------------------------
def save():
    website_entry.get()
    email_entry.get()
    password_entry.get()
    with open("Data.txt", "a") as data_file:
        data_file.write(f"{website_entry} |  {email_entry} | {password_entry}")




#---------------UI SETUP FOR PASSWORD GENERATOR-----------------------

from tkinter import *
window = Tk()
window.title("Password Generator")
window.minsize(height=500, width=400)
window.config(padx= 20, pady=20)

#CANVAS FOR LOGO
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="icon.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0, column=1)

#LABESL

website = Label(text="Website")
website.grid(row=1,column=0)

email = Label(text = "Email/Username")
email.grid(row=2,column=0)
password = Label(text="Password")
password.grid(row=3,column=0)

#ENTRY
website_entry= Entry(width=35)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width = 35)
email_entry.grid(row=2, column=1)
password_entry = Entry(width = 35)
password_entry.grid(row=3, column=1)

#BUTTON

generate_button = Button(text = "Generate & Copy")
generate_button.grid(row= 4, column=1)
add_button = Button(text="Save Record", command= save)
add_button.grid(row=5, column=1)



window.mainloop()