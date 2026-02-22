class Student: 
    def __init__(self ,  name , student_id , grades):
        self.student_id = student_id
        self.name = name
        self.__grades = grades

    def calculate_average(self):
        if len(self.__grades) == 0:
            return 0
        return sum(self.__grades) / len(self.__grades)

    def grade_category(self):
        average = self.calculate_average()
        if average >= 90 and average <= 100 : return 'Excellent'
        elif average >= 80 : return 'Very Good'
        elif average >= 70 : return 'Good'
        elif average >= 60 : return 'excepted'
        elif average >= 50 : return 'bad'
        else : return 'Fail'

    @property
    def grades(self):
        return self.__grades

class Classroom:
    def __init__(self):
        self.students_list = []

    def add_student(self , student ):
        self.students_list.append(student)

    def search_student(self , s_id):
        for i in self.students_list:
            if str(i.student_id) == str(s_id) : return i
        return None

    def remove_student(self , s_id ):
        for i in self.students_list:
            if str(i.student_id) == str(s_id):
                self.students_list.remove(i)
                return True
        return False

    def calculate_classroom_average(self):
        if not self.students_list:
            return 0
        total = 0
        for s in self.students_list:
            total += s.calculate_average()
        return total / len(self.students_list)