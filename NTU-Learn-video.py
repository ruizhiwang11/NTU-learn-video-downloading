from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import re
import time
import urllib.request
import progressbar
class MyProgressBar():
    def __init__(self):
        self.pbar = None

    def __call__(self, block_num, block_size, total_size):
        if not self.pbar:
            self.pbar=progressbar.ProgressBar(maxval=total_size)
            self.pbar.start()

        downloaded = block_num * block_size
        if downloaded < total_size:
            self.pbar.update(downloaded)
        else:
            self.pbar.finish()
	#self define class to show the downloading process
options = Options()
options.add_argument('--headless')
options.add_argument('--mute-audio')
driver = webdriver.Chrome('/home/ruizhi/chromedriver',chrome_options=options) #launch login website with google chrome browser
driver.get("https://ntulearn.ntu.edu.sg/webapps/login/")
USERNAME=input("Please Enter Your NTU_learn User Name: ")
element1 = driver.find_element_by_id("user_id")
element1.send_keys(USERNAME)
PASSWORD=input("Please Enter YOur NTU_learn Password: ")
element2=driver.find_element_by_id("password")
element2.send_keys(PASSWORD)
driver.find_element_by_id("entry-login").click()
record_video_url=input("Please Enter the recorded url link: ")
time.sleep(3)
driver.get(record_video_url)
elems=driver.find_elements_by_xpath("//a[@href]")
All_links=[]
video_link_list=[]
count=1
for elem in elems:
    All_links=elem.get_attribute("href")
    video_link_list+=(re.findall("/webapps/Acu-AcuLe.*",All_links))
for video_link in video_link_list:
    driver.get("https://ntulearn.ntu.edu.sg"+video_link)
    time.sleep(12)
    div_video=driver.find_element_by_xpath("//div[@id='div_video']/div[1]/video[1]")
    video_download_link=div_video.get_attribute("src")
    urllib.request.urlretrieve(video_download_link,(str)(count)+".mp4",MyProgressBar())
    count=count+1
driver.close()

