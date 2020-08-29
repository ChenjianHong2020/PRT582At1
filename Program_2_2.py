import random

print("Welcome to Hangman Game")

def generate_key():
    with open('1000WordsList.txt') as f:
        words_library = [line.rstrip() for line in f]    
#Read the file of the words library which can be updated
    return random.choice(words_library)
#Generate a key from the words library randomly

key = generate_key()
print("key to test: "+key)

length = len(key)
answer_board = []
for letter in key:
    answer_board.append("_")

def validation_input(pick):
    if pick.isalpha() == True and len(pick) == 1:
        return True
    else:
        return False
#The input of the user should be only one letter 

pick_board = []
life = 5
while "_" in answer_board:
    pick_valid = False
    pick_correct = False
    while pick_valid == False:
        pick = input("Try Now!\n").lower()
        if pick in pick_board:
            print("You have tried this one")
        elif validation_input(pick):
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
        if life==0:
            print("You died")
            exit()
    print(" ".join(answer_board))
    #print(pick_board)
print("You win")
exit()              
            
