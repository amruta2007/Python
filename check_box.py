'''
Created on Jul 3, 2019

@author: amruta
'''
from selenium import webdriver

driver = webdriver.Firefox();
driver.get("file:///D:/python/check_box/check_box.HTML");

#To simply click on checkbox regardless of the status
driver.find_element_by_id("privacypolicy").click();

#To find whether the element is a checkbox or not
if driver.find_element_by_id("privacypolicy").get_attribute("type") == "checkbox":
    print "Element is a checkbox";
else:
    print "Element is not a checkbox";

#To find whether the checkbox element is selected or not
isChecked = driver.find_element_by_id("privacypolicy").get_attribute("checked")
if isChecked is not None:
    print "Element checked - "+isChecked;
else:
    print "Element checked - false";

#To find whether the checkbox element is selected or not
result = driver.find_element_by_id("privacypolicy").is_selected();
print "Checkbox status - ",result;

#Select checkbox only when it is not selected 
result = driver.find_element_by_id("privacypolicy").is_selected();
if result:
    print 'Checkbox already selected';
else:
    driver.find_element_by_id("privacypolicy").click();
    print 'Checkbox selected';

#Deselect checkbox only when it is selected 
result = driver.find_element_by_id("privacypolicy").is_selected();
if result:
    driver.find_element_by_id("privacypolicy").click();
    print 'Checkbox deselected';
else:
    print 'Checkbox already deselected';
