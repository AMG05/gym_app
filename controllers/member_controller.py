from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository

member_blueprint = Blueprint("members", __name__)

@member_blueprint.route("/members")
def members():
    members = member_repository.select_all() # NEW
    return render_template("members/index.html", members = members)

@member_blueprint.route("/members/new")
def new_member():
    return render_template("members/new.html")



@member_blueprint.route("/members",  methods=['POST'])
def create_member():
    name = request.form['name']
    age = request.form['age']
    membership_type = request.form['membership_type']
    member = Member(name, int(age), membership_type)
    member_repository.save(member)
    return redirect('/members')

# EDIT (display form)
# GET '/members/<id>/edit

@member_blueprint.route("/members/<id>")
def show_member(id):
    member = member_repository.select(id)
    return render_template("members/show.html", member=member)

@member_blueprint.route('/members/<member_id>/edit')
def edit_member(member_id):
    member = member_repository.select(member_id)
    return render_template('members/edit.html', member=member)

@member_blueprint.route("/members/<member_id>", methods=["POST"])
def update_member(id):
    name = request.form["name"]
    age = request.form["age"]
    membership_type = request.form['membership_type']
    member = Member(name, age, membership_type,id)
    member_repository.update(member)
    return redirect("/members")


@member_blueprint.route("/members/<id>/delete", methods=["POST"])
def delete_member(id):
    member_repository.delete(id)
    return redirect("/members")