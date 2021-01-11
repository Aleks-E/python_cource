from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, Date
from alembic import op
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()

engine = create_engine('sqlite:///main.db', echo=True)
meta = MetaData()

Teacher = Table(
   'Teacher', meta,
   Column('id', Integer, primary_key=True),
   Column('first_name', String),
   Column('last_name', String),
)

Student = Table(
   'Student', meta,
   Column('id', Integer, primary_key=True),
   Column('first_name', String),
   Column('last_name', String),
)

Homework = Table(
   'Homework', meta,
   Column('id', Integer, primary_key=True),
   Column('Teacher_id', Integer, ForeignKey('Teacher.id')),
   Column('Student_id', Integer, ForeignKey('Student.id')),
   Column('created_date', Date)
)





meta.drop_all(engine)
meta.create_all(engine)
# meta.drop_all(engine)


# Session = sessionmaker(bind=engine)
# session = Session()






conn = engine.connect()
ins = Teacher.insert().values(first_name="Daniil", last_name="Shadrin")
# ins = Teacher.delete()
conn.execute(ins)
# conn.close()




# conn = engine.connect()
# ins = Teacher.update().values("id"=1, first_name="Daniil", last_name="Shadrin")
# ins = Teacher.delete()
# conn.execute(ins)
# conn.close()






# a = Teacher(first_name="Daniil", last_name="Shadrin")

# ------------------------
#
# # Session = sessionmaker(bind=engine)
# # session = Session()
#
#
# class Teacher(Base):
#    __tablename__ = 'Teacher'
#
#    id = Column(Integer, primary_key=True)
#    first_name = Column(String)
#    last_name = Column(String)
#
#
# class Student(Base):
#    __tablename__ = 'Student'
#
#    id = Column(Integer, primary_key=True)
#    first_name = Column(String)
#    last_name = Column(String)
#
#
# class Homework(Base):
#    __tablename__ = 'Homework'
#
#    id = Column(Integer, primary_key=True)
#    Teacher_id = Column(Integer, ForeignKey('Teacher.id'))
#    Student_id = Column(Integer, ForeignKey('Student.id'))
#    created_date = Column(Date)
#
#
#
#
# # Base.metadata.create_all(engine)
# # Base.metadata.drop_all(engine)
#
# Session = sessionmaker(bind=engine)
# session = Session()
#
# a = Teacher(first_name="Daniil", last_name="Shadrin")
# session.add(a)
# session.commit()
# session.close()
#
# # Base.metadata.create_all(engine)
# # Base.metadata.drop_all(engine)
#
# # for i in range(1, 4):
# #    a = session.query(Teacher).get(i)
# #    session.delete(a)
# #    session.commit()
#
#
# # a = session.query(Teacher).get(4)
# # a = session.query(Teacher).all()
# # print(a)
#
# # for i in a:
# #    print(i)
#

# ------------------------













# a = session.query(Teacher).filter_by(first_name="Daniil").count()

# print(a)

# session.close()

# session = Session()



# a = session.query(Teacher).get(2)
# a = session.query(Teacher).all()
# print(a)

# for i in a:
#    print(i)




# session.delete(a)
# session.commit()




# print(help(session))








# Session = sessionmaker(bind=engine)
# session = Session()





# a = Teacher(first_name="Daniil", last_name="Shadrin")
#
# session.add(a)
# session.commit()




# ---------------------
# from sqlalchemy import Column, Integer, String
# from sqlalchemy import create_engine
#
# engine = create_engine('sqlite:///sales.db', echo=True)
# from sqlalchemy.ext.declarative import declarative_base
#
# Base = declarative_base()
#
#
# class Customers(Base):
#    __tablename__ = 'customers'
#
#    id = Column(Integer, primary_key=True)
#    name = Column(String)
#    address = Column(String)
#    email = Column(String)
#
#    # def __init__(self, name, address, email):
#    #    self.name = name
#    #    self.address = address
#    #    self.email = email
#
#
# from sqlalchemy.orm import sessionmaker
#
# Session = sessionmaker(bind=engine)
# session = Session()
#
# c1 = Customers(name='Ravi Kumar', address='Station Road Nanded', email='ravi@gmail.com')
#
# session.add(c1)
# session.commit()




