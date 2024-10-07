class Incerment_per_Year:
    def __init__(self, salary,grade):
        # Initializing the grade increments
        self.grade_1 = 145
        self.grade_2 = 200
        self.grade_3 = 300
        self.grade_4 = 400
        self.grade_5 = 500
        self.grade_6 = 600
        self.grade_7 = 700
        self.grade_8 = 800
        self.grade_9 = 900
        self.grade_10 = 1000
        self.grade_11 = 1100
        self.grade_12 = 1200
        self.grade_13 = 1300
        self.grade_14 = 1400
        self.grade_15 = 1500
        self.grade_16 = 1600
        self.grade_17 = 1700
        self.grade_18 = 1800
        self.grade_19 = 1900
        self.grade_20 = 2000
        self.grade_21 = 2100
        self.grade_22 = 2200
        self.salary = salary
    

    def get_increment(self, grade,):
        # Return the increment based on the grade
        if grade == 1:
            return self.grade_1
        elif grade == 2:
            return self.grade_2
        elif grade == 3:
            return self.grade_3
        elif grade == 4:
            return self.grade_4
        elif grade == 5:
            return self.grade_5
        elif grade == 6:
            return self.grade_6
        elif grade == 7:
            return self.grade_7
        elif grade == 8:
            return self.grade_8
        elif grade == 9:
            return self.grade_9
        elif grade == 10:
            return self.grade_10
        elif grade == 11:
            return self.grade_11
        elif grade == 12:
            return self.grade_12
        elif grade == 13:
            return self.grade_13
        elif grade == 14:
            return self.grade_14
        elif grade == 15:
            return self.grade_15
        elif grade == 16:
            return self.grade_16
        elif grade == 17:
            return self.grade_17
        elif grade == 18:
            return self.grade_18
        elif grade == 19:
            return self.grade_19
        elif grade == 20:
            return self.grade_20
        elif grade == 21:
            return self.grade_21
        elif grade == 22:
            return self.grade_22

    def apply_increment(self,grade):
        # Get the increment based on the grade
        increment = self.get_increment(grade)
        # Add the increment to the salary and return the updated salary and the increment amount
        return self.salary + increment, increment
