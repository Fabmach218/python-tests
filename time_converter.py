def millis_to_hhmmss(millis):

    hours = millis // 3600000
    minutes = (millis % 3600000) // 60000
    seconds = (millis // 1000) % 60

    hhmmss = ''

    if hours < 10:
        hhmmss += '0' + str(hours)
    else:
        hhmmss += str(hours)

    hhmmss += ':'

    if minutes < 10:
        hhmmss += '0' + str(minutes)
    else:
        hhmmss += str(minutes)

    hhmmss += ':'

    if seconds < 10:
        hhmmss += '0' + str(seconds)
    else:
        hhmmss += str(seconds)

    return hhmmss

millis = int(input('Enter a time in milliseconds: '))

while millis < 0:
    print('You must enter a positive value!!!')
    millis = int(input('Enter a time in milliseconds: '))

print(millis_to_hhmmss(millis))
