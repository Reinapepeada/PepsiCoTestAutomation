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

class TestTUC01_M_TC02_DT03_DP_AccessTWXdashboard():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tUC01_M_TC02_DT03_DP_AccessTWXdashboard(self):
    self.driver.get(LIGAPRINCIPAL)
    # esperar que cargue los contadores de la pagina
    WebDriverWait(self.driver, 100).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="root_pagemashupcontainer-6_ContainedMashup-12_flexcontainer-131"]')))
    time.sleep(5)
    # abrimos menu izquierdo
    self.driver.find_element(By.XPATH,'//*[@id="flexcontainer-103-expand-btn"]').click()
    time.sleep(2)
    # abrimos dropdown
    dropdown='document.querySelector("#root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100").shadowRoot.querySelector("#select")'
    self.driver.execute_script(f'return {dropdown}').click()
    time.sleep(2)
    # selecciono (departamento) dropdown
    departamento='document.querySelector("#root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100-external-wc").shadowRoot.querySelector("#chunker > div > div > ptcs-list-item:nth-child(2) > ptcs-div")'
    self.driver.execute_script(f'return {departamento}').click()
    time.sleep(2)
    # selecciono (area) botón
    # area='document.querySelector("#cell_PlantModelSelectionForNavigation_RepeaterButton-24_ptcsbutton-43").shadowRoot.querySelector("div")'
    # self.driver.execute_script(f'return {area}').click()
    self.driver.find_element(By.XPATH, '//body[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/ptcs-button[1]').click()

    time.sleep(5)
    # click en la botonera de processing en overview
    overviewButon='document.querySelector("#root_pagemashupcontainer-6_ContainedMashup-13_ptcstabset-410").shadowRoot.querySelector("ptcs-tabs > ptcs-tab:nth-child(1)")'
    self.driver.execute_script(f'return {overviewButon}').click()
    time.sleep(3)
    # evalúo que la linea del TotalProdAmounKG no puede estar por encima de la linea de PriPackSP
     

if __name__== '__main__':
  pytest.main()
