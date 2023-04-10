def main_menu():
    print("Welcome to the Game Menu!")
    print("1. Start Game")
    print("2. Load Game")
    print("3. Quit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        start_game()
    elif choice == "2":
        load_game()
    elif choice == "3":
        quit_game()
    else:
        print("Invalid choice. Please try again.")
        main_menu()

def start_game():
    print("Starting new game...")
    # Add your code for starting a new game here
    print("Game started!")
    main_menu()

def load_game():
    print("Loading game...")
    # Add your code for loading a game here
    print("Game loaded!")
    main_menu()

def quit_game():
    print("Exiting game...")
    exit()

if __name__ == '__main__':
    main_menu()
