from selenium import webdriver

chromedriver="E:\\chromedriver.exe"       #Comment if you want to use Firefox
import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
import os
# driver = webdriver.Firefox()  # Uncomment if you want to use Firefox instead of Chrome

os.environ["webdriver.chrome.driver"]=chromedriver     #Comment if you want to use Firefox
driver=webdriver.Chrome(chromedriver)                 #Comment if you want to use Firefox
driver.get("http://web.whatsapp.com")
wait = ui.WebDriverWait(driver, 60) # timeout after 10 seconds
results = wait.until(lambda driver:driver.find_element_by_css_selector("#pane-side > div > div > div > div:nth-child(1) > div > div > div.chat-body"))
search=driver.find_elements_by_css_selector("#side > div.search-container > div > label > input")
searchbox=search[0]
searchbox.send_keys("CONTACT NAME")
driver.implicitly_wait(5) # seconds
results = wait.until(lambda driver:driver.find_element_by_css_selector("#pane-side > div > div > div > div > div > div > div.chat-body"))
name=driver.find_elements_by_css_selector("#pane-side > div > div > div > div > div > div > div.chat-body")
name[0].click()
text=driver.find_element_by_css_selector("#main > footer > div > div.input-container > div > div.input")
text.send_keys("Hello,Sent Automoatically !!! ")
text.send_keys("\n")
#driver.quit()
