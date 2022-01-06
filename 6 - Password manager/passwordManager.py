from cryptography.fernet import Fernet

#Code used to create key file, not needed after first use
'''def writeKey():
    key = Fernet.generate_key()
    with open('key.key','wb') as keyFile:
        keyFile.write(key)'''

masterPass = input('Enter master password: ')
if masterPass != 'MasterPassword123':
    print('Incorrect password')
    quit()


def loadKey():
    file = open('key.key','rb')
    key = file.read()
    file.close()
    return key

key = loadKey()
fer = Fernet(key)

def add():
    name = input('Account name: ')
    pwd = input('Password: ')
    ePwd = fer.encrypt(pwd.encode()).decode()

    with open ('passwords.txt','a') as x:
        x.write(f'{name}|{ePwd}\n')
def view():
        with open ('passwords.txt','r') as x:
            for line in x.readlines():
                data = line.rstrip()
                user, passw = data.split('|')
                print('User:',user,'| Password:',fer.decrypt(passw.encode()).decode())

while True:
    mode = input('Would you like to view existing passwords, or add a new one (view/add)? (press q to quit) ')
    if mode == 'q':
        break
    elif mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Invalid mode selected')
        continue