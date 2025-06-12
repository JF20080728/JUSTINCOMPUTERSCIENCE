#Minecraft Hangman
import random

#Tuple to store the words
words = ("Creeper", "Griefers", "Biome", "Enderdragon", "Enderman", "Mobs", "Caving",
         "Nether", "Redstone", "Stack", "Wither skeleton", "Adventure Map", "Armor",
         "Beacon", "Bedrock", "Craft", "Drop", "Glitch", "Magma", "Mod", "Ore", "Portal",
         "Potion", "Silverfish")




#dictionary of key:()
hangman_art = {0: ("    ",
                   "    ",
                   "    "),
               1: ("  o  ",
                   "    ",
                   "    "),
               2: ("  o  ",
                   "  |  ",
                   "    "),
               3: ("  o  ",
                   "/ |  ",
                   "    "),
               4: ("  o  ",
                   "/ | \\ ",
                   "    "),
               5: ("  o  ",
                   "/ | \\  ",
                   " /   "),
               6: ("  o  ",
                   "/ | \\ ",
                   " / \\ ")}


#This function shows the human graphic design foreach wrong guesses
def display_man(wrong_guesses):
    print("***************")
    #Prints the hangman drawing from hangman_art based on how many wrong guesses have been made
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("***************")

#This function displays hints for te current situation
#The hint will show you the unguessed letters and the guessed letters
def display_hint(hint):
    print(" ".join(hint))

#This function shows the full correct answer when guessed
def display_answer(answer):
    print(" ".join(answer))



def main():
    #this chooses a random word from the tuple
    answer = random.choice(words)
    #converts letters to lower case
    answer_lower = answer.lower()
    #creates hints with underscores for each letter in the word
    hint = ["_"] * len(answer)
    #counts for wrong guesses
    wrong_guesses = 0
    #Set to store letters that the player had guessed
    guessed_letters = set()
    is_running = True



    while is_running:
        #Shows the hangman picture
        display_man(wrong_guesses)
        #shows the current hint; the correct letters that had been guessed
        display_hint(hint)
        #Converts the letters into lowercase
        guess = input("Guess a letter: ").lower()


#prevent people from entering multiple letters or numbers. Only allows 1 letter per entry
        if len(guess) != 1 or not guess.isalpha():
            print("Sorry, that's not a single letter.")
            continue
#Displays a message to show that multiple letters entered. Thus not registering the input
        #also tells the user and continues the code


 #Stoping already guessed letters
        if guess in guessed_letters:
            print(f"{guess} was already guessed so far.")
            continue
# Displays a message to show that the same letters are guesses. Then it wil inform the user
        # This won't matter if it was lowercase or uppercase. Then continue the code

        guessed_letters.add(guess)

#check if the answer is case sensitive
        if guess in answer_lower:
            for i in range(len(answer)):
                if answer_lower[i] == guess:
                    hint[i] = guess
#Correcting the guesses to make it case insensitive


  #subtracting 1 life from the hangman if it was a wrong guess
        else:
            wrong_guesses += 1

#This line of code shows you how many guesses you have left then shows you the answers. Afterwards, it will celebrate your victory
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("Congratulations, you guessed the word!")
            is_running = False

#This line of code is responsible for showing how many wrong guesses you have and shows you the answer. Then it will display a game over message.
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOST THE GAME! TRY AGAIN LATER!!! ")
            is_running = False

if __name__ == '__main__':
    main()

