loc = input('enter your current location:')

if loc.lower() == 'auto shop':
    print('Welcome to the Auto Shop!')
elif loc.lower() == 'bank':
    print('Welcome to the bank!')
elif loc.lower() == 'uyo':
    print('Welcome to the Land of Promise!')
    street = input('your street name?') 
    if street.lower() == 'nwaniba':
        print("life's cool!")
    else:
        print('Oops..i cant find your current location right now!')
else:
    print('Where are you?')                   