print("Welcome to Hangman Game")

with open('1000WordsList.txt') as f:
    words = [line.rstrip() for line in f]

import random
key = random.choice(words)
length = len(key)
print("key to test: "+key)

answer_board = []
for letter in key:
    answer_board.append("_")
#print(" ".join(answer_board))

pick_board = []
life = 7
while "_" in answer_board:
    pick_valid = False
    pick_correct = False
    while pick_valid == False:
        pick = input("Try Now!\n").lower()
        if pick.isalpha() == True and len(pick) == 1:
            pick_valid = True
            pick_board.append(pick)
            for num in range(length):
                if key[num] == pick:
                    answer_board[num] = pick
                    pick_correct = True
        else:
            print("Guess one letter please")            
    if pick_correct == True:
        print("Correct and "+str(life)+" chances left")
    else:
        life-=1
        print("Wrong and "+str(life)+" chances left")
    print(" ".join(answer_board))
    #print(pick_board)
        
               
            
