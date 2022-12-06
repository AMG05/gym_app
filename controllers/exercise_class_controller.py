from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.exercise_class import Exercise_class
import repositories.exercise_class_repository as exercise_class_repository

exercise_class_blueprint = Blueprint("exerciseClasses", __name__)

@exercise_class_blueprint.route("/exerciseClasses")
def exercise_classes():
    exercise_classes = exercise_class_repository.select_all() # NEW
    return render_template("exerciseClasses/index.html", exercise_classes = exercise_classes)


@exercise_class_blueprint.route("/exerciseClasses/new")
def new_exercise_class():
    exercise_classes = exercise_class_repository.select_all() # NEW
    return render_template("exerciseClasses/new.html", exercise_classes = exercise_classes)

@exercise_class_blueprint.route("/exerciseClasses/<exercise_classes_id>")
def get_exercise_class(exercise_class_id):
    exercise_classes = exercise_class_repository.select(exercise_class_id)
    return render_template("exerciseClasses/show.html", exercise_classes=exercise_classes)

@exercise_class_blueprint.route("/exerciseClasses", methods=['POST'])
def create_exercise_class():
    name = request.form['name']
    type = request.form['type']
    duration = request.form['duration']
    date = request.form['date']
    capacity = request.form ['capacity']
    instructor = request.form ['instructor']
    exercise_class = Exercise_class(name, type, duration, date, capacity, instructor)
    exercise_class_repository.save(exercise_class)
    return redirect('/exerciseClasses')
# CREATE
# POST '/visits'

@exercise_class_blueprint.route("/exerciseClasses/<id>/edit")
def edit_exercise_class(id):
  exercise_classes = exercise_class_repository.select(id)
  return render_template('exerciseClasses/edit.html',  exercise_classes = exercise_classes)

@exercise_class_blueprint.route("/exerciseClasses/<id>", methods=['POST'])
def update_exercise_class(id):
  name = request.form['name']
  type = request.form['type']
  duration = request.form['duration']
  date = request.form['date']
  capacity = request.form['capacity']
  instructor = request.form['instructor']
  exercise_class = Exercise_class(name, type, duration, date, capacity, instructor)
  exercise_class_repository.update(exercise_class)
  return redirect('/exerciseClasses')

@exercise_class_blueprint.route("/exerciseClasses/<id>/delete", methods=["POST"])
def delete_exercise_class(id):
    exercise_class_repository.delete(id)
    return redirect("/exerciseClasses")

