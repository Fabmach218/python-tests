class Student:

    def __init__(self, idnum, fname, lname):

        self.idnum = idnum
        self.fname = fname
        self.lname = lname

    def concat_name(self):
        return self.fname + ' ' + self.lname

list = []

list.append(Student('71694372', 'Fabio', 'Marangon'))
list.append(Student('72674839', 'Juan', 'Perez'))
list.append(Student('84729103', 'Fernando', 'Sanchez'))

print('ID\tFull Name')

for item in list:
    print(item.idnum + '\t' + item.concat_name())

