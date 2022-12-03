from db.run_sql import run_sql
from models.booking import Booking
from models.exercise_class import Exercise_class
from models.member import Member
import repositories.member_repository as member_repository
import repositories.exercise_class_repository as exercise_class_repository


def save(booking):
    sql = "INSERT INTO bookings ( exercise_class_id, member_id ) VALUES ( %s, %s ) RETURNING id"
    values = [booking.exercise_class.id, booking.members.id]
    results = run_sql( sql, values )
    booking.id = results[0]['id']
    return booking


def select_all():
    bookings = []

    sql = "SELECT * FROM bookings"
    results = run_sql(sql)

    for row in results:
        exercise_class = exercise_class_repository(row['exercise_class_id'])
        member = member_repository(row['member_id'])
        booking = Booking(exercise_class, member, row['id]'])
        bookings.append(booking)
    return bookings