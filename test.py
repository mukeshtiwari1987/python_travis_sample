import os

from requests import get
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys

desired_cap = {
 'browser': 'Chrome',
 'browser_version': '62.0',
 'os': 'Windows',
 'os_version': '10',
 'resolution': '1024x768',
 'browserstack.local': 'true',
 'browserstack.localIdentifier': os.environ['BROWSERSTACK_LOCAL_IDENTIFIER'],
 'name': 'force local'
}

driver = webdriver.Remote(
    command_executor="http://" + os.environ['BROWSERSTACK_USER'] + ":" + os.environ['BROWSERSTACK_ACCESS_KEY'] + "@hub.browserstack.com:80/wd/hub",
    desired_capabilities=desired_cap)

ip_travis_machine = get('https://api.ipify.org').text
print "IP address of Travis machine:", ip_travis_machine

driver.get("http://ifconfig.co")
ip_browserstack_machine = driver.find_element_by_xpath("/html/body/div[1]/div/p[1]/code").text
print "IP address of Travis CI machine should match with BrowserStack remote machine"
print "IP address of BrowserStack remote machine:", ip_browserstack_machine
driver.save_screenshot("proof.png")

driver.quit()
