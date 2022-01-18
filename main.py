import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pickle
from selenium.common.exceptions import NoSuchElementException


password = "Audioslave1"
login = "sloboda.lexus@gmail.com"
browser = webdriver.Chrome()


class InstBot:

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.browser = browser
        try:
            browser.get("https://www.instagram.com/")
            time.sleep(5)
            log_info = browser.find_element(By.CLASS_NAME, "-MzZI").find_element(By.NAME, "username")
            log_info.clear()
            log_info.send_keys(self.login)
            time.sleep(5)

            paswd = browser.find_element(By.XPATH,
                                         "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
            paswd.clear()
            paswd.send_keys(self.password)
            time.sleep(5)
            paswd.send_keys(Keys.ENTER)
            time.sleep(10)
        except Exception as ex:
            print(ex)
        self.browser_close()


    def browser_close(self):
        self.browser.close()
        self.browser.quit()

    def logIn(self):

            with open("sloboda_cookie", "wb") as file_cookie:
                pickle.dump(browser.get_cookies(), file_cookie)



            for cookie in pickle.load(open("sloboda_cookie", "rb")):
                browser.add_cookie(cookie)
            time.sleep(4)
            browser.refresh()



    def xpath_exists(self, url):
        browser = self.browser

        try:
            browser.find_element(By.XPATH, "url")
            exist = True
        except NoSuchElementException as ex:
            print(ex)
            exist = False
        return exist

    def put_likes(self, userpage):

        try:
            browser.get("https://www.instagram.com/")
            time.sleep(5)
            log_info = browser.find_element(By.CLASS_NAME, "-MzZI").find_element(By.NAME, "username")
            log_info.clear()
            log_info.send_keys(self.login)
            time.sleep(5)

            paswd = browser.find_element(By.XPATH,
                                         "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
            paswd.clear()
            paswd.send_keys(self.password)
            time.sleep(5)
            paswd.send_keys(Keys.ENTER)
            time.sleep(10)

        except Exception as ex:
            print(ex)

        try:
            url = f"https://www.instagram.com/{userpage}/"
            browser.get(url)
            time.sleep(5)
            urls_posts = []
            hrefs = browser.find_elements(By.TAG_NAME, "a")
            hrefs = [item.get_attribute('href') for item in hrefs if "/p/" in item.get_attribute('href')]

            for href in hrefs:
                urls_posts.append(href)

            time.sleep(5)
            print(urls_posts)

            filename = userpage.split("/")[-1]

            with open(f"{filename}.txt", "a") as file:
                for post_url in urls_posts:
                    file.write(post_url + '\n')

            for post_url in urls_posts:
                try:
                    wrong_userpage = "https://www.instagram.com/p/CX2_BBRAeqkasd/"
                    if self.xpath_exists(wrong_userpage):
                        print("Такого поста не существует")
                    else:
                        print("Пост найден. Начинаю ставить лайки")

                    browser.get(post_url)
                    button_like = browser.find_element(By.CLASS_NAME, "fr66n").find_element(By.CLASS_NAME,
                                                                                            "wpO6b  ").click()
                    time.sleep(5)
                    print("I've liked posts")
                except Exception as ex:
                    print(ex)


        except Exception as ex:
            print(ex)


        finally:
            self.browser_close()

    def put_comments(self, userpage):
        try:
            browser.get("https://www.instagram.com/")
            time.sleep(5)
            log_info = browser.find_element(By.CLASS_NAME, "-MzZI").find_element(By.NAME, "username")
            log_info.clear()
            log_info.send_keys(self.login)
            time.sleep(5)

            paswd = browser.find_element(By.XPATH,
                                         "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
            paswd.clear()
            paswd.send_keys(self.password)
            time.sleep(5)
            paswd.send_keys(Keys.ENTER)
            time.sleep(10)

        except Exception as ex:
            print(ex)

        try:
            url = f"https://www.instagram.com/{userpage}/"
            browser.get(url)
            time.sleep(5)
            posts_urls = []

            hrefs = browser.find_elements(By.TAG_NAME, "a")
            hrefs = [item.get_attribute('href') for item in hrefs if "/p/" in item.get_attribute('href')]

            for href in hrefs:
                posts_urls.append(href)
            time.sleep(5)

            filename = userpage.split("/")[-1]

            for post_url in posts_urls:
                with open(f"{filename}_Comment.txt", "a") as file:
                    file.write(post_url + "\n")

            for post_url in posts_urls:
                browser.get(post_url)
                time.sleep(5)
                button_comment = browser.find_element(By.CLASS_NAME, "_15y0l").find_element(By.CLASS_NAME, "wpO6b  ").click()
                time.sleep(5)
                comment_text = browser.find_element(By.XPATH,
                                                    "/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea")
                time.sleep(10)
                comment = ""
                comment_text.clear()
                comment_text.send_keys(comment)
                comment_text.send_keys(Keys.ENTER)
                time.sleep(5)

        except Exception as ex:
            print(ex)
        self.browser_close()

    def get_all_posts_urls(self, userpage):
        browser = self.browser
        browser.get(userpage)
        time.sleep(5)

        wrong_userpage = f"https://www.instagram.com/{userpage}ads/"
        if self.xpath_exists(wrong_userpage):
            print("Такого пользователя не существует, проверьте URL")
            self.browser_close()
        else:
            print("Пользователь успешно найден, ставим лайки!")
            time.sleep(5)

            posts_urls = []
            hrefs = browser.find_elements(By.TAG_NAME, "a")
            hrefs = [item.get_attribute('href') for item in hrefs if "/p/" in item.get_attribute('href')]
            for href in hrefs:
                posts_urls.append(href)

            filename = userpage.split("/")[-1]

            with open(f"{filename}_set.txt", "a") as file:
                for post_url in posts_urls:
                    file.write(post_url + "\n")

            set_posts_urls = set(posts_urls)
            set_posts_urls = list(set_posts_urls)

            with open(f"{filename}_set.txt", "a") as file:
                for post_url in posts_urls:
                    file.write(post_url + "\n")



#

InstagramBot = InstBot(login, password)
#InstagramBot.logIn()
#InstagramBot.download_userpage_content("https://www.instagram.com/ptuxerman/")
InstagramBot.get_all_posts_urls("https://www.instagram.com/viktoriiashvetss/")