import tkinter as tk
from tkinter import ttk

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
















root.mainloop()