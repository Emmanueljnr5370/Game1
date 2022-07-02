#num = []

#for x in range(0,10000):
#    num.append('{0:04d}'.format(x))
#print(num)    
#with open('C:/Users/User/OneDrive/Desktop/__pycache__/code.txt', 'w') as file:
#    for pin in num:
#        file.write(f'{pin}\n')


import pikepdf

passwords_filename = 'C:/Users/User/OneDrive/Desktop/__pycache__/code.txt'

locked_pdf_file = "C:/Users/User/Downloads/CSS course-protected (1).pdf"

# load passwords file
with open(passwords_filename) as file:

    passwords_list = file.readlines()
    total_passwords = len(passwords_list)

    for index,password in enumerate(passwords_list):
        #try if password  is correct
        try:
            with pikepdf.open(locked_pdf_file, password = password.strip()) as pdf_file:
                print('\n+++++++++success+++++++++')
                print('success--------File is Unblocked and the password is: ', password)
                break
        #if password fail
        except:
            print('\n===========')
            print(f'Trying Password {password} --- Fail!!!')
            scanning = (index/total_passwords)*100
            print('Scanning passwords complete:', round(scanning,2))
            continue    
 


#word = 'abcdefgh'
#print(list(enumerate(word)))
# (x,y) means coordinate i.e tuples unpacking. 

#word = 'abcdefgh'
#for x,y in enumerate(word):
#    print(x,y)































        