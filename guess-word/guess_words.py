import csv
from random import *

def getWord():
    """
    Returns: string
    """
    words = dict()
    with open("words.csv", "r") as words_file:
        csv_reader = csv.reader(words_file, delimiter=',')
        for line in csv_reader:
            words[line[0]] = line[1]
    randNumber = str(randint(1, 10))
    return words[randNumber]
        
    
def guessWord(word):
    """
    Returns: void
    :param word: string
    """
    
    wordLetters = list(word)
    board = ["_"]*len(word)
    win = False
    
    print("I've got a word. Try and guess it!")
    
    while win == False:
        msg = "\nGuess a letter: "
        
        try:
            guess = input(msg)
            assert len(guess) == 1
            assert guess.isalpha()
        except AssertionError:
            print("I need only a single letter!")
            continue
        
        if guess in wordLetters:
            letterIndex = wordLetters.index(guess)
            board[letterIndex] = guess
            wordLetters[letterIndex] = '$'
            
        print(("".join(board)))
        
        if "_" not in board:
              print("\nYOU GUESSED IT!")
              win = True
              break
            
word = getWord()
guessWord(word)
    
