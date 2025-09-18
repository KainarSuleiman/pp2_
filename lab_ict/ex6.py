
students = [('Akezhan', 85), ('Kainar', 92), ('Timur', 78), ('Ali', 88)]


def get_score(student):
    return student[1]

students.sort(key=get_score, reverse=True)

for student, score in students:
    print(f"{student}: {score}")