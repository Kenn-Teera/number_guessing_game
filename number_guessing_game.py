import random
import time

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    high_score = float("inf")
    while True:
        print("\nI'm thinking of a number between 1 and 100.")
        
        difficulty_level = choose_difficulty()
        num_chances = difficulty_level["chances"]
        secret_number = random.randint(1, 100)
        
        print(f"You have {num_chances} chances to guess the correct number.")
        
        start_time = time.time()
        num_attempts = 0
        while num_attempts < num_chances:
            guess = get_user_guess()
            num_attempts += 1
            if guess == secret_number:
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(f"Congratulations! You guessed the correct number in {num_attempts} attempts in {elapsed_time:.2f} seconds.")
                
                if num_attempts < high_score:
                    high_score = num_attempts
                    print(f"New high score: {high_score} attempts!")
                break
            elif guess < secret_number:
                print("Incorrect! The number is greater than your guess.")
                provide_hint(secret_number, guess)
            else:
                print("Incorrect! The number is less than your guess.")
                provide_hint(secret_number, guess)
        else:
            print(f"Sorry, you ran out of chances. The number I was thinking of was {secret_number}.")
        
        play_again = input("Would you like to play again? (y/n) ").lower()
        if play_again != "y":
            print(f"Your high score is {high_score} attempts.")
            print("Thanks for playing! Goodbye.")
            break

def choose_difficulty():
    while True:
        print("\nPlease select the difficulty level:")
        print("1. Easy (10 chances)")
        print("2. Medium (5 chances)")
        print("3. Hard (3 chances)")
        
        user_input = input("Enter your choice: ")
        if user_input == "1":
            return {"chances": 10}
        elif user_input == "2":
            return {"chances": 5}
        elif user_input == "3":
            return {"chances": 3}
        else:
            print("Invalid choice. Please try again.")

def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def provide_hint(secret_number, guess):
    difference = abs(secret_number - guess)
    if difference <= 10:
        print("Hint: You're very close!")
    elif difference <= 20:
        print("Hint: You're getting closer!")
    else:
        print("Hint: Your guess is far off the mark.")

if __name__ == "__main__":
    number_guessing_game()
