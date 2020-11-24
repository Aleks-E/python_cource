import datetime
from typing import Callable
from collections import defaultdict

DeadlineError = Exception

class Personal_Info:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name










class Homework:
    def __init__(self, text: str, deadline: int):
        self.text = text
        self.deadline = datetime.timedelta(deadline)
        self.created = datetime.datetime.now()

    def is_active(self) -> bool:
        return self.created + self.deadline > datetime.datetime.now()


class Teacher(Personal_Info):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        # self.homework_done = {}
        self.homework_done = defaultdict()

    def create_homework(self, text: str, days: int) -> Callable:
        return Homework(text, days)

    def check_homework(self, result):
        if len(result.solution) > 5:
            # self.homework_done = True
            # self.homework_done[result.text] = True
            self.homework_done[result.homework] = result
            return True
        else:
            return False

    def reset_results(self, homework=None):
        if homework is None:
            self.homework_done = {}
        else:
            self.homework_done[homework] = None



class HomeworkResult:
    def __init__(self, homework: Callable, text: str, solution: str):
        if not isinstance(homework, Homework):
            raise Exception('You gave a not Homework object')
        else:
            self.homework = homework
            self.text = text      # ?
            self.solution = solution
        # author - ?
        # created - ?


class Student(Personal_Info):
    def do_homework(self, homework: Homework, solution: str) -> Callable:
        # return homework if homework.is_active() else print("You are late")

        if not homework.is_active():
            raise DeadlineError('You are late')

        return HomeworkResult(homework, homework.text, solution)



# opp_teacher = Teacher('Daniil', 'Shadrin')
# advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')
#
# lazy_student = Student('Roman', 'Petrov')
# good_student = Student('Lev', 'Sokolov')
#
# oop_hw = opp_teacher.create_homework('Learn OOP', 1)        # created Homework
# docs_hw = opp_teacher.create_homework('Read docs', 5)
#
# result_1 = good_student.do_homework(oop_hw, 'I have done this hw')             #  # created HomeworkResult
# result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
# result_3 = lazy_student.do_homework(docs_hw, 'done')
# try:
#     result_4 = HomeworkResult(good_student, "fff", "Solution")
# except Exception:
#     print('There was an exception here')
#
# opp_teacher.check_homework(result_1)
# temp_1 = opp_teacher.homework_done
# print('temp_1', temp_1)
#
# advanced_python_teacher.check_homework(result_1)
# temp_2 = advanced_python_teacher.homework_done
# print('temp_2', temp_2)
# assert temp_1 == temp_2
#
# opp_teacher.check_homework(result_2)
# opp_teacher.check_homework(result_3)
#
# print(opp_teacher.homework_done)
# print(opp_teacher.homework_done[oop_hw])



# ----------------------------
# teacher = Teacher("Daniil", "Shadrin")
# homework = teacher.create_homework("Learn functions", 1)
# student = Student("Roman", "Petrov")
#
# # print(HomeworkResult(homework, "fff", "Solution"))
#
# result = student.do_homework(homework, 'text', '123456')
#
# print(teacher.check_homework(result))
#
# print(teacher.homework_done)
# ----------------------------






defdict = defaultdict(list)

for i in range(5):
    defdict[i].append(i)

print(defdict)




class A:
    # def __init__(self, arg):
    #     self.arg = arg

    def ret(self, arg):
        return arg ** 2



defdict = defaultdict(A)

for i in range(5):
    defdict[i].ret(i)

print(defdict)












