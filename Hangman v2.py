import random
import tkinter as tk

root = tk.Tk()
# Sets a resolution for the window
root.geometry('800x600+100+100')

#Adding a Headline to the GUI
headline_label = tk.Label(root, text='Hangman Game', font=('Arial', 36, 'bold'))
headline_label.pack()

canvas = tk.Canvas(root, width=200, height=200)

# Draw the hangman stand
canvas.create_line(50, 200, 150, 200, width=2)
canvas.create_line(100, 200, 100, 50, width=2)
canvas.create_line(100, 50, 200, 50, width=2)

# Pack the canvas widget
canvas.pack()

# Create a label to display the current word
word_label = tk.Label(root, text='Current word:', font=('Arial', 24, 'bold italic'))
word_label.pack()

# Create a label to display the letters that have been guessed
letters_guessed_label = tk.Label(root, text='Letters guessed:', font=('Arial', 20))
letters_guessed_label.pack()

# Create a label to display the number of guesses remaining
guesses_remaining_label = tk.Label(root, text='Guesses remaining:', font=('Arial', 20))
guesses_remaining_label.pack()

# Create a text entry box for the player to enter a letter
letter_entry = tk.Entry(root)
letter_entry.pack()

# Create a button for the player to submit their guess
guess_button = tk.Button(root, text='Guess')

# Choose a word for the player to guess
words = ['apple', 'avacado', 'banana', 'blackberries', 'blueberry', 'cherry', 'cranberry', 'grape', 'grapefruit',
 'kiwi', 'mango', 'melon', 'nectarine', 'peach', 'pear', 'papaya', 'plantain', 'raspberry', 'fig', 'orange', 'strawberry']
word = random.choice(words)

# Initialize variables to track the game state
guesses_remaining = 6
letters_guessed = []

def guess():
  global guesses_remaining
  
  # Read the letter that the player entered
  letter = letter_entry.get()
  
  if not letter.isalpha() or len(letter) != 1:
      
# Display an error message to the player
    tk.Label(root, text='Please enter a single letter.', font=('Arial', 8)).pack()
  elif letter in letters_guessed:
      
# Display an error message to the player
    tk.Label(root, text='You have already guessed that letter! Please enter a different letter.', font=('Arial', 8)).pack()
  else:
      
# Check if the letter is in the word and update the game state
    if letter in word:
        letters_guessed.append(letter)
    else:
        guesses_remaining -= 1
        
# Add the letter to the list of letters guessed
    letters_guessed.append(letter)
    
# Display the current state of the word with unguessed letters replaced by underscores
  current_word = ''
  for letter in word:
    if letter in letters_guessed:
      current_word += letter
    else:
      current_word += '_'
    current_word += ' '

# Update the labels with the current game state
  word_label.config(text=f'Current word: {current_word}')
  letters_guessed_label.config(text=f'Letters guessed: {", ".join(letters_guessed)}')
  guesses_remaining_label.config(text=f'Guesses remaining: {guesses_remaining}')

# Check if the player has won or lost
  if guesses_remaining == 0:
    tk.Label(root, text='You lost! The word was:', font=('Arial', 24)).pack()
    # Display the word
    tk.Label(root, text=word, font=('Arial', 24)).pack()
  elif all(letter in letters_guessed for letter in word):
    tk.Label(root, text='You won! The word was:', font=('Arial', 24)).pack()

# Bind the guess function to the guess_button widget
guess_button.config(command=guess)
guess_button.pack()

# Start the Tkinter event loop
root.mainloop()
