# Components 
- InputManager: Captures raw CLI input.
- NLPParser: Converts input text into structured Python dict.
- CommandDispatcher: Orchestrates actions to the correct domain router.
- Routers: Forward specific action requests to handlers.
- Handlers: Actually execute Git/Jira/Bitbucket operations.

---

# Component Responsibility Summary

## 1. InputManager
- Captures CLI input as string.
- Forwards input to NLPParser.
- No parsing, no AI communication.

## 2. NLPParser
- Parses input text into a Python `dict` of actions.
- Communicates with GPT-3.5 or local LLM.
- Hides all AI/API complexity from other modules.

## 3. CommandDispatcher
- Receives parsed action dict.
- Orchestrates correct routing to appropriate domain routers.
- Ensures each action is delegated cleanly.

## 4. GitCommandRouter
- Receives Git-specific actions.
- Routes them to GitCommandHandler.
- Translates general intents into Git-specific methods.

## 5. GitCommandHandler
- Encapsulates Git operations via GitPython.
- Executes git actions atomically and safely.
- Cleanly separates API logic from orchestration logic.

---

# Future Scope

| System Extension | Purpose |
|------------------|---------|
| JiraCommandRouter | Manage Jira issue comments, time logs, transitions |
| BitbucketCommandRouter | Manage Bitbucket PRs, link commits to issues |
| Dockerized Deployment | Portable, containerized CLI tool |
| Web UI Interface | Optional graphical interface with Streamlit |


---

# Technologies Used

| Tech | Purpose |
|-----|---------|
| Python 3.11 | Core programming language |
| GitPython | Git API management |
| OpenAI API | GPT-3.5 command parsing (NLP) |
| dotenv | Secure API credential loading |
