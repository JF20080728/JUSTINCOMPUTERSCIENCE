def main():
    answer = random.choice(words)
    answer_lower = answer.lower()  # lowercase version for logic
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Guess a letter: ").lower()

        # Prevent multiple letters or numbers
        if len(guess) != 1 or not guess.isalpha():
            print("Sorry, that's not a single letter.")
            continue

        # Check for already guessed letters
        if guess in guessed_letters:
            print(f"{guess} was already guessed so far.")
            continue

        guessed_letters.add(guess)

        # Check if the guess is in the answer (case-insensitive)
        if guess in answer_lower:
            for i in range(len(answer)):
                if answer_lower[i] == guess:
                    hint[i] = answer[i]  # Preserve original casing
        else:
            wrong_guesses += 1

        # Win condition
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("Congratulations, you guessed the word!")
            is_running = False

        # Loss condition
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOST THE GAME! TRY AGAIN LATER!!! ")
            is_running = False
