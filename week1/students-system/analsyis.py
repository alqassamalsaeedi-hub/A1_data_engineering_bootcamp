def get_top_student(classroom):
    if not classroom.students_list:
        return None
    return max(classroom.students_list , key=lambda i:i.calculate_average())

def get_lowest_student(classroom):
    if not classroom.students_list:
        return None
    return min(classroom.students_list , key=lambda i:i.calculate_average())

def grade_distribution(classroom):
    counts = {"Excellent": 0, "Very Good": 0, "Good": 0, "excepted": 0, "bad": 0, "Fail": 0}
    for s in classroom.students_list:
        category = s.grade_category()
        if category in counts:
            counts[category] += 1
    return counts