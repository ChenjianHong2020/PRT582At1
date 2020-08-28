print("Welcome to Hangman Game")

with open('1000WordsList.txt') as f:
    words = [line.rstrip() for line in f]
#print(words)
import random
key = random.choice(words)
print(key)
