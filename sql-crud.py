from sqlalchemy import (
    create_engine, Column,
    Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# execting instructions from the chinook DB
db = create_engine("postgresql:///chinook")

base = declarative_base()

# create a class based model for Programmer table

class Programmer(base):
    __tablename__ = "Programmer"
    Id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)



Session = sessionmaker(db)

# open an actual session by calling the session() sub class defined above
session = Session()

# creating the database using declarative_base sub class
base.metadata.create_all(db)

# creating records on our Programmer table

susu = Programmer(
    first_name = "Susu",
    last_name = "Hunt",
    gender = "F",
    nationality = "Canadian",
    famous_for = "Programming"
)

bil = Programmer(
    first_name = "Bil",
    last_name = "Gates",
    gender = "M",
    nationality = "USA",
    famous_for = "Micro Soft"
)


lee = Programmer(
    first_name = "Lee",
    last_name = "something",
    gender = "M",
    nationality = "British",
    famous_for = "Internet"
)

# add each intance of our programmer to the session
# session.add(susu)
# session.add(lee)
# session.add(bil)

# commit out session to DB
# session.commit()

# updating a single record
# if you do not append the .first() you will need to itereate over the cursor to access its data
# programmer = session.query(Programmer).filter_by(Id=4).first()
# programmer.famous_for = "testing"
# session.commit()

# updating multiple records
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "female"
#     elif person.gender == "M":
#         person.gender = "male"
#     else:
#         print("Gender not found")
#     session.commit()

# delete record
fname = input('Enter first name')
lname = input('Enter last name')



# qery the DB to find all programmers
programmers = session.query(Programmer)
for p in programmers:
    print(p.Id, p.gender, p.first_name, p.last_name, p.nationality, p.famous_for, sep= " | ")
