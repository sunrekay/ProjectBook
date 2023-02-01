from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


options = webdriver.FirefoxOptions()
options.add_argument('--headless')

browser = webdriver.Firefox(
    service= Service(GeckoDriverManager().install()),
    options = options
)

try:
    browser.get('http://127.0.0.1:8000/')
    assert 'The install worked successfully! Congratulations!' in browser.title
    print('Все нормально.')

except Exception as ex:
    print('Лежит.')

finally:
    browser.close()
    browser.quit()