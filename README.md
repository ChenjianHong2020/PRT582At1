# PRT582At1
Hangman Game Development History
# Program 1.1
Requirement: One word will be generated randomly.
Test input: (Null)
Expected output: (One random word)
# Program 1.2
Requirement: Player will be presented with a number of blank spaces representing the missing letters the player needs to find.
Test input: (Null)
Expected output: (Blank spaces with the length of the word)
# Program 1.3
Requirement: If the player’s chosen letter exists in the answer, then all places in the answer where that letter appear will be revealed.
Test input: 1."a" 2."A" 3."abc" 4."123" 5."!@#" 6.(Null)
Expected output: (Blank spaces with the correct letters revealed)
# Program 1.4
Requirement: Every time the player guesses a letter wrong, the player’s life will be deducted.
Test input: 1.(correct)  2.(wrong)  3.(invalid input)
Expected output: 1.(life not deducted)  2.(life deducted) 3.(invalid message)
# Program 1.5
Requirement: The player must find the missing word before the player’s life becomes zero.
Test input: 1.(life becomes zero) 2.(survive) 3.(the same letter guessed before)
Expected output: 1.(died) 2.(win) 3.(invalid message)
# Program 2.1
Code smell: 	Input validation is not an independent method. This makes it difficult to modify the rule of validation in the future development.		
Solution: 	Define a validation method instead of the old function.
# Program 2.2
Code smell: 	The key word generator is not an independent method. This makes the logic of the game difficult to be understood.	Also, it is not easy to find out how to update the library of the words.
Solution: 	Define a generator method instead of the old function.
# Program 2.3
Code smell: 	The loop for the user to input his/her guesses is too long to read and modify. This greatly increases the complexity of the program.
Solution: 	Split the loop into several parts logically.
# Program 2.4
Code smell: 	The function to check if the input is duplicate makes the new_round() vague and complex. If there are new changes in future requirements, it will cost a lot of time to modify this.
Solution: 	The loop to check the validation of the input could be simplified to make the new_round() method much lighter. Define a new method new_input() instead of the old function.
# Program 2.5
Code smell: 	The scope of the parameters can be adjusted to make the program more stable and clearer.
Solution: 	Define a new method new_game() to start the game and assign the
	Parameters needed.
# Program 3.0
The final vision of this assignment with all the comments.
