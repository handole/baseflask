from app import db
from sqlalchemy.orm import relationship, backref

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def generate_password(password):
        password_hash = generate_password_hash(password)
        return password_hash

    def __repr__(self):
        return '<User {}>'.format(self.username)    


class Task(db.Model):
    __tablename__ = 'task'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True)
    description = db.Column(db.String(1000), index=True)
    search_type = db.Column(db.String(100), index=True)
    search = db.Column(db.String(100), index=True)
    count = db.Column(db.Integer, index=True)
    created_at = db.Column(db.String(100), index=True)
    usage = db.Column(db.Boolean, default=False, nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = relationship(User, backref=backref("tasks", cascade="all, delete-orphan"))

    def is_active(self):
        return True

    def __repr__(self):
        return '<Task {}>'.format(self.name)