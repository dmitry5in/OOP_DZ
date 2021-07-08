class Student:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average_rating(self):
        mark_list = []
        for values in self.grades.values():
            av_rat = sum(values) / len(values)
            mark_list += [av_rat]
        rating = sum(mark_list) / len(mark_list)
        return(rating)

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.lect_grades:
                lecturer.lect_grades[course] += [grade]
            else:
                lecturer.lect_grades[course] = [grade]

    def __str__(self):
        res_1 = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_rating()}\n'
        res_2 = f'Курсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}\n'
        return res_1 + res_2

    def __lt__(self, other):
        res_1 = "Вы отличный студент!"
        res_2 = "Нужно усерднее учиться"
        if not isinstance(other, Student):
            print("Not a Student!")
            return
        if self.average_rating() < other.average_rating():
            return res_2
        else:
            return res_1


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def add_courses(self, courses):
        self.courses_attached += [courses]


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lect_grades = {}

    def average_rating(self):
        mark_list = []
        for values in self.lect_grades.values():
            av_rat = sum(values) / len(values)
            mark_list += [av_rat]
        rating = sum(mark_list) / len(mark_list)
        return rating

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating()}\n'
        return res

    def __lt__(self, other):
        res_1 = "Вы отличный лектор!"
        res_2 = "Нужно усерднее работать"
        if not isinstance(other, Lecturer):
            print("Not a Lecturer!")
            return
        if self.average_rating() < other.average_rating():
            return res_2
        else:
            return res_1


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return res


lecturer1 = Lecturer("John", "Smith")
lecturer2 = Lecturer("Jack", "Wilson")
lecturer1.add_courses("Python")
lecturer2.add_courses("PHP")

stud1 = Student("Ivan", "Ivanov")
stud2 = Student("Petr", "Petrov")
stud1.courses_in_progress = ['Python', "PHP"]
stud2.courses_in_progress = ['Python', "PHP"]
stud1.finished_courses = ["Java"]
stud1.rate_lecture(lecturer1, "Python", 7)
stud1.rate_lecture(lecturer2, "PHP", 8)
stud2.rate_lecture(lecturer1, "Python", 8)
stud2.rate_lecture(lecturer2, "PHP", 6)

rev1 = Reviewer("Mike", "Taylor")
rev2 = Reviewer("Robert", "Moore")
rev1.add_courses("Python")
rev2.add_courses("PHP")
rev1.rate_hw(stud1, "Python", 8)
rev1.rate_hw(stud2, "Python", 9)
rev2.rate_hw(stud1, "PHP", 10)
rev2.rate_hw(stud2, "PHP", 9)

print(rev1)
print(rev2)
print(stud1)
print(stud2)
print(lecturer1)
print(lecturer2)
print(stud1 < stud2)
print(lecturer1 < lecturer2)


def average_course_stud(course, student_list):
    total_list = []
    for student in student_list:
        if course in student.courses_in_progress:
            total_list += student.grades[course]
    res = f'Средняя оценка за домашние задания по курсу {course}: {sum(total_list) / len(total_list)}'
    return res


def average_course_lect(course, lecturer_list):
    total_list = []
    for lecturer in lecturer_list:
        if course in lecturer.courses_attached:
            total_list += lecturer.lect_grades[course]
    res = f'Средняя оценка за лекции по курсу {course}: {sum(total_list) / len(total_list)}'
    return res

print(average_course_stud("Python", [stud1, stud2]))
print(average_course_lect("Python", [lecturer1, lecturer2]))