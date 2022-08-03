class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def get_avg_grade(self):
        sum_grades = 0
        count = 0
        for course in self.grades.values():
            sum_grades += sum[course]
            count += len(course)
        return sum_grades / count

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname}' \
              f'Средняя оценка за домашние задания: {self.get_avg_grade()}' \
              f'Курсы в процессе изучения: {self.courses_in_progress()}' \
              f'Завершенные курсы: {self.finished_courses()}'
        return res

    def __lt__(self, other_student):
        res = self.get_avg_grade() < other_student.get_avg_grade()
        return res

    student_list = []
    def get_avg_student_grade(student_list, course):
        total_sum = 0
        for student in student_list:
            for c, grades_list in student.grades.items():
                if c == course:
                    total_sum += sum(grades_list) / len(grades_list)
        return round(total_sum / len(student_list), 2)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_avg_grade(self):
        sum_grades = 0
        count = 0
        for course in self.grades.values():
            sum_grades += sum[course]
            count += len(course)
        return sum_grades / count

    def __str__(self):
        res = f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname}' \
              f'Средняя оценка за лекции: {self.get_avg_grade()}'
        return res

    def __lt__(self, other_lecturer):
        res = self.get_avg_grade() < other_lecturer.get_avg_grade()
        return res

    lecturer_list = []
    def get_avg_lecturer_grade(lecturer_list, course):
        total_sum = 0
        for lecturer in lecturer_list:
            for c, grades_list in lecturer.grades.items():
                if c == course:
                    total_sum += sum(grades_list) / len(grades_list)
        return round(total_sum / len(lecturer_list), 2)


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
        res = f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname}'
        return res


courses = ('Python', 'Git', 'Введение в программирование')
student_1 = Student('Anna', 'Veber', 'female')
student_2 = Student('Jan', 'Wiks', 'male')
mentor_1 = Mentor('Arkady', 'Anks')
mentor_2 = Mentor('Vova', 'Brain')
lecturer_1 = Lecturer('Andy', 'Wish')
lecturer_2 = Lecturer('Dima', 'Ken')
reviewer_1 = Reviewer('Ivan', 'Rich')
reviewer_2 = Reviewer('Dina', 'Smile')