import unittest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')

        self.browser = webdriver.Firefox(
            service=Service(GeckoDriverManager().install()),
            options=options
        )

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://127.0.0.1:8000/')

        self.assertIn('To-Do', self.browser.title)
        self.fail('Закончить тест')


if __name__ == "__main__":
    unittest.main(warnings='ignore')
