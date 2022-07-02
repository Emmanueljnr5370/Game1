#def f1():
#    print('Called f1')

#print(f1())
#def f2(f):
#    f()
#f2(f1)

#def f1(func):
#    def wrapper(*args, **kwargs):
#        print('Started')
#        val = func(*args, **kwargs)
#        print('Ended')
#        return val
#    return wrapper        

#@f1
#def f():
#    print('Hello')
#f1(f)()
#x = f1(f)

#f()

#@f1
#def f(a, b = 9):
#    print(a, b)

#f('Hi!') 

#@f1
#def add(x, y):
#    return  x + y

#print(add(7,9))    

#from multiprocessing.spawn import import_main_path


#import time

#def before_after(func):
#    def wrapper(*args):
#        print('Before')
#        func(*args)
#        print('After')

#    return wrapper

#class Test:
#    @before_after
#    def decorated_method(self):
#        print('run') 

#t = Test() 
#t.decorated_method() 

#import time
#def timer(func):
#    def wrapper():
#        before = time.time()
#        func()
#        print('Function took:', time.time() - before, 'seconds')

#    return wrapper

#@timer
#def run():
#    time.sleep(0.5)

#run()


#import datetime

#def log(func):
#    def wrapper(*args, **kwargs):
#        with open('logs.txt',  'a') as f:
#            f.write('Called function with ' + ' '.join([str(arg) for arg in args]) + ' at ' + str(datetime.datetime.now()) + '\n')
#        val = func(*args, **kwargs)
#        return val


#    return wrapper 

#@log
#def run(a, b, c = 9):
#    print(a+b+c) 

#run(1,55, c = 9)
              
#Python Generators begin here   

# Generators are functions that return traversable objects.
# They produces items one at a time and only when required compared to the
# list comprehension that produces all the items at once.
# Generators are run along with for loop.
# Generator functons uses the Yield Keyword.
# It runs when the next() method is called. 
# As far as there's a yield statement in that function, that function turns 
# to a Generator function.

# Check what web scraping means, its used for hacking.
# Also read about Beautiful soup 4 and Request, read ahead for the class.
# Check pipy.org for all these libraries. 
# Used chegg.com for solution manual.

#word = 'abcdefgh'
#for x,y in enumerate(word):
#    print(x,y)





























