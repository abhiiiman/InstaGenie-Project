# importing the required libs here.

from tkinter import *
import tkinter as tk
from tkinter import messagebox
import webbrowser

# creating the functions here.
def on_enter1(e):
    entry_1.delete(0, "end")
    entry_1.configure(font=("Microsoft YaHei UI Light", 15, "bold"), fg = "black")

def on_leave1(e):
    email_value = entry_1.get()
    if email_value == "":
        entry_1.insert(0, "Email")
        entry_1.configure(font="Ubuntu 15 bold", fg = "grey")

def on_enter2(e):
    entry_2.delete(0, "end")
    entry_2.configure(font=("Microsoft YaHei UI Light", 15, "bold"), fg = "black", show = u"\u25CF")

def on_leave2(e):
    password_value = entry_2.get()
    if password_value == "":
        entry_2.insert(0, "Password")
        entry_2.configure(font="Ubuntu 15 bold", fg = "grey", show = "")

def get_values():
    if entry_1.get() == "Email" or entry_2.get() == "Password":
        messagebox.showwarning("Invalid Details", "Provide The Required Credentials First !")
    else:
        print(f"Email = {entry_1.get()}")
        print(f"Password = {entry_2.get()}")

def forgot_password():
    print("forgot password !")

def insta_btn():
    response = messagebox.askyesno("InstaGram Redirect", "Opening InstaGram\nAre You Sure?")
    if response == True:
        webbrowser.open("https://www.instagram.com/_m_abhijit_/")
    else:
        pass
def youtube_btn():
    response = messagebox.askyesno("YouTube Redirect", "Opening YouTube\nAre You Sure?")
    if response == True:
        webbrowser.open("https://youtube.com/@m_abhijit_")
    else:
        pass
def linkedin_btn():
    response = messagebox.askyesno("LinkedIn Redirect", "Opening LinkedIn\nAre You Sure?")
    if response == True:
        webbrowser.open("https://www.linkedin.com/in/abhijit-mandal-842428220")
    else:
        pass
def github_btn():
    response = messagebox.askyesno("GitHub Redirect", "Opening GitHub\nAre You Sure?")
    if response == True:
        webbrowser.open("https://github.com/abhiiiman")
    else:
        pass

def sign_up():
    print("create new account")

# creating the window here.
window = Tk()
window.title("InstaGenie - Your InstaGram Genie : Login")
height = 630
width = 960
window.geometry(f"{width}x{height}")
window.resizable(False, False)
window.iconbitmap("icon.ico")

# placing the window at the center here.
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = (screen_width / 2) - (width / 2)
y_coordinate = (screen_height / 2) - (height / 2)
window.geometry("%dx%d+%d+%d" % (width, height, x_coordinate, y_coordinate))

# creating the background canvas here.
canvas = Canvas(window,bg = "white",height = 630,width = 960,bd = 0,highlightthickness = 0,relief = "ridge")
canvas.place(x = 0, y = 0)
background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(480.0, 315.0,image=background_img)

# creating the entry text feilds here.
entry_1 = Entry(bd=0, bg="#FFFFFF", highlightthickness=0, font="Ubuntu 15 bold", fg = "grey")
entry_1.insert(0, "Email")
entry_1.place(x=515, y=238, width=293.0, height=36.0)
entry_1.bind("<FocusIn>", on_enter1)
entry_1.bind("<FocusOut>", on_leave1)

entry_2 = Entry(bd=0, bg="#FFFFFF", highlightthickness=0, font="Ubuntu 15 bold", fg = "grey")
entry_2.insert(0, "Password")
entry_2.place(x=515, y=305, width=293.0, height=20.0)
entry_2.bind("<FocusIn>", on_enter2)
entry_2.bind("<FocusOut>", on_leave2)

# creating the buttons here.
button_1 = Button(text = "Get Started Now", font = "Ubuntu 16 bold", relief="flat",background="#30BBC8", activebackground="#30BBC8", borderwidth = 0, highlightthickness = 0, command = get_values)
button_1.place(x=573.0, y=365.0, width=165.0, height=30.0)

button_2 = Button(text = "Forgot Password ?", font = "Ubuntu 16 bold", relief="flat",background="#B5A3FF", activebackground="#B5A3FF", borderwidth = 0, highlightthickness = 0, command = forgot_password)
button_2.place(x=553.0, y=430.0, width=200.0, height=30.0)

button_3 = Button(text = "Create New Account", font = "Ubuntu 15 bold", relief="flat",background="#F96EBF", activebackground="#F96EBF", borderwidth = 0, highlightthickness = 0, command = sign_up)
button_3.place(x=160.0, y=458.0, width=205.0, height=30.0)

img1 = PhotoImage(file="button1.png")
b1 = Button(image = img1,borderwidth = 0,highlightthickness = 0,command = insta_btn,relief = "flat", bg = "#AFA8BF", activebackground = "#AFA8BF")
b1.place(x = 158, y = 386)

img2 = PhotoImage(file="button2.png")
b2 = Button(image = img2,borderwidth = 0,highlightthickness = 0,command = youtube_btn,relief = "flat", bg = "#AFA8BF", activebackground = "#AFA8BF")
b2.place(x = 198, y = 386)

img3 = PhotoImage(file="button3.png")
b3 = Button(image = img3,borderwidth = 0,highlightthickness = 0,command = linkedin_btn,relief = "flat", bg = "#AFA8BF", activebackground = "#AFA8BF")
b3.place(x = 240, y = 386)

img4 = PhotoImage(file="button4.png")
b4 = Button(image = img4,borderwidth = 0,highlightthickness = 0,command = github_btn,relief = "flat", bg = "#AFA8BF", activebackground = "#AFA8BF")
b4.place(x = 282, y = 386)

# running the window in loop here.
window.mainloop()
