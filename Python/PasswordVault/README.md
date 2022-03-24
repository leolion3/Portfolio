# Python Password Vault

This small script contains a standalone password vault, secured with Multi-Layer AES-256 Encryption.

The passwords are stored within an unencrypted SQLite Database, the data inside the database is however fully encrypted.

## Requirements

The following libraries are required to run the software:

```
pycryptodome
pyperclip
getpass
hashlib
```

## Functionality

The Password Vault - like any good password manager - can store as many passwords as you wish. These can be modified at any point
with the appropriate commands.

* Note: the ID parameter is the Primary Key used in the SQLite database, it can be shown using the --list command *

The following commands are supported by the Password Vault:

```python
--list [username]                 - list all stored password usernames (passwords are hidden)
--display username ID             - display password for a specific username
--copy username ID                - Copy a password to clipboard
--add username password           - add a new password to the database
--edit usr pass newusr newpass ID - edit an existing password
--remove username ID              - remove a password from the database
--changepass                      - change login password
clear or cls                      - clear the screen
--exit                            - exit
```

**NOTE: LOSING THE MASTER PASSWORD MEANS LOSING ACCESS TO THE DATABASE! DO. NOT. LOSE. THE. MASTER. PASSWORD.**

## Technical Functionality

Disclaimer: I'd like to state first and foremost that I'm no expert in cryptography and this is one of my first cryptographic projects. I did however do my research and take into account the security risks involved in creating such a project.

As such, the database uses AES-CBC to encrypt its data. The database encryption key is encrypted using 2 layers of AES-256 and 3 different salts (each layer unlocks the next) which can be found in the "decryptEverything" function.

To prevent brute-force attacks against the password, the password hash is computed in combination with the 3 abovementioned salts and a bit of AES-256 (completely insane, but does the job). The password is used to decrypt the first salt. The password is then encrypted using the first salt, then concatenated with the first salt to create the decryption key for the second salt. The second salt is then used along with the encrypted second salt as the decryption key for the saved password hash, which is then ran against the hash of the entered password. As mentioned before, insane.

The password hash is then concatenated with the first salt to create a decryption key for the database key, which is finally used to decrypt the actual data in the SQLite database.

## Author

Created by: Leonard Haddad 

## License

This script is provided under the terms of the MIT License. You may modify, share and use the script however you like. I do not take responsibility for any damage caused by the use of this script.
