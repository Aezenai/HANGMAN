import random
print('Input capital letters only')
letter = input('Guess a letter: ')
lines = open("words.txt").read().splitlines()
word = random.choice(lines)
guessed_letters = []
HANGMAN_PICS = ['''
     +---+
         |
         |
         |
        ===''', '''
     +---+
     o   |
         |
         |
        ===''', '''
     +---+
     o   |
     |   |
         |
        ===''', '''
     +---+
     o   |
    /|   |
         |
        ===''', '''
     +---+
     o   |
    /|\  |
         |
        ===''', '''
     +---+
     o   |
    /|\  |
    /    |
        ===''', '''
     +---+
     o   |
    /|\  |
    / \  |
        ===''']



unfinished = '_' * len(word)
incorrect_guesses = 0
word_as_list = list(unfinished)

print(unfinished)
while incorrect_guesses < 7:
  if letter.upper() not in word:
    print(HANGMAN_PICS[incorrect_guesses])
    incorrect_guesses +=1
    guessed_letters.append(letter)
    if incorrect_guesses == 7:
      print('You lose')
    else: letter = input('Guess another letter: ')
  
  elif letter in guessed_letters:
    print('You have already guessed this letter')
    letter = input('Guess another letter: ')
    
  
  else:
    print('Correct guess!')
    indices = [i for i, val in enumerate(word) if val == letter]
    for i in indices:
        word_as_list[i] = letter
    unfinished = ''.join(word_as_list)
    print(unfinished)
    guessed_letters.append(letter)
    letter = input('Guess another letter: ')

if incorrect_guesses < 7:
    print('Congratulations, you have successfully guessed the word!')            
        

  
