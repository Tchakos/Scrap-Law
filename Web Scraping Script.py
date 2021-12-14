# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 12:27:17 2021

@author: tchak
"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import requests
from bs4 import BeautifulSoup as bs
import pickle 


prtnt("hehehahahahahha this is an error) 

page = pickle.load(open("C:\\Users\\tchak\\OneDrive\\page.p", "rb"))
soup = bs(page.content, "html.parser")

driver = webdriver.Chrome(executable_path = "C:\\Users\\tchak\\chromedriver.exe")
driver.get("https://www.illinoiscourts.gov/top-level-opinions?type=supreme")
#x_path = '//*[@id="ctl04_ddlFilterFilingDate"]'
x_path = "//*[contains(@href, '/resources')]"

links = driver.find_element_by_xpath(x_path)

#select = Select(driver.find_element_by_xpath(x_path))
#select.select_by_visible_text("Last 90 Days")
ls_of_names = []
for i in soup.find_all("a", href=True):
    if "/resources/" in i["href"] and i.has_attr("target") and not i.has_attr("class"):     
        print(i)
        case_name = i.text
        #case_name = case_name.replace(" ", "%20")
        #ls_of_names.append(i["href"] + "/" + case_name + "%20")
        ls_of_names.append("//a[@href='" + i["href"] + "']")

# put into for loop 
links = driver.find_element_by_xpath(x_path)

driver.quit() 
