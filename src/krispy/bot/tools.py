class Colors:
    HEADER = '\033[95m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    END = '\033[0m'

    @staticmethod
    def c(colors, text: str) -> str:
        return f"{colors}{text}{Colors.END}" if type(colors) == str else f"{''.join(color for color in colors)}{text}{Colors.END}"


class symbols:
    right = Colors.c((Colors.BOLD, Colors.GREEN), '✔')
    wrong = Colors.c((Colors.BOLD, Colors.RED), '✘')
    exclamation = Colors.c((Colors.BOLD, Colors.RED), '❗')
    waiting = '⌚'
    doughnut = '🍩'
    brown_heart = '🤎'


class Log:

    def __init__(self) -> None:
        """"""
        self._level = 0
        self._doing = False

    def title(str):
        pass

    def doing(str):
        pass

    def section(self, message, level=0):
        print(f"\n{' ' * level * 2}{message}... {symbols.waiting}")
        self.level = 1

    def end_section(self):
        print('')

    def task(self, task):
        if self.is_doing:
            exit("Hasn't closed last task")
        levels = {1: "⁃", 2: "•", 3: "∙"}
        if self.level > level:
            print()
        print(f"{levels[(level - 1) % 3 + 1]:>{level*2}} {task}", end='')
        self.is_doing, self.level = True, level

    def done(self, task=None, done=None, failed=False):
        return
        if self.is_doing:
            if failed:
                print(f" {symbols.wrong}")
            else:
                print(
                    f": {Colors.colorize((Colors.BLUE, Colors.BOLD), done)}" if done else '.', symbols.right)
        self.is_doing = False

    def failed(self, task):
        print(f" {symbols.wrong}")
        self.is_doing = False

    @staticmethod
    def completed(message, answer=None, log=True):
        def wrapper(func):
            if not log:
                return func
            else:
                def inner(*args, **kwargs):
                    print(f'• {message}', end='')
                    value = func(*args, **kwargs)
                    print(
                        f": {Colors.c(Colors.YELLOW, answer)}" if answer else '.', symbols.right)
                    return value

                return inner

        return wrapper


if __name__ == '__main__':
    log = Log()

    log.section("Loading Browser")

    log.section('Chrome')
    log.task('Downloading Webdriver')
    log.done('Downloading Webdriver', failed=True)
    log.secdone()

    log.section('Edge')
    log.task('Downloading Webdriver')
    log.done('Downloading Webdriver', failed=True)
    log.secdone()

    log.section('Firefox')
    log.task('Downloading Webdriver')
    log.done('Downloading Webdriver')
    log.secdone()

    log.secdone()

    log.title("Navigating to 'www.google.com'")
    log.title('Page 1', 1)
    log.done('Loaded')
    log.task('Language', 2)
    log.done('English')
    log.task('Store Number', 2)
    log.done('21715')
    log.title('Page 2', 1)
    log.done('Loaded')
    log.task('Question 2', 2)
    log.done('Take Away')
