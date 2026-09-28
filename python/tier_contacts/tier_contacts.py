import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import openpyxl
import sqlite3

def setup_database():
    connection = sqlite3.connect("tier_contacts.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id TEXT PRIMARY KEY, 
            name TEXT NOT NULL,
            grade TEXT,
            phone TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS enrollments (
            student_id TEXT NOT NULL,
            course TEXT NOT NULL,
            PRIMARY KEY (student_id, course),
            FOREIGN KEY(student_id) REFERENCES students(student_id)
        )
    """)

    connection.commit()
    connection.close()

#This prompts user to import their roster
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

        #This checks for missing columns in source spreadsheet
        if missing_headers:
            messagebox.showerror(
                "Invalid Roster",
                "Missing required columns: " + "," .join(missing_headers)
            )
        else:
            messagebox.showinfo(
                "Roster Valid",
                "The roster contains all required columns."
            )

            column_map = {
                "Id": headers.index("Id"),
                "Name": headers.index("Name"),
                "Grade": headers.index("Grade"),
                "Phone": headers.index("Phone"),
                "Course": headers.index("Course")
            }

            students = {}

            for row in worksheet.iter_rows(min_row=2, values_only=True):
                student_id = row[column_map["Id"]]
                name = row[column_map["Name"]]
                grade = row[column_map["Grade"]]
                phone = row[column_map["Phone"]]
                course = row[column_map["Course"]]

                if student_id not in students:
                    students[student_id] = {
                        "id": student_id,
                        "name": name,
                        "grade": grade,
                        "phone": phone,
                        "courses": []
                    }
                students[student_id]["courses"].append(course)

            connection = sqlite3.connect("tier_contacts.db")
            cursor = connection.cursor()

            for student in students.values():
                cursor.execute("""
                    INSERT OR REPLACE INTO students (
                        student_id,
                        name,
                        grade,
                        phone
                    )
                    VALUES (?, ?, ?, ?)
                """, (
                    student["id"],
                    student["name"],
                    student["grade"],
                    student["phone"]
                ))

                for course in student["courses"]:
                    cursor.execute("""
                        INSERT OR IGNORE INTO enrollments (
                        student_id,
                        course
                        )
                        VALUES (?, ?)
                    """, (
                        student["id"],
                        course
               ))

            connection.commit()
            connection.close()

            print("Roster saved to database.")
                    
            print("Roster rows:", worksheet.max_row - 1)
            print("Unique students:", len(students))
            
        print("Header found:", headers)
        print("Missing headers:", missing_headers)

    else:
        multiple_course_students = 0
        
            for student in students.values():
                if len(student["courses"])>1:
                    multiple_course_students += 1
            print("Students with multiple courses:", multiple_course_students)        
    
            for row in worksheet.iter_rows(min_row=1, max_row=5, values_only=True):
                print(row)
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

    roster_table = ttk.Treeview(
        roster_frame,
        columns=("Id", "Name", "Grade", "Phone", "Courses"),
        show="headings"
    )
    roster_table.heading("Id", text="Id")
    roster_table.heading("Name", text="Name")
    roster_table.heading("Grade", text="Grade")
    roster_table.heading("Phone", text="Phone")
    roster_table.heading("Courses", text="Course(s)")
    roster_table.pack(fill="both", expand=True, pady=10)

setup_database()

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