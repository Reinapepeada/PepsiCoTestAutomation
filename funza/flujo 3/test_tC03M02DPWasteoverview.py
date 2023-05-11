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

class TestTC03M02DPDowntimeoverview():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tC03M02DPDowntimeoverview(self):
    # Test name: TC03_M_02_DP_Downtime overview
    # Step # | name | target | value
    # 1 | open | https://09384038:ARbg95917284.@meswebgsftmexicali.azure.intra.pepsico.com/Thingworx/Runtime/index.html#master=PepsiCo_Master&mashup=MES_Dashboard&__applyThemeName=PepsiCo%20Default%20Theme&_refreshTS=1670527225809 | 
    self.driver.get(LIGAPRINCIPAL)
    wasteBt = 'document.querySelector("#root_pagemashupcontainer-6_ContainedMashup-13_ptcstabset-237").shadowRoot.querySelector("ptcs-tabs > ptcs-tab:nth-child(9) > ptcs-label").shadowRoot.querySelector("#label")'
    #over_underBt = 'document.querySelector("#root_pagemashupcontainer-6_ContainedMashup-13_mashupcontainer-217_radiobuttonlist-146 > table > tbody > tr > td.widget-radio-button-item.button-selected > span")' #'//*[@id="root_pagemashupcontainer-6_ContainedMashup-13_mashupcontainer-217_radiobuttonlist-146"]/table/tbody/tr/td[2]/span'#'document.querySelector("#root_pagemashupcontainer-6_ContainedMashup-13_mashupcontainer-217_radiobuttonlist-146 > table > tbody > tr > td:nth-child(2) > span")'
    # espero a que la pagina cargue
    try:
        # WebDriverWait(self.driver, 100).until(expected_conditions.presence_of_element_located((By.ID, "root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_mashupcontainer-5_gridadvanced-109")))
       time.sleep(5) 
       print("load page")
    except:
        print("page not load")
    try:
        # WebDriverWait(driver,100).until(expected_conditions.presence_of_all_elements_located(By.XPATH, '//*[@id="root_pagemashupcontainer-6_ContainedMashup-13_mashupcontainer-217_mashupcontainer-176_ContainedMashup-62_timeserieschart-13"]/svg/rect[1]'))
        self.driver.execute_script(f'return {wasteBt}').click()
        print("Entro al waste")
    except:
        print("no se pudo ingresar")
    time.sleep(5)
    try:
        #WebDriverWait(driver,100).until(expected_conditions.presence_of_all_elements_located(By.ID, ''))
        #driver.execute_script(f'return {over_underBt}').click()
        over = self.driver.find_element(By.XPATH, '//*[@id="root_pagemashupcontainer-6_ContainedMashup-13_mashupcontainer-217_radiobuttonlist-146"]/table/tbody/tr/td[2]')
        over.click()
        print("Entro al over under stacked")
    except:
        print("elemento no encontrado")
    
if __name__ == '__main__':
  pytest.main()