#                                           PYTHON PASSWORD VAULT
# ========================================================================================================
# The Python Password Vault is an AES-256 Encrypted Database in which you can store your passwords 
# The Vault uses 3 seperate salts that are connected together in impossible ways to create a database key
#
# This script is provided under the MIT License by Leonard Haddad
#
# ========================================================================================================
#
from getpass import getpass
from os import system, name
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import hashlib
import time
import base64
import sqlite3
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
import pyperclip
BLOCK_SIZE = 32
BYTE_LEN = 16


plain_text_salt = b''
encrypted_first_step_salt = b''
encrypted_second_step_salt = b''
iv = ''
encrypted_password_hash = ''
password = ''
password_hash = ''
second_step_salt = ''
first_step_salt = ''
database_encryption_key = ''
database_cursor = ''
database_connection=''


# ===== Clear the screen =====
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


# ===== Hash data =====
def hash_data(data,salt):
    return hashlib.sha256(salt + data.encode() + salt + data.encode()).hexdigest()


# ===== Decrypt data =====
def decrypt_data(key,data,iv):
    global BLOCK_SIZE
    aes = AES.new(key,AES.MODE_CBC,iv)
    return unpad(aes.decrypt(data),BLOCK_SIZE)

    
# ===== Encrypt data =====
def encrypt_data(key,data,iv):
    global BLOCK_SIZE
    aes = AES.new(key,AES.MODE_CBC,iv)
    return aes.encrypt(pad(data,BLOCK_SIZE))


# ===== Decrypt everything =====
def decrypt_everything():
    global first_step_salt,second_step_salt,plain_text_salt,encrypted_first_step_salt,encrypted_second_step_salt,iv, encrypted_password_hash,password,password_hash
    # Decode from base64
    plain_text_salt = base64.b64decode(plain_text_salt)
    encrypted_first_step_salt = base64.b64decode(encrypted_first_step_salt)
    encrypted_second_step_salt = base64.b64decode(encrypted_second_step_salt)
    iv = base64.b64decode(iv)
    encrypted_password_hash = base64.b64decode(encrypted_password_hash)
    # Decrypt first step salt using password
    first_step_salt = decrypt_data(bytes(password[0:BYTE_LEN],'utf-8'),encrypted_first_step_salt,iv)
    # Encrypt password using plain text salt
    encrypted_password = encrypt_data(plain_text_salt,bytes(password,'utf-8'),iv)
    # Decrypt second salt using password and first step salt
    second_step_salt_key = str(encrypted_password[0:8]) + str(first_step_salt[0:8])
    second_step_salt = decrypt_data(bytes(second_step_salt_key[0:BYTE_LEN],'utf-8'),encrypted_second_step_salt,iv)
    # Decrypt password hash using second salt
    password_hash = decrypt_data(second_step_salt,encrypted_password_hash,iv)
    

# ===== Help =====
def help():
    print('\n==================== Password Vault ====================')
    print("\nPython password vault functions:")
    print()
    print('--list [username]                 - list all passwords (encrypted)')
    print('--display username ID             - display password for a specific username')
    print('--copy username ID                - Copy a password to clipboard')
    print('--add username password           - add a new password to the database')
    print('--edit usr pass newusr newpass ID - edit an existing password ')
    print('--remove username ID              - remove a password from the database')
    print('--changepass                      - change login password')
    print('clear or cls                      - clear the screen')
    print('--exit                            - exit\n')
    print('========================================================\n')
    

