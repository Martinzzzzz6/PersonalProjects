import random
import myProjects.cipher_projects.hangman.hangman_word_list as hangman_word_list

print("Welcome to Hangman")
input_difficulty = input("Choose a difficulty: easy, food, animals, geography, colors, mythology: ").lower()

random_word = random.choice(hangman_word_list.word_list[input_difficulty])
word_length = len(random_word)
display = ["_" for _ in range(word_length)]
guessed_letters = set()
print(display)

user_lives = 6

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

while "_" in display and user_lives > 0:
    user_input = input("Guess a letter: ").lower()
    
    if user_input in guessed_letters:
        print("Letter already guessed. ")
        user_lives -= 1
        print(f"You have {user_lives} lives left")
        print(stages[user_lives])
    else:
        guessed_letters.add(user_input)
        if user_input not in random_word:
            print("You guessed wrong")
            user_lives -= 1
            print(f"You have {user_lives} lives left")
            print(stages[user_lives])
            if user_lives == 0:
                print("You lose")
                break
        else:
            counter = 0
            for position in range(word_length):
                letter = random_word[position]
                if letter == user_input:
                    display[position] = letter

        print(display)

if "_" not in display:
    print("You win")
    print(f"The word was {random_word}")