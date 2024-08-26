import json


students = {}


def add():
    full_name = input("Enter student's name:")
    while True:
        try:
            math_grade = float(input(f'Enter {full_name} grade in Math: '))
            if math_grade < 0 or math_grade > 100:
                print('Grade should be in 0-100 range')
                continue
            break
        except ValueError:
            print('The grade should be an integer')
    while True:
        try:
            science_grade = float(input(f'Enter {full_name} grade in Science: '))
            if 0 > science_grade or science_grade > 100:
                print('Grade should be in 0-100 range')
                continue
            break
        except ValueError:
            print('The grade should be an integer')
    while True:
        try:
            english_grade = float(input(f'Enter {full_name} grade in English: '))
            if 0 > english_grade or english_grade > 100:
                print('Grade should be in 0-100 range')
                continue
            break
        except ValueError:
            print('The grade should be an integer')

    students[full_name] = {
        'Math': math_grade,
        'Science': science_grade,
        'English': english_grade,
        'Average': round((math_grade + science_grade + english_grade) / 3)
    }


def display():
    if not students:
        print('There is no students available')
    else:
        for student, grades in students.items():
            print(f'Student: {student}')
            for subject, grade in grades.items():
                print(f'{subject}: {grade}')


def find_top():
    if not students:
        print("No students available.")
    else:
        top_student = max(students, key=lambda name: students[name]['Average'])
        print(f"Top student: {top_student} with an average grade of {students[top_student]['Average']}")


def save_data():
    with open('students.json', mode='w') as file:
        json.dump(students, file)
    print('Data saved successfully')


def load_data():
    global students
    with open('students.json', mode='r') as file:
        students = json.load(file)
        print(students)


def main():
    while True:
        print(f'''
        1. Add a new student
        2. Display all students and their grades
        3. Find the top student
        4. Save data to file
        5. Load data from file
        6. Exit''')

        while True:
            try:
                user = int(input('Choose an option between 1-6: '))
                if user not in [1, 2, 3, 4, 5, 6]:
                    print('Input should be integer between 1-6')
                    continue
                else:
                    break
            except ValueError:
                print('Input should be integer')

        match user:
            case 1: add()
            case 2: display()
            case 3: find_top()
            case 4: save_data()
            case 5: load_data()
            case 6:
                print('Goodbye!')
                quit()


if __name__ == '__main__':
    main()
