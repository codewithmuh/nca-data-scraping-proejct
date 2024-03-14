from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import json

url = "https://web1.ncaa.org/saTransfer/otherInstitutions"

# Configure Chrome options
opts = Options()
opts.add_argument("--remote-debugging-port=9222")  # Adjusted for macOS

# Initialize Chrome webdriver with configured options
driver = webdriver.Chrome(options=opts)
driver.get(url)

# You may want to add some delay here to ensure the page loads completely
sleep(5)

# Get cookies
cookies = driver.get_cookies()

# Write cookies to a JSON file
with open('cookie2.json', 'w') as outputfile:
    json.dump(cookies, outputfile)

# Close the driver
driver.quit()
