def main_of_students_teacher():
    lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
    }
    alice = {
        "name": "Alice",
        "homework": [100.0, 92.0, 98.0, 100.0],
        "quizzes": [82.0, 83.0, 91.0],
        "tests": [89.0, 97.0]
    }
    tyler = {
        "name": "Tyler",
        "homework": [0.0, 87.0, 75.0, 22.0],
        "quizzes": [0.0, 75.0, 78.0],
        "tests": [100.0, 100.0]
    }

    # Add your function below!
    total =0
    def average(numbers):
        total = sum(numbers)
        total = float(total)
        return total/len(numbers)


    # for calculating average marks of student
    def get_average(student):
        homework = average(student["homework"])
        quizzes = average(student["quizzes"])
        tests = average(student["tests"])
        return 0.1*homework + 0.3*quizzes + 0.6*tests
    total = get_average(alice)
    print(total)

    def get_ledder_grade(score):
        if score>=90:
            return "A"
        elif score>=80:
            return "B"
        elif score>=70:
            return "C"
        elif score>=60:
            return "D"
        else:
            return "F"


        print(get_letter_grade(total))






    def get_class_average(students):
        results = []
        avg = 0
        for student in students:

            results.append(get_average(student))

        return average(results)

    students =[lloyd,alice,tyler]
    total = get_class_average(students)
    print(total)


    print(get_ledder_grade(get_class_average(students)))
