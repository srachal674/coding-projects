import tkinter as tk
from tkinter import ttk, filedialog
import openpyxl

def import_roster():
    file_path = filedialog.askopenfilename(
        title="Select PowerSchool Roster",
        filetypes=[
            ("Excel files", "*.xlsx"),
            ("All files", "*.*")
        ]
    )

    if file_path:
        print("File selected:", file_path)
    else:
        print("No file selected.")

def open_roster():
    roster_window = tk.Toplevel(root)

    roster_window.title("Student Roster")
    roster_window.geometry("800x500")
    roster_title = ttk.Label(
        roster_window,
        text="Student Roster",
        font=("Arial", 20, "bold")
    )

    roster_title.pack(pady=20)
    roster_frame = ttk.Frame(roster_window)
    roster_frame.pack(padx=20, pady=10, fill="both", expand=True)

    import_button = ttk.Button(
        roster_frame,
        text="Import Roster",
        command=import_roster
    )
    import_button.pack(pady=10)

root = tk.Tk()
root.title("Tier Contacts")
root.geometry("900x600")

title_label = ttk.Label(
    root,
    text="Tier Contacts",
    font=("Arial", 24, "bold")
)
title_label.pack(pady=30)

menu_frame = ttk.Frame(root)
menu_frame.pack(pady=20)

roster_button = ttk.Button(
    menu_frame,
    text="Student Roster",
    command=open_roster
)
roster_button.pack(pady=10)














root.mainloop()