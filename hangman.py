import random

print("===================================")
print("      WORD GUESSING GAME")
print("===================================")


words = ["python", "coding", "program", "developer", "computer"]
word = random.choice(words)


pattern = ""
for i in range(len(word)):
    if i % 2 == 0:
        pattern += word[i]
    else:
        pattern += "_"

attempts = 3

print("\nGuess the word:")
print("Word:", pattern)

while attempts > 0:
    guess = input("\nEnter the full word: ").lower()

    if guess == word:
        print("\n🎉 Correct! You guessed the word!")
        break
    else:
        attempts -= 1
        print("❌ Wrong guess!")
        print("Attempts left:", attempts)

if attempts == 0:
    print("\n💀 Game Over!")
    print("The correct word was:", word)
  break

print("\n==============================")
print("Game Finished!")
print("Your Score:", score, "/", len(words))
print("==============================")
