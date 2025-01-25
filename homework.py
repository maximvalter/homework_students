class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if (
            isinstance(lecturer, Lecturer) and
            course in self.courses_in_progress and
            course in lecturer.courses_attached
        ):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        total_grades = 0
        count = 0
        for grades in self.grades.values():
            total_grades += sum(grades)
            count += len(grades)
        return total_grades / count if count > 0 else 0

    def __str__(self):
        avg_grade = self.average_grade()
        courses_in_progress = ", ".join(self.courses_in_progress) if self.courses_in_progress else "Нет курса"
        finished_courses = ", ".join(self.finished_courses) if self.finished_courses else "Нет оконченного курса"
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade:.1f}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}")

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()
        return False

    def __le__(self, other):
        if isinstance(other, Student):
            return self.average_grade() <= other.average_grade()
        return False

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() > other.average_grade()
        return False

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.average_grade() >= other.average_grade()
        return False

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_grade() == other.average_grade()
        return False

    def __ne__(self, other):
        if isinstance(other, Student):
            return self.average_grade() != other.average_grade()
        return False


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        total_grades = 0
        count = 0
        for grades in self.grades.values():
            total_grades += sum(grades)
            count += len(grades)
        return total_grades / count if count > 0 else 0

    def __str__(self):
        avg_grade = self.average_grade()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade:.1f}")

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() < other.average_grade()
        return False

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() <= other.average_grade()
        return False

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() > other.average_grade()
        return False

    def __ge__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() >= other.average_grade()
        return False

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() == other.average_grade()
        return False

    def __ne__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() != other.average_grade()
        return False


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if not isinstance(student, Student):
            return 'Ошибка: Неверный тип студента'
        if course not in self.courses_attached:
            return 'Ошибка: Этот курс не прикреплён к проверяющему'
        if course not in student.courses_in_progress:
            return 'Ошибка: Студент не проходит этот курс'
        if course in student.grades:
            student.grades[course].append(grade)
        else:
            student.grades[course] = [grade]
        return 'Оценка добавлена'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


def average_grade_for_homework(students, course):
    total_homework_grade = 0
    count = 0
    for student in students:
        if course in student.courses_in_progress:
            total_homework_grade += student.average_grade()
            count += 1
    if count == 0:
        return 0
    return round(total_homework_grade / count, 1)


def average_grade_for_lectures(lecturers, course):
    total_lecture_grade = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.courses_attached:
            total_lecture_grade += lecturer.average_grade()
            count += 1
    if count == 0:
        return 0
    return round(total_lecture_grade / count, 1)


student1 = Student('Ruoy', 'Eman', 'female')
student1.courses_in_progress = ['Python', 'Git']
student1.finished_courses = ['Введение в программирование']
student1.grades = {'Python': [10, 9, 10], 'Git': [8, 9, 10]}

student2 = Student('John', 'Smith', 'male')
student2.courses_in_progress = ['Python']
student2.finished_courses = ['Введение в программирование']
student2.grades = {'Python': [9, 8, 7]}

lecturer1 = Lecturer('Oleg', 'Bulygin')
lecturer1.courses_attached = ['Python']
lecturer1.grades = {'Python': [9, 10, 8]}

lecturer2 = Lecturer('Timur', 'Anvartdinov')
lecturer2.courses_attached = ['Python']
lecturer2.grades = {'Python': [10, 10, 9]}

reviewer1 = Reviewer('Some', 'Buddy')
reviewer1.courses_attached = ['Python']
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 9)

reviewer2 = Reviewer('Some', 'Buddy 2')
reviewer2.courses_attached = ['Python']
reviewer2.rate_hw(student2, 'Python', 8)

print("Первый студент: " + f"\n{student1}\n")
print("Второй студент: " + f"\n{student2}\n")
print("Первый лектор: " + f"\n{lecturer1}\n")
print("Второй лектор: " + f"\n{lecturer2}\n")
print("Первый проверяющий: "+ f"\n{reviewer1}\n")
print("Второй проверяющий: "+ f"\n{reviewer2}\n")

students = [student1, student2]
lecturers = [lecturer1, lecturer2]

print(f"Средняя оценка за домашние задания по курсу Python: {average_grade_for_homework(students, 'Python')}")
print(f"Средняя оценка за лекции по курсу Python: {average_grade_for_lectures(lecturers, 'Python')}")
