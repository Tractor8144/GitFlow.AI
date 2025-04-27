# test_nlp_parser.py

class TestNLPParser:
    """
    A minimal NLP parser for testing purposes.
    Takes natural language input and returns
    a list of action dictionaries.
    """

    def parse(self, input_text: str) -> list:
        input_text = input_text.strip().lower()

        if "create branch" in input_text or "new branch" in input_text:
            return [
                {
                    "action": "create_branch",
                    "params": {"branch_name": "feature/test_branch"},
                    "raw_input": input_text
                }
            ]
        elif "commit" in input_text:
            return [
                {
                    "action": "add_all",
                    "params": {},
                    "raw_input": "Stage all changes"
                },
                {
                    "action": "commit",
                    "params": {"message": "Test commit message"},
                    "raw_input": input_text
                }
            ]
        elif "push" in input_text:
            return [
                {
                    "action": "push",
                    "params": {"remote_name": "origin"},
                    "raw_input": input_text
                }
            ]
        elif "pull" in input_text:
            return [
                {
                    "action": "pull",
                    "params": {"remote_name": "origin"},
                    "raw_input": input_text
                }
            ]
        else:
            # If no known command matched
            return [
                {
                    "action": "unknown",
                    "params": {},
                    "raw_input": input_text
                }
            ]
