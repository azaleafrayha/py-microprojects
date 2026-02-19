import random
target = random.randint(1, 10) # putting it outside the loop so it only generates once per game (not every time the user wants to play again)

print("Welcome to the Number Guessing Game!")
print("I have selected a random number between 1 and 10. Can you guess it?")

while True:
    n = int(input("Enter your guess: ")) #TODO: ADD ERROR HANDLING   
    
    if n == target: # check the correct one first, then the wrong ones
        print("Aw you guessed it! Wanna try again?")            
    elif n < target:
        print("Haha, too low! Try again if you dare.")        
    elif n > target:
        print("Damn that's too high! Wanna give it another shot?")

    play_again = input("Press Y to play again: ")
    if play_again.strip() == 'Y' or play_again.strip() == 'y':
        continue 
    else:
        print("Alright thanks for playing! Goodbye!")
        break
