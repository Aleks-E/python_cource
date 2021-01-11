"""empty message

Revision ID: f2b374af6635
Revises: ef308e141eaa
Create Date: 2021-01-11 21:48:02.400702

"""
from alembic import op
import sqlalchemy as sa
from task_1 import engine, Teacher, Student, Homework, HomeworkResult
from sqlalchemy.orm import sessionmaker
from datetime import date


# revision identifiers, used by Alembic.
revision = 'f2b374af6635'
down_revision = 'ef308e141eaa'
branch_labels = None
depends_on = None


def upgrade():
    Session = sessionmaker(bind=engine)
    session = Session()
    teacher = Teacher(first_name="Daniil", last_name="Shadrin")
    session.add(teacher)
    student = Student(first_name="Roman", last_name="Petrov")
    session.add(student)
    homework = Homework(teacher_id=1, created_date=date(year=2021, month=1, day=1), deadline_date=date(year=2021, month=1, day=7), text="text")
    session.add(homework)
    homework_result = HomeworkResult(homework_id=1, author_id=1, solution="solution", created_date=date(year=2021, month=1, day=1))
    session.add(homework_result)
    session.commit()
    session.close()


def downgrade():
    Session = sessionmaker(bind=engine)
    session = Session()
    teacher = session.query(Teacher).get(1)
    session.delete(teacher)
    student = session.query(Student).get(1)
    session.delete(student)
    homework = session.query(Homework).get(1)
    session.delete(homework)
    homework_result = session.query(HomeworkResult).get(1)
    session.delete(homework_result)
    session.commit()
    session.close()
