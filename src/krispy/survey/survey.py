import re
from typing import ValuesView

from .receipt import Receipt
from ..bot.data import SURVEY_DATA
from ..bot.tools import Log, symbols
from .questions import QuestionsAnswers


class Survey:
    """Loads and preparse Survey data"""

    __slots__ = ('url', 'data', 'receipt', 'answers')

    URL_REGEX = re.compile(
        r'^(?:http)s?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    def __init__(self, url: str, receipt: str, answers: str) -> None:

        # if not re.match(self.URL_REGEX, url):
        # else:
        #     raise ValueError("url")
        self.url = url

        self.data = SURVEY_DATA
        self.receipt = Receipt(receipt)
        self.answers = QuestionsAnswers(answers, self.data.keys())
