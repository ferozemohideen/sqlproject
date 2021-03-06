from sqlalchemy import sql, orm
from app import db


#TODO: Add relationships. Right now we don't understand why some relationships like Frequents are one sided, posted on piazza and will update once we get an update on piazza
class Class(db.Model):
    __tablename__ = 'class'
    name = db.Column('name', db.String(100))
    classID = db.Column('classID', db.Integer, primary_key=True)
    frequents = orm.relationship('Frequents')

class Student(db.Model):
    __tablename__ = 'student'
    name = db.Column('name', db.String(100))
    email = db.Column('email', db.String(100), nullable=True)
    studentID = db.Column('studentID', db.Integer, primary_key=True)

class Comment(db.Model):
    __tablename__ = "comment"
    text = db.Column('text', db.String(10000))
    upvotes = db.Column('upvotes', db.Integer)
    downvotes = db.Column('downvotes', db.Integer)
    studentID = db.Column('studentID', db.Integer, db.ForeignKey('student.studentID'))
    commentID = db.Column('commentID', db.Integer, primary_key=True)
    
class Department(db.Model):
    __tablename__ = "department"
    name = db.Column('name', db.String(100))
    departmentID = db.Column('departmentID', db.Integer, primary_key=True)

class Taken(db.Model):
    __tablename__ = "taken"
    semester = db.Column('semester', db.String(4))
    starNumber = db.Column("starNumber", db.Float)
    commentID = db.Column("commentID", db.Integer, primary_key=True)
    studentID = db.Column('studentID', db.Integer, db.ForeignKey('student.studentID'))
    classID = db.Column('classID', db.Integer, db.ForeignKey('class.classID'))


class Professor(db.Model):
    __tablename__ = "professor"
    name = db.Column('name', db.String(100))
    professorID = db.Column('professorID', db.Integer, primary_key=True)

class Teaches(db.Model):
    classID = db.Column('classID', db.Integer, db.ForeignKey('class.classID'), primary_key=True)
    professorID = db.Column('professorID', db.Integer, db.ForeignKey('professor.professorID'),primary_key=True)
    semester = db.Column('semester', db.String(4))

# class Drinker(db.Model):
#     __tablename__ = 'drinker'
#     name = db.Column('name', db.String(20), primary_key=True)

#     likes = orm.relationship('Likes')
#     frequents = orm.relationship('Frequents')
#     @staticmethod
#     def edit(old_name, name, address, beers_liked, bars_frequented):
#         try:
#             db.session.execute('DELETE FROM likes WHERE drinker = :name',
#                                dict(name=old_name))
#             db.session.execute('DELETE FROM frequents WHERE drinker = :name',
#                                dict(name=old_name))
#             db.session.execute('UPDATE drinker SET name = :name, address = :address'
#                                ' WHERE name = :old_name',
#                                dict(old_name=old_name, name=name, address=address))
#             for beer in beers_liked:
#                 db.session.execute('INSERT INTO likes VALUES(:drinker, :beer)',
#                                    dict(drinker=name, beer=beer))
#             for bar, times_a_week in bars_frequented:
#                 db.session.execute('INSERT INTO frequents'
#                                    ' VALUES(:drinker, :bar, :times_a_week)',
#                                    dict(drinker=name, bar=bar,
#                                         times_a_week=times_a_week))
#             db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             raise e

# class Beer(db.Model):
#     __tablename__ = 'beer'
#     name = db.Column('name', db.String(20), primary_key=True)
#     brewer = db.Column('brewer', db.String(20))

# class Bar(db.Model):
#     __tablename__ = 'bar'
#     name = db.Column('name', db.String(20), primary_key=True)
#     address = db.Column('address', db.String(20))
#     serves = orm.relationship('Serves')

# class Likes(db.Model):
#     __tablename__ = 'likes'
#     drinker = db.Column('drinker', db.String(20),
#                         db.ForeignKey('drinker.name'),
#                         primary_key=True)
#     beer = db.Column('beer', db.String(20),
#                      db.ForeignKey('beer.name'),
#                      primary_key=True)

# class Serves(db.Model):
#     __tablename__ = 'serves'
#     bar = db.Column('bar', db.String(20),
#                     db.ForeignKey('bar.name'),
#                     primary_key=True)
#     beer = db.Column('beer', db.String(20),
#                      db.ForeignKey('beer.name'),
#                      primary_key=True)
#     price = db.Column('price', db.Float())

# class Frequents(db.Model):
#     __tablename__ = 'frequents'
#     drinker = db.Column('drinker', db.String(20),
#                         db.ForeignKey('drinker.name'),
#                         primary_key=True)
#     bar = db.Column('bar', db.String(20),
#                     db.ForeignKey('bar.name'),
#                     primary_key=True)
#     times_a_week = db.Column('times_a_week', db.Integer())
