import random
print("welcome to ROCK PAPER SCISSOR game \n type 0 FOR paper \n 1 FOR rock \n 2 FOR SCISSOR")
comp_score =0
score=0
ans="y"
art=["paper","rock","scissor"]
while ans == 'y':
    choice = int (input("enter your coice (0,1,2)"))
    comp_choice= random.randint(0,2)
    if (choice<0 or choice>2):
        print("invalid choice")
    else:
        print(f"your choice \n {art[choice]}")
        print(f"computer choice \n {art[comp_choice]}")
    if (choice==2 and comp_choice ==0):
        print("you win")
        score+=1
    elif (choice< comp_choice):
        print ("you win")
        score+=1
    elif (choice == comp_choice):
        print("tie")
    elif (choice > comp_choice):
        print("you lost")
        comp_score+=1
    ans=input("do you want to continue yes =y")
print (f"YOUR FINAL SCORE {score} and computer score {comp_score}")
