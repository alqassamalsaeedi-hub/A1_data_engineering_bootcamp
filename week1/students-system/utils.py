import csv
import os

def save_to_csv(classroom , file_name = 'data.csv'):
    with open(file_name , 'w' , newline= '', encoding='utf-8') as f:
        writer = csv.writer(f)
        for s in classroom.students_list:
            grades_str = ",".join(map(str, s.grades))
            writer.writerow([s.name, s.student_id, grades_str])

def load_student(file_name = 'data.csv'):
    from models import Student
    students = []
    if not os.path.exists(file_name):
        return students
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            reader=csv.reader(f)
            for row in reader:
                if len(row) == 3:
                    name, s_id, g_str = row
                    g_list = [float(x) for x in g_str.split(",")] if g_str else []
                    students.append(Student(name, s_id, g_list))
    except FileNotFoundError:
        pass 
    return students

class Validator:
    @staticmethod
    def is_valid_grade(grade):
        try:
            g = float(grade)
            return 0 <= g <= 100
        except:
            return False

    @staticmethod
    def is_valid_id(student_id):
        try:
            s_id = str(student_id).strip()
            return s_id.isdigit() and len(s_id) > 0
        except:
            return False

    @staticmethod
    def is_valid_name(name):
        try:
            clean_name = str(name).replace(" ", "")
            return clean_name.isalpha() and len(name.strip()) > 2
        except:
            return False