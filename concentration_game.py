import random
       
def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''

    # YOUR CODE GOES HERE
    
    substitute = None

    for i in range(len(deck)):

        subNum = (random.randint(0,len(deck)-1))

        substitute = deck[i]
        deck[i] = deck[subNum]
        deck[subNum] = substitute
        
    print("Shuffling the deck...\n")

def create_board(size):
    '''int->list of str
       Precondition: size is even positive integer between 2 and 52
       Returns a rigorous deck (i.e. board) of a given size.
    '''
    board = [None]*size 

    letter='A'
    for i in range(len(board)//2):
          board[i]=letter
          board[i+len(board)//2 ]=board[i]
          letter=chr(ord(letter)+1)
    return board

def print_board(a):
    '''(list of str)->None
       Prints the current board in a nicely formated way
    '''
    for i in range(len(a)):
        print('{0:4}'.format(a[i]), end=' ')
    print()
    for i in range(len(a)):
        print('{0:4}'.format(str(i+1)), end=' ')
    print()


def wait_for_player():
    '''()->None
    Pauses the program/game until the player presses enter
    '''
    input("\nPress enter to continue. ")
    print()

def print_revealed(discovered, p1, p2, original_board):
    '''(list of str, int, int, list of str)->None
    Prints the current board with the two new positions (p1 & p2) revealed from the original board
    Preconditions: p1 & p2 must be integers ranging from 1 to the length of the board
    '''
    # YOUR CODE GOES HERE

    discovered[p1-1] = original_board[p1-1]
    discovered[p2-1] = original_board[p2-1]

    print_board(discovered)

    if discovered[p1-1] != discovered[p2-1]:

        discovered[p1-1] = '*'
        discovered[p2-1] = '*'

#############################################################################
#   FUNCTIONS FOR OPTION 1 (with the board being read from a given file)    #
#############################################################################

def read_raw_board(file):
    '''str->list of str
    Returns a list of strings represeniting a deck of cards that was stored in a file. 
    The deck may not necessarifly be playable
    '''
    raw_board = open(file).read().splitlines()
    for i in range(len(raw_board)):
        raw_board[i]=raw_board[i].strip()
    return raw_board


def clean_up_board(l):
    '''list of str->list of str

    The functions takes as input a list of strings representing a deck of cards. 
    It returns a new list containing the same cards as l except that
    one of each cards that appears odd number of times in l is removed
    and all the cards with a * on their face sides are removed
    '''
    print("\nRemoving one of each cards that appears odd number of times and removing all stars ...\n")
    playable_board=[]

    # YOUR CODE GOES HERE

    for i in range(len(l)):

        if l.count(l[i])%2 != 0:

            l[i] = '*'

        if l[i] == '*':

            continue

        playable_board += [l[i]]
    
    return playable_board


def is_rigorous(l):
    '''list of str->True or None
    Returns True if every element in the list appears exactlly 2 times or the list is empty.
    Otherwise, it returns False.

    Precondition: Every element in the list appears even number of times
    '''

    # YOUR CODE GOES HERE

    for i in range(0,len(l)):

        numElements = 0

        for j in range(0,len(l)):

            if l[i] == l[j]:

                numElements += 1

        if numElements%2 != 0:

            return False

    return True

###############################
#   Additional function(s)    #
###############################

def clean():
    '''(None) -> None
    Clears the python shell to create a clean layout.'''

    print("\n"*100)

def ascii_text_box(textBox):
    '''(String) -> None
    Creates a textbox to display message for user'''

    print("***" + ("*" * len(textBox)) + "***")
    print("* "," " * len(textBox)," *")
    print("* ",textBox," *")
    print("* "," " * len(textBox)," *")
    print("***" + ("*" * len(textBox)) + "***")


##############################################################################

def play_game(board):
    '''(list of str)->None
    Plays a concentration game using the given board
    Precondition: board a list representing a playable deck
    '''
    clean()

    print("Ready to play ...\n")

    # this is the function that plays the game
    # YOUR CODE GOES HERE

    game_board = ['*']*len(board)

    gameFinished = False
    guessCounter = 0

    while gameFinished != True:

        print_board(game_board)
        
        validGuess = False
        
        while validGuess == False:
            print("\nEnter two distinct positions on the board that you want to revealed.\ni.e two integers in the range [1,"+str(len(board))+"]")
            guess1 = int(input("Enter position 1: "))
            guess2 = int(input("Enter position 2: "))

            if guess1 == guess2:
                print('You chose the same positions.')
                print('Please try again. This guess does not count. Your current number of guesses is ' + str(guessCounter))

            elif game_board[guess1-1] != '*' or game_board[guess2-1] != '*':

                print('One or both of your chosen positions has already been paired.')
                print('Please try again. This guess does not count. Your current number of guesses is ' + str(guessCounter))

            else:

                validGuess = True

        
        print("")
        print_revealed(game_board, guess1, guess2, board)
        guessCounter += 1
        print("")
        wait_for_player()
        clean()

        if game_board == board:

            gameFinished = True
            
    print("Congratulations! You've completed the game with " + str(guessCounter) + " guesses! That is " + str(int(guessCounter - (len(board)/2))) + " more than the best possible outcome!")

###############################################################################
# MAIN 
###############################################################################

ascii_text_box("__Welcome to my Concentration game__")
    
# YOUR CODE TO GET A CHOICE 1 or CHOICE 2 from a player GOES HERE

option = int(input("\nWould you like (enter 1 or 2 to indicate your choice):\n(1) me to generate a rigorous deck of cards for you\n(2) or, would you like me to read a deck from a file?\n"))

while type(option) == int:
    if option == 1:
        
        # YOUR CODE FOR OPTION 1 GOES HERE
        # In option 1 somewhere you need to and MUST have a call like this:
        # board=create_board(size)

        print("You chose to have a rigorous deck generated for you")
        numCards = -1

        while numCards > 52 or numCards < 2 or numCards%2 != 0:

            numCards = int(input("\nHow many cards do you want to play with?\nEnter an even number between 2 and 52: "))

        board = create_board(numCards)
        shuffle_deck(board)
        wait_for_player()

        play_game(board)
        break

    elif option == 2:
        
        # YOUR CODE FOR OPTION 2 GOES HERE
        # In option 2 somewhere you need to and MUST have the following 4 lines of code one after another
        #
        #print("You chose to load a deck of cards from a file")
        #file=input("Enter the name of the file: ")
        #file=file.strip()
        #board=read_raw_board(file)
        #board=clean_up_board(board)

        print("You chose to load a deck of cards from a file")
        file=input("Enter the name of the file: ")
        file=file.strip()
        board=read_raw_board(file)
        board=clean_up_board(board)

        ascii_text_box("__This deck is now playable but not rigorous. It has " + str(len(board)) + " cards.__")

        wait_for_player()
        clean()

        if len(board) == 0:

            print("The resulting board is empty.\nIt is impossible to play the Concentration game with an empty board.\nGood bye!!")
            break

        shuffle_deck(board)
        wait_for_player()

        play_game(board)
        break

    else:

        option = int(input(str(option) + " is not existing option. Please try again. Enter 1 or 2 to indicate your choice\n"))

