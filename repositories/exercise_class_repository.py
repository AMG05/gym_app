from db.run_sql import run_sql
from models.exercise_class import Exercise_class
from models.booking import Booking
from models.member import Member
from models.instructor import Instructor
import repositories.instructor_repository as instructor_repository

def save(exercise_class):
    sql = "INSERT INTO exercise_classes(name, type, duration, date, capacity, instructor_id) VALUES ( %s, %s, %s, %s, %s, %s ) RETURNING id"
    values = [exercise_class.name, exercise_class.type, exercise_class.duration, exercise_class.date, exercise_class.capacity, exercise_class.instructor_id]
    results = run_sql( sql, values )
    exercise_class.id = results[0]['id']
    return exercise_class

    

def select_all():
    exercise_classes = []

    sql = "SELECT * FROM exercise_classes"
    results = run_sql(sql)
    for row in results:
        exercise_class = Exercise_class(row['name'], row['type'], row['duration'], row['date'], row['capacity'],row['instructor'],row['id'])
        exercise_classes.append(exercise_class)
    return exercise_class