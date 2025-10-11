import random

def guess_game():
    number = random.randint(1, 50)
    attempts = 0
    
    print("Guess the number (1-50)")
    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1
            
            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(f"Correct! You won in {attempts} attempts!")
                break
        except:
            print("Enter a valid number!")

def dice_roll():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    
    print(f"Dice 1: {dice1}")
    print(f"Dice 2: {dice2}")
    print(f"Total: {total}")
    
    if dice1 == dice2:
        print("Double!")
    if total == 7:
        print("Lucky 7!")

def quick_math():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    op = random.choice(['+', '-', '*'])
    
    if op == '+':
        answer = a + b
    elif op == '-':
        answer = a - b
    else:
        answer = a * b
    
    user_answer = int(input(f"What is {a} {op} {b}? "))
    
    if user_answer == answer:
        print("Correct!")
    else:
        print(f"Wrong! Answer: {answer}")

def main():
    while True:
        print("\n1. Guess Game")
        print("2. Dice Roll")
        print("3. Quick Math")
        print("4. Exit")
        
        choice = input("Choose: ")
        
        if choice == '1':
            guess_game()
        elif choice == '2':
            dice_roll()
        elif choice == '3':
            quick_math()
        elif choice == '4':
            print("Bye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()