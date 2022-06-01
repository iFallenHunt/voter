age = int(input('Enter your age: '))

if age < 16:
    print('Not a voter')
else:
    if age < 18 or age > 65:
        print('Falcultative voter')
    else:
        print('Mandatory voter')