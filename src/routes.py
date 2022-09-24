from flask import render_template, request, redirect, url_for, flash
from src.models import User, Phone, Email
from src import db
from sqlalchemy import update
from sqlalchemy.orm import joinedload
from . import app


@app.route("/healthcheck")
def healthcheck():
    return 'I am alive!'


@app.route('/', strict_slashes=False)
def index():
    contacts = User.query.options(joinedload(User.phone), joinedload(User.email)).all()
    return render_template('index.html', contacts=contacts)


@app.route('/detail/<int:id>', strict_slashes=False)
def detail(id):
    contact = User.query.options(joinedload(User.phone), joinedload(User.email)).filter_by(id=id).first()
    return render_template('detail.html', contact=contact)


@app.route('/contact', methods=['GET', 'POST'], strict_slashes=False)
def add_user():
    if request.method == 'POST':
        user = User(name=request.form['name'], address=request.form['address'])
        phone = Phone(phone_number=request.form['phone'])
        email = Email(email=request.form['email'])
        user.phone.append(phone)
        user.email.append(email)
        db.session.add(user)
        db.session.commit()
        flash('Contact added successfully')
        return redirect(url_for('index'))
    return render_template('contact.html')


@app.route('/delete/<int:id>', strict_slashes=False)
def delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    flash('Contact deleted successfully')
    return redirect(url_for('index'))


@app.route('/update/<int:id>', methods=['GET', 'POST'], strict_slashes=False)
def update(id):
    user = User.query.get(id)
    phone = Phone.query.get(id)
    email = Email.query.get(id)
    if request.method == 'POST':
        user.name = request.form['name']
        user.address = request.form['address']
        phone.phone_number = request.form['phone']
        email.email = request.form['email']
        db.session.commit()
        flash('Contact updated successfully')
        return redirect(url_for('index'))
