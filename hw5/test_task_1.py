import datetime


from hw5.task_1 import Student, Teacher


def test_teacher_attribute():
    first_name, last_name = "Daniil", "Shadrin"
    teacher = Teacher(first_name, last_name)
    assert teacher.first_name == first_name
    assert teacher.last_name == last_name


def test_homework_attribute():
    teacher = Teacher("Daniil", "Shadrin")
    text_of_homework = "Learn functions"
    deadline_days = 1
    homework = teacher.create_homework(text_of_homework, deadline_days)
    assert homework.text == text_of_homework
    assert homework.deadline == datetime.timedelta(days=1)


def test_student_attribute():
    first_name, last_name = "Roman", "Petrov"
    student = Student(first_name, last_name)
    assert student.first_name == first_name
    assert student.last_name == last_name


def test_return_homework_by_the_student_after_deadline():
    student = Student("Roman", "Petrov")
    teacher = Teacher("Daniil", "Shadrin")
    deadline_days = 0
    homework = teacher.create_homework("Learn functions", deadline_days)
    assert student.do_homework(homework) is None


def test_return_homework_by_the_student_before_deadline():
    student = Student("Roman", "Petrov")
    teacher = Teacher("Daniil", "Shadrin")
    deadline_days = 1
    homework = teacher.create_homework("Learn functions", deadline_days)
    assert student.do_homework(homework) is homework


def test_student_print_out_after_deadline(capsys):
    student = Student("Roman", "Petrov")
    teacher = Teacher("Daniil", "Shadrin")
    deadline_days = 0
    homework = teacher.create_homework("Learn functions", deadline_days)
    student.do_homework(homework)
    out, err = capsys.readouterr()
    assert out == "You are late\n"


def test_student_print_out_before_deadline(capsys):
    student = Student("Roman", "Petrov")
    teacher = Teacher("Daniil", "Shadrin")
    deadline_days = 1
    homework = teacher.create_homework("Learn functions", deadline_days)
    student.do_homework(homework)
    out, err = capsys.readouterr()
    assert out == ""
