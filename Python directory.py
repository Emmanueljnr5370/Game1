#import os
#print(os.getcwd())
#for files in os.listdir('C:\\Users\\User\\Downloads\\Mypythondownloads'):
#    print(files) #this will list the items in that particular file


#import os
#print(os.getcwd()) #This helps you get the current working directory. getcwd

#for files in os.listdir('C:\\Users\\User\\Downloads\\YouTube'):
#    print(files)
# This one line of code is for deleting.
#    print('deleting file...')
#    os.remove(f'C:\\Users\\User\\Downloads\\YouTube\\{files}')
#else:
#    print('done!')    

#import os
#print(os.getcwd())

#os.rename('C:\\Users\\User\\Downloads\\YouTube','C:\\Users\\User\\Downloads\\Mypythondownloads')


#file = open('C:\\Users\\User\\OneDrive\\Desktop\\__pycache__\\myfile.txt','r') # r means read It literally means display.
#print(file.read())


#file = open("C:\\Users\\User\\OneDrive\\Pictures\\Screenshots\\Screenshot (5).png",'rb')  # rb Readbyte is for images,videos and musics while r (read) is for texts only. 
#print(file.read())
#file.close()

# Writable means if a file support an action
#with open("C:\\Users\\User\\OneDrive\\Desktop\\__pycache__\\myfile.txt",'w') as file:   # write(w) means remove the old text and add a new  text. 
#    file.write('adding new text to my file....')
#    print('done!')

#with open('C:\\Users\\User\\OneDrive\\Desktop\\__pycache__\\myfile.txt','a') as file:  #(a) means append
#    file.write('\n adding a new text to my file...')
#    file.write('\n adding a new text to my file2...')

#with open('C:\\Users\\User\\OneDrive\\Desktop\\__pycache__\\myfile.txt','r') as file: # It will count the first 20 senctence both spaces and alphabet.
#    print(file.read(20))

#with open('C:\\Users\\User\\OneDrive\\Desktop\\__pycache__\\myfile.txt','r') as file:
#    print(file.seek(10)) #seek forwards a text and it will remove ten alphabet.
#    print(file.read())



# More on requests...

#from bs4 import BeautifulSoup
#import requests

#URL = 'https://web.facebook.com/?_rdc=1&_rdr'
# Attributes of requests are... Post, get, put, headers. 
# Post is used for authentication.
# GET request is used to obtain the requested data from a specific server.
# Status codes are issued by a server in response to a clients requests made to a server. 
#response = requests.get(URL)
#print(response.status_code)
#print(response.headers)

# Headers are used  to view response and also view the server and the Admin URL.

# Response content is also used to get source.


#from bs4 import BeautifulSoup
#import requests
#URL = "https://cdn.pixabay.com/photo/2022/04/04/18/40/sunset-7112135_960_720.jpg"
#response = requests.get(URL)
#soup = BeautifulSoup(response.content, 'html5lib')
#a = soup.find_all('img')
#with open(r'C:\\Users\\User\\Downloads\\Mypythondownloads\\myimage.jpg','wb') as file: # w mode means write its used to get object into your device but youve to add b(byte) to it since what you want to get is an image or video or music.
#    file.write(response.content) # r mode  means read its used to display object
#    print('Download complete!')



#from bs4 import BeautifulSoup
#import requests
#URL = "https://static.xx.fbcdn.net/rsrc.php/y8/r/dF5SId3UHWd.svg" # If the image link is svg youve to change the path too to svg
#response = requests.get(URL)
#soup = BeautifulSoup(response.content, 'html5lib')  
#a = soup.find_all('img')
#with open(r'C:\\Users\\User\\Downloads\\Mypythondownloads\\myimage.svg','wb') as file:
#    file.write(response.content) 
#    print('Download complete!')


#from bs4 import BeautifulSoup
#import requests
#URL = 'https://edu.anarcho-copy.org/Programming%20Languages/Python/Web%20Scraping%20with%20Python,%202nd%20Edition.pdf'
#response = requests.get(URL,stream = True)

