from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.common.exceptions
import time
import logging

# creating the logger
# if you need more detailed information about logs, you can change the level from logging.INFO to logging.DEBUG
logging.basicConfig(filename="Logs.log", level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def youtube():
    youtube_running = True
    while youtube_running:
        # creating the path to the google chrome browser engine for selenium to use, instantiating the name "driver"
        # to the webdriver that is using chrome's browser engine and accessing the website "youtube.com"

        PATH = "C:\Program Files (x86)\chromedriver.exe"
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        # detaching the browser from the function so that when the function is done, the browser won't close
        driver = webdriver.Chrome(options=options, executable_path=PATH)

        try:
            driver.get("https://www.google.ro")
            elem = driver.find_element_by_xpath().get_attribute("content")
        except:
            try:
                driver.find_element(By.XPATH, '//body[@class="neterror"]')
                print(f"No internet, moving on with the recording... - {time.strftime('%H:%M:%S')}")
                break
            except:
                pass




        try:
            driver.get("https://www.youtube.com")
            print(f"Opened the browser and detached it  - {time.strftime('%H:%M:%S')}")
            logger.info(f"Opened the browser and detached it  - {time.strftime('%H:%M:%S')}")
        except:
            try:
                driver.find_element(By.XPATH, '//body[@class="neterror"]')
                print(f"No internet, moving on with the recording... - {time.strftime('%H:%M:%S')}")
                break
            except:
                pass


        # has_connection(driver)
        # if not has_connection(driver):
        #     print('No Internet connection, aborted!')
        #     driver.quit()
        #     exit()
        # else:
        #     print("working")


        # finding and pressing the "accept all" button for youtube's cookies

        try:
            # time.sleep(2)
            accept_button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/a/tp-yt-paper-button")))
            accept_button.click()
            time.sleep(2)
            print(f"Accepted the cookies  - {time.strftime('%H:%M:%S')}")
            logger.info(f"Accepted the cookies  - {time.strftime('%H:%M:%S')}")
        except:
            try:
                print(f"Cookies not found, moving on... - {time.strftime('%H:%M:%S')}")
                logger.info(f"Cookies not found, moving on... - {time.strftime('%H:%M:%S')}")
            except:
                try:
                    driver.find_element(By.XPATH, '//body[@class="neterror"]')
                    print(f"No internet, moving on with the recording... - {time.strftime('%H:%M:%S')}")
                    logger.info(f"No internet, moving on with the recording... - {time.strftime('%H:%M:%S')}")
                    break
                except:
                    pass

        # finding and searching anything on youtube's input search bar by sending the keys, here we need to wait 2 seconds after accepting youtube's cookies for the page to fully load


        try:
            searchbox = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input")))
            time.sleep(2)
            searchbox.send_keys("you say run")
            print(f"Typing the keys in the searchbox...  - {time.strftime('%H:%M:%S')}")
            logger.info(f"Typing the keys in the searchbox...  - {time.strftime('%H:%M:%S')}")
        except:
            try:
                driver.find_element(By.XPATH, '//body[@class="neterror"]')
                print(f"No internet, moving on with the recording... - {time.strftime('%H:%M:%S')}")
                break
            except:
                pass


        # finding and pressing the search button in order to search for the keys that we entered

        try:
            search_button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button")))
            time.sleep(2)
            search_button.click()
            print(f"Clicking the search button - {time.strftime('%H:%M:%S')}")
            logger.info(f"Clicking the search button - {time.strftime('%H:%M:%S')}")
        except:
            try:
                driver.find_element(By.XPATH, '//body[@class="neterror"]')
                print(f"No internet, moving on with the recording... - {time.strftime('%H:%M:%S')}")
                break
            except:
                pass


        # finding and clicking on the first video that appears in the list after searching
        try:
            firstvideo = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a")))
            time.sleep(2)
            firstvideo.click()
            print(f"Clicking on the first video - {time.strftime('%H:%M:%S')}")
            logger.info(f"Clicking on the first video - {time.strftime('%H:%M:%S')}")
            print(f"youtube_player.py Process finished - {time.strftime('%H:%M:%S')}")
            logger.info(f"youtube_player.py Process finished - {time.strftime('%H:%M:%S')}")
        except:
            try:
                driver.find_element(By.XPATH, '//body[@class="neterror"]')
                print(f"No internet, moving on with the recording... - {time.strftime('%H:%M:%S')}")
                break
            except:
                pass


        youtube_running = False



    # try:
    #     # this is a custom skip button, it has some flaws, it only works on 5-6 seconds advertisements
    #     skip_button = WebDriverWait(driver, 8).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[17]/div/div[3]/div/div[2]/span/button")))
    #     time.sleep(1)
    #     skip_button.click()
    # except:
    #     skip_button = WebDriverWait(driver, 8).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[17]/div/div[3]/div/div[2]/span/button")))
    #     time.sleep(20)
    #     skip_button.click()

