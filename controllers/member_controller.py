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
    members = member_repository.select_all() # NEW
    return render_template("members/new.html", members = members)

@member_blueprint.route("/members/<member_id>")
def get_member(member_id):
    member = member_repository.select(member_id)
    return render_template("members/show.html", member=member)