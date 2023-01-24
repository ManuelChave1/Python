print("Welcome to the World Game challenge!!!")
print("You have three chances do got it, so Good Look!!")
print()
secret_word = "Manuel Chave"
guess = ""
attempt = 3

while guess != secret_word and attempt >= 1:
    attempt -= 1
    guess = input("What is your Guess?: ")
    if attempt == 1:
        print("You still have " + str(attempt) + " attept")
    elif attempt == 0:
        print("You have no more attempts!")
    else:
        print("You still have " + str(attempt) + " attepts")

if guess == secret_word:
    print("Congratulations!!! You win!")
else:
    print("You lose! try one more time")