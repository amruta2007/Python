'''
Created on Jun 8, 2019

@author: facebook
'''
from selenium import webdriver

driver = webdriver.Firefox();


driver.get("file:///D:/python/RADIO/radio.HTML");

#To simply click on radio button regardless of the status
driver.find_element_by_id("savingsaccount").click();

#To find whether the element is a radio button or not
if driver.find_element_by_id("savingsaccount").get_attribute("type") == "radio":
    print "Element is a radio button";
else:
    print "Element is not a radio button";

#To find whether the radio button element is selected or not
isSelected = driver.find_element_by_id("savingsaccount").get_attribute("checked")
if isSelected is not None:
    print "Element checked - "+isSelected;
else:
    print "Element checked - false";

#To find whether the radio button element is selected or not
result = driver.find_element_by_id("savingsaccount").is_selected();
print "radio button status - ",result;

#Select radio button. This check is not mandatory
result = driver.find_element_by_id("savingsaccount").is_selected();
if result:
    print 'radio button already selected';
else:
    driver.find_element_by_id("savingsaccount").click();
    print 'radio button selected';
