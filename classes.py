class Student:

    def __init__(self, idnum, fname, lname):

        self.idnum = idnum
        self.fname = fname
        self.lname = lname

list = []

list.append(Student('71753072', 'Fabio', 'Marangon'))
list.append(Student('72674839', 'Juan', 'Perez'))
list.append(Student('84729103', 'Fernando', 'Sanchez'))

print('ID\tFirst Name\tLast Name')

for item in list:
    print(item.idnum + '\t' + item.fname + '\t' + item.lname)

