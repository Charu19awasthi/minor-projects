import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
digits=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','&','*','^','<']
print("welcome to password generator")
l=int(input("enter how many letters want to enter in password"))
s=int(input("how many symbols want to add"))
d=int(input("how many digits want to add"))
password=[]
for i in range(0,l):
     a = random.choice(letters)
     password.append(a)
for i in range(0,d):
     a=random.choice (digits)
     password.append(a)
for i in range(0,s):
     a=random.choice (symbols)
     password.append(a)
random.shuffle(password)
finalpassword=""
for i in password:
     finalpassword+=i
print(f"password created according to your choices ,\n {finalpassword}")


