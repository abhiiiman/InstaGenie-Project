#importing library
from tkinter import *
from PIL import ImageTk, Image
import time
import customtkinter
import os
import sys
import subprocess

# updating the progressbar here logically.
def update_progress():
    global progressbar, current_value
    current_value += 1
    if current_value < 50:
        progressbar.step()
        progressbar.update_idletasks()
        w.after(50, update_progress)
    else:
        progressbar.set(current_value)
        w.destroy()
        py = sys.executable
        # os.system(("%s %s") % (py, "window.py"))
        subprocess.run([py, "window.py"])

w = customtkinter.CTk()
width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
w.overrideredirect(1) #for hiding titlebar

# creating the background canvas with image here.
canvas = Canvas(w,bg = "white",height = 630,width = 960,bd = 0,highlightthickness = 0,relief = "ridge")
canvas.place(x = 0, y = 0)
background_img = PhotoImage(file = f"splashbg.png")
background = canvas.create_image(213.0, 125.0,image=background_img)

# creating the progressbar here.
progressbar = customtkinter.CTkProgressBar(w, width = 280, fg_color = "grey", progress_color = "white")
progressbar.place(x = 70, y = 150)
current_value = 0
progressbar.set(current_value)
w.after(30, update_progress)

# running the loop here.
w.mainloop()
