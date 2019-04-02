employees = []

class Employee :

    office_name = "Nimmetry Inc "

    def __init__(self,name,last_name,designation,employee_id=332,):
        self.name = name
        self.employee_id = employee_id
        self.last_name = last_name
        self.designation = designation
        employees.append(self)

    def __str__(self):
        return "employee "+ self.name

    def get_name_capitalize(self):
        return  self.name.capitalize()

    def get_last_name_capitalize(self):
        return  self.last_name.capitalize()


    def get_office_name(self):
        return self.office_name