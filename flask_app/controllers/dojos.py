from flask import Flask, render_template, request, redirect, session

from flask_app import app
from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import Ninja


@app.route('/')
def home():
	return redirect('/dojos')

@app.route('/dojos')
def dojos():
	return render_template('dojos.html', dojos = Dojo.get_all())

@app.route('/dojos/create', methods=['POST'])
def create_dojo():
	Dojo.create(request.form)
	return redirect('/dojos')

@app.route('/dojos/<id>')
def show_dojo(id):
	data = {'id': id}
	dojo_id = {'dojo_id': id}
	return render_template('dojo.html', dojo = Dojo.get_dojo(data), ninjas = Ninja.get_all_ninjas(dojo_id))