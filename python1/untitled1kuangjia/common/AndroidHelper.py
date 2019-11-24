
#!/usr/bin/python
# -*-coding:utf8-*-
from appium import webdriver
from time import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import logging.config
import logging
import yaml


logging.config.fileConfig(r"D:\untitled1kuangjia")
logging.getLogger()

with open(r"E:\project_kj\config\APP_yaml.yaml","r") as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    value = list(data.values())

desired_cap = {
    'platformName': value[0],
    'platformVersion': value[1],
    'deviceName': value[2],
    'appPackage': value[3],
    'appActivity': value[4],
    'noReset': value[5],
    'unicodeKeyboard': value[6],
    'resetKeyboard': value[7],
    'ip': value[8],
    'port': value[9]
}
logging.info("Start up APP")
driver_web = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
driver_web.implicitly_wait(3)  # 隐性等待
sleep(3)


class Helper():
    def __init__(self):
        try:
            driver_web.find_element_by_id('com.tal.kaoyan:id/tv_skip')
        except NoSuchElementException:
            pass
        else:
            WebDriverWait(driver_web, 5).until(lambda x: x.find_element_by_id("com.tal.kaoyan:id/tv_skip")).click()
            WebDriverWait(driver_web, 5).until(lambda x: x.find_element_by_id("com.tal.kaoyan:id/tip_commit")).click()
            logging.info("APP starts normally")

    def quit(self):
        driver_web.quit()

    def Local_Time(self):
        local_Time = strftime("%Y-%m-%d %H %M %S")
        return local_Time

    def SrceenShot(self):
        sleep(1)
        # local_Time = strftime("%Y-%m-%d %H %M %S")
        driver_web.get_screenshot_as_file(r"{}.png".format(self.Local_Time()))
        logging.info("Screenshot of success")


# a = Helper()
# a.SrceenShot()


