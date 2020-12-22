from crud import db,Puppy
#creates all the database tables
db.create_all()

sam=Puppy("sammy",3)
frank=Puppy("frankie",4)

#none is expected

print(sam.id)
print(frank.id)

db.session.add(sam)
db.session.add(frank)

db.session.commit()
print(sam.id)
print(frank.id)
