from datetime import datetime

class Student:

    def __init__(self, studid, name, dob, classification):
        self.__studid = studid
        self.__name = name
        self.__dob = dob
        self.__classification = classification

    def calculate_age(self):
        today = datetime.today()
        dob_year = int(self.__dob.split("/")[2])
        age = today.year - dob_year
        return age

    def get_registration_dates(self):
        registration_dates = {
            'Senior': '4/1 thru 4/3',
            'Junior': '4/4 thru 4/6',
            'Sophomore': '4/7 thru 4/9',
            'Freshman': '4/10 thru 4/12'
        }
        return registration_dates[self.__classification]

    def display_student(self):
        age = self.calculate_age()
        registration_dates = self.get_registration_dates()
        print(f"{self.__name} is {age} years old and can register from {registration_dates}.")
