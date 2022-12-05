from statistics import mean


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

    def mean_grades(self):
        list_grades = []
        all_grades = [el for el in self.grades.values()]
        for el in range(len(all_grades)):
            list_grades += all_grades[el]
        return round(mean(list_grades), 1)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такого лектора не существует')
            return
        return f'{self.mean_grades() < other.mean_grades()}\n'

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такого лектора не существует')
            return
        return f'{self.mean_grades() > other.mean_grades()}\n'


class Student(Mentor):

    def __init__(self, name, surname, gender):
        super().__init__(name, surname)
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []

    def __str__(self):
        return f"\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка " \
               f"за домашние задания: {Student.mean_grades(self)}\nКурсы в " \
               f"процессе изучения: {', '.join(self.courses_in_progress)}\n" \
               f"Завершенные курсы: {', '.join(self.finished_courses)}\n"

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress \
                and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f"\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка" \
               f" за лекции: {Lecturer.mean_grades(self)}"


class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"\nИмя: {self.name}\nФамилия: {self.surname}"


def average_grade_for_homework(list_of_student, course_name):
    x = []
    for el in list_of_student:
        if isinstance(globals()[el], Student) and course_name in globals()[
            el].grades.keys():
            x += globals()[el].grades[course_name]
            assessed_group = "студентов"
        elif isinstance(globals()[el], Lecturer) and course_name in globals()[
            el].grades.keys():
            x += globals()[el].grades[course_name]
            assessed_group = "лекторов"
        else:
            return f'\nПроизошла ошибка проверьте входные данные.'
    return f'\nСредняя оценка у {assessed_group} по предмету {course_name}: {round(mean(x), 1)}'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'C++']
best_student.finished_courses += ['Введение в программирование']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python', 'C++']

cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(best_student, 'C++', 7)
cool_reviewer.rate_hw(best_student, 'Python', 8)

print(best_student.grades)

lecturer = Lecturer('Evgeny', 'Shmargunov')
lecturer.courses_attached += ['Python']

best_student.rate_hw(lecturer, 'Python', 9)
best_student.rate_hw(lecturer, 'С++', 8)
best_student.rate_hw(lecturer, 'Python', 9)

print(lecturer.grades)

print(cool_reviewer)

print(lecturer)

print(best_student)

print(best_student < lecturer)

print(best_student > lecturer)

student_a = Student('Вадим', 'Розизнан', 'Мужчина')
student_a.courses_in_progress += ['Python', 'C++']
student_a.finished_courses += ['Введение в программирование']

reviewer_a = Reviewer('Ben', 'Duglas')
reviewer_a.courses_attached += ['Python', 'C++']

reviewer_a.rate_hw(student_a, 'Python', 10)
reviewer_a.rate_hw(student_a, 'C++', 5)
reviewer_a.rate_hw(student_a, 'Python', 8)

print(student_a.grades)

lecturer_a = Lecturer('Albert', 'Inshtean')
lecturer_a.courses_attached += ['Python']

student_a.rate_hw(lecturer_a, 'Python', 9)
student_a.rate_hw(lecturer_a, 'С++', 3)
student_a.rate_hw(lecturer_a, 'Python', 9)

print(lecturer_a.grades)

print(reviewer_a)

print(lecturer_a)

print(student_a)

student_b = Student('Тони', 'Старк', 'Мужчина')
student_b.courses_in_progress += ['Python', 'C++']
student_b.finished_courses += ['Введение в программирование']

reviewer_b = Reviewer('Халк', 'Петров')
reviewer_b.courses_attached += ['Python', 'C++']

reviewer_b.rate_hw(student_b, 'Python', 8)
reviewer_b.rate_hw(student_b, 'C++', 9)
reviewer_b.rate_hw(student_b, 'Python', 2)

print(student_b.grades)

lecturer_b = Lecturer('Человек', 'Паук')
lecturer_b.courses_attached += ['Python']

student_b.rate_hw(lecturer_b, 'Python', 8)
student_b.rate_hw(lecturer_b, 'С++', 4)
student_b.rate_hw(lecturer_b, 'Python', 9)

print(lecturer_b.grades)

print(reviewer_b)

print(lecturer_b)

print(student_b)

print(average_grade_for_homework(['student_a', 'best_student'], 'Python'))

print(average_grade_for_homework(['lecturer', 'lecturer_a'], 'Python'))