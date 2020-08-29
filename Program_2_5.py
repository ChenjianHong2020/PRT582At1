import random

print("Welcome to Hangman game")
#Welcome message when program running

def new_game():
#Method to start a new game
    
    print("New game begins!")

    key = generate_key()
    print("The key is: "+key+" (easy to test)") 
    #For test
    
    life = 6
    #The total chances of the player

    answer_board = [] 
    for letter in key:
        answer_board.append("_")    
    #Initialize the answer board
        
    pick_board = []
    #Here are the letters guessed before
    
    print("You have "+str(life)+" chances to find out the key")
    print(" ".join(answer_board))
    new_round(life,answer_board,pick_board,key)
    
def generate_key():
#Method to generate the key
    
    with open('1000WordsList.txt') as f:
        words_library = [line.rstrip() for line in f]    
        #Read the file of the words library which can be updated
        
    return random.choice(words_library)
    #Generate a key from the words library randomly



def validation_input(pick):
#Method to validate the input
    
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
        
def new_round(life,answer_board,pick_board,key):
#Method to start a guessing round

    pick_correct = False

    pick = new_input(pick_board)
    #Get a avaliable input
    
    pick_board.append(pick)
    #Add to the list including the letters have been guessed before

    for num in range(len(key)):
        if key[num] == pick:
            answer_board[num] = pick
            pick_correct = True          
    #Check the letter existing in the answer or not
            
    if pick_correct == True:
        print("Correct and "+str(life)+" chances left")
    #If the guess is correct     

    else:
        life-=1
        print("Wrong and "+str(life)+" chances left")
    #If the guess is wrong 
        
    print(" ".join(answer_board))
    check_status(life,answer_board,pick_board,key)
    #Check the game can be continued or not
    
def check_status(life,answer_board,pick_board,key):
#Method to check the game can be continued or not

    if life == 0:
        return lose_result()
    #Life equals to zero, player loses
    
    elif "_" in answer_board:
        return new_round(life,answer_board,pick_board,key)
    #Answer is still not found, game continues
    
    else:
        return win_result()
    #Answer is found, player wins

def lose_result():
    print("You lose")
    print("---------------------------------")
    new_game()
    
def win_result():
    print("You win")
    print("---------------------------------")
    new_game()       
         
new_game()
#Game begins
