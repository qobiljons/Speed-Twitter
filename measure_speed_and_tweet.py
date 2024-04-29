from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(self.chrome_options)

    def get_internet_speed(self):
        # Getting internet speed from fast.com

        self.driver.get("https://fast.com/")
        speed_item = self.driver.find_element(By.ID, value="speed-value")
        time.sleep(12)
        speed = int(speed_item.text)
        return speed

    def tweet(self, username, password, speed):
        # Using Twitter

        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(7)

        post_username = self.driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="username"]')
        post_username.send_keys(username)

        time.sleep(2)
        next_page = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        next_page.click()

        time.sleep(2)
        # using input to solve captcha manually
        input()
        post_password = self.driver.find_element(By.CSS_SELECTOR, value='input[autocomplete="current-password"]')
        post_password.send_keys(password)
        time.sleep(2)
        login = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        login.click()
        time.sleep(5)

        tweet = self.driver.find_element(By.CSS_SELECTOR, value="div[contenteditable='true']")
        tweet.send_keys(f"My internet speed is {speed} Mbps ")

        post = self.driver.find_element(By.CSS_SELECTOR, "div[data-testid='tweetButtonInline']")
        post.click()

        time.sleep(2)
        self.driver.quit()