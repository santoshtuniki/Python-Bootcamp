student_scores = {
    'Harry': 81,
    'Ron': 78,
    'Hermione': 99,
    'Draco': 74,
    'Neville': 62,
}

student_grades = {}


def grades(score):
    if score > 90 and score <= 100:
        return 'Outstanding'
    elif score > 80 and score <= 90:
        return 'Exceeds Expectations'
    elif score > 70 and score <= 80:
        return 'Acceptable'
    else:
        return 'Fail'


for key in student_scores:
    student_grades[key] = grades(student_scores[key])

print(student_grades)
