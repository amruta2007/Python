'''
Created on Jul 5, 2019

@author: amruta
'''
from selenium import webdriver
from selenium.webdriver import ActionChains
    
driver = webdriver.Firefox();

driver.get("https://opensource-demo.orangehrmlive.com")
     
button= driver.find_element_by_xpath("//*[@id='txtUsername']")
action = ActionChains(driver)
action.context_click(button).perform()