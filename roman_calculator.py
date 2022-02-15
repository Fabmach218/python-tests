def start():

    option = int(input('''Welcome to the roman calculator!!!, what do you wanna do?\n
                       1 Convert number to roman\n
                       2 Convert roman to number'''))

    return option

def int_to_roman(number):

    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    roman = ''
    i = 0

    while number > 0:

        for x in range(number // val[i]):
            roman += syb[i]
            number -= val[i]

        i += 1

    return roman

def roman_to_int(rom):

    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    number = 0

    for x in range(len(rom)):

        if x > 0 and rom_val[rom[x]] > rom_val[rom[x - 1]]:
            number += rom_val[rom[x]] - 2 * rom_val[rom[x - 1]]
        else:
            number += rom_val[rom[x]]

    return number

def check_roman(rom):

    for x in range(len(rom)):

        if (rom[x] not in ('I', 'V', 'X', 'L', 'C', 'D', 'M')):
            return False
        
    return True
            

choice = start()

while choice != 1 and choice != 2:
    print('You must write 1 or 2!!!')
    choice = start()
    
if choice == 1:

    num = int(input('Enter a positive integer number: '))

    while num <= 0:
        num = int(input('Enter a positive integer number: '))
    
    print(str(num) + ' in romans is: ' + int_to_roman(num))
    
else:

    roman = input('Enter a roman numeral: ')

    while not check_roman(roman):
        print('Bad written roman numeral!!! Please, try again')
        roman = input('Enter a roman numeral: ')

    if check_roman(roman):
        print(roman + ' in numbers is: ' + str(roman_to_int(roman)))