# ===== Change Password =====
def change_password():
    global plain_text_salt,encrypted_first_step_salt,encrypted_second_step_salt,iv,encrypted_password_hash,password,password_hash,second_step_salt,first_step_salt
    global database_encryption_key,database_cursor,database_connection
    query = """SELECT * FROM passwords;"""
    database_cursor.execute(query)
    encrypted_data = database_cursor.fetchall()
    data = []
    for a in encrypted_data:
        new_iv_encoded = a[3]
        new_iv = base64.b64decode(new_iv_encoded)
        data.append((decrypt_data(database_encryption_key[0:BYTE_LEN],base64.b64decode(a[1]),new_iv),decrypt_data(database_encryption_key[0:BYTE_LEN],base64.b64decode(a[2]),new_iv)))
    query = """DROP TABLE passwords;"""
    database_cursor.execute(query)
    database_connection.commit()
    plain_text_salt = b''
    encrypted_first_step_salt = b''
    encrypted_second_step_salt = b''
    iv = ''
    encrypted_password_hash = ''
    password = ''
    password_hash = ''
    second_step_salt = ''
    first_step_salt = ''
    database_encryption_key = ''
    # Generate new salts
    sign_up()
    # Reenter password
    print('\nPlease enter the password again!\n')
    password = getpass("#> ")
    # Load data
    f = open('credentials','rb')
    data1 = f.readlines(1)
    data2 = f.readlines(1)
    data3 = f.readlines(1)
    data4 = f.readlines(1)
    data5 = f.readlines(1)
    f.close()
    encrypted_password_hash = data1[0][:-1]
    plain_text_salt = data2[0][:-1]
    encrypted_first_step_salt = data3[0][:-1]
    encrypted_second_step_salt = data4[0][:-1]
    iv = data5[0]
    # Decrypt data
    decrypt_everything()
    print('decrypted data')
    database_encryption_key = bytes(hash_data(password_hash.decode(),plain_text_salt),'utf-8')
    query = """CREATE TABLE IF NOT EXISTS passwords (id integer PRIMARY KEY AUTOINCREMENT,username BLOB,password BLOB,iv BLOB,searchIndex BLOB);"""
    database_cursor.execute(query)
    for a in data:
        print('trying to persist data')
        new_iv = get_random_bytes(BYTE_LEN)
        searchIndex = base64.b64encode(bytes(hash_data(a[0].decode(),iv),'utf-8'))
        encrypted_username = base64.b64encode(encrypt_data(database_encryption_key[0:BYTE_LEN],a[0],new_iv))
        encrypted_password = base64.b64encode(encrypt_data(database_encryption_key[0:BYTE_LEN],a[1],new_iv))
        new_iv_encoded = base64.b64encode(new_iv)
        database_cursor.execute("""INSERT INTO passwords VALUES (NULL,?,?,?,?);""",(encrypted_username,encrypted_password,new_iv_encoded,searchIndex,))
    database_connection.commit()
    print('\nPassword changed successfully!\n')
    print('You will need to relog! Loggin out in 3 seconds!')
    time.sleep(3)
    setup()
        

# ===== Edit Password =====
def edit_password(username, password, newusername, newpassword, ID):
    global database_cursor, database_encryption_key, iv, database_connection
    searchIndex = base64.b64encode(bytes(hash_data(username,iv),'utf-8'))
    database_cursor.execute("""SELECT * FROM passwords WHERE id = ? AND searchIndex = ?;""",(int(ID),searchIndex))
    data = database_cursor.fetchall()
    new_iv = b''
    for a in data:
        new_iv_encoded = a[3]
        new_iv = base64.b64decode(new_iv_encoded)
        encrypted_username = base64.b64encode(encrypt_data(database_encryption_key[0:BYTE_LEN],bytes(username,'utf-8'),new_iv))
        encrypted_password = base64.b64encode(encrypt_data(database_encryption_key[0:BYTE_LEN],bytes(password,'utf-8'),new_iv))
        if not (encrypted_username == a[1] and encrypted_password == a[2]):
            data.remove(a)
    if len(data) == 0:
        print('Username or password incorrect!')
    else:
        database_cursor.execute("""DELETE FROM passwords WHERE username = ? AND id = ? AND password = ?;""",(encrypted_username,int(ID),encrypted_password))
        encrypted_username = base64.b64encode(encrypt_data(database_encryption_key[0:BYTE_LEN],bytes(newusername,'utf-8'),new_iv))
        encrypted_password = base64.b64encode(encrypt_data(database_encryption_key[0:BYTE_LEN],bytes(newpassword,'utf-8'),new_iv))
        database_cursor.execute("""INSERT INTO passwords VALUES (NULL,?,?,?,?);""",(encrypted_username,encrypted_password,new_iv_encoded,searchIndex))
        database_connection.commit()
        print('\n===== Updated Successfully! =====\n')


# ===== Copy Password =====
def copy_password(username,ID):
    global database_cursor, database_encryption_key, iv, database_connection
    encrypted_data = []
    searchIndex = base64.b64encode(bytes(hash_data(username,iv),'utf-8'))
    database_cursor.execute("""SELECT * FROM passwords WHERE searchIndex = ? AND id = ?;""",(searchIndex,int(ID)))
    encrypted_data = database_cursor.fetchall()
    data = []
    for a in encrypted_data:
        new_iv_encoded = a[3]
        new_iv = base64.b64decode(new_iv_encoded)
        data.append((str(decrypt_data(database_encryption_key[0:BYTE_LEN],base64.b64decode(a[1]),new_iv))[2:-1],str(decrypt_data(database_encryption_key[0:BYTE_LEN],base64.b64decode(a[2]),new_iv))[2:-1]))
    for a in data:
        pyperclip.copy(a[1])
        print('\n===== Password copied to clipboard! =====\n')


