import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

print(f"There are {word_length} letters.")
print(f"{' '.join(display)} \n\n")

past_guesses = []

while not end_of_game:
    guess = input(">> Guess a letter: ").lower()

    if guess in past_guesses:
      print(f"You've already tried {guess} before, try another one. \n")
    else:
      past_guesses.append(guess)
      
      #Check guessed letter
      for position in range(word_length):
          letter = chosen_word[position]
          if letter == guess:
              display[position] = letter
  
      #Check if user is wrong.
      if guess not in chosen_word:
          print(f"Oops, {guess} is not in the word. \n")
          lives -= 1
          if lives == 0:
              end_of_game = True
              print(f"The word was {chosen_word}. You lose.")
  
      #Join all the elements in the list and turn it into a String.
      print(f"{' '.join(display)}")
  
      #Check if user has got all letters.
      if "_" not in display:
          end_of_game = True
          print("You win.")
  
      print(hangman_art.stages[lives])