from .git_command_handler import GitHandler
from .logger import Logger
import os


class RepoManager:
    def __init__(self):
        self._repos = {}
        self._active_repo = ''
        self.logger = Logger()

    # Makes it active repo
    def add_repo(self, name: str, path: str) -> None:
        if not name or name == '':
            name = os.path.basename(path)
            self.logger.info(f'Feel free to refer to your repo by {name}')
        if name in self._repos.keys() and self._repos.get(name) != path:
            self.logger.info(f'path to repo {name} changed!')
        self._repos[name] = path
        self._active_repo = name

    def switch_repo(self, name: str) -> bool:
        if name in self._repos.keys():
            self._active_repo = name
            return True
        else:
            return False

    def get_active_repo_path(self) -> str:
        return self._repos.get(self._active_repo)

    def get_active_repo_name(self) -> str:
        return self._active_repo

    def get_active_repo_handler(self) -> GitHandler:
        repo_path = self.get_active_repo_path()
        if repo_path == None or repo_path == '':
            raise NotADirectoryError('No known repo found')
        git_handler = GitHandler(repo_path)
        return git_handler
