from git import Repo
from gitflow_ai.git_command_handler import GitHandler
from gitflow_ai.git_router import GitCommandRouter
from gitflow_ai.test_nlp_parser import TestNLPParser
from gitflow_ai.input_manager import InputManager
from gitflow_ai.openai_client import OpenAIClient
from gitflow_ai.nlp_parser import NLPParser
import sys


def main():
    print("Welcome to GitFlow.AI")

    input_manager = InputManager()
    repo = Repo("D:\\Projects\\FastAPI_Basic\\FastAPI-Basic")
    git_handler = GitHandler(repo)
    router = GitCommandRouter(git_handler)
    # parser = TestNLPParser()
    openai = OpenAIClient()
    parser = NLPParser(openai)

    while True:
        user_input = input_manager.get_input()
        if user_input in ['quit', 'exit', 'bye', 'see you later']:
            print("Quitting GitFlow.AI. Goodbye!")
            sys.exit(0)
        print(f'You asked command {user_input}')
        try:
            action_list = parser.parse(user_input)
        except:
            print("Sorry! Could not understand the message. Please try again!")
            continue
        router.route_list(action_list)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Quitting GitFlow.AI. Goodbye!")
        sys.exit(0)
