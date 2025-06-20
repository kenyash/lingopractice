import csv
import random


usedword= []
     
def csv_list():
    """opens csv files, saves word to global list for program use"""
    lingolist = []
    with open('LingoDictionary.csv',  newline='') as lingowords:
        worddict = csv.reader(lingowords) #opening list of words as csv reader object
        for row in worddict:
            for word in row:
                lingolist.append(word) 
    return lingolist


def return_random_word(low):
    """obtaining random word for game"""
    chosenw = random.choice(low) #choose a psuedorandom word from the list
    usedword.append(chosenw)
    return chosenw


def display_fl(word):
    """coded to always display firstletterof randomword"""
    first_letter = word[0]
    return first_letter

def get_user_input():
    """obtaining user guess with validation checking"""
    user_guess = input("Welcome to lingo, baby!!!, Please enter a 5 letter word starting with the first letter displayed ")
    try:
        if len(user_guess) != 5:
            raise ValueError("Please enter a input of 5 letters")
    except ValueError as val :
        print(val)

    try:
        if not user_guess.isalpha():
            raise TypeError("Please enter letters only")
    except TypeError as ty:
        print(ty)
            
    return user_guess

def compare_input(user_guess, word):
    """compare user input with randomized word"""
    comp_dict = {} #will hold a list of two values which will determine how square should be shaded
    "setting the logic for squares"
    for i in range(len(word)):
        if word[i] == user_guess[i]:
            comp_dict[i] = [True, True] ##if index and letter correct
        elif user_guess[i] in word and word[i] != user_guess[i]: ##if letter is in the word but index incorrect
            comp_dict[i] =[True, False]
        else:
            comp_dict[i] = [False, False] #if letter not in word and index not correct 
    print(comp_dict)
    return     
    

    

if __name__ == "__main__":
    low = csv_list()
    word = return_random_word(low)
    print(word)
    ug = get_user_input()
    compare_input(ug, word)
    #compare_input(user_guess, word)
    
    
    
    
