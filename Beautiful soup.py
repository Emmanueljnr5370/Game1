#from bs4 import BeautifulSoup
#import requests
#URL = 'https://www.livescore.com/en/tennis/'
#r = requests.get(URL)

#soup = BeautifulSoup(r.content, 'html5lib')

# To get all the  source code from a site use...
#print(soup.prettify())

#tag = soup.handle_data
#print(tag.content[0,5])

# How to get different items in a site...

#from bs4 import BeautifulSoup
#import requests
#URL = 'https://www.livescore.com/en/football/'
#r = requests.get(URL)

#soup = BeautifulSoup(r.content, 'html5lib')
#print(soup.title)
#print(soup.title.name)
#print(soup.title.string)

#from bs4 import BeautifulSoup
#import requests
#URL = 'https://www.livescore.com/en/tennis/'
#r = requests.get(URL)

#soup = BeautifulSoup(r.cookies, 'html5lib')
#print(soup.text)


#from bs4 import BeautifulSoup
#import requests
#URL = 'https://web.facebook.com/?_rdc=1&_/'
#r = requests.get(URL)

#soup = BeautifulSoup(r.content, 'html5lib')
#a = soup.img
#print(a.attrs['src'])
#print(soup.img)

#from bs4 import BeautifulSoup
#import requests
#URL = 'https://www.udemy.com/course/python-beyond-the-basics-object-oriented-programming/'
#r = requests.get(URL)

#soup = BeautifulSoup(r.content, 'html5lib')
#a = soup.img
#print(a.attrs['src'])
#print(soup.img)
#print(soup.video)


#from bs4 import BeautifulSoup
#import requests
#URL = 'https://web.facebook.com/'
#r = requests.get(URL)

#soup = BeautifulSoup(r.content, 'html5lib')
#a = soup.head
#for x in range(len(a.contents)):
#    print(x)

#from bs4 import BeautifulSoup
#import requests
#URL = 'https://www.udemy.com/course/python-beyond-the-basics-object-oriented-programming/'
#r = requests.get(URL)
#soup = BeautifulSoup(r.content, 'html5lib')
#html5lib = r.read()
#r.close()
#soup.h1



#from email.headerregistry import BaseHeader
#import requests
#from bs4 import BeautifulSoup

#URL = 'https://VideoCards
#r = requests.get(URL)

#soup = BeautifulSoup(r.text, 'html.parser')
#print(soup.prettify())

#prices = soup.findAll(text='$')
#parent = prices[0].parent
#strong = parent.find('strong')
#print(strong.string)


Beautiful helps analyze a web page, then twill help you fetch the page.
DOM  means 'Document object model'
html5lib is used to display the output
CRUD Create Read Update and Delete; it  works  only  on objects.
All the pentesting tools are used to find bugs. Examples are metaploit, kali linux, john ripper etc..
Read about offensive pentesting.

from bs4 import BeautifulSoup
import requests
URL = 'https://www.facebook.com/'
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')


from bs4 import BeautifulSoup
import requests
URL = 'https://www.facebook.com/'
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')
last_a_tag = soup.findAll('a', id='link3')
print(last_a_tag)


from bs4 import BeautifulSoup
import requests
URL = 'https://www.facebook.com/'
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
tag = soup.find_all('div','_6a_608n')
print(tag)

# To get images and logos
# Requests is used for downloading and getting object. 

from bs4 import BeautifulSoup
import requests
URL = 'https://www.facebook.com/'
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
tag = soup.find_all(['img', 'button'])
print(tag)

# To grab a particular name of a tag or to find the name of each tag.
# Read on Browser  object model and cross site scripting.
from bs4 import BeautifulSoup
import requests
URL = 'https://www.facebook.com/'
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')

for x in soup.find_all(True):
    print(x.name)


# Dictionary is mutable  that means you can change something in dictionary {}.

from bs4 import BeautifulSoup
import requests
URL = 'https://www.facebook.com/'
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
tag = soup.button
print(tag.attrs)  


from bs4 import BeautifulSoup
import requests
URL = 'https://www.facebook.com/'
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
tag = soup.button
print(tag.attrs['src'])  

# This line of code shows how you can change things in Dictionary{}.
from bs4 import BeautifulSoup
import requests
URL = 'https://www.facebook.com/'
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
tag = soup.button
tag.attrs['src'] = 'https://www.tiktok.com/en/' 
print(tag.attrs) 

# server is used to store information or data or text messages, its just like a CPU
# BeautifulSoup is used to modify or change.
# String Keyword is used to modify or change a text in a button.

from bs4 import BeautifulSoup
import requests
URL = 'https://www.facebook.com/'
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
tag = soup.button
print('old..',tag.string)
tag.string = 'RICE'
print('updated..',tag.string) # This changes is tempeorary


#append is used to remove a old thing and put a new one..

from bs4 import BeautifulSoup
import requests
URL = 'https://www.facebook.com/'
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
tag = soup.button
print('old..',tag.string)
print(tag.append('RICE'))
print('updated..',tag.string)

# Read about UTF 8 its means Unicode Transformation Format, UNIcode, Ascii means American Standard code for information Interchange(How document are prepared and stored)
# Read about python requests.

#  Clear(): The clear keyword used for removing or deleting something forever
from bs4 import BeautifulSoup
import requests
URL = 'https://www.facebook.com/'
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
tag = soup.button
print('old..',tag.clear())

# get_text: also try this get_text keyword at home to get the code the clear keyword deleted.





























