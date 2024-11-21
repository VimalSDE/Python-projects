
import random
print ("welcome to random password generater!")
randomechars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*"
nbrofpwds=int(input("Please Enter the nuber of passwordto be generater:"))
pwdlen=int(input("Please enter the lenth of the password needed:"))

print("here are your randome paswords:")
for x in range(nbrofpwds):
    pwd = ""
    for chars in range(pwdlen):
       pwd= pwd + random.choice(randomechars)
    print(pwd)
