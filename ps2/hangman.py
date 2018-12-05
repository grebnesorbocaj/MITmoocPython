# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    temp = True
    for c in secret_word:
        if c not in letters_guessed:
            temp = False
    return temp



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed = ""
    for c in secret_word:
        if c not in letters_guessed:
            guessed = guessed + "_ "
        elif c in letters_guessed:
            guessed = guessed + c + " "
    return guessed



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters = string.ascii_lowercase
    for c in letters_guessed:
        if c in letters:
            letters = letters.replace(c, "")
    return letters
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_guessed = []
    guesses = 6
    num_let = len(secret_word)
    print("This word is %s letters long!" %num_let)
    while(True):
        if(guesses<=0):
            print("Out of guesses!")
            print("You lose!! ----------- You lose!! --------- You lose!!")
            print("The word was %s" %secret_word)
            break
        print("You have %s guesses!" %guesses)
        print("Letters left: %s" %get_available_letters(letters_guessed))

        guess = str(input("Guess a letter! "))
        guess = guess.lower()
        if(guess not in string.ascii_lowercase):
            print("You must guess a letter!")
            continue
        if(len(guess) > 1):
            print("You must guess a single letter!")
            continue    
        letters_guessed.append(guess)

        if(is_word_guessed(secret_word, letters_guessed)==False):
            if(guess in secret_word):
                guesses = guesses
            elif(guess in 'aeiou'):
                guesses = guesses - 2
            else:
                guesses = guesses - 1
            print(get_guessed_word(secret_word,letters_guessed))
        else:
            print("_________________________")
            print("Congrats! you got it!")
            print(get_guessed_word(secret_word,letters_guessed))
            break
        print("_________________________")





# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    index = 0
    my_word = my_word.replace(" ", "")
    if(len(my_word)==len(other_word)):
        for c in my_word:
            # print("My: %s ---Other: %s" %(c,other_word[index]))
            if c == '_':
                index = index + 1
                continue
            elif c != other_word[index]:
                return False
            index = index + 1
        return True



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    of_words = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            of_words.append(word)

    if len(of_words) == 0:
        print("No matching words!")
        return

    print(of_words)



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_guessed = []
    guesses = 6
    num_let = len(secret_word)
    print("This word is %s letters long!" %num_let)
    while(True):
        if(guesses<=0):
            print("Out of guesses!")
            print("You lose!! ----------- You lose!! --------- You lose!!")
            print("The word was %s" %secret_word)
            break
        print("You have %s guesses!" %guesses)
        print("Letters left: %s" %get_available_letters(letters_guessed))

        guess = str(input("Guess a letter! "))
        guess = guess.lower()
        if(guess == '*'):
            show_possible_matches(get_guessed_word(secret_word,letters_guessed))
        if(guess not in string.ascii_lowercase):
            print("You must guess a letter!")
            continue
        if(len(guess) > 1):
            print("You must guess a single letter!")
            continue    
        letters_guessed.append(guess)

        if(is_word_guessed(secret_word, letters_guessed)==False):
            if(guess in secret_word):
                guesses = guesses
            elif(guess in 'aeiou'):
                guesses = guesses - 2
            else:
                guesses = guesses - 1
            print(get_guessed_word(secret_word,letters_guessed))
        else:
            print("_________________________")
            print("Congrats! you got it!")
            print(get_guessed_word(secret_word,letters_guessed))
            break
        print("_________________________")



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

    # show_possible_matches("aaaabbb_ ")

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
