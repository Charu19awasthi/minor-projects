import os
import random
import followers
import execise
print(execise.high)
score=0
  
def account_holder(account):
    name=account['name']
    description=account['description']
    country=account['country']
    return (f"{name}, a {description}, from {country}")

def check(guess,followers_count_1,followes_count_2):
    if followers_count_1>followes_count_2:
        if guess==2:
            return False
        else:
            return True
    else:
        if guess==1:
            return True
        else:
            return False
account2=random.choice(followers.dict)
continue_flag=True
while continue_flag:
    account1=account2
    account2=random.choice(followers.dict)
    while account1==account2:
         account2=random.choice(followers.dict)

    print(f"COMPARE 1 : {account_holder(account1)}")
    print(execise.vs)
    print(f"COMPARE 2 : {account_holder(account2)}")
    guess=int(input("who has more followers ..type 1 or 2"))
    followers_count1=account1['followers']
    followers_count2=account2['followers']
    is_correct=check(guess,followers_count1,followers_count2)
    print(os.system('cls'))
    if is_correct:
        score+=1
        print(f"correct answer your score is {score}")
    else:
        print(f"you are wrong .your final score is{score}")
        continue_flag=False
        print(execise.bye)
