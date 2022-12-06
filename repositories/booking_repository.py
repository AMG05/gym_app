from db.run_sql import run_sql
from models.booking import Booking
from models.exercise_class import Exercise_class
from models.member import Member
import repositories.exercise_class_repository as exercise_class_repository
import repositories.member_repository as member_repository



def save(booking):
    sql = "INSERT INTO bookings (exercise_classes_id, members_id) VALUES ( %s, %s ) RETURNING *"
    values = [booking.exercise_class.id, booking.member.id]
    results = run_sql( sql, values )
    booking.id = results[0]['id']
    return booking


def select_all():
    bookings = []

    sql = "SELECT * FROM bookings"
    results = run_sql(sql)

    for row in results:
        exercise_class = exercise_class_repository.select(row['exercise_classes_id'])
        member = member_repository.select(row['members_id'])
        booking = Booking(exercise_class, member, row['id]'])
        bookings.append(booking)
    return bookings

def select(id):
    sql = "SELECT * FROM BOOKINGS where id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    exercise_class = exercise_class_repository.select(result["exercise_class_id"])
    member = member_repository.select(result["member_id"])
    booking = Booking(exercise_class, member, result["id"])
    return booking


def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(booking):
    sql = "UPDATE bookings SET (exercise_class_id, member_id) = (%s, %s) WHERE id = %s"
    values = [booking.exercise_class.id, booking.member.id, booking.id]
    run_sql(sql, values)