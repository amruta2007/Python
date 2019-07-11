'''
Created on Jun 8, 2019

@author: facebook
'''
from selenium import webdriver
from selenium.webdriver import ActionChains
    
driver = webdriver.Firefox();

driver.get("https://opensource-demo.orangehrmlive.com")
     
driver.find_element_by_xpath("//*[@id='txtUsername']").send_keys(admin)
driver.find_element_by_xpath("//*[@id='txtPassword']").send_keys(admin123)
driver.find_element_by_xpath("//*[@id="btnLogin"]").click()

admin=driver.find_element_by_xpath("//*[@id="menu_admin_UserManagement"]".click()
usermngmnt=driver.find_element_by_xpath("//*[@id="menu_admin_UserManagement"]".click()
users=driver.find_element_by_xpath("//*[@id="menu_admin_viewSystemUsers"]".click()

action = ActionChains(driver);

action.move_to_element(admin).move_to_element(usermngmnt).move_to_element(users).click().perform()
