import random

#Function to load a list of words from a file
def load_dictionary(file_path):
    with open(file_path) as f:
        word = [line.strip().lower() for line in f if line.strip()]
    return word #Return the list with lowercased letters

#This function checks if the guesses are valid or not
def is_valid_guess(guess, guesses):
    #Requirement of the guess has to be 5 letters long
    return len(guess) == 5 and guess in guesses

#function to check the guessed word with the secret word
def evaluate_guess(guess, word):
    result = "" #make the colour of the result


    for i in range(5): #loop over each character in the 5 letter guess
        if guess[i] == word[i]:
            #Green letters if the guess is correct and in the right place
            result += "\033[32m" + guess[i]

        else:
            if guess[i] in word:

                #Yellow if theres a right letter but wrong place
                result += "\033[33m" + guess[i]

                #no colours if the guess is wrong
            else: result += "\033[0m" + guess[i]

    return result + "\033[0m" #resets colour after show the guess

#Wordle game function
def wordle(guesses, answers):
    print("welcome to Wordle! Get 6 chances to guess a secret word")
    secret_word = random.choice(answers) #chooses a secret word from the answers list

#starts the game at 1st guess
    attempts = 1
    #max guess is 6 times
    max_attempts = 6

#loop while the player still has remaining attempts
    while attempts <= max_attempts:
        guess = input("Enter guess #" + str(attempts) + ": ").lower()

        #varify the guess before procedding
        if not is_valid_guess(guess, guesses):
            print("invalid guess. Please try again.")
            continue

#if the secret word is guessed correctly then it plays a victory message and the code breaks
        if guess == secret_word:
            print(" Congratulation! You guessed the secret word!")
            break

#provides colour feedback based on the guess
        feedback = evaluate_guess(guess, secret_word)
        print(feedback)

        #moes on to the next attempt
        attempts +=1

#when the player runs out of guesses without guessing the secret word then it plays the losing message
    if attempts >max_attempts:
        print("Game over> The secret word was: " + secret_word)


#Load the words from the files
guesses = load_dictionary("guesses.txt")
answers = load_dictionary("answers.txt")

#This part makes sure that the files are loaded correctly and allows us to double if it is bugged
print(f"Loaded {len(guesses)} guesses. Sample: {guesses[:5]}")
print(f"Loaded {len(answers)} answers. Sample: {answers[:5]}")
print(f"Total guesses loaded: {len(guesses)}")
print(f"First 3: {guesses[:3]}")
print(f"Last 3: {guesses[-3:]}")

#starts the game
wordle(guesses, answers)





