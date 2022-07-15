# importing the needed packages for this script to run
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

# creating the path to the google chrome browser engine for selenium to use, instantiating the name "driver"
# to the webdriver that is using chrome's browser engine and accessing the website "youtube.com"
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.youtube.com")


# finding and pressing the "accept all" button for youtube's cookies

def accept_cookies():
    try:
        accept_button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/a/tp-yt-paper-button")))
        accept_button.click()
        time.sleep(2)
    except:
        pass

# finding and searching anything on youtube's input search bar by sending the keys, here we need to wait 2 seconds after accepting youtube's cookies for the page to fully load

def search():
    searchbox = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input")))
    time.sleep(2)
    searchbox.send_keys("you say run")

# finding and pressing the search button in order to search for the keys that we entered

def search_start():
    search_button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button")))
    time.sleep(2)
    search_button.click()

# finding and clicking on the first video that appears in the list after searching

def play_first_video():
    firstvideo = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a")))
    time.sleep(2)
    firstvideo.click()


def skip_advertisements():
    try:
        # this is a custom skip button, it has some flaws, it only works on 5-6 seconds advertisements
        skip_button = WebDriverWait(driver, 8).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[17]/div/div[3]/div/div[2]/span/button")))
        time.sleep(1)
        skip_button.click()
    except:
        skip_button = WebDriverWait(driver, 8).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[17]/div/div[3]/div/div[2]/span/button")))
        time.sleep(20)
        skip_button.click()



accept_cookies()
search()
search_start()
play_first_video()

# uncomment this if you want to skip adds
# skip_advertisements()



