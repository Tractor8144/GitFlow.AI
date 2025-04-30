from repo_manager import RepoManager
from git_command_handler import GitHandler
from git_router import GitCommandRouter
from logger import Logger


class ActionDispatcher:

    def __init__(self, repo_manager: RepoManager):
        self.repo_manager = repo_manager
        self.logger = Logger()
        self.git_actions = {"add_all", "commit", "pull", "push",
                            "create_branch", "checkout_branch"}
        self.repo_actions = {"add_repo", "switch_repo", "get_active_repo"}

    def dispatch(self, action_list: list) -> None:
        for action in action_list:
            action_name = action.get('action')
            if action_name in self.git_actions:
                self._handle_git_action(action)
            elif action_name in self.repo_actions:
                self._handle_repo_action(action)
            else:
                self.logger.warning(f"Sorry, do not understand {action_name}")
                raise ValueError(f"Unknown action received: {action_name}")

    def _handle_repo_action(self, action: dict):
        action_name = action.get('action')
        if action_name == 'add_repo':
            params = action.get('params')
            self.repo_manager.add_repo(params.get(
                'repo_name'), params.get('repo_path'))
        elif action_name == 'switch_repo':
            params = action.get('params')
            success = self.repo_manager.switch_repo(params.get('repo_name'))
            if not success:
                self.logger.error(
                    f'repo named {params.get('repo_name')} not found')
                raise ValueError(
                    f'repo named {params.get('repo_name')} not found')
        elif action_name == 'get_active_repo':
            repo_name = self.repo_manager.get_active_repo_name()
            if repo_name == '':
                self.logger.warning('No known repos yet')
                raise ValueError('No known repos yet')

    def _handle_git_action(self, action: dict):
        git_handler = self.repo_manager.get_active_repo_handler()
        git_router = GitCommandRouter(git_handler)
        git_router.route(action)
