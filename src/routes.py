from flask import render_template, request, redirect, url_for, flash
from . import app


@app.route("/healthcheck")
def healthcheck():
    return 'I am alive!'


@app.route('/', strict_slashes=False)
def index():
    return render_template('index.html')
