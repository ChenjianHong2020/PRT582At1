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

def new_input(pick_board):
#Method for the player to input
    
    while True:
        pick = input("Try a letter!\n").lower()
        #Ignore the case
        
        if pick in pick_board:
            print("You have tried this letter. Change another one.")
        #Check if the letter has been guessed before
           
        elif validation_input(pick) == False:
            print("The input should be only one letter.")
        #Validation
            
        else:
            return pick
            break

pick_board = []
life = 5
def new_round(life,answer_board):
    pick_correct = False
    pick = input("Try a letter!\n").lower()
    if pick in pick_board:
        print("You have tried this one")
    elif validation_input(pick) == False:
        print("Guess one letter please")
    else:
        pick_valid = True
        pick_board.append(pick)
        for num in range(length):
            if key[num] == pick:
                answer_board[num] = pick
                pick_correct = True           
    if pick_correct == True:
        print("Correct and "+str(life)+" chances left")
    else:
        life-=1
        print("Wrong and "+str(life)+" chances left")    
    print(" ".join(answer_board))
    check_status(life,answer_board)          
    
def check_status(life,answer_board):
    if life == 0:
        return lose_result()
    elif "_" in answer_board:
        return new_round(life,answer_board) 
    else:
        return win_result()

def lose_result():
    print("You lose")
    
def win_result():
    print("You win")
           
new_round(life,answer_board)
