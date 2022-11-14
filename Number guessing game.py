#Number Guessing Game Objectives:
import random
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

computer_select = random.randint(1, 100)

Repeat = True
while Repeat:

  def game():
    print("This is number guess game.")
    print("It will be fun. Let's goo !!")
    print("Please guess the number/numbers between 1 and 100.\n\n")
    level = input('Enter your level : HARD / EASY\n').lower()
    if level == 'hard':
      i = 5
      for times in range(i):
        print(f"You have {i} chance to guess.")
        Guess = int(input("Enter the number : "))
        if Guess == computer_select:
          print("You win.")
          print(f"The actual number is {computer_select}. And your guessing number is {Guess}.")
          print("Yess you do it !!")
          break
        elif Guess > computer_select:
          print("Too high.") 
          i -= 1 
        elif Guess < computer_select:
          print("Too low.")
          i -= 1

    elif level == 'easy':
      i = 10
      for times in range(i):
        print(f"You have {i} chance to guess.")
        Guess = int(input("Enter the number : "))
        if Guess == computer_select:
          clearConsole()
          print("You win.")
          print(f"The actual number is {computer_select}. And your guessing number is {Guess}.")
          print("Yess you do it !!")
          break
        elif Guess > computer_select:
          print("Too high.") 
          i -= 1 
        elif Guess < computer_select:
          print("Too low.")
          i -= 1

    else:
      clearConsole()
      print("You enter a worng input.\n\n") 
      
  game()      

  Ask = input("Are you want play again : YES / NO\n").lower()
  if Ask == 'yes':
    clearConsole()
    game()  
  else:
    Repeat = False
    clearConsole()
    print("Good Bye !!")
    print("Please Visit Again !!")  