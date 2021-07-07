class ReceiptDate:
    __slots__ = ('year', 'month', 'day')  # Has 3 attributes.

    def __init__(self, year: str, month: str, day: str) -> None:
        self.year, self.month, self.day = year, month, day

    def __str__(self) -> str: return f'{self.day}/{self.month}/{self.year}'


class ReceiptTime:
    __slots__ = ('hour', 'minute', 'meridian')  # Has 3 attributes.

    def __init__(self, hour: str, minute: str, meridian: str) -> None:
        self.hour, self.minute, self.meridian = hour, minute, meridian

    def __str__(
        self) -> str: return f'{self.hour}:{self.minute} {self.meridian}'
