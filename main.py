from ast import Return
import hashlib

flag = 0

pass_hash = input("Enter md5 hash: ")

wordlist = input("File name: ")

try:
    pass_file = open (wordlist, "r")
except:
    print("No file found")
    quit()

try:
    for word in pass_file:

        enc_wrd = word.encode('utf-8')
        digest = hashlib.md5(enc_wrd.strip()).hexdigest()
        
        if digest == pass_hash:
            print("PASSWORD FOUND")
            print("password is " + word)
            flag = 1
            break
except:
    print("END OF FILE REACHED!")

if flag == 0:
    print("password/passphrase is not in the list")
