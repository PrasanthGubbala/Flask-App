from config import db


class Employee(db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),index=True)
    age = db.Column(db.Integer)
    salary = db.Column(db.Float)


