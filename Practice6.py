num = []

for x in range(0,10000):
    num.append('{0:04d}'.format(x))
print(num)

with open('C:/Users/User/OneDrive/Desktop/__pycache__/text3.txt','w') as file:
    for pin in num:
        file.write(f'{pin}\n')



import pikepdf

passwords_filename = 'C:/Users/User/OneDrive/Desktop/__pycache__/text3.txt'

locked_pdf_file = "C:/Users/User/Downloads/CSS course-protected (1).pdf"

with open(passwords_filename) as file:
    passwords_list = file.readlines()
    total_passwords =len(passwords_list)

    for index,password in enumerate(passwords_list):
        try:
            with pikepdf.open(locked_pdf_file, password = password.strip()) as pdf_file:
                print('\n+++++++++++++success+++++++++++++')
                print('Success------ File is unlocked and the password is: ', password)
                break

        except:
            print('\n========')
            print(f'Trying Password {password} ---- Fail!!!') 
            scanning = (index/total_passwords)*100
            print('scanning passwords complete:', round(scanning,2))
            continue   
