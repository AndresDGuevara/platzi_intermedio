import random 
import os

def clear(): # Function to clear the terminal
    os.system("clear")

def print_hangman(values): # Functuion to print the hangman
    print("\n\t +--------+")
    print("\t |       | |")
    print("\t {}       | |".format(values[0]))
    print("\t{}{}{}      | |".format(values[1], values[2], values[3]))
    print("\t {}       | |".format(values[4]))
    print("\t{} {}      | |".format(values[5],values[6]))
    print("\t         | |")
    print("  _______________|_|___")
    print("  `````````````````````\n")
    
def print_hangman_win(): # Function to print the hangman after winning
    print("\n\t +--------+")
    print("\t         | |\n")
    print("\t         | |")
    print("\t O       | |")
    print("\t/|\\      | |")
    print("\t |       | |")
    print("  ______/_\\______|_|___")
    print("  `````````````````````\n")
    
def print_word(values): # Function to print the word to be guessed
    print("\n\t", end="")
    for x in values:
        print(x, end=" ")
    print()
    
def check_win(values): # Function to check for win
    for char in values:
        if char == '_':
            return False
    return True

def hangman_game(word): # Function for each hangman game
    clear()
    # Stores the letters to be displayed
    word_display = []
    # Store the correct letters in the word
    correct_letters = []
    # Stores the incorrect guesses made by the player
    incorrect = []
    # Number of chances (incorrect guesses)
    chances = 0
    # Stores the hangman's body values
    hangman_values = ['O','/','|','\\','|','/','\\']
    # Stores the hangman's body values to be shown to the player
    show_hangman_values = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
    # Loop for creating the display word
    for char in word:
        if char.isalpha():
            word_display.append('_')
            correct_letters.append(char.upper())
        else:
            word_display.append(char)
    # Inner game Loop
    while True:
        # Printing necessary values
        print_hangman(show_hangman_values)
        print_word(word_display)            
        print("\nIncorrect characters : ", incorrect)
           # Accepting player input
        inp = input("\nEnter a character = ")
        if len(inp) != 1:
            clear()
            print("Wrong choice!! Try Again")
            continue
        # Checking whether it is a alphabet
        if not inp[0].isalpha():
            clear()
            print("Wrong choice!! Try Again")
            continue
        # Checking if it already tried before   
        if inp.upper() in incorrect:
            clear()
            print("Already tried!!")
            continue  
            # Incorrect character input 
        if inp.upper() not in correct_letters:
            # Adding in the incorrect list
            incorrect.append(inp.upper())
            # Updating the hangman display
            show_hangman_values[chances] = hangman_values[chances]
            chances = chances + 1
            # Checking if the player lost
            if chances == len(hangman_values):
                clear()
                print("\n\tGAME OVER!!!")
                print_hangman(hangman_values)
                print("The word is :", word.upper())
                break
            # Correct character input
        else:
            # Updating the word display
            for i in range(len(word)):
                if word[i].upper() == inp.upper():
                    word_display[i] = inp.upper()
            # Checking if the player won        
            if check_win(word_display):
                clear()
                print("\tCongratulations! ")
                print_hangman_win()
                print("The word is :", word.upper())
                break
        clear()

def run(): # Function with the GAME LOOP
    # Types of categories
    topics = {1: "DC characters", 2:"Marvel characters", 3:"Dragon Ball characters"}
    # Words in each category
    dataset = {"DC characters":["SUPERMAN", "JOKER", "HARLEY QUINN", "GREEN LANTERN", "FLASH", "WONDER WOMAN", "AQUAMAN", "MARTIAN MANHUNTER", "BATMAN"],\
                "Marvel characters":["CAPTAIN AMERICA", "IRON MAN", "THANOS", "HULK", "BLACK PANTHER", "BLACK WIDOW", "THOR"],
                "Dragon Ball characters":["SON GOKU", "VEGETA", "KRILLIN", "BULMA", "PICCOLO", "MASTER ROSHI", "FRIEZA", "BROLI", "MAJIN BUU", "GOTEN", "GOHAN"]
                }
                
    print("\n\tWELCOME TO HANGMAN GAME")
    while True:
        # Printing the game menu
        print("\n-----------------------------------------")
        print("\t\tGAME MENU")
        print("-----------------------------------------\n")
        for key in topics:
            print("\tPress", key, "for", topics[key])
        print("\nPress", len(topics)+1, "to quit\n")    
        # Handling the player category choice
        try:
            choice = int(input("Enter your choice = "))
        except ValueError:
            clear()
            print("Wrong choice!!! Try again")
            continue
        # Sanity checks for input
        if choice > len(topics)+1:
            clear()
            print("No such topic!!! Try again.")
            continue   
        # The EXIT choice   
        elif choice == len(topics)+1:
            print("\nThank you for playing!")
            break
        # The topic chosen
        chosen_topic = topics[choice]
        # The word randomly selected
        ran = random.choice(dataset[chosen_topic])
        # The overall game function
        hangman_game(ran)
        
if __name__ == '__main__':
    clear()
    run()