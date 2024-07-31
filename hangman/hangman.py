import random
from words import words

print(words)



def get_valid_word(words):
    word = random.choice(words) #randomlly chooses something from the list

    while '-' in word or '' in word:
        word = random.choice(words)
    return word

def hangman():
    word  = get_valid_words(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letter = set() # what the user has guessed

    while len(word_letters) > 0:
        #letters used
        print('You have used these letters: ', ' '.join(used_letter))

        # what current word is (ie W - R D)
        word_list = [letter if letter in usedchat]
        user_letter = input('Guess a letter: ').upper()
        if user_letter in word_letters:
            word_letters.remove(user_letter)
        elif user_letter in user_letters:
            print("You have already used that character. Please try again.")
        
        else:
            print("You didnt type a valid character.")


user_input = input('Type something')
print(user_input)