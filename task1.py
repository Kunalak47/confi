import random

secret_number = random.randint(1, 100) 
guesses_left = 7

print("I'm thinking of a number between 1 and 100.")

while guesses_left > 0:
  print(f"You have {guesses_left} guesses left.")
  guess = int(input("Your guess: "))

  if guess == secret_number:
    print("Congratulations! You guessed it!")
    break # End the loop
  elif guess < secret_number:
    print("Too low!")
  else:
    print("Too high!")

  guesses_left -= 1 

if guesses_left == 0:
  print(f"You're out of guesses! The number was {secret_number}") 