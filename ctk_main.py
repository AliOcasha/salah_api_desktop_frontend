import tkinter as tk
import customtkinter as ctk
from datetime import datetime
# Views
global clock
global dropdown
## Prayer Views
global fajr
global dhuhr
global asr
global maghreb
global ischaa

def intialize():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    root.title("Hello World")
    root.geometry("960x540")

def draw_clock():
    global clock
    clock = ctk.CTkLabel(root, text=datetime.now().strftime("%H:%M %S"), font=("Arial", 120))
    clock.pack_configure(side="top")

def draw_dropdown():
    global dropdown
    options = ["Option 1", "Option 2", "Option 3"]
    dropdown = ctk.CTkComboBox(root,values=options,height=72,width=300)
    dropdown.pack_configure(side="bottom")

def create_prayer_element(prayer_name,prayer_time):
    frame = ctk.CTkFrame(root)
    time = ctk.CTkLabel(frame,text=prayer_time,font=("Arial",30))
    label = ctk.CTkLabel(frame,text=prayer_name,font=("Arial",30))
    time.pack()
    label.pack()
    return frame

def draw_prayer_widgets():
    global fajr
    global dhuhr
    global asr
    global maghreb
    global ischaa
    fajr = create_prayer_element("Fajr","01:00")
    fajr.pack(side="left", fill="x", expand=True) 

    dhuhr = create_prayer_element("Dhuhr","02:00") 
    dhuhr.pack(side="left", fill="x", expand=True)   
    asr = create_prayer_element("Asr","03:00")
    asr.pack(side="left", fill="x", expand=True)   
    maghreb = create_prayer_element("Maghreb","04:00")
    maghreb.pack(side="left", fill="x", expand=True)   
    ischaa = create_prayer_element("Ischaa","05:00")
    ischaa.pack(side="left", fill="x", expand=True)   
def draw():
    draw_clock()
    draw_dropdown()
    draw_prayer_widgets()

def clock_update_init():
    clock.configure(text=datetime.now().strftime("%H:%M %S"))
    root.after(1000,clock_update_init)

root = ctk.CTk()
intialize()
draw()
clock_update_init()
root.mainloop()