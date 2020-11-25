"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную


1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)

HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'

    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания

2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.

3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования

4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.

    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from typing import Callable
from collections import defaultdict

class DeadlineError(Exception):
    ...

class Personal_Info:
    def __init__(self, first_name: str, last_name: str):        # ok
        self.first_name = first_name
        self.last_name = last_name


class Teacher(Personal_Info):
    homework_done = defaultdict(list)

    def create_homework(self, text: str, days: int) -> Callable:            # ok
        return Homework(text, days)

    @classmethod
    def check_homework(cls, result):
        if len(result.solution) > 5:
            if result.homework not in cls.homework_done:
                cls.homework_done[result.homework].append(result)
            elif result not in cls.homework_done[result.homework]:
                cls.homework_done[result.homework].append(result)

            # cls.homework_done[result.homework].append(result)
            return True
        else:
            return False

    @classmethod
    def reset_results(cls, homework=None):
        if homework is None:
            cls.homework_done.clear()
        else:
            del cls.homework_done[homework]


class Homework:
    def __init__(self, text: str, deadline: int):       # ok
        self.text = text
        self.deadline = datetime.timedelta(deadline)
        self.created = datetime.datetime.now()

    def is_active(self) -> bool:                        # ok
        return self.created + self.deadline > datetime.datetime.now()


class Student(Personal_Info):
    def do_homework(self, homework: Homework, solution: str) -> Callable:       # ok
        # if not homework.is_active():
        #     raise DeadlineError('You are late')

        # return HomeworkResult(homework, self, solution)
        result = HomeworkResult(homework, self, solution)           # Review
        if not homework.is_active():
            raise DeadlineError('You are late')
        return result


class HomeworkResult:
    def __init__(self, homework: Homework, author: Student, solution: str):     # ok
        if not isinstance(homework, Homework):
            raise Exception('You gave a not Homework object')
        else:
            self.homework = homework
            self.author = author
            self.solution = solution
            self.created = datetime.datetime.now()



"""
1 Домашнее задание, переданное студенту, неправильного типа




1 Просрочено домашнее задание


1 Результат записался в homework_done
2 Результат содержит правильный ответ
3 Результат принадлежит конкретному студенту
4 Результат относится к конкретной работе


"""











# opp_teacher = Teacher('Daniil', 'Shadrin')
# print('Teacher_personal_info\t', opp_teacher.first_name, opp_teacher.last_name)
#
# lazy_student = Student('Roman', 'Petrov')
# print('Student_personal_info\t', lazy_student.first_name, lazy_student.last_name)
#
# oop_hw = opp_teacher.create_homework('Learn OOP', 0)
# # result = lazy_student.do_homework(lazy_student, 'I have done this hw')       # Exception: You gave a not Homework object
#
# # result = lazy_student.do_homework(oop_hw, 'I have done this hw')            #     raise DeadlineError('You are late')
#                                                                             # Exception: You are late
#
# oop_hw = opp_teacher.create_homework('Learn OOP', 1)
# print('oop_hw\t', oop_hw)
# print('oop_hw_attr\t', oop_hw.text, oop_hw.deadline, oop_hw.created)
#
#
# result = lazy_student.do_homework(oop_hw, '12345')
# print('result_1\t', result)
# print('result_1_attr\t', result.homework, result.author, result.solution, result.created)
#
# print(opp_teacher.check_homework(result))     # False
# print(opp_teacher.homework_done)                # defaultdict(None, {})
#
#
#
# result = lazy_student.do_homework(oop_hw, 'I have done this hw')
# print(opp_teacher.check_homework(result))     # True
# print(opp_teacher.homework_done)                # defaultdict(None, {<__main__.HomeworkResult object at 0x0000000002148208>: True})
#
#
# advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')
# good_student = Student('Lev', 'Sokolov')
# docs_hw = opp_teacher.create_homework('Read docs', 5)
#
# result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
# result_3 = lazy_student.do_homework(docs_hw, 'done   ')
#
# opp_teacher.check_homework(result_2)
# opp_teacher.check_homework(result_2)
# opp_teacher.check_homework(result_3)
#
#
# print(advanced_python_teacher.homework_done)
#
#
# for i in advanced_python_teacher.homework_done:
#     print('i\t', i, advanced_python_teacher.homework_done[i])
#
#
# Teacher.reset_results()
# print(advanced_python_teacher.homework_done)
#
# opp_teacher.check_homework(result_2)
# print(advanced_python_teacher.homework_done)
#
# opp_teacher.check_homework(result_3)
# opp_teacher.check_homework(result)
# print(advanced_python_teacher.homework_done)
#
# Teacher.reset_results(oop_hw)
# print(advanced_python_teacher.homework_done)














# ---------------------------------
# def func(arg):
#     if arg < 0:
#         raise Exception('www')
#
# # func(-4)
# ---------------------------------





# ---------------------------------
# class MyClass:
#     @staticmethod
#     def ex_static_method():
#         print("static method")
#
#     @classmethod
#     def ex_class_method(cls):
#         print("class method")
# ---------------------------------



# defdict = defaultdict(list)
#
# class A:
#     my_list = []
#
#     # @classmethod
#     def adder(cls, arg):
#         cls.my_list.append(arg)


# a_1 = A()
# a_2 = A()
#
# print(A.my_list)
# print(a_1.my_list)
# print(a_2.my_list)
#
# a_1.adder(1)
# print(A.my_list)
# print(a_1.my_list)
# print(a_2.my_list)
#
# a_2.adder(2)
# print(A.my_list)
# print(a_1.my_list)
# print(a_2.my_list)
#
# print(a_1.my_list is a_2.my_list)
# ------------------------------



# ====================================================================
# ------------------------------

# defdict = defaultdict(list)
#
# for i in range(5):
#     defdict[i].append(i)
#
# print(defdict)

# ------------------------------

# my_str = 'qwertyqw'
# d = defaultdict(int)
# for key in my_str:
#     d[key] += 1
#
# print(d)

# ------------------------------

# d = defaultdict(int)
# d['a'] += 3
# print(d)

# ---------------------------

# d = defaultdict(list)
# d['a'].append(3)
# d['a'] += [5, 7]
# print(d)

# ---------------------------

# d = defaultdict(int)
# print(d['r'])               # 0

# ---------------------------

# def a():
#     return 22
#
# defdict = defaultdict(a)
#
# print(defdict['q'])     # 22
# ---------------------------

# class A:
#     def a(self):
#         return 33
#
#
# defdict = defaultdict(A().a)
#
# print(defdict['q'])     # 33
# print(defdict)

# ---------------------------

# defdict = defaultdict(bool)
#
# # defdict('1')
#
# print(defdict['1'])
# print(defdict)

# ---------------------------




# defdict = defaultdict(list)
#
#
# defdict['1']
#
#
# print(defdict)








