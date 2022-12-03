from db.run_sql import run_sql
from models.member import Member
from models.instructor import Instructor

def save(member):
    sql = "INSERT INTO members( name, age, membership_type ) VALUES ( %s, %s, %s) RETURNING id"
    values = [member.name, member.age, member.membership_type]
    results = run_sql( sql, values )
    member.id = results[0]['id']
    return member


def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['name'],row['age'],row['membership_type'], row['id'])
        members.append(member)
    return members