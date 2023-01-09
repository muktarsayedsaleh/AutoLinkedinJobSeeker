from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from linkedineasyapply import LinkedinEasyApply


def init_browser():
    browser_options = Options()
    options = [
        "--disable-blink-features",
        "--no-sandbox",
        "--start-maximized",
        "--disable-extensions",
        "--ignore-certificate-errors",
        "--disable-blink-features=AutomationControlled",
    ]

    for option in options:
        browser_options.add_argument(option)

    driver = webdriver.Chrome(
        ChromeDriverManager().install(), chrome_options=browser_options
    )

    driver.set_window_position(0, 0)
    driver.maximize_window()

    return driver

if __name__ == "__main__":
    browser = init_browser()

    bot = LinkedinEasyApply(browser)
    bot.login()
    bot.security_check()
    bot.start_applying()
