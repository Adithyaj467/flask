from crud import db, Puppy


my_puppy=Puppy("Rufus",5)
db.session.add(my_puppy)
db.session.commit()

##orm object relation mapper
all_puppies=Puppy.query.all()
print(all_puppies)

#select by id
puppy_one=Puppy.query.get(1)
print(puppy_one.name)
#filters
#generates sql code
puppy_frankie=Puppy.query.filter_by(name='Frankie')
print(puppy_frankie.all())
#updates

first_puppy=Puppy.query.get(1)
first_puppy.age=10
db.session.add(first_puppy)
db.session.commit()

#del

second_pup=Puppy.query.get(2)
db.session.delete(second_pup)
db.session.commit()

all_puppies=Puppy.query.all()
print(all_puppies)