# ===== Display a Password =====
def display_password(username,ID):
    global database_cursor, database_encryption_key, iv, database_connection
    encrypted_data = []
    searchIndex = base64.b64encode(bytes(hash_data(username,iv),'utf-8'))
    database_cursor.execute("""SELECT * FROM passwords WHERE searchIndex = ? AND id = ?;""",(searchIndex,int(ID)))
    encrypted_data = database_cursor.fetchall()
    data = []
    for a in encrypted_data:
        new_iv_encoded = a[3]
        new_iv = base64.b64decode(new_iv_encoded)
        data.append((str(decrypt_data(database_encryption_key[0:BYTE_LEN],base64.b64decode(a[1]),new_iv))[2:-1],str(decrypt_data(database_encryption_key[0:BYTE_LEN],base64.b64decode(a[2]),new_iv))[2:-1]))
    for a in data:
        print('\n===== Password =====\n\nUsername: %s | Password: %s\n\n====================\n' % (a[0],a[1]))
        

# ===== Remove Password =====
def remove_password(username,ID):
    global database_cursor, database_encryption_key, iv, database_connection
    print('\n===== Are you sure? =====\n')
    user_input = input("Yes? #> ")
    if 'y' in user_input.lower():
        searchIndex = base64.b64encode(bytes(hash_data(username,iv),'utf-8'))
        database_cursor.execute("""DELETE FROM passwords WHERE searchIndex = ? AND id = ?;""",(searchIndex,int(ID)))
        database_connection.commit()
    print('\n===== Deleted! =====\n')


# ===== Store Password =====
def add_password(username,password):
    global database_cursor, database_encryption_key, iv, database_connection
    new_iv = get_random_bytes(BYTE_LEN)
    encrypted_username = base64.b64encode(encrypt_data(database_encryption_key[0:BYTE_LEN],bytes(username,'utf-8'),new_iv))
    encrypted_password = base64.b64encode(encrypt_data(database_encryption_key[0:BYTE_LEN],bytes(password,'utf-8'),new_iv))
    searchIndex = base64.b64encode(bytes(hash_data(username,iv),'utf-8'))
    new_iv_encoded = base64.b64encode(new_iv)
    database_cursor.execute("""INSERT INTO passwords VALUES (NULL,?,?,?,?);""",(encrypted_username,encrypted_password,new_iv_encoded,searchIndex,))  
    database_connection.commit()
    print('\n===== Password added successfully! =====\n')


# ===== List passwords =====
def list(name):
    global database_cursor,database_encryption_key, iv
    encrypted_data = []
    if len(name)>0:
        searchIndex = base64.b64encode(bytes(hash_data(username,iv),'utf-8'))
        database_cursor.execute("""SELECT * FROM passwords WHERE searchIndex = ?;""",(searchIndex,))
        encrypted_data = database_cursor.fetchall()
    else:
        query = """SELECT * FROM passwords;"""
        database_cursor.execute(query)
        encrypted_data = database_cursor.fetchall()
    data = []
    for a in encrypted_data:
        new_iv_encoded = a[3]
        new_iv = base64.b64decode(new_iv_encoded)
        data.append((a[0],str(decrypt_data(database_encryption_key[0:BYTE_LEN],base64.b64decode(a[1]),new_iv))[2:-1]))
    print('\n========== Stored Passwords ==========\n')
    for a in data:
        print('Username: %s | Password: Hidden | ID: %s' % (a[1],str(a[0])))
    print('\n======================================\n')

    
# ===== Access to database =====
def running():
    global password_hash,first_step_salt,second_step_salt,database_cursor,database_connection
    clear()
    # Connect to sqlite database
    conn = None
    try:
        conn = sqlite3.connect("passwords.db")
    except Exception as e:
        print(e)
    database_cursor = conn.cursor()
    database_connection = conn
    query = """CREATE TABLE IF NOT EXISTS passwords (id integer PRIMARY KEY AUTOINCREMENT,username BLOB,password BLOB);"""
    database_cursor.execute(query)
    print('==================== Password Vault ====================')
    print('\nTo display all functionalities, type --help')
    print('\n========================================================\n')
    while True:
        user_input = input("#> ")
        if "--h" in user_input.lower():
            help()
        elif "--l" in user_input:
            try:
                command, rest = user_input.split(" ")
                list(rest)
            except Exception as g:
                list('')
        elif "--add" in user_input:
            try:
                items = user_input.split(' ')
                command = items[0]
                usr = items[1]
                passwd = items[2]
                add_password(usr,passwd)
            except Exception as e:
                print("Not enough arguments given!")
        elif '--d' in user_input.lower():
            try:
                command, name, ID = user_input.split(" ")
                display_password(name,ID)
            except Exception as e:
                print('Incorrect usage! Usage --display username ID')
        elif '--r' in user_input.lower():
            try:
                command, name, ID = user_input.split(" ")
                remove_password(name,ID)
            except Exception as g:   
                print('Incorrent usage! Usage: --remove username ID')
        elif '--copy' in user_input.lower():
            try:
                command, name, ID = user_input.split(" ")
                copy_password(name,ID)
            except Exception as g:   
                print('Incorrent usage! Usage: --copy username ID')
        elif '--edit' in user_input.lower():
            try:
                command, name, passwd, newname, newpasswd, ID = user_input.split(" ")
                edit_password(name,passwd,newname,newpasswd,ID)
            except Exception as g:
                print(g)
                print('Incorrent usage! Usage: --edit username password newUsername newPassword ID')
        elif '--changepass' in user_input.lower():
            change_password()
        elif 'cls' in user_input.lower() or 'clear' in user_input.lower():
            clear()
            print('==================== Password Vault ====================')
            print('\nTo display all functionalities, type --help')
            print('\n========================================================\n')
        elif '--exit' in user_input.lower():
            clear()
            exit()


