#!/usr/bin/env python
#Program to fill in a google doc for a party invite
import time
import yaml
import logging

logging.basicConfig(level=logging.INFO)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
logging.info("loading the config yaml file")
with open("config.yaml", 'r') as stream:
    data_load = yaml.safe_load(stream)
    url = data_load['url']
    driver_path = data_load['driver']['path']
    name = data_load['testcase1']['name_input']
URL = url
driver = webdriver.Chrome(driver_path)
driver.get(URL)
driver.find_element_by_class_name("quantumWizTextinputPaperinputInput").send_keys(name)
driver.find_element_by_class_name("freebirdFormviewerViewItemsRadioOptionContainer:nth-child(1)").click()
driver.find_elements_by_class_name("quantumWizTogglePapercheckboxInnerBox")[2].click()
time.sleep(10)
driver.find_elements_by_class_name("quantumWizButtonPaperbuttonDark")[0].click()
time.sleep(10)
driver.close()
