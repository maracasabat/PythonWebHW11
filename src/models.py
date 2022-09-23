from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from src import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column('address', db.String(120), nullable=True)
    phone = relationship('Phone', back_populates='user', cascade="all, delete-orphan")
    email = relationship('Email', back_populates='user', cascade='all, delete-orphan')


class Phone(db.Model):
    __tablename__ = 'phones'
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column('phone_number', db.String(20), nullable=False)
    user_id = db.Column('user_id', db.Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='phone')


class Email(db.Model):
    __tablename__ = 'emails'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column('email', db.String(120), nullable=False)
    user_id = db.Column('user_id', db.Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='email')
