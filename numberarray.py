import random

numbers = []
total = 0

for x in range(10):
    numbers.append(random.randrange(0,20))

print('Numbers: ')

for x in range(10):
    total += numbers[x]
    print(numbers[x])

print('Sum: ' + str(total))

def orderA(numberList):

    ascendent = numberList

    for x in range(10-1):
        for y in range (x+1,10):

            auxA = 0

            if(ascendent[x] > ascendent[y]):

               auxA = ascendent[x]
               ascendent[x] = ascendent[y]
               ascendent[y] = auxA

    return ascendent

def orderD(numberList):

    descendent = numberList

    for x in range(10-1):
        for y in range (x+1,10):

            auxD = 0

            if(descendent[x] < descendent[y]):

               auxD = descendent[x]
               descendent[x] = descendent[y]
               descendent[y] = auxD

    return descendent
                 
print('Ascendent: ')

for x in range(10):
           print(orderA(numbers)[x])

print('Descendent: ')

for x in range(10):
           print(orderD(numbers)[x])

