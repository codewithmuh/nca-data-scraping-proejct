

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by  import By
import pickle
import json



url = "https://web1.ncaa.org/saTransfer/otherInstitutions"

opts = Options()
opts.add_experimental_option('debuggerAddress', 'localhost:9222')
driver = webdriver.Chrome(options=opts)
driver.get(url) 


input()
sleep(5)

data=driver.get_cookies()
# write to temp file        
with open('cookie2.json', 'w') as outputfile:
    json.dump(data, outputfile)
    driver.close()
    outputfile.close()








