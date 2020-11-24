import datetime


from hw6.task_1 import Teacher, Student


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


def test_homework_attribute():
    teacher = Teacher("Daniil", "Shadrin")
    text_of_homework = "Learn functions"
    deadline_days = 1
    homework = teacher.create_homework(text_of_homework, deadline_days)
    assert homework.text == text_of_homework
    assert homework.deadline == datetime.timedelta(days=1)











