import os

a = os.listdir('C:\\Users\\User\\Music\\ActionMovies')
b = os.listdir('C:\\Users\\User\\Desktop\\SciMovies')

x = set(a)
y = set(b)

z = x.intersection(y)

for x in a:
    if x in z:
        print(os.remove(f'C:\\Users\\User\\Music\\ActionMovies\\{x}'))
else:
    print('task is perfectly completed!')