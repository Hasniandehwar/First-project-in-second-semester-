class Allowance:
    def __init__(self, grade):
        self.grade = grade
        self.housing_allowance = 0
        self.transport_allowance = 0
        self.medical_allowance = 0
        self.calculate_allowances()

    def calculate_allowances(self):
        
        # These are just examples; you can adjust the values as needed
        if self.grade == 1:
            self.housing_allowance = 500
            self.transport_allowance = 200
            self.medical_allowance = 100
        
        elif self.grade == 2:
            self.housing_allowance = 500
            self.transport_allowance = 200
            self.medical_allowance = 100
        
        elif self.grade == 3:
            self.housing_allowance = 500
            self.transport_allowance = 200
            self.medical_allowance = 100
        
        
        elif self.grade == 4:
            self.housing_allowance = 500
            self.transport_allowance = 200
            self.medical_allowance = 100
        
        elif self.grade == 5:
            self.housing_allowance = 500
            self.transport_allowance = 200
            self.medical_allowance = 100
        
        
        elif self.grade == 6:
            self.housing_allowance = 500
            self.transport_allowance = 200
            self.medical_allowance = 100
        
        elif self.grade == 7:
            self.housing_allowance = 500
            self.transport_allowance = 200
            self.medical_allowance = 100
        
        elif self.grade == 8:
            self.housing_allowance = 500
            self.transport_allowance = 200
            self.medical_allowance = 100
        
        elif self.grade == 9:
            self.housing_allowance = 500
            self.transport_allowance = 200
            self.medical_allowance = 100
        
        elif self.grade == 10:
            self.housing_allowance = 500
            self.transport_allowance = 200
            self.medical_allowance = 100
        
        
        elif self.grade == 11:
            self.housing_allowance = 500
            self.transport_allowance = 200
            self.medical_allowance = 100
        
        
        elif self.grade == 12:
            self.housing_allowance = 500
            self.transport_allowance = 200
            self.medical_allowance = 100
        
        
        elif self.grade == 13:
            self.housing_allowance = 500
            self.transport_allowance = 200
            self.medical_allowance = 100
        
        elif self.grade == 14:
            self.housing_allowance = 500
            self.transport_allowance = 200
            self.medical_allowance = 100
        elif self.grade == 15:
            self.housing_allowance = 700
            self.transport_allowance = 300
            self.medical_allowance = 150
        elif self.grade == 16:
            self.housing_allowance = 1000
            self.transport_allowance = 400
            self.medical_allowance = 200
        elif self.grade==17:
            self.housing_allowance = 1200
            self.transport_allowance = 500
            self.medical_allowance = 300
        elif self.grade==18:
            self.housing_allowance = 1200
            self.transport_allowance = 500
            self.medical_allowance = 300
        elif self.grade==19:
            self.housing_allowance = 1200
            self.transport_allowance = 500
            self.medical_allowance = 300
        elif self.grade==20:
            self.housing_allowance = 1200
            self.transport_allowance = 500
            self.medical_allowance = 300
        elif self.grade==21:
            self.housing_allowance = 1200
            self.transport_allowance = 500
            self.medical_allowance = 300
        elif self.grade==22:
            self.housing_allowance = 1200
            self.transport_allowance = 500
            self.medical_allowance = 300
    
    def get_total_allowance(self):
        return self.housing_allowance + self.transport_allowance + self.medical_allowance
