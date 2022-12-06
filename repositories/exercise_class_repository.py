from db.run_sql import run_sql
from models.exercise_class import Exercise_class
from models.booking import Booking
from models.member import Member

def save(exercise_class):
    sql = "INSERT INTO exercise_classes(name, type, duration, date, capacity, instructor) VALUES ( %s, %s, %s, %s, %s, %s ) RETURNING *"
    values = [exercise_class.name, exercise_class.type, exercise_class.duration, exercise_class.date, exercise_class.capacity, exercise_class.instructor]
    results = run_sql( sql, values )
    exercise_class.id = results[0]['id']
    return exercise_class
  

def select_all():
    exercise_class = []

    sql = "SELECT * FROM exercise_classes"
    results = run_sql(sql)
    exercise_classes = []
    for row in results:
        exercise_class = Exercise_class(row['name'], row['type'], row['duration'], row['date'], row['capacity'], row['instructor'], row['id'])
        exercise_classes.append(exercise_class)
    return exercise_classes

def select(id):
    exercise_class = None
    sql = "SELECT * FROM exercise_classes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        exercise_class = Exercise_class(result['name'], result['type'], result['duration'], result['date'], result['capacity'],result['instructor'], result['id'])
    return exercise_class

def delete_all():
    sql = "DELETE FROM exercise_classes"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM exercise_classes WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def member(exercise_class):
    exercise_classes = []
    sql = "SELECT exercise_classes.* from exercise_classes INNER JOIN members ON members.user_id = members.id WHERE exercise_classes_id = %s"
    values = [exercise_classes.id]
    results = run_sql(sql, values)
    members = []
    for row in results:
        member = Member(row['name'], row['age'], row['membership_type'],row['id'])
        members.append(member)
    return members

def update(exercise_class):
    sql = "UPDATE exercise_classes SET (name, type, duration, date, capacity, instructor) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [exercise_class.name, exercise_class.type, exercise_class.duration, exercise_class.date, exercise_class.capacity, exercise_class.instructor]
    run_sql(sql, values)

def select_members_of_exercise_class(id):
  members = []
  sql = "SELECT members.* FROM members INNER JOIN bookings ON bookings.member_id = members.id WHERE bookings.workout_id = %s"
  values = [id]
  results = run_sql(sql, values)
  for result in results:
    member = Member(result["name"], result["age"], result["membership_type"])
    members.append(member)
  return members

 


  