# ===== Login =====
def login():
    global second_step_salt,password_hash,password,database_encryption_key
    try:
        print('\n==================== Password Vault ====================\n')
        print('Enter password!\n')
        print('========================================================\n')
        password = getpass('#> ')
        decrypt_everything()
        # Hash password using password and second salt
        password_hash2 = hash_data(password,second_step_salt)
        password_hash2 = bytes(password_hash2,'utf-8')
        if password_hash2 != password_hash:
            print('Incorrect password! Try again!')
            time.sleep(3)
            clear()
            login()
        # Database encryption key
        database_encryption_key = bytes(hash_data(password_hash.decode(),plain_text_salt),'utf-8')
        running()
    except Exception as e:
        #clear()
        print(e)
        print('\nIncorrect credentials! Terminating!\n')
        time.sleep(3)
        exit()
    

# ===== Sign-up =====
def sign_up():
    global plain_text_salt,encrypted_first_step_salt,encrypted_second_step_salt,iv, encrypted_password_hash
    plain_text_salt = get_random_bytes(BYTE_LEN)
    first_step_salt = get_random_bytes(BYTE_LEN)
    second_step_salt = get_random_bytes(BYTE_LEN)
    iv = get_random_bytes(BYTE_LEN)
    print('Select a password!')
    password = getpass('Password: ')
    password2 = getpass('Again: ')
    if password != password2:
        print('Passwords dont match! Try again!')
        time.sleep(3)
        clear()
        sign_up()
    if len(password) < BYTE_LEN:
        print('Password must be at least 16 characters long!')
        time.sleep(3)
        clear()
        sign_up()
    # Encrypt first salt using password
    encrypted_first_step_salt = encrypt_data(bytes(password[0:BYTE_LEN],'utf-8'),first_step_salt,iv)
    # Encrypt password  using plain text salt
    encrypted_password = encrypt_data(plain_text_salt,bytes(password,'utf-8'),iv)
    # Encrypt second salt using encrypted password + first salt
    second_step_salt_key = str(encrypted_password[0:8]) + str(first_step_salt[0:8])
    encrypted_second_step_salt = encrypt_data(bytes(second_step_salt_key[0:BYTE_LEN],'utf-8'),second_step_salt,iv)
    # Hash password using password with second salt as salt
    password_hash = hash_data(password,second_step_salt)
    # Encrypt the password hash
    encrypted_password_hash = encrypt_data(second_step_salt,bytes(password_hash,'utf-8'),iv)
    # Write them all to file
    f = open('credentials','wb+')
    f.write(base64.b64encode(encrypted_password_hash)+b'\n')
    f.write(base64.b64encode(plain_text_salt)+b'\n')
    f.write(base64.b64encode(encrypted_first_step_salt)+b'\n')
    f.write(base64.b64encode(encrypted_second_step_salt)+b'\n')
    f.write(base64.b64encode(iv))
    f.close()
        
        
# ===== Setup =====
def setup():
    global plain_text_salt,encrypted_first_step_salt,encrypted_second_step_salt,iv, encrypted_password_hash
    registered_user = False
    # Try to read credentials and salts from plaintext files
    try:
        f = open('credentials','rb')
        data1 = f.readlines(1)
        data2 = f.readlines(1)
        data3 = f.readlines(1)
        data4 = f.readlines(1)
        data5 = f.readlines(1)
        f.close()
        encrypted_password_hash = data1[0][:-1]
        plain_text_salt = data2[0][:-1]
        encrypted_first_step_salt = data3[0][:-1]
        encrypted_second_step_salt = data4[0][:-1]
        iv = data5[0]
        registered_user = True
    except Exception as e:
        registered_user = False
    # Registered user sign-in
    if registered_user:
        login()
    # Sign up
    else:
        sign_up()
        setup()
        
setup()