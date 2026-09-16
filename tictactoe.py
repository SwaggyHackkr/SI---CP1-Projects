#SI, Period 1, Tic tac toe pseudocode assignment

#SUBCOMPONENT 1: Board Setup
#Represent the board as 9 spaces, numbered 1 to 9 in reading order:
#1 | 2 | 3
#4 | 5 | 6
#7 | 8 | 9
#     - Every space starts EMPTY
#     - Player 1 uses the symbol X
#     - Player 2 uses the symbol O

#SUBCOMPONENT 2: Taking a Turn (for the current player)
#DISPLAY the current board
#DISPLAY which player’s turn it is
#GET the space number the player wants to mark 
#REPEAT the asking step until the player picks a space that is EMPTY
#     (WHEN the space is already take, DISPLAY “Space taken, pick another” and ask again)
#MARK that space with the current player’s symbol

#SUBCOMPONENT 3: Checking for a winner
#CHECK all 8 possible winning lines:
#Top row   (spaces 1, 2, 3)
#Middle row (spaces 4, 5, 6)
#Bottom row (spaces 7, 8, 9)
#Left column (spaces 1, 4, 7)
#Middle column (spaces 2, 5, 8)
#Right column (spaces 3, 6, 9
#Diagonal down (spaces 1, 5, 9)
#Diagonal up (spaces 3, 5, 7)

#WHEN any one of these lines holds the same player’s symbol 3 times, that player is the winner

#SUBCOMPONENT 4: Checking for a Tie
#CHECK whether all 9 spaces are filled
#CHECK whether there is no winner
#WHEN both are true, the game is a tie

#FULL SEQUENCE 

#START
# CREATE a board with 9 spaces, all empty, numbered 1 to 9
#SET current player TO Player 1
#SET winner TO NOBODY
#SET spaces filled to 0
#DISPLAY the empty board

#REPEAT the following until winner is found OR spaces filled reaches 0

#	DISPLAY a message saying whose turn it is (current player)
#	GET a space number from the current player
#	REPEAT the asking until the chosen space is EMPTY
#		DISPLAY “That space is taken, choose another”
#   MARK the chosen space with the current player’s symbol
#   ADD 1 TO spaces filled 
#   DISPLAY the updated board


#CHECK all 8 winning lines for 3 matching symbols in a row
#WHEN a winning line matches the current player’s symbols, 
#	SET winner TO current player

#CHECK whether spaces filled now equals 9 AND winner is still NOBODY
#WHEN both are true, SET result TO “TIE”

#SWITCH current player TO the other player

#END REPEAT

#CHECK the winner
#WHEN winner is Player1, DISPLAY “Player 1 wins!”
#WHEN winner is Player 2, Display “Player 2 wins!”
#WHEN result is “TIE”, DISPLAY “It’s a tie!”
#DISPLAY the final board
#END