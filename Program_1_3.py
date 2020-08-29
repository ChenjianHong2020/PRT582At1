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
pick_valid = False
pick_correct = False
pick = input("Try Now!\n").lower()
if pick.isalpha() == True and len(pick) == 1:
    pick_valid = True
if pick_valid == False:
    print("Guess one letter please")
    exit()
else:
    pick_board.append(pick)
    for num in range(length):
        if key[num] == pick:
            answer_board[num] = pick
            pick_correct = True
if pick_correct == True:
    print("Correct")
else:
    print("Wrong")
print(" ".join(answer_board))
#print(pick_board)
