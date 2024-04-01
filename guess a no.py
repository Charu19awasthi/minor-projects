import random
import execise
attempt=10
attempt_hard=5
c=True
print(execise.logo)
def easy():
    global attempt
    global c
    attempt=attempt-1
    user_choice=int(input("make a guess :"))
    if user_choice>think:
        print(f"your choice is too high ,\n guesss again \n\n you have {attempt} attempts left")
    elif user_choice<think:
        print(f"your choice is too low ,\n guesss again \n\n you have {attempt} attempts left")
    elif user_choice==think:
        c=False
        print(f"YOU MADE A RIGHT GUESS NO IS {think}")
        print(execise.win)

def hard():
    global c
    global attempt_hard
    attempt_hard=attempt_hard-1
    user_choice=int(input("make a guess :"))
    if user_choice>think:
        print(f"your choice is too high ,\n guesss again \n\n you have {attempt_hard} attempts left \n")
    elif user_choice<think:
        print(f"your choice is too low ,\n guesss again \n\n you have {attempt_hard} attempts left \n")
    elif user_choice==think:
        c=False
        print(f"YOU MADE A RIGHT GUESS NO IS {think}")
        print(execise.win)


print("LET ME THINK OF A NO BETWEEN 1 TO 50")
choice=input("choose level of difficulty easy or hard  \n").lower()
think=random.randint(1,50)
if choice=='easy':
    print(f"you have {attempt} attempts to guess the no \n")
    while c==True:
        easy()
        if attempt==0:
            print("out of guesses , YOU LOSE !!!!")
            print(execise.lose)
            c=False
            
elif choice=='hard':
    print(f"you have {attempt_hard} attempts to guess the no \n")
    while c==True:
        hard()
        if attempt_hard==0:
            print("out of guesses , YOU LOSE !!!!")
            print(execise.lose)
            c=False


    
