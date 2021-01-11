from sqlalchemy import Column, Date, ForeignKey, Integer, String, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine("sqlite:///main.db", echo=True)


class Teacher(Base):
    __tablename__ = "Teacher"

    id = Column(Integer, primary_key=True)  # noqa A003 - builtin name (id)
    first_name = Column(String)
    last_name = Column(String)


class Student(Base):
    __tablename__ = "Student"

    id = Column(Integer, primary_key=True)  # noqa A003 - builtin name (id)
    first_name = Column(String)
    last_name = Column(String)


class Homework(Base):
    __tablename__ = "Homework"

    id = Column(Integer, primary_key=True)  # noqa A003 - builtin name (id)
    teacher_id = Column(Integer, ForeignKey("Teacher.id"))
    created_date = Column(Date)
    deadline_date = Column(Date)
    text = Column(Text)


class HomeworkResult(Base):
    __tablename__ = "HomeworkResult"

    id = Column(Integer, primary_key=True)  # noqa A003 - builtin name (id)
    homework_id = Column(Integer, ForeignKey("Homework.id"))
    author_id = Column(Integer, ForeignKey("Student.id"))
    solution = Column(Text)
    created_date = Column(Date)
