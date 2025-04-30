from .git_command_handler import GitHandler


class RepoManager:
    def __init__(self):
        self.repos = {}
        self.active_repo = ''

    # Makes it active repo
    def add_repo(self, name: str, path: str) -> None:
        self._repos[name] = path
        self._active_repo = name

    def switch_repo(self, name: str) -> bool:
        if name in self._repos.keys():
            self._active_repo = name
            return True
        else:
            return False

    def get_active_repo_path(self) -> str:
        return self._repos.get(self.active_repo)

    def get_active_repo_name(self) -> str:
        return self._active_repo

    def get_active_repo_handler(self) -> GitHandler:
        repo_path = self.get_active_repo_path()
        git_handler = GitHandler(repo_path)
        return git_handler
