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

    # task 3
    def __str__(self):
        return f"Имя: {self.name}" + "\n" + f"Фамилия: {self.surname}"


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
        print(f"В словаре лектора: {self.scores}")

    # Average lecturer score
    def avg_score(self):
        common_lst = sum(self.scores.values(), start=[])
        return round(sum(common_lst) / len(common_lst), 1)

    # task 3
    def __str__(self):
        return (
            f"Имя: {self.name}"
            + "\n"
            + f"Фамилия: {self.surname}"
            + "\n"
            + f"Средняя оценка за лекции: {self.avg_score()}"
        )


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


some_reviewer = Reviewer("Some", "Buddy")

some_lecturer = Lecturer("Gvido", "Van")
some_lecturer.courses_attached += ["Python"]
some_lecturer.courses_attached += ["Git"]

some_student.rate_lecturer(some_lecturer, "Python", 9)
some_student.rate_lecturer(some_lecturer, "Python", 10)
some_student.rate_lecturer(some_lecturer, "Git", 4)

print(some_reviewer)
print(some_lecturer)
# справочно
some_lecturer.show_scores()
