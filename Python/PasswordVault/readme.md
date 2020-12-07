# Python Password Vault

This small script contains a standalone password vault, secured with Multi-Layer AES-256 Encryption.

The passwords are stored within an unencrypted SQLite Database, the data inside the database is however fully encrypted.

## Author

Created by: Leonard Haddad 

## Function

The script uses 3 salts (2 of which are encrypted) to generate the database key. The database key is then used to encrypt the data within the database.

The first salt is used with the password in order to encrypt the second salt. The second salt can therefor only be accessed with the correct password, don't lose the master password! (Can be modified from within the app)

The second salt, along with the encrypted password is used to encrypt the 3rd salt. The 3rd salt is used with the password's hash (salted with 2nd salt) in order to encrypt the database data.

DO NOT LOSE THE MASTER PASSWORD OR YOU WILL LOSE ACCESS TO ALL THE DATA IN THE DATABASE


## License

This script is provided under the terms of the MIT License. You may modify, share and use the script however you like. I do not take responsibility for any damage caused by the use of this script.
