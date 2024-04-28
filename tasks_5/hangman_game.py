#!/usr/bin/python3
import random

def choose_word():
    words = ["gamepad", "mouse", "keyboard", "screen", "laptop", "headphones"]
    return random.choice(words)

def display_word(word, guessed_letter):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letter:
            displayed_word += letter
        else:
            displayed_word += "-"

    return displayed_word


def hangman_game():
    word = choose_word()
    guessed_letters = []
    print("the game is on".upper())
    print(display_word(word, guessed_letters))
    while "-" in display_word(word, guessed_letters):
        guess = input("guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("please enter one letter at a time")
            continue
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        if guess not in word:
            print(f"Sorry, {guess} is not in the word.")
        guessed_letters.append(guess)
        print(display_word(word, guessed_letters))
    print("Congratulations, you've guessed the word!")


def main():
    hangman_game()


if __name__ == "__main__":
    main()

