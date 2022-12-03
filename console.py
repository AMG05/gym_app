import pdb
from models.booking import Booking
from models.exercise_class import Exercise_class
from models.instructor import Instructor
from models.member import Member

import repositories.booking_repository as booking_repository
import repositories.exercise_class_repository as exercise_class_repository
import repositories.instructor_repository as instructor_repository
import repositories.member_repository as member_repository

# booking_repository.delete_all()
# exercise_class_repository.delete_all()
# instructor_repository.delete_all()
# member_repository.delete_all()

member1 = Member('Natalie Webster', 35, 'premium')
member_repository.save(member1)

member2 = Member('Anna Kelso', 36, 'standard')
member_repository.save(member2)

member3 = Member('Melanie Heskett', 32, 'premium')
member_repository.save(member3)


exercise_class1 = Exercise_class('Yoga', 'Hatha', '60 mins', '4/12/22', 20, 'instructor_id')
exercise_class_repository.save(exercise_class1)

exercise_class2 = Exercise_class('Circuits', 'Cardio', '45 mins', '4/12/22', 15, 'instructor_id')
exercise_class_repository.save(exercise_class2)

exercise_class3 = Exercise_class('Body Attack', 'Cardio', '55 mins', '5/12/22', 25, 'instructor_id')
exercise_class_repository.save(exercise_class3)

exercise_class4 = Exercise_class('Full Body Kettlebells', 'strength', '45 mins', '4/12/22', 12, 'instructor_id')
exercise_class_repository.save(exercise_class4)

instructor1 = Instructor('Sarah', exercise_class1)
instructor_repository.save(instructor1)

instructor2 = Instructor('Aisha', exercise_class3)
instructor_repository.save(instructor2)

instructor3 = Instructor('Jamie', exercise_class2)
instructor_repository.save(instructor3)

instructor4 = Instructor('Alana', exercise_class4)
instructor_repository.save(instructor4)

booking1 = Booking('exercise_class4', 'member1')
booking_repository.save(booking1)

booking2 = Booking('exercise_class3', 'member3')
booking_repository.save(booking2)


pdb.set_trace()
