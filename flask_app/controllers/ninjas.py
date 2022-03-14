from flask import Flask, render_template, request, redirect, session

from flask_app import app
from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import Ninja

@app.route('/ninjas')
def ninjas():
	return render_template('ninjas.html', dojos = Dojo.get_all())

@app.route('/ninjas/create', methods=['POST'])
def create_ninjas():
  Ninja.create(request.form)
  return redirect('/dojos')