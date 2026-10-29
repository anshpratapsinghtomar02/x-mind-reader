import random


def play_game():
    print("\n" + "=" * 44)
    print("             MIND READER")
    print("             THE NUMBER HUNT")
    print("-" * 44)
    print("                NOT YOUR LIV")
    print("=" * 44)

    secret_number = random.randint(1, 100)
    attempts = 0
    previous_distance = None

    print("\nI'm thinking of a number between 1 and 100.")
    print("Find it using my HOT & COLD hints!")
    print("Let's see if you can read my mind.\n")

    while True:
        try:
            guess = int(input("Enter your guess: "))

            if not 1 <= guess <= 100:
                print("Please guess between 1 and 100.\n")
                continue

            attempts += 1
            distance = abs(secret_number - guess)

            if guess == secret_number:
                print("\nBOOM! YOU CRACKED THE CODE!")
                print(f"The secret number was {secret_number}.")
                print(f"You found it in {attempts} attempts!")

                if attempts <= 3:
                    print("LEGENDARY! Incredible intuition!")
                elif attempts <= 6:
                    print("IMPRESSIVE! Sharp instincts!")
                elif attempts <= 10:
                    print("NICE WORK! Mystery solved!")
                else:
                    print("NEVER GAVE UP! Well done!")

                break

            if guess < secret_number:
                print("\nTOO LOW! Try a bigger number.")
            else:
                print("\nTOO HIGH! Try a smaller number.")

            if distance <= 3:
                print("BURNING HOT! You're extremely close!")
            elif distance <= 7:
                print("HOT! Just a tiny step away!")
            elif distance <= 15:
                print("WARM! You're getting closer!")
            elif distance <= 30:
                print("COLD! Think of another range.")
            else:
                print("FREEZING! You're far from the number!")

            if previous_distance is not None:
                if distance < previous_distance:
                    print("You're getting WARMER! Keep going!")
                elif distance > previous_distance:
                    print("You're getting COLDER! Try another number!")
                else:
                    print("Same distance! Try a different number.")

            previous_distance = distance
            print(f"Attempts so far: {attempts}\n")

        except ValueError:
            print("Invalid input! Please enter a whole number.\n")


def main():
    while True:
        play_game()

        again = input("\nAnother round? (yes/no): ").strip().lower()

        if again not in ("yes", "y"):
            print("\n" + "=" * 44)
            print("       THANKS FOR PLAYING!")
            print("           NOT YOUR LIV")
            print("=" * 44)
            print("Until next time, number hunter!")
            break


if __name__ == "__main__":
    main()
