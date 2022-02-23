import random

class Student:

    #Constructor (use self before parameters)
    def __init__(self, fname, lname):

        self.idnum = Student.gen_id() #Calling static method (class goes always before)
        self.fname = fname
        self.lname = lname

    #Instance method
    def concat_name(self):
        return self.fname + ' ' + self.lname

    #Static method
    def gen_id():

        idnum = str(random.randrange(1,10**8))

        while len(idnum) < 8:

            idnum = '0' + idnum

        return idnum

list = []

list.append(Student('Fabio', 'Marangon')) ##Self parameter in constructor is not put here
list.append(Student('Juan', 'Perez'))
list.append(Student('Fernando', 'Sanchez'))

print('ID\tFull Name')

for item in list:
    print(item.idnum + '\t' + item.concat_name()) ##Calling instance method (no self)

