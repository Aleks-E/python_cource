import datetime
import time


from hw5.task_1 import Homework, Student, Teacher


def test_teacher_attribute():
    first_name, last_name = "Daniil", "Shadrin"
    teacher = Teacher(first_name, last_name)
    assert (teacher.first_name, teacher.last_name) == (first_name, last_name)


def test_create_homework_by_the_theacher():
    teacher = Teacher("Daniil", "Shadrin")
    homework = teacher.create_homework("Learn functions", 1)
    assert isinstance(homework, Homework)


def test_homework_attribute():
    teacher = Teacher("Daniil", "Shadrin")
    text_of_homework = "Learn functions"
    deadline_days = 1
    homework = teacher.create_homework(text_of_homework, deadline_days)
    assert (homework.text, homework.deadline) == (
        text_of_homework,
        datetime.timedelta(days=1),
    )


def test_student_attribute():
    first_name, last_name = "Roman", "Petrov"
    student = Student(first_name, last_name)
    assert (student.first_name, student.last_name) == (first_name, last_name)


def test_return_homework_by_the_sturent():
    student = Student("Roman", "Petrov")
    teacher = Teacher("Daniil", "Shadrin")
    deadline_1_sec = 1 / 24 / 60 / 60
    deadline_days = deadline_1_sec
    homework = teacher.create_homework("Learn functions", deadline_days)
    assert student.do_homework(homework) is homework
    time.sleep(2)
    assert student.do_homework(homework) is None


def test_sturent_print_out(capsys):
    student = Student("Roman", "Petrov")
    teacher = Teacher("Daniil", "Shadrin")
    deadline_1_sec = 1 / 24 / 60 / 60
    deadline_days = deadline_1_sec
    homework = teacher.create_homework("Learn functions", deadline_days)
    student.do_homework(homework)
    out, err = capsys.readouterr()
    assert out == ""
    time.sleep(2)
    student.do_homework(homework)
    out, err = capsys.readouterr()
    assert out == "You are late\n"
