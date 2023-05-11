# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import sys,os
p = os.path.abspath('..')
sys.path.insert(1, p)
from utilities.ligasPlanta import LIGAPRINCIPAL

class TestTC01MPC01DPAccessTWXdashboard():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tC01MPC01DPAccessTWXdashboard(self):
    # Test name: TC01_M_PC01_DP_Access_TWX_dashboard
    # Step # | name | target | value
    # 1 | open | https://09384038:ARbg95917284.@meswebgsftmexicali.azure.intra.pepsico.com/Thingworx/Runtime/index.html#master=PepsiCo_Master&mashup=MES_Dashboard&__applyThemeName=PepsiCo%20Default%20Theme&_refreshTS=1670527225809 | 
    self.driver.get(LIGAPRINCIPAL)
    # 2 | waitForElementPresent | id=root_pagemashupcontainer-6_ContainedMashup-13_ptcstabset-237 | 10000
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.ID, "root_pagemashupcontainer-6_ContainedMashup-13_ptcstabset-237")))
    # 3 | assertTitle | PepsiCo Apps - Mexicali | 
    assert self.driver.title == "PepsiCo Apps - Mexicali"
  
