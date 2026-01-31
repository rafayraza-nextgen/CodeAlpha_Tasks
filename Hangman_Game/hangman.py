import random

words = [
    "programming",
    "internet",
    "database",
    "software",
    "algorithm"
]

word = random.choice(words)
word_letters = list(word)
guessed_letters = []
display = ["_"] * len(word)
attempts = 6

print("=== Hangman Game ===")
print("Topic: Technology & Real-World Concepts")

while attempts > 0 and "_" in display:
    print("\nWord:", " ".join(display))
    print("Wrong attempts left:", attempts)
    print("Guessed letters:", " ".join(guessed_letters))
    
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter only.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_letters:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
        print("Correct!")
    else:
        attempts -= 1
        print("Incorrect!")

if "_" not in display:
    print("\nYou won! The word was:", word)
else:
    print("\nYou lost! The word was:", word)
