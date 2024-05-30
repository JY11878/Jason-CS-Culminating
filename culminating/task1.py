# student Information system
import tkinter as tk
from tkinter import messagebox

class students:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

class studentInformationSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Information System")

        self.students = []

        # Name label and entry
        self.nameLabel = tk.Label(root, text="Name:")
        self.nameLabel.pack()
        self.nameEntry = tk.Entry(root)
        self.nameEntry.pack()

        # Age label and entry
        self.ageLabel = tk.Label(root, text="Age:")
        self.ageLabel.pack()
        self.ageEntry = tk.Entry(root)
        self.ageEntry.pack()

        # Grade label and entry
        self.gradeLabel = tk.Label(root, text="Grade:")
        self.gradeLabel.pack()
        self.gradeEntry = tk.Entry(root)
        self.gradeEntry.pack()

        # Add student button
        self.addButton = tk.Button(root, text="Add Student", command=self.addStudent)
        self.addButton.pack()

        # Display students button
        self.displayButton = tk.Button(root, text="Display Students", command=self.displayStudents)
        self.displayButton.pack()

        # Search student label and entry
        self.searchLabel = tk.Label(root, text="Search by Name:")
        self.searchLabel.pack()
        self.searchEntry = tk.Entry(root)
        self.searchEntry.pack()
        self.searchButton = tk.Button(root, text="Search Student", command=self.searchStudent)
        self.searchButton.pack()

        # Update student label and entry
        self.updateLabel = tk.Label(root, text="Update by Name:")
        self.updateLabel.pack()
        self.updateEntry = tk.Entry(root)
        self.updateEntry.pack()
        self.updateButton = tk.Button(root, text="Update Student", command=self.updateStudent)
        self.updateButton.pack()

    def addStudent(self):
        # Get input values
        name = self.nameEntry.get()
        age = self.ageEntry.get()
        grade = self.gradeEntry.get()

        # Validate inputs
        if name == "" or age == "" or grade == "":
            messagebox.showerror("Input Error", "All fields are required")
            return

        try:
            age = int(age)
        except ValueError:
            messagebox.showerror("Input Error", "Age must be a number")
            return

        # Create student object
        student = students(name, age, grade)
        self.students.append(student)
        messagebox.showinfo("Success", "Student added successfully!")
        self.clearEntries()

    def displayStudents(self):
        # Check if list is empty
        if len(self.students) == 0:
            messagebox.showinfo("No Students", "No student records available.")
            return

        # Display student information
        studentsInfo = ""
        for student in self.students:
            studentsInfo += f"Name: {student.name}, Age: {student.age}, Grade: {student.grade}\n"
        messagebox.showinfo("Student Records", studentsInfo)

    def searchStudent(self):
        # Get search name
        searchName = self.searchEntry.get()
        if searchName == "":
            messagebox.showerror("Input Error", "Please enter a name")
            return

        # Search for student
        for student in self.students:
            if student.name == searchName:
                messagebox.showinfo("Student Found", f"Name: {student.name}, Age: {student.age}, Grade: {student.grade}")
                return
        messagebox.showinfo("Not Found", "Student not found.")

    def updateStudent(self):
        # Get update name
        updateName = self.updateEntry.get()
        if updateName == "":
            messagebox.showerror("Input Error", "Please enter a name")
            return

        # Update student information
        for student in self.students:
            if student.name == updateName:
                newAge = self.ageEntry.get()
                newGrade = self.gradeEntry.get()
                if newAge == "" or newGrade == "":
                    messagebox.showerror("Input Error", "Both age and grade are needed")
                    return
                try:
                    student.age = int(newAge)
                except ValueError:
                    messagebox.showerror("Input Error", "Age should be a number")
                    return
                student.grade = newGrade
                messagebox.showinfo("Success", "Student updated successfully!")
                self.clearEntries()
                return
        messagebox.showinfo("Not Found", "Student not found")

    def clearEntries(self):
        # Clear all entries
        self.nameEntry.delete(0, tk.END)
        self.ageEntry.delete(0, tk.END)
        self.gradeEntry.delete(0, tk.END)
        self.searchEntry.delete(0, tk.END)
        self.updateEntry.delete(0, tk.END)

# Create main window
root = tk.Tk()
app = studentInformationSystem(root)
root.mainloop()

