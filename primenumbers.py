num = int(input('Enter a positive integer number'))
div = '1, '
flag = -1

for i in range(2,num):
	if num % i == 0:
                flag = i
                div = div + str(i) + ', '

div = div + str(num)

if flag != -1:
        print('Not prime')
else:
        print('Prime')

print('Divisors: ' + div)
