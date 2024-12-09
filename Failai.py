# # # vardas = input("Iveskite savo varda: ")
# # # print(f"Sveiki {vardas}")
# # import os

# # # print(os.getcwd())

# # # os.system("clear")

# # # print(os.stat("Failai.py").st_mtime)

# # # import datetime

# # # data  = datetime.datetime.fromtimestamp(os.stat("Failai.py").st_mtime)

# # # print(data)

# # # print(datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo)
# # # 10-11-2024

# # # os.mkdir("Testine2")
# # # os.mkdir(r"C:\Users\guiku\Desktop\Naujas")
# # # os.chdir()

# # # failas = open("Naujas.txt","a+")

# # # failas.write("As esu geras failas")

# # # nuskaityta = failas.read()
# # # print(nuskaityta)
# # import pickle

# # class Student():
# #     def __init__(self, name : str, last_name : str, age : int):
# #         self.name = name
# #         self.last_name = last_name
# #         self.age = age

# #     def __str__(self):
# #         return f"Pilietis vardu {self.name} {self.last_name}"
# #     def mokytis(self):
# #         print("MOkausi labai intensyviai, ir mokesiu dar daugiau")

# # studentas1 =  Student("Jonas","Jonaitis",40)
# # studentas2 =  Student("Antanas","Antanaitis",40)

# # # with open("Naujas.pickle","ab+") as file: # file = open("Naujas.txt","a+")
# # #     pickle.dump(studentas1,file) # file.write()

# # with open("Naujas.pickle","rb+") as file: # file = open("Naujas.txt","a+")
# #     grazintas = pickle.load(file)

# # if isinstance(grazintas,Student):
# #     print("Gryzo studentas")
# #     grazintas.mokytis()



# # zodynas = {}
# # zodynas.get()



# import pickle
# from datetime import datetime


# class Human:
#     def __init__(self, name, surname, age, birth_year):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.birth_year = birth_year


# class Student(Human):
#     def __init__(self, name, surname, age, birth_year, admission_date, course, grades):
#         super().__init__(name, surname, age, birth_year)
#         self.admission_date = admission_date
#         self.course = course
#         self.grades = grades
#         self.id = f"S-{id(self)}" 


# class Lecturer(Human):
#     def __init__(self, name, surname, age, birth_year, salary, work_start_date, status):
#         super().__init__(name, surname, age, birth_year)
#         self.salary = salary
#         self.work_start_date = work_start_date
#         self.status = status
#         self.id = f"L-{id(self)}"  


# class Association:
#     def __init__(self):
#         self.assignments = {}

#     def assign(self, lecturer_id, student_id):
#         if lecturer_id not in self.assignments:
#             self.assignments[lecturer_id] = []
#         self.assignments[lecturer_id].append(student_id)


# def calculate_average_grades(lecturer_id, students, association):
#     student_ids = association.assignments.get(lecturer_id, [])
#     all_grades = [grade for sid in student_ids for grade in students[sid].grades]
#     return sum(all_grades) / len(all_grades) if all_grades else 0


# def find_extremes(students, lecturers):
#     youngest_student = min(students.values(), key=lambda s: s.age)
#     oldest_student = max(students.values(), key=lambda s: s.age)
#     longest_working_lecturer = max(lecturers.values(), key=lambda l: datetime.now().year - int(l.work_start_date.split('-')[0]))
#     shortest_working_lecturer = min(lecturers.values(), key=lambda l: datetime.now().year - int(l.work_start_date.split('-')[0]))

#     age_diff = oldest_student.age - youngest_student.age
#     work_diff = (datetime.now().year - int(longest_working_lecturer.work_start_date.split('-')[0])) - \
#                 (datetime.now().year - int(shortest_working_lecturer.work_start_date.split('-')[0]))

#     return youngest_student, oldest_student, longest_working_lecturer, shortest_working_lecturer, age_diff, work_diff


# def save_data(filename, data):
#     with open(filename, 'wb') as f:
#         pickle.dump(data, f)


# def load_data(filename):
#     try:
#         with open(filename, 'rb') as f:
#             return pickle.load(f)
#     except (FileNotFoundError, EOFError):
#         return {}


# def main():
#     students = load_data('students.pkl')
#     lecturers = load_data('lecturers.pkl')
#     association = Association()

#     student1 = Student("Jonas", "Jonaitis", 20, 2003, "2021-09-01", "IT Inzinerija", [85, 90, 95])
#     lecturer1 = Lecturer("Dr. Antanas", "Antanaitis", 45, 1978, 5000, "2015-08-15", "Profesorius")

#     students[student1.id] = student1
#     lecturers[lecturer1.id] = lecturer1
#     association.assign(lecturer1.id, student1.id)

#     save_data('students.pkl', students)
#     save_data('lecturers.pkl', lecturers)

#     avg_grade = calculate_average_grades(lecturer1.id, students, association)
#     print(f"Average Grade: {avg_grade}")

#     extremes = find_extremes(students, lecturers)
#     print("Extremes:", extremes)


# main()

print("As smagiai printinu failuose")