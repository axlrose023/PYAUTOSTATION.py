# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
# import requests
# login = "//"
# password = "\"
# browser = webdriver.Chrome()
# userpage = "https://www.instagram.com/ekatesrina11sdkad/"
# browser.get("https://www.instagram.com/")
# time.sleep(5)
# log_info = browser.find_element(By.CLASS_NAME, "-MzZI").find_element(By.NAME, "username")
# log_info.clear()
# log_info.send_keys(login)
# time.sleep(5)
#
# paswd = browser.find_element(By.XPATH,
#                              "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
# paswd.clear()
# paswd.send_keys(password)
# paswd.send_keys(Keys.ENTER)
# time.sleep(10)
# browser.get(userpage)
# posts_urls = []
# hrefs = browser.find_elements(By.TAG_NAME, "a")
# hrefs = [item.get_attribute('href') for item in hrefs if "/p/" in item.get_attribute('href')]
# for href in hrefs:
#     posts_urls.append(href)
#
# filename = userpage.split("/")[-2]
#
# with open(f"{filename}_set.txt", "a") as file:
#     for post_url in posts_urls:
#         file.write(post_url + "\n")
#
# set_posts_urls = set(posts_urls)
# set_posts_urls = list(set_posts_urls)
#
# with open(f"{filename}_set.txt", "a") as file:
#     for post_url in posts_urls:
#         file.write(post_url + "\n")
#
# img_and_video_src = []
#
# img_src = "/html/body/div[6]/div[2]/div/article/div/div[1]/div/div/div[1]/img"
# video_src = "/html/body/div[6]/div[2]/div/article/div/div[1]/div/div/div[1]/div/div/video"
#
# with open(f"{filename}_set.txt") as file:
#     url_list = file.readlines()
#
# for post_url in url_list[0:6]:
#     browser.get(post_url)
#     img_src_url = browser.find_elements(By.XPATH, img_src).get_attribute('src')
#     video_src_url = browser.find_elements(By.XPATH, video_src).get_attribute('src')
#
#     get_img = requests.get(img_src_url)
#     with open(f"{filename}_img.jpg", "wb") as img_file:
#         img_file.write(get_img.content)
#
#     get_video = requests.get(video_src_url, stream=True)
#     with open(f"{filename}_video.mp4", "wb") as video_file:
#         for chunk in get_video.iter_content(chunk_size=1024 * 1024):
#             if chunk:
#                 video_file.write(chunk)
#
#     img_and_video_src.append(img_src_url)
#     img_and_video_src.append(video_src_url)
#     print(img_and_video_src)
import pyautogui as pg

pg.position()
