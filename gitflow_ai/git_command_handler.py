from git import Repo, GitCommandError
from git import Remote
from .logger import Logger


class GitHandler:

    def __init__(self, repo: Repo = None):
        if not repo:
            self.repo = Repo()
        else:
            self.repo = repo
        self.logger = Logger()

    def add_all(self):
        self.repo.git.add(A=True)

    def commit(self, message: str) -> None:
        self.repo.index.commit(message=message)

    def get_branch(self) -> str:
        try:
            return self.repo.active_branch.name
        except TypeError:
            return "DETACHED"

    def create_branch(self, branch_name: str = 'new_branch') -> bool:
        try:
            self.repo.git.checkout('-b', branch_name)
            return True
        except GitCommandError:
            self.repo.git.checkout(branch_name)
            return False

    def checkout_branch(self, branch_name: str) -> bool:
        try:
            self.repo.git.checkout(branch_name)
            return True
        except GitCommandError:
            self.repo.git.checkout('-b', branch_name)
            return False

    # def status(self) -> str:
    #     pass

    # def log(self) -> str:
    #     pass

    def pull(self, remote_name: str) -> bool:
        try:
            remote = self.repo.remote(name=remote_name)
            remote.pull()
            return True
        except GitCommandError:
            return False

    def push(self, remote_name: str) -> bool:
        try:
            remote = self.repo.remote(name=remote_name)
            remote.push()
            return True
        except GitCommandError:
            return False


# repo = Repo("D:\\Projects\\FastAPI_Basic\\FastAPI-Basic")
# git_handler = GitHandler(repo)
# git_handler.checkout_branch('main')
# git_handler.add_all()
# git_handler.commit('Committed using GitPython')
# git_handler.pull('origin')
# git_handler.push('origin')
