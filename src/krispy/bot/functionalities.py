from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.common.exceptions as Exceptions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


class Functionalities:

    def create_session(self, host: str, port: int):
        """"""

        remote = f'http://{host}:{str(port)}'

        browser = self.browser.lower()

        if browser == 'firefox':
            from selenium.webdriver.firefox.options import Options
        elif browser == 'chrome':
            from selenium.webdriver.chrome.options import Options
        elif browser == 'edge':
            from selenium.webdriver.edge.options import Options
        elif browser == 'opera':
            from selenium.webdriver.opera.options import Options
        else:
            raise ValueError(f"Browser '{self.browser}' not found.")

        options = Options()
        # options.headless = True

        # self.driver = webdriver.Firefox(options=options)

        try:
            self.driver = webdriver.Remote(
                command_executor=remote, options=options)
        except Exception:
            print("Failed, trying headless...")
            options.headless = True
            self.driver = webdriver.Remote(
                command_executor=remote, options=options)

        # def edge(executable):
        #     print(f"\n • Edge... {symbols.waiting}", end='')
        #     if executable == None:
        #         from webdriver_manager.microsoft import EdgeChromiumDriverManager
        #         executable = EdgeChromiumDriverManager().install()
        #     return webdriver.Edge(executable_path=executable, service_log_path=log_path)

        # def opera(executable):
        #     print(f"\n • Opera... {symbols.waiting}", end='')
        #     if executable == None:
        #         from webdriver_manager.opera import OperaDriverManager
        #         executable = OperaDriverManager().install()

        #     from selenium.webdriver.chrome.options import Options
        #     options = Options()
        #     options.add_argument('--log-level=0')
        #     return webdriver.Opera(executable_path=executable, options=options, service_log_path=log_path)

        # def chrome(executable):
        #     print(f"\n • Chrome... {symbols.waiting}", end='')
        #     if executable == None:
        #         from webdriver_manager.chrome import ChromeDriverManager
        #         executable = ChromeDriverManager().install()
        #         # from selenium.webdriver.chrome.options import Options
        #     return webdriver.Chrome(executable_path=executable, service_log_path=log_path)

        # def firefox(executable):
        #     print(f"\n • Firefox... {symbols.waiting}", end='')
        #     if executable == None:
        #         from webdriver_manager.firefox import GeckoDriverManager
        #         executable = GeckoDriverManager().install()
        #         # from selenium.webdriver.chrome.options import Options
        #     return webdriver.Firefox(executable_path=executable, service_log_path=log_path)

        # def chromium(executable):
        #     print(f"\n • Chromium... {symbols.waiting}", end='')1
        #     if executable == None:
        #         from webdriver_manager.chrome import ChromeDriverManager, ChromeType
        #         executable = ChromeDriverManager(ChromeType=ChromeType.CHROMIUM).install()
        #     return webdriver.Chrome(executable_path=executable, service_log_path=log_path)

        # browsers = {'edge': edge, 'opera': opera, 'chrome': chrome, 'firefox': firefox, 'chromium': chromium}

        # print(f"\nLoading Browser... {symbols.waiting}", end='')

        # if browser != None and browser.title() in ('Edge', 'Opera', 'Chrome', 'Firefox', 'Chromium'):
        #     try:
        #         return browsers[browser.lower()](executable_path)
        #     except Exception as error:
        #         print(error)

        # for browser_function in sorted(list(browsers.values()), key=lambda k: random.random()):
        #     try:
        #         return browser_function(executable_path)
        #     except Exception as error:
        #         print(browser)

        # exit(f"All Browsers Failed {symbols.wrong}")

    def navigate_to(self, url: str) -> None:
        self.driver.get(url)

    def get_element(self, paths, by=By.XPATH):
        return self.try_all(paths, lambda path: self.driver.find_element(by, path))

    def get_elements(self, paths, by=By.XPATH) -> list:
        for path in paths:
            if len(found_elements := self.driver.find_elements(by, path)):
                return found_elements
        return []

    def get_element_text(self, paths, by=By.XPATH) -> str:
        return self.get_element(paths, by=by).text

    def get_elements_text(self, paths, by=By.XPATH) -> list:
        for path in paths:
            if len(found_elements := self.driver.find_elements(by, path)):
                return list(element.text for element in found_elements)
        return []

    def click_element(self, paths, by=By.XPATH) -> None:
        if by == By.XPATH:
            self.try_all(paths, lambda path: self.driver.find_element(
                By.XPATH, path).click())
        elif by == By.LINK_TEXT:
            self.try_all(paths, lambda: self.driver.find_element(
                By.LINK_TEXT).click())
        elif by == By.ID:
            self.try_all(paths, lambda element: element.click())

    def select_element(self, element_path, value, by=By.XPATH) -> None:
        self.try_all(element_path, lambda path: Select(
            self.driver.find_element(by, path)).select_by_value(getattr(*value)))

    def get_element_when_exists(self, paths, wait: int = 2, by=By.XPATH):
        return self.try_all(paths, lambda path: WebDriverWait(self.driver, wait).until(presence_of_element_located(by, path)),)

    def check_element_exist(self, paths, by=By.XPATH) -> bool:
        return len(self.get_elements(paths, by=by)) > 0

    def wait_loading(self, path=None, seconds: int = 1, by=By.XPATH) -> None:
        return WebDriverWait(self.driver, seconds).until(presence_of_element_located((by, path)))

    def get_element_if_exists(self, paths, by=By.XPATH):
        for path in paths:
            try:
                return self.driver.find_element(by, path)
            except LookupError:
                continue
            except Exceptions.NoSuchElementException:
                continue
        return False

    def try_all(self, paths, task) -> None:
        """
        - Takes a function 'task' and tries it on all given paths.
        - Stops on the first complete execution, and exit('✘') if all failed.
        """
        for path in [paths] if type(paths) == str else paths:
            try:
                return task(path)
            except LookupError:
                continue
        raise LookupError

    def save_screenshot(self, path):
        self.driver.save_screenshot(f"{self.assets_location}{path}")

    def quit(self) -> None:
        self.driver.quit()

    def adjust_window(self):
        height = sum(self.get_element(
            f"//*[@id='{window}']").size['height']for window in ('header', 'middle', 'footer'))
        self.driver.set_window_size(822, height+200)
