'''
Created on Jul 5, 2019

@author: amruta
'''
from selenium import webdriver
from selenium.webdriver import ActionChains
from training.double_click import actions
    
driver = webdriver.Firefox();

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
     
driver.maximize_window()

sourse_element=driver.find_element_by_xpath("//*[@id='box2'']")
target_element=driver.find_element_by_xpath("//*[@id='box107']")

action = ActionChains(driver)

actions.drag_and_drop(sourse_element, target_element).perform()


