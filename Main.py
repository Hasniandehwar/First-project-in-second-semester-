import tkinter as tk
from tkinter import messagebox
from Increment import Incerment_per_Year
from Salary import SalaryIncrease
from Apply_A import Apply_Absent

class SalaryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Salary Management System")

        # Add form labels and input fields
        tk.Label(self.root, text="Employee Name:", bg= "green", fg= "white").grid(row=0, column=0)
        self.entry_name = tk.Entry(self.root)
        self.entry_name.grid(row=0, column=1)

        tk.Label(self.root, text="Grade:", bg= "yellow", fg= "white").grid(row=1, column=0)
        self.entry_grade = tk.Entry(self.root)
        self.entry_grade.grid(row=1, column=1)

        tk.Label(self.root, text="Salary:", bg= "lightblue", fg= "white").grid(row=2, column=0)
        self.entry_salary = tk.Entry(self.root)
        self.entry_salary.grid(row=2, column=1)

        tk.Label(self.root, text="Percentage Increase:", bg= "lightpink", fg= "white").grid(row=3, column=0)
        self.entry_percentage = tk.Entry(self.root)
        self.entry_percentage.grid(row=3, column=1)

        tk.Label(self.root, text="Absent Days:", bg= "red", fg= "white").grid(row=4, column=0)
        self.entry_absent_days = tk.Entry(self.root)
        self.entry_absent_days.grid(row=4, column=1)

        # Add buttons
        increment_button = tk.Button(self.root, text="Apply Increment", command=self.on_increment, bg="lightblue", fg="White")
        increment_button.grid(row=5, column=0)

        increase_button = tk.Button(self.root, text="Increase Salary", command=self.on_salary_increase,bg="green", fg="white")
        increase_button.grid(row=5, column=1)

        absent_button = tk.Button(self.root, text="Handle Absence", command=self.on_absent, bg="red", fg="white")
        absent_button.grid(row=5, column=2)

    def on_increment(self):
        try:
            name = self.entry_name.get()  # Get employee name
            grade = int(self.entry_grade.get())  # Get employee grade from user input
            salary = float(self.entry_salary.get())  # Get salary input from user

            increment = Incerment_per_Year(salary, grade)  # Initialize the increment class with salary
            final_salary, increment_amount = increment.apply_increment(grade)  # Pass the grade to apply_increment

            messagebox.showinfo("Increment Applied", f"Increment: {increment_amount}\nTotal Salary: {final_salary:.2f}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid data!")

    def on_salary_increase(self):
        try:
            name = self.entry_name.get()
            salary = float(self.entry_salary.get())
            percentage = float(self.entry_percentage.get())
            grade = int(self.entry_grade.get())  # Assuming you have an entry field for grade as well

            salary_increase = SalaryIncrease(salary, grade)  # Pass both salary and grade
            new_salary, increase_amount = salary_increase.apply_increase(percentage)

            messagebox.showinfo("Salary Increased", f"Increase: {increase_amount}\nNew Salary: {new_salary:.2f}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid data!")

    def on_absent(self):
        try:
            name = self.entry_name.get()
            salary = float(self.entry_salary.get())
            absent_days = int(self.entry_absent_days.get())

            absent = Apply_Absent(salary)
            remaining_salary, deduction = absent.Absent(absent_days)

            messagebox.showinfo("Absence Deduction", f"Days Absent: {absent_days}\nDeduction: {deduction:.2f}\nRemaining Salary: {remaining_salary:.2f}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid data!")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = SalaryApp(root)
    root.mainloop()
