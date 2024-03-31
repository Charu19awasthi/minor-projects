import os
def bider(a):
    high=0
    n=""
    for i in a:
        if a[i]>high:
            high=a[i]
            n=i
    print(f"the list of all bidders is {a}")     
    print(f"the winner is {n} and the bidding amount is{high}")   

stud={}
c=True
while c==True:
    name=input("enter name")
    bid=int(input("enter bid :"))
    stud[name]=bid
    d=input("are there any other bider yes or no").lower()
    if d=='yes':
        os.system('cls')
    elif d=='no':
        c=False
        bider(stud)    


