#from bs4 import BeautifulSoup 
#import requests
#URL =  'https://web.facebook.com/?_rdc=1&_rdr/'
#r = requests.get(URL)
#soup = BeautifulSoup(r.content, 'html5lib')
#tag = soup.button
#tag.attrs['faxx'] = 'https://www.tiktok.com/'
#print(tag.attrs)


#from bs4 import BeautifulSoup 
#import requests
#URL =  'https://web.facebook.com/?_rdc=1&_rdr/'
#r = requests.get(URL)
#soup = BeautifulSoup(r.content, 'html5lib')
#tag = soup.button
#print('old..',tag.clear())


#from bs4 import BeautifulSoup 
#import requests
#URL =  'https://web.facebook.com/?_rdc=1&_rdr/'
#r = requests.get(URL)
#soup = BeautifulSoup(r.content, 'html5lib')
#tag = soup.button
#print('old..',tag.get_text())

#from bs4 import BeautifulSoup 
#import requests
#URL =  'https://web.facebook.com/?_rdc=1&_rdr/'
#r = requests.get(URL)
#soup = BeautifulSoup(r.content, 'html5lib')
#tag = soup.button
#print(tag.string)

#from bs4 import BeautifulSoup 
#import requests
#URL =  'https://web.facebook.com/?_rdc=1&_rdr/'
#r = requests.get(URL)
#soup = BeautifulSoup(r.content, 'html5lib')
#tag = soup.button
#print(soup.original_encoding)


#from bs4 import BeautifulSoup
#import requests
#URL = 'https://www.newegg.com/seagate-expansion-18tb-black/p/N82E16822184976?Item=N82E16822184976&cm_sp=Homepage_SS-_-P2_22-184-976-_-05232022&quicklink=true'
#r = requests.get(URL)
#soup = BeautifulSoup(r.content, 'html5lib')
#prices = soup.find_all(text='$')
#parent = prices[0].parent
#strong = parent.find('strong')
#print(strong.string)
#img = soup.find_all('img')
#print(img)
#print(product_name)


#print(dict(('py', 'th', 'on')))


#import os  
#print(os.getcwd())
#for files in os.listdir("C:\\Users\\User\\OneDrive\\Pictures\\Screenshots"):
#    print(files)
#else:
#    print("Done listing!")  

#import os
#print(os.getcwd())

#files = os.listdir
#files1 = os.remove
#if files == os.listdir('C:\\Users\\User\\Downloads\\Mypythondownloads'):
#    print(os.listdir)
#elif files1 == os.remove("C:\\Users\\User\\Downloads\\Mypythondownloads\\FASTEST_Way_to_Learn_Coding_and_ACTUALLY_Get_a_Job(720p).mp4"
#"C:\\Users\\User\\Downloads\\Mypythondownloads\\How to register for the LMS.mp4"
#"C:\\Users\\User\\Downloads\\Mypythondownloads\\Iyanya feat Ayra Starr - Call (Music Video).mp4"):
#    print(os.remove)

#else:
#    print('Done!')


#import os
#print(os.getcwd())
#for files in os.listdir('C:\\Users\\User\\Downloads\\Mypythondownloads'):
##    print(files)
#    print('deleting file...!')
#    os.remove(f'C:\\Users\\User\\Downloads\\Mypythondownloads\\{files}')
#else:
#    print('Done!')    

#import os
#print(os.getcwd())
#print(os.listdir('C:\\Users\\User\\Downloads\\Mypythondownloads'))

#os.rename("C:\\Users\\User\\Downloads\\Mypythondownloads1","C:\\Users\\User\\Downloads\\Mypythondownloads")
#print('Done!')

#print(os.remove('C:\\Users\\User\\Downloads\\Mypythondownloads'))
#os.remove("C:\\Users\\User\\Downloads\\Mypythondownloads")
#print("Done!")
   


#file1 = open('C:\\Users\\User\\OneDrive\\Desktop\\__pycache__\\myfile1.txt','r')
#print(file1.read())



#import os
#print(os.getcwd)

#file1 = open("C:\\Users\\User\\Music\\Break_Thou_the_Bread_of_Life(128k).m4a",'rb')
#print(file1.read())
#file1.close()

#with open('C:\\Users\\User\\OneDrive\\Desktop\\__pycache__\\myfile1.txt','w') as file1:
#    file1.write('Adding a new text to my file1')
#    file1.write('\nAdding a new text to my file2')
#    print('Done!')

