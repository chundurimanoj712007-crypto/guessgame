import random

print("🎮 NUMBER GUESSING GAME")
print("Guess the number between 1 and 100")
print("You have 7 attempts!")

while True:

    number = random.randint(1, 100)
    attempts = 7
    score = 100

    while attempts > 0:

        try:
            guess = int(input("\nEnter your guess: "))
        except ValueError:
            print("❌ Please enter a valid number!")
            continue

        if guess < 1 or guess > 100:
            print("⚠️ Enter a number between 1 and 100.")
            continue

        attempts -= 1

        if guess == number:
            print("🎉 Congratulations! You guessed the number!")
            print("🏆 Your score:", score)
            break

        elif guess < number:
            print("📈 Too low!")

        else:
            print("📉 Too high!")

        if abs(number - guess) <= 10:
            print("💡 Hint: You are very close!")

        score -= 10

        print("Attempts remaining:", attempts)

    if guess != number:
        print("\n💀 Game Over!")
        print("The correct number was:", number)

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("👋 Thanks for playing!")
        break