import re
from ...bot.tools import symbols
from .time import ReceiptDate, ReceiptTime


class Receipt:

    __slots__ = ('number', 'date', 'time')  # Has 3 attributes.

    def __init__(self, receipt: dict) -> None:
        self.number, self.date, self.time = self._validate(receipt)

    def __repr__(self) -> str:
        return f"• Receipt:\n  - Branch Number: {self.number}\n  - {self.time}\n  - {self.date}\n"

    @staticmethod
    def _validate(receipt: dict) -> tuple[int, ReceiptDate, ReceiptTime]:
        errors = list()

        # Check Branch Number format.
        if not re.match('^\d{5}$', number := receipt['number']):
            errors.append('number')
        # Check Date Year format.
        if not re.match('^\d{4}$', year := receipt['date']['year']):
            errors.append('year')
        # Check Date Month format.
        if not 1 <= int(month := receipt['date']['month']) <= 12:
            errors.append('month')
        # Check Date Day format.
        if not 1 <= int(day := receipt['date']['day']) <= 31:
            errors.append('day')
        # Check Time Hour format.
        if not 1 <= int(hour := receipt['time']['hour']) <= 12:
            errors.append('hour')
        # Check Time Minute format.
        if not 0 <= int(minute := receipt['time']['minute']) <= 59:
            errors.append('minute')
        # Check Time Meridian format.
        if not re.match('^[AP]M$', meridian := receipt['time']['meridian'].upper()):
            errors.append('meridian')

        # Exit if validation failed, and print error message. else return validated data.
        if errors:
            exit(
                f"• Wrong receipt data {symbols.exclamation}\n  • " + f'{errors}' + f" {symbols.wrong}")
        else:
            return number, ReceiptDate(year, f'{int(month)}', f'{int(day)}'), ReceiptTime(f'{int(hour):0>2}', f'{int(minute):0>2}', meridian)
