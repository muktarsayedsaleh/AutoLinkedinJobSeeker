from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from linkedineasyapply import LinkedinEasyApply


def init_browser():
    browser_options = webdriver.ChromeOptions()
    
    browser_options.add_argument("--disable-blink-features")
    browser_options.add_argument("--no-sandbox")
    browser_options.add_argument("--start-maximized")
    browser_options.add_argument("--disable-extensions")
    browser_options.add_argument("--ignore-certificate-errors")
    browser_options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(
        # service=ChromeDriverManager().install(),
        options=browser_options
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
