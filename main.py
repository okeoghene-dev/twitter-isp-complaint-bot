import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "C:/Users/Oke.Esosuakpo/chromedriver-win32/chromedriver.exe"
TWITTER_EMAIL = "jiloke2000@gmail.com"
TWITTER_PASSWORD = "JupiterJil@3"
SPEEDTEST_SITE = "https://www.speedtest.net/"
TWITTER_SITE = "https://x.com/"
USERNAME = "ji_but48451"

class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.service = Service(driver_path)
        self.driver = webdriver.Chrome(service=self.service)
        self.wait = WebDriverWait(self.driver, 10)
        self.up = 0
        self.down = 0


    def get_internet_speed(self):
        self.driver.get(SPEEDTEST_SITE)
        go_button = self.wait.until(
            ec.element_to_be_clickable(
                (By.CSS_SELECTOR, ".start-button a")
            )
        )
        go_button.click()
        time.sleep(60)
        self.up = self.driver.find_element(
            By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span'
        ).text
        self.down = self.driver.find_element(
            By.XPATH,value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'
        ).text

        print("Download:", self.down)
        print("Upload:", self.up)

        # print(self.driver.title)

    def tweet_at_provider(self):
        self.driver.get(TWITTER_SITE)
        log_in_link = self.wait.until(
            ec.element_to_be_clickable(
                (By.XPATH, "//a[@href='/login']")
            )
        )
        log_in_link.click()

        email_input = self.wait.until(
            ec.element_to_be_clickable((By.XPATH, "//input[@autocomplete='username']"))
        )
        email_input.send_keys(TWITTER_EMAIL)

        next_button = self.driver.find_element(By.XPATH, "//button[.//span[text()='Next']]")
        next_button.click()
        # time.sleep(30)

        username_input = self.wait.until(
            ec.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/label/div/div[2]/div/input'))
        )
        username_input.send_keys(USERNAME)
        next2_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/button/div/span/span')
        next2_button.click()

        password_input = self.wait.until(
            ec.element_to_be_clickable((By.XPATH, "//input[@name='password']"))
        )
        password_input.send_keys(TWITTER_PASSWORD)

        login_button = self.wait.until(
            ec.element_to_be_clickable((By.XPATH, "//button[@data-testid='LoginForm_Login_Button']"))
        )
        login_button.click()

        tweet_post = self.wait.until(
            ec.element_to_be_clickable((By.XPATH, "//div[@data-testid='tweetTextarea_0']"))
        )
        tweet_post.send_keys(f"upload speed:{self.up}, download speed:{self.down}")

        post_button = self.driver.find_element(By.XPATH, "//button[@data-testid='tweetButtonInline']")
        post_button.click()





bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
# bot.get_internet_speed()
bot.tweet_at_provider()