#with open(r'C:/Users/User/OneDrive/Desktop/YouTube/web3.pdf','wb') as file:
#    for char in response.iter_content(chunk_size=1024):
#        file.write(char)     #iter or iteration allows the computer download the file one at a them one at a time
#      
#    else:
#        print('Download Completed!')    
              


#import requests
#URL = 'https://archive.org/download/CC_1914_08_31_TheGoodforNothing/CC_1914_08_31_TheGoodforNothing_512kb.mp4'
#response = requests.get(URL, stream = True) # stream is used for both pdf's and mp4 files 

#with open(r'C:\\Users\\User\\OneDrive\\Desktop\\YouTube\\video1.mp4','wb') as  file:
#    for chunk in response.iter_content(chunk_size=56*1024):
#        if chunk:
#           file.write(chunk)

#    else:
#        print('Download Successful!')    



#import random

#random.choice(['a','b',1,2,'c'])
# random.choice is different from random.randint in that it contains both 
# a tuple and a list with both alphanumerics. 
# You can as well use random.randint() # this contains only a tuple and it contains
# two range of values like (0,200) 
# You can as well use two tuples.

#  HASHING BEGINS HERE

#import hashlib

#print(hashlib.algorithms_available)
#print(hashlib.algorithms_guaranteed)

#import hashlib
#word = b'fc barcelona' # b here means bite is used for getting.
#s1 = hashlib.sha1(word)
#print(s1.digest())

# Check out this site, Hacktoday.com (Search about dictionary attack here.)
# Set is a Dictionary with only keys e.g {''} or its an unordered unique variables


#import hashlib
#word = b'fc barcelona'
#s1 = hashlib.sha224(word)
#print(s1.digest())

#import hashlib
#word = b'fc barcelona'
#s1 = hashlib.sha224(word)
#s2 = hashlib.sha224(word)

#print(s1.digest())
#print(s2.digest())

#print(s1.digest() == s2.digest())


#import hashlib
#word = b'fc barcelona'
#salt = 'rat%%poison$%'
#s1 = hashlib.sha384(word + salt.encode())
#s2 = hashlib.sha384(word + salt.encode())

#print('added salt..',s1.digest(),'\n')

#print(s2.digest())

#print(s1.digest() == s2.digest())


# Weakness of sha3
# If you dont add salt to your code it will have  no collision resistant. 

# Another way of encrypting is called blake2b

#import hashlib
#word = b'fc barcelona'
#salt = '%%p$%'
#s1 = hashlib.md5(word + salt.encode())
#s2 = hashlib.md5(word)

#print('added salt..',s1.digest(),'\n')

#print(s2.digest())

#print(s1.digest() == s2.digest())

#import hashlib
#word = b'fc barcelona'
#salt = '%%p$%'
#s1 = hashlib.blake2b(word + salt.encode())
#s2 = hashlib.blake2b(word)

#print(s1.digest(),'\n')

#print(s2.digest())

#print(s1.digest() == s2.digest())



#import hashlib
#word = b'fc barcelona'

#s1 = hashlib.pbkdf2_hmac(hash_name='md5',password=word,salt=b'rat%%poison$%',iterations=30)
#s2 = hashlib.pbkdf2_hmac(hash_name='md5',password=word,salt=b'rat%%poison$%',iterations=30)

#print(s1.hex(),'\n')

#print(s2.hex())

#print(s1.hex() == s2.hex())

# When your iterations are the same you'll have TRUE but when your iterations are different you'll have FALSE.

# Password cracking begins here.
# check this site  >> smallpdf.com where you can put pdf  password.

num = []

for x in range(0,10000):
    num.append('{0:04d}'.format(x))
print(num)

with open('C:/Users/User/OneDrive/Desktop/code.txt') as file:
    for pin in num:
        file.write(f'{pin}\n')























































