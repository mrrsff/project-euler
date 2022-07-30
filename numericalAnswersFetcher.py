from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time


options = Options()
options.headless = False
options.add_argument("--window-size=1920,1200")

DRIVER_PATH = os.path.abspath("chromedriver.exe")
driver = webdriver.Chrome(options= options,executable_path=DRIVER_PATH)
driver.get("https://projecteuler.net/recent")
soup = BeautifulSoup(driver.page_source, "html.parser")
recentProblems = soup.find("table", {"id": "problems_table"})
lastProblem = recentProblems.find("td").getText()
driver.get("https://projecteuler.net/sign_in")
time.sleep(20)
with open(r"answers.txt","w") as sheet:
    for i in range(1,int(lastProblem)+1):
        driver.get("https://projecteuler.net/problem="+str(i))
        soup2 = BeautifulSoup(driver.page_source, "html.parser")
        answer = soup2.find("span", {"class": "strong"})
        if not answer:
            sheet.write("Problem " + str(i) + ":\n")
        else:
            sheet.write("Problem "+str(i)+": "+answer.getText()+"\n")
driver.quit()