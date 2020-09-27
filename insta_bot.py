from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time
from ast import literal_eval
import json


class InstagramBot(object):

    def __init__(self):

        self.browserProfile = webdriver.ChromeOptions()
        prefs = {'intl.accept_languages': 'en,en_US'}
        mobile_emulation = {
            'deviceMetrics': {'width': 360, 'height': 640, 'pixelRatio': 3.0},
            'userAgent': 'Mozilla/5.0 (Linux; Android 4.2.1; en-us; '
                         'Nexus 5 Build/JOP40D) AppleWebKit/535.19 '
                         '(KHTML, like Gecko) Chrome/18.0.1025.166 '
                         'Mobile Safari/535.19'
        }
        self.browserProfile.add_experimental_option('prefs', prefs)
        self.browserProfile.add_experimental_option(
            'mobileEmulation',
            mobile_emulation
        )

        try:
            self.browser = webdriver.Chrome(chrome_options=self.browserProfile)
        except:
            self.browser = webdriver.Chrome(ChromeDriverManager().install(),
                                            chrome_options=self.browserProfile)

        self.url = 'https://www.instagram.com'
        self.email = 0
        self.password = 0
        self.followers_from_file = 0
        self.following_from_file = 0
        self.followers = 0
        self.following = 0
        self.count_followers = 0
        self.count_followers_new = 0
        self.count_following = 0
        self.message = 'Добрый день! Я Инста Бот) А как зовут тебя?) '

    def sign_in(self):

        self.browser.get(self.url + '/accounts/login/')
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, "//input[@name='username']"))).click()

        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, "//input[@name='username']"))).send_keys(self.email)

        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, "//input[@name='password']"))).click()

        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, "//input[@name='password']"))
        ).send_keys(self.password)

        self.browser.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(3)

        self.browser.find_element_by_xpath(
            """//*[@id="react-root"]/section/main/div/div/div/button""").click()
        time.sleep(2)

        self.browser.find_element_by_css_selector("""body > div.RnEpo.Yx5HN > 
        div > div > div > div.mt3GC > button.aOOlW.HoLwm""").click()
        time.sleep(2)

    def go_to_profile(self):

        self.browser.find_element_by_xpath(
            """//*[@id="react-root"]/section/nav[2]/
            div/div/div[2]/div/div/div[5]/a/span"""
        ).click()
        time.sleep(2)

    def save_link_followers(self):
        self.count_followers = int(self.browser.find_element_by_xpath(
            """//*[@id="react-root"]/section/main/div/ul/li[2]/a/span"""
        ).text.replace(',', ''))

        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, """//*[@id="react-root"]
                /section/main/div/ul/li[2]/a/span"""))
        ).click()
        time.sleep(2)
        count_href = 0

        while self.count_followers > count_href + 2:
            try:
                    element = self.browser.find_element_by_xpath(
                        """//*[@id="react-root"]/section/nav""")
                    actions = ActionChains(self.browser)
                    actions.move_to_element(element).perform()
                    time.sleep(1)
            except:
                break

            soup = BeautifulSoup(self.browser.page_source, 'html.parser')
            body = soup.find('body')
            section = body.find('section')
            main = section.find('main', role='main')
            ul = main.find('ul', class_='jjbaz _6xe7A')
            all_a = ul.find_all('a', href=True)
            count_href = len(list((set([a['href'] for a in all_a]))))

        soup = BeautifulSoup(self.browser.page_source, 'html.parser')
        body = soup.find('body')
        section = body.find('section')
        main = section.find('main', role='main')
        ul = main.find('ul', class_='jjbaz _6xe7A')
        all_a = ul.find_all('a', href=True)
        self.followers = list(set([a['href'] for a in all_a]))

        self.browser.find_element_by_xpath(
            """//*[@id="react-root"]/section/nav/
            div/div/div[2]/div/div/div[5]/a/span"""
        ).click()
        time.sleep(2)

    def save_link_following(self):
        self.count_following = int(self.browser.find_element_by_xpath(
            """//*[@id="react-root"]/section/main/div/ul/li[3]/a/span"""
        ).text.replace(',', ''))

        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, """//*[@id="react-root"]/section/
                main/div/ul/li[3]/a/span"""))
        ).click()
        time.sleep(2)
        count_href = 0

        while self.count_following > count_href + 1:
            try:
                element = self.browser.find_element_by_xpath(
                    """//*[@id="react-root"]/section/nav""")
                actions = ActionChains(self.browser)
                actions.move_to_element(element).perform()
                time.sleep(1)
            except:
                break

            soup = BeautifulSoup(self.browser.page_source, 'html.parser')
            body = soup.find('body')
            span = body.find('span')
            main = span.find('main', role='main')
            all_a = main.find_all('a', href=True)
            count_href = len(list((set([a['href'] for a in all_a]))))

        soup = BeautifulSoup(self.browser.page_source, 'html.parser')
        body = soup.find('body')
        span = body.find('span')
        main = span.find('main', role='main')
        all_a = main.find_all('a', href=True)
        self.following = list(set([a['href'] for a in all_a]))

        self.browser.find_element_by_xpath(
            """//*[@id="react-root"]/section/nav[2]/
            div/div/div[2]/div/div/div[5]/a/span"""
        ).click()
        time.sleep(2)

    def read_data(self):
        with open('info.txt', 'r') as f:
            data = literal_eval(f.read())
            self.email = data['login']
            self.password = data['password']
            self.count_followers = data['count_followers']
            self.count_following = data['count_following']
            self.followers_from_file = data['followers']
            self.following_from_file = data['following']

    def save_data(self):
        with open('info.txt', 'r+') as f:
            data = literal_eval(f.read())
            data['count_followers'] = self.count_followers
            data['count_following'] = self.count_following
            data['followers'] = self.followers
            data['following'] = self.following
            f.seek(0)
            f.write(json.dumps(data))

    def send_message_new_followers(self):

        for follower in self.followers:

            if follower not in self.followers_from_file:
                self.browser.get(self.url + '/direct/inbox/')

                try:
                    self.browser.find_element_by_xpath(
                        """/html/body/div[4]/div/div/div/div[3]/button[2]"""
                    ).click()
                    time.sleep(2)

                    self.browser.find_element_by_xpath(
                        """/html/body/div[3]/div/div[2]/div/div[5]/button"""
                    ).click()
                    time.sleep(2)

                    WebDriverWait(self.browser, 10).until(
                        EC.element_to_be_clickable((
                            By.XPATH,
                            """//*[@id="react-root"]/section/
                            div[2]/div/div[1]/div/div[2]/input"""
                        ))
                    ).send_keys(follower.replace('/', ''))
                    time.sleep(2)

                    self.browser.find_element_by_xpath(
                        """//*[@id="react-root"]/section/
                        div[2]/div/div[2]/div/div/div[3]/button/span"""
                    ).click()
                    time.sleep(2)

                    self.browser.find_element_by_xpath(
                        """//*[@id="react-root"]/section/
                        div[1]/header/div/div[2]/button"""
                    ).click()
                    time.sleep(2)

                    WebDriverWait(self.browser, 10).until(
                        EC.element_to_be_clickable((
                            By.XPATH,
                            """//*[@id="react-root"]/section/
                        div[2]/div/div/div[2]/div/div/div/textarea"""
                        ))).send_keys(self.message)
                    time.sleep(2)

                    self.browser.find_element_by_xpath(
                        """//*[@id="react-root"]/section/
                        div[2]/div/div/div[2]/div/div/div[2]/button"""
                    ).click()
                    time.sleep(2)
                except:
                    self.browser.find_element_by_xpath(
                        """//*[@id="react-root"]/section/
                        div[1]/header/div/div[2]/button"""
                    ).click()
                    time.sleep(2)

                    WebDriverWait(self.browser, 10).until(
                        EC.element_to_be_clickable((
                            By.XPATH,
                            """//*[@id="react-root"]/section/
                            div[2]/div/div[1]/div/div[2]/input"""
                        ))
                    ).send_keys(follower.replace('/', ''))
                    time.sleep(2)

                    self.browser.find_element_by_xpath(
                        """//*[@id="react-root"]/section/
                        div[2]/div/div[2]/div/div/div[3]/button/span"""
                    ).click()
                    time.sleep(2)

                    self.browser.find_element_by_xpath(
                        """//*[@id="react-root"]/section/
                        div[1]/header/div/div[2]/button"""
                    ).click()
                    time.sleep(2)

                    WebDriverWait(self.browser, 10).until(
                        EC.element_to_be_clickable((
                            By.XPATH,
                            """//*[@id="react-root"]/section/
                        div[2]/div/div/div[2]/div/div/div/textarea"""
                        ))).send_keys(self.message)
                    time.sleep(2)

                    self.browser.find_element_by_xpath(
                        """//*[@id="react-root"]/section/
                        div[2]/div/div/div[2]/div/div/div[2]/button"""
                    ).click()
                    time.sleep(2)

    def close(self):
        self.browser.quit()

bot = InstagramBot()
bot.read_data()
bot.sign_in()
bot.go_to_profile()
bot.save_link_followers()
# bot.send_message_new_followers()
bot.save_data()
bot.close()
