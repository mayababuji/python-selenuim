#!/usr/bin/env python
#Program to fill in a google doc for a party invite
import time
import yaml
import logging

logging.basicConfig(level=logging.INFO)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

items_map = {"Mains":0,"Salad":1}

def test_party_invite(conf_details):
    """
    Test scenarios with people attending and not attending
    """
    URL = url
    driver = webdriver.Chrome(driver_path)
    driver.get(URL)
    name = conf_details.get("name_input")
    attenting = conf_details.get("attending")

    if attenting:

        item_name = conf_details.get("items")
        item_num = items_map[item_name]
        logging.info("{0} is attending the party and getting {1} dishes".format(name,item_name))
        driver.find_element_by_class_name("quantumWizTextinputPaperinputInput").send_keys(name)
        driver.find_element_by_class_name("freebirdFormviewerViewItemsRadioOptionContainer:nth-child(1)").click()

        driver.find_elements_by_class_name("quantumWizTogglePapercheckboxInnerBox")[item_num].click()
    else:

        logging.info("{0} is not attending the party".format(name))
        driver.find_element_by_class_name("quantumWizTextinputPaperinputInput").send_keys(name)
        driver.find_element_by_class_name("freebirdFormviewerViewItemsRadioOptionContainer:nth-child(2)").click()

    time.sleep(3)
    driver.find_elements_by_class_name("quantumWizButtonPaperbuttonDark")[0].click()

    time.sleep(5)
    driver.close()

if __name__ == "__main__":
    test_cases = None

    logging.info("loading the config yaml file")
    with open("config.yaml", 'r') as stream:
        config_load = yaml.safe_load(stream)
        url = config_load['url']
        driver_path = config_load['driver_path']

    with open("positive_tc.yaml") as test_conf:
        test_cases = yaml.safe_load(test_conf)

    for case in list(test_cases):
        test_party_invite(test_cases[case])
