import random 

 def load_dictionary(file_patch):
    with open(file_path) as f:
       words = [line.strip() for line in f]
    return words

 def is_valid_gess(guess, guesses):
    return guess in guesses 

 def evaliate_guess(guess, word):
     str = ""

     for i in range(5)
         if guess[i] == word[i]:
            str += "\033[33n" + guess [i]
        else: 
            if guess [i]in word:
            else:
                str +="\033[0n"+ guess[i]

    return str "\033[0n


def wordle(guesses, answers):
    print("welcome to wordle! get 6 chances to guess a 5-letter word,")

guesses = load_dictionary("guesses.text")
answers = load_dictionary("guesses.text")

wordle(guesses, answers)
