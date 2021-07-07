import random
from . import Answer
from ...bot.tools import symbols


class QuestionsAnswers:
    __slots__ = ('questions', 'answers')  # Has 2 attributes.

    def __init__(self, questions: dict, commands: tuple) -> None:
        self.questions, self.answers = self._validate(questions, commands)

    def __repr__(self) -> str:
        return '\n'.join(f"• Questions: {question}?\n - {answer.command:>6}: {answer.answers}." for question, answer in self.answers.items())

    @staticmethod
    def _validate(data: dict, commands: tuple) -> tuple[list[str], dict[str, Answer]]:
        """- Asserts all questions has valid command."""

        questions, answers = list(), dict()

        # Check every question & action, if command exist append to questions else exit, finally return validated questions.
        try:
            for question in data:
                questions.append(question['question'])
                if (command := question['command']) in commands:
                    answers[question['question']] = Answer(command, tuple(question['answers']))
                else:
                    raise ValueError(f"• Question: ('{question}') has unknown command: ('{command}') {symbols.wrong}\n  • Valid commands: {commands} {symbols.right}")
            return questions, answers
        except ValueError as error:
            exit(error)
        except Exception:
            exit(f"• Wrong questions format. {symbols.wrong}")

    def get_question(self, question_element) -> str:
        """Takes a Selenium Web Element (Question Element), and searches for the matching question~ in the questions list."""
        for question in self.questions:
            if question in question_element.text:
                self.questions.remove(question)
                return question

    def get_answer(self, question) -> str:
        """Takes a question and returns one random answer from its corresponding answers."""
        answers = self.answers[question].answers
        self.answers.pop(question)
        return random.choice(answers)

    def get_question_answer(self, question_element) -> tuple[str, str]:
        """Takes a Question Element, and returns it's question as well as its corresponding answers."""
        return (question := self.get_question(question_element)), self.get_answer(question)

    def get_questions(self, question_elements):
        """Takes a a list of Question Elements, and yields their questions one at a time."""
        for question_element in question_elements:
            yield self.get_question(question_element)

    def get_questions_answers(self, question_elements):
        """Takes a list of Question Elements, and yields their questions as well as their corresponding answers."""
        for question_element in question_elements:
            yield self.get_question_answer(question_element)