print("Welcome to Hangman Game")

with open('1000WordsList.txt') as f:
    words = [line.rstrip() for line in f]

import random
key = random.choice(words)
length = len(key)
print(key)

answer_board = []
for letter in key:
    answer_board.append("_")
print(" ".join(answer_board))
