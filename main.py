class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    grades = {}
    sum = 0
    for n in grades:
        average_st_grade = float(sum(grades) / len(grades))
        print(average_st_grade)

    def add_courses(self, course_name):
        self.finished_course.append(course_name)

    def rate_lecturer(self, name, surname, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return self.name, self.surname, self.courses_in_progress, self.finished_courses, 'average_st_grade'
        print(some_student)

student_1 = Student('Anna', 'Veber', 'female')
student_2 = Student('Jan', 'Wiks', 'male')

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

mentor_1 = Mentor('Arkady', 'Anks')
mentor_2 = Mentor('Vova', 'Brain')

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return self.name, self.surname, 'average_lec_grade'
        print(some_lecturer)

    # sum = 0
    # for n in self.grades:
    #     average_st_grade = float(sum(self.grades) / len(self.grades))
    #     print(average_lec_grade)

lecturer_1 = Lecturer('Andy', 'Wish')
lecturer_2 = Lecturer('Dima', 'Ken')

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
        return self.name, self.surname
        print(some_reviewer)

reviewer_1 = Reviewer('Ivan', 'Rich')
reviewer_2 = Reviewer('Dina', 'Smile')

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

print(best_student.grades)

def __lt__(self, other):
    return self.grades < other.grades

courses = ('Python', 'Git', 'Введение в программирование')