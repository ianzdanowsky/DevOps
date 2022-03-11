from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
option.add_experimental_option("excludeSwitches", ['enable-automation'])
#option.add_argument("--headless")
#option.add_argument("disable-gpu")



svc = Service("/home/ianzpimentel/GetEdu/chromedriver.exe")

# browser = webdriver.Chrome(service=svc, option=option)

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get('https://docs.google.com/forms/d/e/1FAIpQLSf8mvUYtYkCg5FcJA_nvegTg8W5Oe2K-B9lXRcxelVe_0ua5w/viewform?usp=sf_link')


multiple_choice = browser.find_elements_by_class_name("docssharedWizToggleLabeledContainer")

multiple_choice.random().click()