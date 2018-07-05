num = int(input('Enter a no '))
fact = 1
if num < 0:
    print('Number cant be smaller than 0 ')
elif num == 0 or num == 1:
    print('Factorial of a Number', num, ' =  1')
else:
    for i in range(num, 1, -1):
        fact = fact * i

print('Factorial of a number', num, ' = ', fact)
