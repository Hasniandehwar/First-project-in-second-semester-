# absent.py
class Apply_Absent:
    def __init__(self, Salary ,):
        self.Salary=Salary
        self.Total_number_Days= 30
    def Absent(self, Days , ): # Dedction form your salary if you are abesent 
        
        if Days>=1 and Days <= self. Total_number_Days:  # Comdition for the days 
            daily_salary = self.Salary / self.Total_number_Days # calculating daily base salary
            deduction= daily_salary * Days # simply perfoming calculation for the ddeduction   
            remaining_salary = self.Salary - deduction  # dedction form the Salary 
           
            return remaining_salary, deduction

        else: # some Months have 31 days 
            daily_salary = self.Salary / self.Total_number_Days 
            deduction= daily_salary * Days
            remaining_salary = self.Salary - deduction
            return remaining_salary, deduction