class Answer:
    __slots__ = ('command', 'answers') # Has 2 attributes.

    def __init__(self, command: str, answers: tuple) -> None:
        self.command, self.answers = command, answers

    def __repr__(self): return f"{{{self.command}: {self.answers.__repr__()}}}"
