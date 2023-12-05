class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.avg_grade = 0

    def __str__(self):
        return super().__str__() + f"\nСредняя оценка за лекции: {self.avg_grade}"

    def update_avg_grade(self, grades):
        self.avg_grade = sum(grades) / len(grades)



class Reviewer(Mentor):
    def __str__(self):
        return super().__str__() + "\nУ лекторов:"


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def add_grade(self, course, grade):
        if course in self.grades:
            self.grades[course].append(grade)
        else:
            self.grades[course] = [grade]

    def calculate_avg_grade(self):
        total_sum = sum(sum(grades) / len(grades) for grades in self.grades.values())
        total_count = sum(len(grades) for grades in self.grades.values())
        return total_sum / total_count if total_count > 0 else 0

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.calculate_avg_grade()}\n" \
               f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n" \
               f"Завершенные курсы: {', '.join(self.finished_courses)}"
students = [
    Student('Ruoy', 'Eman', 'your_gender'),
    Student('Hagrid', 'Rubius', 'male'),
    Student('Rubi', 'Scarlet', 'female')
]

lecturers = [
    Lecturer('Some', 'Buddy'),
    Lecturer('Duck', 'Nuckem'),
    Lecturer('Nazu', 'Dragnil')
]

students[0].courses_in_progress.append('Python')
students[0].finished_courses.append('Введение в программирование')

students[1].courses_in_progress.append('Python')
students[1].finished_courses.append('Автоматизация тестирования в Selenium')

students[2].courses_in_progress.append('Python')
students[2].finished_courses.append('Избранные вопросы ООП')

students[0].add_grade('Python', 9)
students[0].add_grade('Python', 9)
students[0].add_grade('Python', 10)
students[0].add_grade('Math', 8)

students[1].add_grade('Python', 7)
students[1].add_grade('Автоматизация тестирования в Selenium', 9)
students[1].add_grade('Python', 9)
students[1].add_grade('Python', 8)

students[2].add_grade('Python', 8)
students[2].add_grade('Избранные вопросы ООП', 9)
students[2].add_grade('Python', 10)
students[2].add_grade('Python', 10)

lecturers[0].update_avg_grade([10, 10, 9, 9])
lecturers[1].update_avg_grade([10, 8, 10, 9])


best_student = max(students, key=lambda student: student.calculate_avg_grade())
best_lecturer = max(lecturers, key=lambda lecturer: lecturer.avg_grade)

print(f"Лучший студент:\n{best_student}")
print(f"\nЛучший лектор:\n{best_lecturer}")