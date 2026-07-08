import pytest
from selenium import webdriver
from Pageobjects.loginpage import LoginPage
from Utilities.readProperties import Readconfig
from Utilities.customLogger import LogGen

class Test_001_login:
    print('inside class ')
    baseurl = Readconfig.getapplicationurl()
    username = Readconfig.getUseremail()
    password = Readconfig.getPassword()
    try:
        print('inside try block')
        logger = LogGen.logger()
        print(logger.handlers)
        logger.info("TEST LOG MESSAGE")
        print("Logger initialized successfully")
    except Exception as e:
        print(f"Logger initialization failed: {e}")
        # brea

    @pytest.mark.regression
    def test_homepagetitle(self,setup):
        self.logger.info("*****************Test_001_login*********** ")
        self.logger.info("*****************home page title Test_start*********** ")
        
        self.driver = setup
        self.driver.get(self.baseurl)
        act_title = self.driver.title
        if act_title == 'nopCommerce demo store. Login':
            self.logger.info("*****************home page title is passed *********** ")
            self.driver.close()
            assert True
        else: 
            self.driver.save_screenshot(r'Pageobjects\Screenshorts\test_homepagetitle.png')
            self.driver.close()
            self.logger.error("*****************home page title is failed *********** ")
            assert False 
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("*****************home page login test start *********** ")
        self.driver =  setup
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        #self.driver.wait(10)
        act_title = self.driver.title
        if act_title == 'Dashboard / nopCommerce administation123':
            self.driver.close()
            self.logger.info("*****************home page login is passed *********** ")
            assert True
            
        else:
            print ('inside else block for login')
            self.driver.save_screenshot(r"Pageobjects\Screenshorts\test_login.png")
            self.logger.error("*****************home page login is failed *********** ")
            self.driver.close()
            assert False


