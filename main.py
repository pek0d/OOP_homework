class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, score):
        """Оценивает лектора"""
        if (
            isinstance(lecturer, Lecturer)
            and course in self.courses_in_progress
            and course in lecturer.courses_attached
        ):
            if course in lecturer.scores:
                lecturer.scores[course] += [score]
            else:
                lecturer.scores[course] = [score]
        else:
            return "Ошибка"

    def avg_grade(self):
        """Cчитает среднюю оценку студента"""
        if self.grades:
            common_grade_lst = sum(self.grades.values(), start=[])
            return round(sum(common_grade_lst) / len(common_grade_lst), 1)
        else:
            return "Нет оценок"

    def show_grades(self):
        """Выводит все оценки студента"""
        print(f"В словаре с оценками студента: {self.grades}")

    # task 3.1 (магичечский метод строки)
    def __str__(self):
        return (
            f"Имя: {self.name}"
            + "\n"
            + f"Фамилия: {self.surname}"
            + "\n"
            + f"Средняя оценка за домашние задания: {self.avg_grade()}"
            + "\n"
            + f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}"
            + "\n"
            + f"Завершенные курсы: {', '.join(self.finished_courses)}"
        )

    # task 3.2 (магический метод сравнения less then)
    def __lt__(self, other):
        if self.avg_grade:
            return self.avg_grade() < other.avg_grade()
        else:
            return "Нет оценок, нечего сравнивать"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


# task 1 and task 2
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.scores = {}

    def show_scores(self):
        """Выводит все баллы лектора"""
        print(f"В словаре с оценками лектора: {self.scores}")

    def avg_score(self):
        """Cчитает средний балл лектора"""
        if self.scores:
            common_score_lst = sum(self.scores.values(), start=[])
            return round(sum(common_score_lst) / len(common_score_lst), 1)
        else:
            return "Нет оценок"

    # task 3.1 (магичечский метод строки)
    def __str__(self):
        return (
            f"Имя: {self.name}"
            + "\n"
            + f"Фамилия: {self.surname}"
            + "\n"
            + f"Средняя оценка за лекции: {self.avg_score()}"
        )

    # task 3.2 (магический метод сравнения less then)
    def __lt__(self, other):
        if self.avg_score:
            return self.avg_score() < other.avg_score()
        else:
            return "Нет оценок, нечего сравнивать"


# task 1 and task 2
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        """Оценивает студента"""
        if isinstance(student, Student) and course in self.courses_attached:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"

    # task 3.1 (магичечский метод строки)
    def __str__(self):
        return f"Имя: {self.name}" + "\n" + f"Фамилия: {self.surname}"


# СОЗДАНИЕ ЭКЗЕМПЛЯРОВ (task 4)
some_student1 = Student("Ruoy", "Eman", "male")
some_student1.courses_in_progress += ["Python"]
some_student1.courses_in_progress += ["Git"]
some_student1.finished_courses += ["Введение в программирование"]

some_student2 = Student("Lupa", "Pupa", "female")
some_student2.courses_in_progress += ["Python"]
some_student2.courses_in_progress += ["Git"]
some_student2.finished_courses += ["GIT для начинающих"]

some_lecturer1 = Lecturer("Gvido", "Van")
some_lecturer1.courses_attached += ["Python"]

some_lecturer2 = Lecturer("Tig", "Master")
some_lecturer2.courses_attached += ["Git"]

some_reviewer1 = Reviewer("Some", "Buddy")
some_reviewer1.courses_attached += ["Python"]

some_reviewer2 = Reviewer("Linus", "Torwalds")
some_reviewer2.courses_attached += ["Git"]

# Вызов всех созданных методов

some_reviewer1.rate_hw(some_student1, "Python", 8)
some_reviewer1.rate_hw(some_student2, "Python", 6)
some_reviewer2.rate_hw(some_student1, "Git", 10)
some_reviewer2.rate_hw(some_student2, "Git", 10)

some_student1.rate_lecturer(some_lecturer1, "Python", 9)
some_student1.rate_lecturer(some_lecturer2, "Git", 5)
some_student2.rate_lecturer(some_lecturer1, "Python", 6)
some_student2.rate_lecturer(some_lecturer2, "Git", 5)

# Справочно
# some_lecturer1.show_scores()
# some_student1.show_grades()

# Вызов перегруженных методов (task 3.1)
print(some_reviewer1)
# Добавлено для читаемости принтов (пустая строка)
print()

print(some_lecturer1)
# Добавлено для читаемости принтов (пустая строка)
print()

print(some_student1)
# Добавлено для читаемости принтов (пустая строка)
print()


# Вызов перегруженного метода (task 3.2 (for Student())
print(some_student1 < some_student2)
# Вызов перегруженного метода (task 3.2 (for Lecturer())
print(some_lecturer1 > some_lecturer2)

# task 4.1
student_lst = [some_student1, some_student2]


def avg_grade_all_students(students_lst, course):
    """Считает среднюю оценку всех студентов"""
    overall_grade = []
    if students_lst:
        for student in student_lst:
            for key, value in student.grades.items():
                if key == course:
                    overall_grade += value
        return round(sum(overall_grade) / len(overall_grade), 1)
    else:
        return "Список студентов пустой, нечего считать"


print(avg_grade_all_students(student_lst, "Python"))


# task 4.2
lecturer_lst = [some_lecturer1, some_lecturer2]


def avg_score_all_lecturers(lecturer_lst, course):
    """Считает средний балл всех лекторов"""
    overall_score = []
    if lecturer_lst:
        for lecturer in lecturer_lst:
            for key, value in lecturer.scores.items():
                if key == course:
                    overall_score += value
        return round(sum(overall_score) / len(overall_score), 1)
    else:
        return "Список лекторов пустой, нечего считать"


print(avg_score_all_lecturers(lecturer_lst, "Git"))
