import tkinter as tk
from tkinter import ttk

def open_roster():
    print("Opening Student Roster")
    
root = tk.Tk()
root.title("Tier Contacts")
root.geometry("900x600")

title_lable = ttk.Label(
    root,
    text="Tier Contacts",
    font=("Arial", 24, "bold")
)
title_lable.pack(pady=30)

menu_frame = ttk.Frame(root)
menu_frame.pack(pady=20)

roster_button = ttk.Button(
    menu_frame,
    text="Student Roster"
    command=open_roster
)
roster_button.pack(pady=10)














root.mainloop()