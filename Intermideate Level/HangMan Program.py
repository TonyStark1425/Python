# Hangman in Python

from wordlist import words
import random


#dictionary of key:()
hangman_art = {0:("   ",
                  "   ",
                  "   "),
               1:(" o ",
                  "   ",
                  "   "),
               2:(" o  ",
                  " |  ",
                  "   "),
               3:("  o  ",
                  " /|  ",
                  "   "),
               4:("  o ",
                  " /|\\ ",
                  "   "),
               5:("  o ",
                  " /|\\ ",
                  " / "),
               6:("  o ",
                  " /|\\ ",
                  " / \\ ")}

def display_man(wrong_gusses):
    print("**********")
    for line in hangman_art[wrong_gusses]:
        print(line)
    print("**********")
def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_gusses = 0
    gussed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_gusses)
        display_hint(hint)
        guess = input("Enter a letter (of Bollywood Movie): ").lower().title()

        # if len(guess) != 1 or not guess.isalpha():
        if len(guess) != 1 :
            print("Invalid input")
            continue

        if guess in gussed_letters:
            print(f"{guess} is already guessed")
            continue

        gussed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_gusses += 1
        if"_" not in hint:
            display_man(wrong_gusses)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False

        elif wrong_gusses >= len(hangman_art) - 1:
            display_man(wrong_gusses)
            display_answer(answer)
            print("YOU LOSE!")
            is_running = False

if __name__ == "__main__":
    main()