import math
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def encrypt(text,shift):
    newtext=""
    for i in text:
        if i in letters:
            c=letters.index(i)
            d=letters[(c+shift)%52]
            newtext=newtext+d
        else:
            newtext+=i
    print(f"your encrypted text is ; {newtext}")

def decrypt(text,shift):
    newtext=""
    for i in text:
        if i in letters:
            c=letters.index(i)
            e=c-shift
            if e < 0:
                e=e+52
            d=letters[e%52]
            newtext+=d
        else:
            newtext+=i
    print(f"your decrypted text is ; {newtext}")
choice='yes'
while choice=='yes':
    a=input(f"type encrypt for encryption and decrypt for decryption , \n")
    t=input("TYPE YOUR TEXT : ,\n")
    s=int(input("TYPE SHIFT NO :, \n"))
    if a.lower() == 'encrypt':
        encrypt(text=t,shift=s)
    elif a.lower()=='decrypt':
        decrypt(text=t,shift=s)
    choice=input("type yes if you want to continure :")
    if choice!="yes":
        print("GOODBYE!!!!,HAVE A NICE DAY")