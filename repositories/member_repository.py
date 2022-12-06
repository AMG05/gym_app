from db.run_sql import run_sql
from models.member import Member
from models.exercise_class import Exercise_class

#To save a new member to a members table
def save(member):
    sql = "INSERT INTO members(name, age, membership_type ) VALUES ( %s, %s, %s) RETURNING *"
    values = [member.name, member.age, member.membership_type]
    results = run_sql( sql, values )
    member.id = results[0]['id']
    return member

#To select all members
def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['name'],row['age'],row['membership_type'], row['id'])
        members.append(member)
    return members

def select(id):
   members = None
   sql = "SELECT * FROM members WHERE id = %s"
   values = [id]
   result = run_sql(sql, values)[0]

   if result is not None:
        member = Member(result['name'], result['age'], result['membership_type'], result['id'])
   return member

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

#To delete a member from a members table
def delete(id):
    sql = "DELETE FROM members WHERE members.id = %s"
    values = [id]
    run_sql(sql, values)


def exercise_classes(member):
    exercise_classes = []
    sql = "SELECT exercise_classes.* from exercise_classes INNER JOIN bookings ON booking.exercise_classes_id = exercise_classes.id WHERE member_id = %s"
    values = [member.id]
    results = run_sql(sql, values)
    exercise_classes=[]
    for row in results:
        exercise_class = Exercise_class(row['name'], row['type'], row['duration'],row['date'], row['capacity'], row['instructor'], row['id'])
        exercise_classes.append(exercise_class)
    return exercise_class

def update(member):
    sql = "UPDATE members SET (name, age, membership_type) = (%s, %s, %s) WHERE id = %s"
    values = [member.name, member.age, member.membership_type]
    run_sql(sql, values)