meters = float(input('Insert any distance in meters'))

while meters < 0:
    meters = float(input('Insert any distance in meters'))

feet = meters / 0.3048
miles = feet / 5280

feet = round(feet, 2)
miles = round(miles, 2)

print('Feet: ' + str(feet) + ' ft')
print('Miles: ' + str(miles) + ' mi')
