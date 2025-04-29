# # # # # # Schema for NLP Parser output expected
# # # {
# # #     "action": "<action_name>",  # e.g., "create_branch", "commit", "push", "pull"
# # #     "params": {
# # #         # Key-value pairs specific to the action
# # #     },
# # #     "raw_input": "<original user command>"  # Optional, for debugging/logging
# # # }

# # # List of action dictionries
# # # [
# # #     {
# # #         "action": "create_branch",
# # #         "params": {"branch_name": "feature/login"},
# # #         "raw_input": "Create branch feature/login"
# # #     },
# # #     {
# # #         "action": "push",
# # #         "params": {"remote_name": "origin"},
# # #         "raw_input": "Push to origin"
# # #     }
# # # ]


# actions to support
# 1. add_all
# 2. commit
# 3. get_branch
# 4. create_branch
# 5. checkout_branch
# 6. pull
# 7. push

from .git_command_handler import GitHandler
from .logger import Logger


class GitCommandRouter:
    def __init__(self, git_handler: GitHandler):
        self.git = git_handler
        self.actions = {
            'add_all': git_handler.add_all,
            'commit': git_handler.commit,
            'get_branch': git_handler.get_branch,
            'create_branch': git_handler.create_branch,
            'checkout_branch': git_handler.checkout_branch,
            'pull': git_handler.pull,
            'push': git_handler.push
        }
        self.logger = Logger()

    def route(self, action_dict: dict) -> None:
        if 'action' not in action_dict:
            self.logger.error('Unable to understand command, daddy!')
            return

        action = action_dict['action']
        handler = self.actions.get(action)

        if handler:
            params = action_dict.get('params', {})
            self.logger.info(f"Performing {action}!!")
            try:
                handler(**params)
            except TypeError:
                self.logger.error(
                    f"Missing or invalid parameters for {action}")
            self.logger.info(f"Successfully finished performing {action}")
        else:
            self.logger.error(
                f"Something went wrong performing action {action}")

    def route_list(self, action_list: list) -> None:
        for action_dict in action_list:
            self.route(action_dict)
