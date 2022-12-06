from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.exercise_class_repository as exercise_class_repository
import repositories.member_repository as member_repository

bookings_blueprint = Blueprint("bookings", __name__)


@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all()
    return render_template("bookings/index.html", bookings=bookings)


@bookings_blueprint.route("/booking/new", methods = ['GET'])
def new_booking():
  exercise_classes = exercise_class_repository.select_all()
  members = member_repository.select_all()
  return render_template("booking/new.html", exercise_classes = exercise_classes, members = members)

@bookings_blueprint.route("/bookings", methods=["POST"])
def create_booking():
  exercise_class_id = request.form["exercise_class_id"]
  member_id = request.form["member_id"]
  exercise_classes = exercise_class_repository.select(exercise_class_id)
  member = member_repository.select(member_id)
  new_booking = Booking(exercise_classes, member)
  booking_repository.save(new_booking)
  return redirect("/bookings")

@bookings_blueprint.route("/booking/<id>/edit")
def edit_booking(id):
  booking = booking_repository.select(id)
  exercise_classes = exercise_class_repository.select_all()
  members = member_repository.select_all()
  return render_template("/booking/edit.html", booking=booking, exercise_classes = exercise_classes, members=members)

@bookings_blueprint.route("/booking/<id>", methods=["POST"])
def update_booking(id):
  exercise_class_id = request.form["exercise_class_id"]
  member_id = request.form["member_id"]
  exercise_classes = exercise_class_repository.select(exercise_class_id)
  member = member_repository.select(member_id)
  booking = Booking(exercise_classes, member, id)
  booking_repository.update(booking)
  return redirect("/bookings")

@bookings_blueprint.route("/booking/<id>/delete", methods=["POST"])
def delete_booking(id):
    booking_repository.delete(id)
    return redirect("/bookings")