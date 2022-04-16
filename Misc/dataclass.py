from dataclasses import dataclass

@dataclass
class Employee:
    """Class for storing Employee data"""
    id: int
    forename: str
    surname: str
    dob: str
    employment_details: str
    employee_details: str

    def __repr__(self):
        return f"<Employee {self.forename} {self.surname}>"

    def __str__(self):
        return self.__repr__()

chris = Employee(0, "Chris", "Fires", "09/02/1999", "balh", "wah")

class x:
    pass

y = x()
z = x()
