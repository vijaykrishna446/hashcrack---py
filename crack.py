import hashlib

flag = 0

pass_hash = input("Enter your hash: ")

wordlist = input("Enter your wordlist: ")

try:
       pass_file = open (wordlist, "r")
except:
         print("no file found")
         quit()

for word in pass_file:
       
       enc_wrd = word.encode('utf-8')
       digest = hashlib.md5(enc_wrd.strip()).hexdigest()
       
       print(word)
       print(digest)
       print(pass_hash)
       
       if digest == pass_hash:
             print("password found")
             print("password is " + word)
             flag = 1
if flag == 0:
    print("password not found")
