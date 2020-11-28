import datetime

from hw6.task_1 import DeadlineError, HomeworkResult, ObjectError, Student, Teacher

import pytest


def test_teacher_attribute():
    first_name, last_name = "Daniil", "Shadrin"
    teacher = Teacher(first_name, last_name)
    assert teacher.first_name == first_name
    assert teacher.last_name == last_name


def test_student_attribute():
    first_name, last_name = "Roman", "Petrov"
    student = Student(first_name, last_name)
    assert student.first_name == first_name
    assert student.last_name == last_name


def test_wrong_object_of_homework():
    lazy_student = Student("Roman", "Petrov")
    with pytest.raises(ObjectError, match="You gave a not Homework object"):
        lazy_student.do_homework(1, "solution")


def test_expired_deadline_of_homework():
    opp_teacher = Teacher("Daniil", "Shadrin")
    lazy_student = Student("Roman", "Petrov")
    deadline = 0
    oop_hw = opp_teacher.create_homework("Learn OOP", deadline)
    with pytest.raises(DeadlineError, match="You are late"):
        lazy_student.do_homework(oop_hw, "I have done this hw")


def test_type_of_object_returned_by_the_student():
    opp_teacher = Teacher("Daniil", "Shadrin")
    lazy_student = Student("Roman", "Petrov")
    deadline = 1
    oop_hw = opp_teacher.create_homework("Learn OOP", deadline)
    result = lazy_student.do_homework(oop_hw, "I have done this hw")
    assert isinstance(result, HomeworkResult)


def test_wrong_result_of_the_homework():
    opp_teacher = Teacher("Daniil", "Shadrin")
    lazy_student = Student("Roman", "Petrov")
    deadline = 1
    oop_hw = opp_teacher.create_homework("Learn OOP", deadline)
    solution = "12345"
    result = lazy_student.do_homework(oop_hw, solution)
    assert not opp_teacher.check_homework(result)
    assert not opp_teacher.homework_done


def test_right_result_of_the_homework():
    opp_teacher = Teacher("Daniil", "Shadrin")
    lazy_student = Student("Roman", "Petrov")
    deadline = 1
    oop_hw = opp_teacher.create_homework("Learn OOP", deadline)
    solution = "123456"
    result = lazy_student.do_homework(oop_hw, solution)
    assert opp_teacher.check_homework(result)
    assert opp_teacher.homework_done[oop_hw] == [result]


def test_the_same_homework_completed_by_two_students():
    opp_teacher = Teacher("Daniil", "Shadrin")
    lazy_student = Student("Roman", "Petrov")
    good_student = Student("Lev", "Sokolov")
    deadline = 1
    oop_hw = opp_teacher.create_homework("Learn OOP", deadline)
    solution = "123456"
    result_1 = lazy_student.do_homework(oop_hw, solution)
    result_2 = good_student.do_homework(oop_hw, solution)
    opp_teacher.check_homework(result_1)
    opp_teacher.check_homework(result_2)
    assert opp_teacher.homework_done[oop_hw] == [result_1, result_2]


def test_different_homework_completed_by_different_students():
    opp_teacher = Teacher("Daniil", "Shadrin")
    lazy_student = Student("Roman", "Petrov")
    good_student = Student("Lev", "Sokolov")
    deadline = 1
    oop_hw = opp_teacher.create_homework("Learn OOP", deadline)
    docs_hw = opp_teacher.create_homework("Read docs", deadline)
    solution = "123456"
    result_1 = lazy_student.do_homework(oop_hw, solution)
    result_2 = good_student.do_homework(docs_hw, solution)
    opp_teacher.check_homework(result_1)
    opp_teacher.check_homework(result_2)
    assert opp_teacher.homework_done[oop_hw] == [result_1]
    assert opp_teacher.homework_done[docs_hw] == [result_2]


