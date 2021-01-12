"""empty message

Revision ID: f2b374af6635
Revises: ef308e141eaa
Create Date: 2021-01-11 21:48:02.400702

"""
from datetime import date

from sqlalchemy.orm import sessionmaker

from task_1 import Homework, HomeworkResult, Student, Teacher, engine


# revision identifiers, used by Alembic.
revision = "f2b374af6635"
down_revision = "ef308e141eaa"
branch_labels = None
depends_on = None


def upgrade() -> None:
    session = sessionmaker(bind=engine)
    sess = session()
    teacher = Teacher(first_name="Daniil", last_name="Shadrin")
    sess.add(teacher)
    student = Student(first_name="Roman", last_name="Petrov")
    sess.add(student)
    homework = Homework(
        teacher_id=1,
        created_date=date(year=2021, month=1, day=1),
        deadline_date=date(year=2021, month=1, day=7),
        text="text",
    )
    sess.add(homework)
    homework_result = HomeworkResult(
        homework_id=1,
        author_id=1,
        solution="solution",
        created_date=date(year=2021, month=1, day=1),
    )
    sess.add(homework_result)
    sess.commit()
    sess.close()


def downgrade() -> None:
    session = sessionmaker(bind=engine)
    sess = session()
    teacher = sess.query(Teacher).get(1)
    sess.delete(teacher)
    student = sess.query(Student).get(1)
    sess.delete(student)
    homework = sess.query(Homework).get(1)
    sess.delete(homework)
    homework_result = sess.query(HomeworkResult).get(1)
    sess.delete(homework_result)
    sess.commit()
    sess.close()
