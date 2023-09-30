class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, score):
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

    # Average student grade
    def avg_grade(self):
        if self.grades:
            common_grade_lst = sum(self.grades.values(), start=[])
            return round(sum(common_grade_lst) / len(common_grade_lst), 1)
        else:
            return "Нет оценок"

    # справочно
    def show_grades(self):
        print(f"В словаре с оценками студента: {self.grades}")

    # task 3.1
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

    # task 3.2
    def __lt__(self, other):
        return self.avg_grade() < other.avg_grade()


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

    # справочно
    def show_scores(self):
        print(f"В словаре с оценками лектора: {self.scores}")

    # Average lecturer score
    def avg_score(self):
        if self.scores:
            common_score_lst = sum(self.scores.values(), start=[])
            return round(sum(common_score_lst) / len(common_score_lst), 1)
        else:
            return "Нет оценок"

    # task 3.1
    def __str__(self):
        return (
            f"Имя: {self.name}"
            + "\n"
            + f"Фамилия: {self.surname}"
            + "\n"
            + f"Средняя оценка за лекции: {self.avg_score()}"
        )

    # task 3.2
    def __lt__(self, other):
        return self.avg_score() < other.avg_score()


# task 1 and task 2
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"

    # task 3
    def __str__(self):
        return f"Имя: {self.name}" + "\n" + f"Фамилия: {self.surname}"


some_student = Student("Ruoy", "Eman", "male")
some_student.courses_in_progress += ["Python"]
some_student.courses_in_progress += ["Git"]
some_student.finished_courses += ["Введение в программирование"]


some_reviewer = Reviewer("Some", "Buddy")
some_reviewer.courses_attached += ["Python"]
some_reviewer.courses_attached += ["Git"]
some_reviewer.rate_hw(some_student, "Python", 8)
some_reviewer.rate_hw(some_student, "Git", 10)

some_lecturer = Lecturer("Gvido", "Van")
some_lecturer.courses_attached += ["Python"]
some_lecturer.courses_attached += ["Git"]

some_student.rate_lecturer(some_lecturer, "Python", 9)
some_student.rate_lecturer(some_lecturer, "Python", 10)
some_student.rate_lecturer(some_lecturer, "Git", 5)

# справочно
# some_lecturer.show_scores()
# some_student.show_grades()

# task 3.1
print(some_reviewer)
print(some_lecturer)
print(some_student)
# task 3.2
print(int(some_student.avg_grade()) < int(some_lecturer.avg_score()))
