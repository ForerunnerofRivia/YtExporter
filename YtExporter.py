from selenium import webdriver
from configparser import SafeConfigParser
from selenium.webdriver.common.keys import Keys
import time

parser = SafeConfigParser()
parser.read('./auth.cfg')

driverPath = parser.get('DRIVERPATH','driverPath')
login = parser.get('CREDENTIAL','login')
password = parser.get('CREDENTIAL','password')


playlistToExport = "https://www.youtube.com/playlist?list=LL"


driver = webdriver.Chrome()


driver.get("https://www.youtube.com/")
time.sleep(2000)

login_button = driver.find_element_by_xpath('//*[@id="buttons"]/ytd-button-renderer/a')
login_button.click()


time.sleep(20)

