if __name__ == '__main__':
    exit("This module is meant to be imported.")

from ..survey import Survey
from .tools import Log, symbols, Colors as Clr
from .functionalities import Functionalities, By, Exceptions

import re
import time
import datetime


class Bot(Functionalities):
    """## Krispy Kreme Bot."""

    def __init__(self, url: str, receipt: str, answers: str, browser: str = 'firefox', host: str = 'localhost', port: int = '4444', assets: str = '/tmp/assets') -> None:
        self.duration = time.time()
        self.duration_temp = self.duration
        self.browser = browser
        self.assets_location = assets if assets[-1] == '/' else f'{assets}/'
        self.code: str = ""
        self.log = Log()
        self.page = 1

        print(f"\nValidating Survey Data... {symbols.waiting}")
        # Load Survey data.
        self.survey = Survey(url, receipt, answers)
        self.print_time()

        print(f"\nRequesting Web Session... {symbols.waiting}")
        # Create Browser Session.

        self.create_session(host, port)
        self.print_time()

    def finish_survey(self):

        duration = time.time()

        try:
            self.open_survey()
            self.assert_english()
            self.fill_receipt_info()
            self.fill_survey()

        except Exceptions.NoSuchWindowException:
            exit(
                f"\nNoSuchWindowException: Browser {Clr.c(Clr.BOLD, self.browser)} closed {symbols.wrong}")
        else:
            self.save_screenshot('Code.png')
            print(
                f"\n{Clr.c((Clr.BOLD, Clr.UNDERLINE, Clr.GREEN), 'Validation Code:')}", end='')
            print(f" {Clr.c((Clr.BOLD, Clr.BLUE), self.code)}.")
            # Print the time taken.
            print(
                f"\nSurvey finished in: {Clr.c(Clr.BOLD, f'{time.time() - duration:.2f}')} seconds.")
        finally:
            try:
                self.quit()
            except Exceptions.WebDriverException:
                pass

    def open_survey(self) -> None:
        print(f"\nNavigating to '{self.survey.url}'... {symbols.waiting}")

        # Log.title(f"Navigating to '{self.survey.url}'")
        self.navigate_to(self.survey.url)
        # Log.doing('Page Loading')
        self.wait_loading(self.survey.data['survey']['content'])
        # Log.done()

        self.print_time()

    def assert_english(self) -> None:
        # Log.doing('Page language')
        self.click_element(self.survey.data['survey']['language'])
        # Log.done('English')

    def fill_receipt_info(self):

        # @Log.completed('Store Number', self.survey.receipt.number)
        def fill_store_number() -> None:
            Log.doing('Store Number')

            self.get_element(self.survey.data['receipt']['answers']['number']['input']).send_keys(
                self.survey.receipt.number)

            Log.done(self.survey.receipt.number)

        # @Log.completed('Date', self.survey.receipt.date)
        def fill_date() -> None:
            page_month = None
            survey_day = str(self.survey.receipt.date.day)
            try:
                page_month = self.get_element_text(
                    self.survey.data['receipt']['answers']['date']['month'])
            except Exception:
                self.click_element(
                    self.survey.data['receipt']['answers']['date']['input'])
                try:
                    page_month = self.get_element_text(
                        self.survey.data['receipt']['answers']['date']['month'])
                except Exception:
                    exit(f" {symbols.wrong}")

            if page_month != datetime.date(1, int(self.survey.receipt.date.month), 1).strftime('%B'):
                self.click_element(
                    self.survey.data['receipt']['answers']['date']['prev'])

            for day_element in self.get_elements(self.survey.data['receipt']['answers']['date']['day']):
                if day_element.text == survey_day:
                    return day_element.click()
            try:
                self.click_element(survey_day, By.LINK_TEXT)
            except Exception:
                exit(f" {symbols.wrong}")

        # @Log.completed('Time', self.survey.receipt.time)
        def fill_time() -> None:
            self.click_element(
                self.survey.data['receipt']['questions']['time'])
            for time_input_element in self.survey.data['receipt']['answers']['time'].keys():
                self.select_element(self.survey.data['receipt']['answers']['time'][time_input_element], (
                    self.survey.receipt.time, time_input_element))

        self.adjust_window()

        print(
            f"\nFilling Receipt Info '{self.survey.url}'... {symbols.waiting}")

        for receipt_info in (fill_store_number, fill_date, fill_time):
            receipt_info()

    def fill_survey(self) -> None:
        """Complete the survey and return the code."""

        def next_page():

            self.print_time()

            try:
                self.save_screenshot(f'Page_{self.page:0>2}.png')

                self.click_element(self.survey.data['survey']['next'])

                self.page += 1
                print(f"\nPage {self.page}... {symbols.waiting}")

                self.wait_loading(self.survey.data['survey']['content'])

                if error_element := self.get_element_if_exists(self.survey.data['survey']['error']):
                    exit(
                        f"An error happened while finishing the survey {symbols.exclamation}\n • {error_element.text}")

                self.adjust_window()

                return True
            except Exceptions.NoSuchElementException:
                return False

        def choose() -> None:
            answers_elements = self.get_elements(
                self.survey.data['choose']['answer'])
            for question in filter(None, (self.survey.answers.get_question(question) for question in self.get_elements(self.survey.data['choose']['question']))):
                print(f'• {question}', end='')
                answer = self.survey.answers.get_answer(question)
                for answer_element in answers_elements:
                    if answer in answer_element.text or answer_element.text in answer:
                        answer_element.click()
                        answers_elements.remove(answer_element)
                        print(
                            f': {Clr.c((Clr.BOLD, Clr.YELLOW), answer_element.text)} {symbols.right}')
                        break
                else:
                    exit(f' {symbols.wrong}')

        def rate() -> None:
            def select_rating(question_number, answer):
                path = self.survey.data['rate']['answers'].replace('#QUESTION#', str(question_number)).replace(
                    '#ANSWER#', str(7 - int(answer)) if re.match('^\d+$', answer) else str({'yes': 2, 'no': 3}[answer.lower()]))
                self.click_element(path)

            for question_number, (question, answer) in enumerate(self.survey.answers.get_questions_answers(self.get_elements(self.survey.data['rate']['questions'])), start=1):
                Log.completed(question, answer)(
                    select_rating)(question_number, answer)

        def note() -> None:
            def type_answer(answer):
                for character in answer:
                    self.get_element(
                        self.survey.data['note']['answer']).send_keys(character)

            Log.completed(question := self.survey.answers.get_question(self.get_element(
                self.survey.data['note']['question'])), answer := self.survey.answers.get_answer(question))(type_answer)(answer)

        while next_page():
            for question_type in (choose, rate, note):
                if self.check_element_exist(self.survey.data[question_type.__name__]['page']):
                    question_type()

        self.code = self.get_element_text(self.survey.data['code'])[-5:]

    def print_time(self):
        print(
            f"{Clr.c(Clr.BOLD, f'{time.time() - self.duration_temp:g}')} sec.")
        self.duration_temp = time.time()
