import tkinter as tk
from tkinter import ttk, filedialog, messagebox
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
        workbook = openpyxl.load_workbook(file_path)
        print("Workbook opened successfully!")
        print("Worksheets:", workbook.sheetnames)
        worksheet = workbook.active

        headers = [cell.value for cell in worksheet[1]]
        required_headers = ['Id', 'Name', 'Grade', 'Phone', 'Course']
        missing_headers = []
        for header in required_headers:
            if header not in headers:
                missing_headers.append(header)


        if missing_headers:
            messagebox.showerror(
                "Invalid Roster",
                "Missing required colimns: " + "," .join(missing_headers)
            )
        else:
            messagebox.showinfo(
                "Roster Valid",
                "The roster contains all required columns."
            )
        
        print("Header found:", headers)
        print("Missing headers:", missing_headers)

        for row in worksheet.iter_rows(min_row=1, max_row=5, values_only=True):
            print(row)

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