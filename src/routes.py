from flask import render_template, request, redirect, url_for, flash
from src.models import User
from src import db
from sqlalchemy.orm import joinedload
from . import app


@app.route("/healthcheck")
def healthcheck():
    return 'I am alive!'


@app.route('/', strict_slashes=False)
def index():
    contacts = User.query.all()
    return render_template('index.html', contacts=contacts)


@app.route('/detail/<int:id>', strict_slashes=False)
def detail(id):
    contact = User.query.get(id)
    return render_template('detail.html', contact=contact)


@app.route('/contact', methods=['GET', 'POST'], strict_slashes=False)
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        address = request.form['address']
        user = User(name=name, phone=phone, email=email, address=address)
        db.session.add(user)
        db.session.commit()
        flash('Contact added successfully!')
        return redirect(url_for('index'))
    return render_template('contact.html')


#
@app.route('/delete/<int:id>', strict_slashes=False)
def delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    flash('Contact deleted successfully!')
    return redirect(url_for('index'))


#
@app.route('/update', defaults={'id': None}, methods=['POST'])
@app.route('/update/<int:id>', methods=['GET', 'POST'], strict_slashes=False)
def update(id):
    if request.method == 'POST':
        user = User.query.get(request.form['id'])
        user.name = request.form['name']
        user.phone = request.form['phone']
        user.email = request.form['email']
        user.address = request.form['address']
        db.session.commit()
        flash('Contact updated successfully!')
        return redirect(url_for('index'))
    user = User.query.get(id)
    return render_template('update.html', user=user)