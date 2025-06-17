# START
### wordle game
FUNCTION load_dictionary(file_path)
OPEN the file at file_path
FOR each line in the file
IF line is not empty
CONVERT line to lowercase and add to a list
RETURN the list of words
END FUNCTION
FUNCTION is_valid_guess(guess, guesses_list)
RETURN True if guess is 5 letters long AND exists in guesses_list
ELSE return False
END FUNCTION
FUNCTION evaluate_guess(guess, secret_word)
SET result to an empty string
FOR i from 0 to 4
IF guess[i] == secret_word[i]
ADD green-colored letter to result
ELSE IF guess[i] is in secret_word
ADD yellow-colored letter to result
ELSE
ADD normal-colored letter to result
RETURN result with color reset
END FUNCTION
FUNCTION wordle_game(guesses_list, answers_list)
DISPLAY "Welcome to Wordle! Get 6 chances to guess a secret word"
CHOOSE a random word from answers_list as secret_word
SET attempts to 1
SET max_attempts to 6
WHILE attempts ≤ max_attempts
PROMPT user to enter a guess
CONVERT guess to lowercase
IF guess is not valid using is_valid_guess 
DISPLAY "Invalid guess. Please try again." 
CONTINUE to next iteration
IF guess == secret_word 
DISPLAY "Congratulations! You guessed the secret word!" 
BREAK loop
CALL evaluate_guess with guess and secret_word 
DISPLAY the feedback with color coding
INCREMENT attempts
 IF attempts > max_attempts
DISPLAY "Game over. The secret word was: " + secret_word
END FUNCTION
MAIN PROGRAM
LOAD guesses from "guesses.txt" using load_dictionary 
LOAD answers from "answers.txt" using load_dictionary 
PRINT sample data to verify loading 
CALL wordle_game with guesses and answers
END
