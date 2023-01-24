print('Welcome to the Word guessing Game')
print()
secret_word = "Manuel Chave"
guess = ""
guess_count = 0

while guess != secret_word and guess_count != secret_word:
   
    guess = input("What is your Guess?: ")
    if guess != secret_word:
             print("Your Guess was not correct!")
    guess_count += 1
    
if guess == secret_word:
    print("Congratulations! you guessed it")
    print(f"It took you {guess_count} Guesses!")
	    
print("Thanks to play")