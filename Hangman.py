import random
import tkinter as tk

root = tk.Tk()

# Create a label to display the current word
word_label = tk.Label(root, text='Current word:')
word_label.pack()

# Create a label to display the letters that have been guessed
letters_guessed_label = tk.Label(root, text='Letters guessed:')
letters_guessed_label.pack()

# Create a label to display the number of guesses remaining
guesses_remaining_label = tk.Label(root, text='Guesses remaining:')
guesses_remaining_label.pack()

# Create a text entry box for the player to enter a letter
letter_entry = tk.Entry(root)
letter_entry.pack()

# Create a button for the player to submit their guess
guess_button = tk.Button(root, text='Guess')
guess_button.pack()


# Choose a word for the player to guess
words = ['apple', 'avacado', 'banana', 'blackberries', 'blueberry', 'cherry', 'cranberry', 'grape', 'grapefruit',
 'kiwi', 'mango', 'melon', 'nectarine', 'peach', 'pear', 'papaya', 'plantain', 'raspberry', 'fig', 'plantain', 'plantain', 'orange', 'strawberry']
word = random.choice(words)

# Initialize variables to track the game state
guesses_remaining = 6
letters_guessed = []

while True:
  # Display the current state of the word with unguessed letters replaced by underscores
  current_word = ''
  for letter in word:
    if letter in letters_guessed:
      current_word += letter
    else:
      current_word += '_'

  # Print the current word, the letters that have been guessed, and the number of guesses remaining
  print(f'Current word: {current_word}')
  print(f'Letters guessed: {", ".join(letters_guessed)}')
  print(f'Guesses remaining: {guesses_remaining}')

  # Prompt the player to enter a letter
  letter = input('Enter a letter: ')

  # Check if the letter is in the word
  if letter in word:
    letters_guessed.append(letter)
  else:
    guesses_remaining -= 1

  # Check if the player has won or lost
  if guesses_remaining == 0:
    print('You lost! The word was:', word)
    break
  elif all(letter in letters_guessed for letter in word):
    print('You won! The word was:', word)
    break
 