#with open('C:\\Users\\User\\OneDrive\\Desktop\\__pycache__\\myfile1.txt','a') as file1:
#    file1.write('\nAdding a new text to my file1')
#    file1.write('\nAdding a new text to my file2')
#    print('Done!')


#with open('C:\\Users\\User\\OneDrive\\Desktop\\__pycache__\\myfile1.txt','r') as file1:
#    print(file1.read(20))



#with open('C:\\Users\\User\\OneDrive\\Desktop\\__pycache__\\myfile1.txt','r') as file1:
#    print(file1.seek(10))
#    print(file1.read())


#from fpdf import FPDF

#pdf = FPDF()

#pdf.add_page('C:\\Users\\User\\Downloads\\Mypythondownloads')

#pdf.set_font('Arial', size = 15)

#f = open('myfile1.txt', 'r')

#for x in f:
#    pdf.cell(200, 10, txt  = x, ln = 1, align = 'c')

#pdf.output('mywork.pdf')

#import os
#print(os.getcwd())

#os.rename('C:/Users/User/OneDrive/Desktop/YouTube','C:/Users/User/OneDrive/Desktop/MyYouTube')
#print('Done!')

#for files in os.listdir('C:/Users/User/OneDrive/Desktop/MyYouTube/hdjjjjii'):
#     print(files)
#     print('Deleting file!')
#os.rename('C:/Users/User/OneDrive/Desktop/MyYouTube','C:/Users/User/OneDrive/Desktop/YouTube')
#print('Done')

#from bs4 import BeautifulSoup
#import requests
#URL = 'https://www.thenetnaija.com/videos/series/14011-love-death-and-robots/season-1/episode-1/download-sub'
#response = requests.get(URL, stream = True)
#with open(r'C:\\Users\\User\\OneDrive\\Desktop\\YouTube\\download-sub','wb') as file:
#    for char in response.iter_content(chunk_size=1024):
#        file.write(char)
#    else:
#3        print('Dowmload Completed!') 


#import requests
#URL = ''
#response = requests.get(URL, stream = True)
#with open(r'C:\\Users\\User\\OneDrive\\Desktop\\YouTube\\Video3.mp4','wb') as file:
#    for char in response.iter_content(char_size=56*1024):
#        if char:
#            file.write(char)
#    else:
#        print('Download COmpleted!')       


#import hashlib

#print(hashlib.algorithms_available)
#print(hashlib.algorithms_guaranteed)

#import hashlib

#word = b'Man United'
#s1 = hashlib.sha1(word)
#print(s1.digest())

#import hashlib
#word = b'Man United'
#s1 = hashlib.sha224(word)
#print(s1.digest())



#import hashlib
#word = b'Man United'
#s1 = hashlib.sha224(word)
#s2 = hashlib.sha224(word)
#print(s1.digest())
#print(s2.digest())
#print(s1.digest() == s2.digest())



#import hashlib
#word = b'Man United'
#salt = 'rat%%poison$%'
#s1 = hashlib.sha384(word + salt.encode())
#s2 = hashlib.sha384(word + salt.encode())

#print('adding salt..', s1.digest(),'\n')
#print(s2.digest())

#print(s1.digest() == s2.digest())


#import hashlib
#word = b'Man United'
#salt = '%%p$%'
#s1 = hashlib.md5(word + salt.encode())
#s2 = hashlib.md5(word)

#print('adding salt..', s1.digest(),'\n')
#print(s2.digest())

#print(s1.digest() == s2.digest())



#import hashlib
#word = b'Man United'
#salt = '%%p$%'
#s1 = hashlib.blake2b(word + salt.encode())
#s2 = hashlib.blake2b(word + salt.encode())

#print(s1.digest(),'\n')
#print(s2.digest())

#print(s1.digest() == s2.digest())


#import hashlib
##word = b'Man United'
#salt = '%%p$%'
#s1 = hashlib.blake2b(word + salt.encode())
#s2 = hashlib.blake2b(word)

#print(s1.digest(),'\n')
#print(s2.digest())

#print(s1.digest() == s2.digest())


import hashlib
word = b'Man United'
s1 = hashlib.pbkdf2_hmac(hash_name='md5',password=word,salt=b'rat%%poison$%',iterations=660)
s2 = hashlib.pbkdf2_hmac(hash_name='md5',password=word,salt=b'rat%%poison$%',iterations=660)

print(s1.hex(),'\n')
y
print(s2.hex())

print(s1.hex() == s2.hex())

























