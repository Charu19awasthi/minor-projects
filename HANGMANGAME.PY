import random
list=['apple','mango','peacock','teacher','blue','potato']
hangman = ['''
+---+
 |   |
 O   |
/|\  |
/ \  |
     |      
=======
''',''' 
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=======
''','''
+---+
 |   |
 O   |
/|\  |
     |
     |
=======
''','''
+---+
 |   |
 O   |
/|   |
     |
     |
=======
''','''
+---+
 |   |
 O   |
 |   |
     |
     |
=======
''','''
+---+
 |   |
 O   |
     |
     |
     |
=======
''','''
+---+
 |   |
     |
     |
     |
     |
=======
''']
lives=6
print("lets play a hangman game!!!")
print("you have only 6 attempts,\n GOOD LUCK !!!")
selected_word=random.choice(list)
m=[]
for i in range(len(selected_word)):
    m+='_'
print(m)
game_play=True
while game_play==True:
    entered_letter=input("guess a letter").lower()
    for index in range(len(selected_word)):
        if selected_word[index]==entered_letter:
            m[index]=entered_letter
            print(m)
        
    if entered_letter not in selected_word:
        lives=lives-1
    print(hangman[lives])
    if lives==0:
                game_play=False
                print("YOU LOST !!!")
            
    if '_' not in m:
        game_play=False
        print("YOU WIN !!")
