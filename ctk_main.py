import tkinter as tk
import customtkinter as ctk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
root = ctk.CTk()
root.geometry("1000x750")
root.title("Hello World")

label = tk.Label(root, text="Hello", font=("Arial", 24))
label.pack()

options = ["Option 1", "Option 2", "Option 3"]
dropdown = ctk.CTkComboBox(root,values=options)
dropdown.pack()

root.mainloop()