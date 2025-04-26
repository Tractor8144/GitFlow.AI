from gitflow_ai.input_manager import InputManager
import sys

def main():
    print("Welcome to GitFlow.AI")

    input_manager = InputManager()

    while True:
        user_input = input_manager.get_input()
        if user_input in ['quit', 'exit', 'bye', 'see you later']:
            print("Quitting GitFlow.AI. Goodbye!")
            sys.exit(0)
            break
        print(f'You asked command {user_input}')


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Quitting GitFlow.AI. Goodbye!")
        sys.exit(0)