import random






def choose_word():
    words = ["python", "hangman", "programming", "computer", "algorithm", "developer", "code"]
    choosed = random.choice(words)
    return  choosed


#select word



def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display


def hangman():
    print("welcome to hangman! ")
guessed_letters = []
word_to_guess = choose_word()
attempts = 10




while attempts > 0:
    current_display = display_word(word_to_guess, guessed_letters)
    print(current_display)
    guess = input("guess a letter ").lower()
    if guess not in word_to_guess:
        attempts -= 1
        continue
    guessed_letters.append(guess)


if __name__ == "__main__":
    hangman()















# guessed_letters = ""
















# print(word)
# letter = input("enter your letter here ")

# def display(letter ):
#     display_word = ""
#     for i in word:
#         if i == letter:
#             display_word += letter
#         else:
#             display_word += "_"
#     return display_word
    
    
# while display_word != word:
#     letter = input("enter your letter here ")
#     print(display(letter)

