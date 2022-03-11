from operator import mul
from random import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


option = webdriver.ChromeOptions()
option.add_argument("-incognito")
option.add_experimental_option("excludeSwitches", ['enable-automation'])
option.add_experimental_option("detach", True)
# option.add_argument("--headless")
# option.add_argument("disable-gpu")

myDriver = webdriver.Chrome(ChromeDriverManager().install(), options=option)

openPage = myDriver.get("https://forms.gle/bqAJti8A1ExZFNdFA")


# multiple_choice = myDriver.find_elements_by_class_name("d7L4fc bJNwt  aomaEc ECvBRb")

multiple_choice = myDriver.find_elements_by_class_name("docssharedWizToggleLabeledContainer")

# sendButton = myDriver.find_element_by_class_name("appsMaterialWizButtonPaperbuttonContent")


i = 0
for choice in multiple_choice:
    # random(range(multiple_choice[i],multiple_choice[i+4]))
    # multiple_choice[i].click()
    randomIndex = random(range(i,i+4))
    multiple_choice[randomIndex].click()
    i += 4
