from db.run_sql import run_sql
from models.instructor import Instructor
from models.exercise_class import Exercise_class
import repositories.instructor_repository as instructor_repository
import repositories.member_repository as member_repository

def save(instructor):
    sql = "INSERT INTO instructors(name, exercise_class) VALUES ( %s, %s) RETURNING id"
    values = [instructor.name, instructor.exercise_class]
    results = run_sql( sql, values )
    instructor.id = results[0]['id']
    return instructor


def select_all():
    instructors = []

    sql = "SELECT * FROM instructors"
    results = run_sql(sql)

    for row in results:
        instructor = Instructor (row['name'],row['exercise_class'],row['id'])
        instructors.append(instructor)
    return instructors