def test_different_homework_completed_by_one_student():
    opp_teacher = Teacher("Daniil", "Shadrin")
    lazy_student = Student("Roman", "Petrov")
    deadline = 1
    oop_hw = opp_teacher.create_homework("Learn OOP", deadline)
    docs_hw = opp_teacher.create_homework("Read docs", deadline)
    solution = "123456"
    result_1 = lazy_student.do_homework(oop_hw, solution)
    result_2 = lazy_student.do_homework(docs_hw, solution)
    opp_teacher.check_homework(result_1)
    opp_teacher.check_homework(result_2)
    assert opp_teacher.homework_done[oop_hw] == [result_1]
    assert opp_teacher.homework_done[docs_hw] == [result_2]


def test_the_same_homework_result():
    opp_teacher = Teacher("Daniil", "Shadrin")
    lazy_student = Student("Roman", "Petrov")
    deadline = 1
    oop_hw = opp_teacher.create_homework("Learn OOP", deadline)
    solution = "123456"
    result = lazy_student.do_homework(oop_hw, solution)
    opp_teacher.check_homework(result)
    opp_teacher.check_homework(result)
    assert opp_teacher.homework_done[oop_hw] == [result]


def test_reset_results_of_definite_homework():
    opp_teacher = Teacher("Daniil", "Shadrin")
    lazy_student = Student("Roman", "Petrov")
    deadline = 1
    oop_hw = opp_teacher.create_homework("Learn OOP", deadline)
    docs_hw = opp_teacher.create_homework("Read docs", deadline)
    solution = "123456"
    result_1 = lazy_student.do_homework(oop_hw, solution)
    result_2 = lazy_student.do_homework(docs_hw, solution)
    opp_teacher.check_homework(result_1)
    opp_teacher.check_homework(result_2)
    assert opp_teacher.homework_done[oop_hw] == [result_1]
    assert opp_teacher.homework_done[docs_hw] == [result_2]
    opp_teacher.reset_results(oop_hw)
    assert opp_teacher.homework_done[oop_hw] == []
    assert opp_teacher.homework_done[docs_hw] == [result_2]


def test_reset_results_of_all_homework():
    opp_teacher = Teacher("Daniil", "Shadrin")
    lazy_student = Student("Roman", "Petrov")
    deadline = 1
    oop_hw = opp_teacher.create_homework("Learn OOP", deadline)
    docs_hw = opp_teacher.create_homework("Read docs", deadline)
    solution = "123456"
    result_1 = lazy_student.do_homework(oop_hw, solution)
    result_2 = lazy_student.do_homework(docs_hw, solution)
    opp_teacher.check_homework(result_1)
    opp_teacher.check_homework(result_2)
    assert opp_teacher.homework_done[oop_hw] == [result_1]
    assert opp_teacher.homework_done[docs_hw] == [result_2]
    opp_teacher.reset_results()
    assert opp_teacher.homework_done[oop_hw] == []
    assert opp_teacher.homework_done[docs_hw] == []


def test_is_the_list_of_homework_results_common_to_all_teachers():
    opp_teacher = Teacher("Daniil", "Shadrin")
    advanced_python_teacher = Teacher("Aleksandr", "Smetanin")
    assert opp_teacher.homework_done is advanced_python_teacher.homework_done


def test_attribute_homework_result():
    opp_teacher = Teacher("Daniil", "Shadrin")
    lazy_student = Student("Roman", "Petrov")
    deadline = 1
    oop_hw = opp_teacher.create_homework("Learn OOP", deadline)
    solution = "123456"
    result = lazy_student.do_homework(oop_hw, solution)
    assert result.homework == oop_hw
    assert result.author == lazy_student
    assert result.solution == solution


def test_attribute_homework():
    opp_teacher = Teacher("Daniil", "Shadrin")
    lazy_student = Student("Roman", "Petrov")
    text_of_homework = "Learn OOP"
    deadline = 1
    oop_hw = opp_teacher.create_homework(text_of_homework, deadline)
    solution = "123456"
    result = lazy_student.do_homework(oop_hw, solution)
    assert result.homework.text == text_of_homework
    assert result.homework.deadline == datetime.timedelta(days=deadline)
