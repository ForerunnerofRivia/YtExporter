from selenium import webdriver
from configparser import SafeConfigParser
from selenium.webdriver.common.keys import Keys
import time

parser = SafeConfigParser()
parser.read('./auth.cfg')

driverPath = parser.get('DRIVERPATH','driverPath')

playlistToExport = "https://www.youtube.com/playlist?list=LL"

driver = webdriver.Chrome()



time.sleep(20)

