name = 'faxx fasino'
pin = 2244

username = input('enter username:')
password = int(input('enter password:'))
if (username == name) or (password == pin):
    print('login successful')
else:
    print('incorrect username or password')