## create a simple number question game
# the user get 10 chances to guess a number.
# if the user guesses the number before 10 chances , stop asking the number from the user, say congrats and end the game
# if the user never guesses the number, ask them 10 time then end the game
import random

welcome_message=("Welcome to the number guessing game. we have a number that needs to be guessed. you have ten chances. \nThe Secret number is between 1-50. ")
welcome_message=welcome_message.title()
print(welcome_message)
num=1
Secret_number= random.randint(1,51)
attempts=5
attempts_exhausted=False
while num <= 5:
    print(f"you have {attempts} attempts left")
    Guess=int(input("Enter your Guess Value  between 1-50:"))
    if Guess==Secret_number:
        print(f"Congrats!, You guessed the correct number.\nCorrect number is {Secret_number}")
        attempts_exhausted = True
        break
    else:
        if Guess>Secret_number:
            Higher_or_lower="lower"
        else:
            Higher_or_lower="higher"
        print(f"Your Guess is Wrong. try {Higher_or_lower} number ")

    num+=1
    attempts-=1
if attempts_exhausted == False:
    print("Bad luck! You exhausted all your attempts and couldn't guess the number. ")
print(f"The Secret number was {Secret_number}. Game over!")
