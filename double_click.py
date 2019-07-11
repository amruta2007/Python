'''
Created on Jul 5, 2019

@author: amruta
'''
from selenium import webdriver
from selenium.webdriver import ActionChains
    
driver = webdriver.Firefox();

driver.get("https://testautomationpractice.blogspot.com/")
     
driver.maximize_window()

element=driver.find_element_by_xpath("//*[@id='HMTL10']/div[1]/button")

actions=ActionChains(driver)

actions.double_click(element).perform()