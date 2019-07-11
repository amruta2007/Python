'''
Created on Jun 7, 2019

@author: facebook
'''
import time
from selenium import webdriver

class switch_window():
    
    def __init__(self ):
        '''
            Initializing driver
        '''
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        
    
    def open_facebook(self):
        '''
           open facebook Help
        '''
    
        self.driver.get("https://www.facebook.com")
        
        # get the window handle after the window has opened
        self.window_0 = self.driver.window_handles[0]
        
        window_0_title = self.driver.title
        print(" First Page Title" + window_0_title)

    def open_twitter(self):
        '''
           open twitter
        '''
        # open a new window
        self.driver.execute_script("window.open('https://www.twitter.com', 'new window')")
        
        # get the window handle after a new window has opened
        self.window_1 = self.driver.window_handles[1]
        window_1_title = self.driver.title
        print(" Second Page Title" + window_1_title)
        
    #===========================================================================
    # def open_google(self):
    #         # open a new window
    #     self.driver.execute_script("window.open('https://www.google.com', 'new window')")
    #     
    #     # get the window handle after a new window has opened
    #     self.window_2 = self.driver.window_handles[2]
    #     window_2_title = self.driver.title
    #     print(" Third Page Title" + window_2_title)
    #     
    #===========================================================================
    def switch(self,switch_to_window):
        # switch on to new child window
        self.window_before_title = self.driver.title
        self.driver.switch_to.window(switch_to_window)
        time.sleep(10)
        
        window_after_title = self.driver.title
        print("Title after switch:" + window_after_title)
        
        # Compare and verify that main window and child window title don't match
        if self.window_before_title != window_after_title:
            print('Context switched to Twitter, so the title did not match')
        else:
            print('Control did not switch to new window')
    def switch_back(self,original_window):
        # switch back to original window
        self.driver.switch_to.window(original_window)
        
        # Verify that the title now match
        if self.window_before_title == self.driver.title:
            print('Context returned to parent window. Title now match')
        time.sleep(10)
        print(self.driver.title)
    
    def close_driver(self):
        '''
        closing driver
        '''
        
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    switchObj = switch_window()
    switchObj.open_facebook()
    fb_window = switchObj.window_0
    switchObj.open_twitter()
    tw_window = switchObj.window_1
    #===========================================================================
    # switchObj.open_google()
    # gl_window = switchObj.window_2
    #===========================================================================
    switchObj.switch(tw_window)
    switchObj.switch_back(fb_window)
    switchObj.close_driver()
    
    
    
