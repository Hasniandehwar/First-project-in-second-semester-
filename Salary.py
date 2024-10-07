# salary_increase.py
from Allowences import Allowance

class SalaryIncrease:
    def __init__(self, salary, grade):
        self.salary = salary
        self.allowance = Allowance(grade)  # Initialize the allowance with the grade

    def apply_increase(self, percentage):
        # Subtract the total allowance (which is a float) from the salary
        basic_pay = self.salary - self.allowance.get_total_allowance()  
        increase_amount = basic_pay * percentage / 100
        new_salary = self.salary + increase_amount
        return new_salary, increase_amount
