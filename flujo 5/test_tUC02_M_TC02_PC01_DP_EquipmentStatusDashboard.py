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

class TestTC02MPC04DPEntitySelectionleftslider():
  def setup_method(self, method):
    self.driver = webdriver.Chrome('chromedriver.exe')
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tC02MPC04DPEntitySelectionleftslider(self):
    # Test name: TC02_M_PC04_DP_Entity Selection left slider
    # 1 | open | https://09384038:ARbg95917284.@meswebgsftmexicali.azure.intra.pepsico.com/Thingworx/Runtime/index.html#master=PepsiCo_Master&mashup=MES_Dashboard&__applyThemeName=PepsiCo%20Default%20Theme&_refreshTS=1670527225809 | 
    self.driver.get("https://09384038:ARbg95917284.@meswebgsftmexicali.azure.intra.pepsico.com/Thingworx/Runtime/index.html#master=PepsiCo_Master&mashup=MES_Dashboard&__applyThemeName=PepsiCo%20Default%20Theme&_refreshTS=1670527225809")
    # 2 | waitForElementPresent | xpath=//div[@id='root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_mashupcontainer-5_gridadvanced-109-bounding-box']/div[3] | 11000
    # WebDriverWait(self.driver, 100).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@id=\'root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_mashupcontainer-5_gridadvanced-109-bounding-box\']/div[3]")))
    time.sleep(8)
    # 3 | click | xpath=//div[@id='root_pagemashupcontainer-6_flexcontainer-200-bounding-box']/div[2] | 
    self.driver.find_element(By.XPATH, "//div[@id=\'root_pagemashupcontainer-6_flexcontainer-200-bounding-box\']/div[2]").click()
    time.sleep(1)
    # 4 | click | xpath=//div[@id='root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100-bounding-box']/ptcs-dropdown | 
    self.driver.find_element(By.XPATH, "//div[@id=\'root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100-bounding-box\']/ptcs-dropdown").click()
    time.sleep(1)
    # 5 | click | xpath=//body[@id='runtime']/ptcs-list | 
    self.driver.execute_script(f'return document.querySelector("#root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100-external-wc").shadowRoot.querySelector("#chunker > div > div > ptcs-list-item:nth-child(1)")').click()
   # 7 | assertElementPresent | id=root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100 | 
    time.sleep(2)
    # 6 | click | xpath=//div[@id='cell_PlantModelSelectionForNavigation_RepeaterButton-12_ptcsbutton-43-bounding-box']/ptcs-button | 
    self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/ptcs-button[1]").click()
    time.sleep(2)
    # 10 | assertElementPresent | xpath=//div[@id='root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_flexcontainer-4-bounding-box']/div | 
    # click en el dropdown de dash boards del navbar
    self.driver.find_element(By.XPATH,'//body[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[3]/table[1]/tbody[1]/tr[1]/td[1]').click()
    time.sleep(2)
    # ----------------------
    # dashboard='document.querySelector("#root_Menu-50 > li:nth-child(3) > table > tbody")'
    # self.driver.execute_script(f'return {dashboard}')
    # ----------------------
    self.driver.find_element(By.XPATH,'//body[1]/ul[2]/li[1]').click()
    time.sleep(2)
    # click en equipment status li
    equipmentStatus='document.querySelector("#root_Menu-50 > li:nth-child(2)")'
    self.driver.execute_script(f'return {equipmentStatus}').click()
    time.sleep(4)

    #defino una variable que contiene los mensajes de error
    errores="\n  "

    tablePath='//*[@id="root_pagemashupcontainer-6_mashupcontainer-142_gridadvanced-4-grid-advanced"]/div[2]/table/tbody'
    filas=self.driver.find_elements(By.XPATH,'//*[@id="root_pagemashupcontainer-6_mashupcontainer-142_gridadvanced-4-grid-advanced"]/div[2]/table/tbody/tr')
    columnas=self.driver.find_elements(By.XPATH,'//*[@id="root_pagemashupcontainer-6_mashupcontainer-142_gridadvanced-4-grid-advanced"]/div[2]/table/tbody/tr[2]/td')
    filas=len(filas)
    columnas=len(columnas)
    for f in range(2,filas+1):
      departamento=self.driver.find_element(By.XPATH,'//*[@id="root_pagemashupcontainer-6_mashupcontainer-142_gridadvanced-4-grid-advanced"]/div[2]/table/tbody/tr['+str(f)+']/td[1]').text
      linea=self.driver.find_element(By.XPATH,'//*[@id="root_pagemashupcontainer-6_mashupcontainer-142_gridadvanced-4-grid-advanced"]/div[2]/table/tbody/tr['+str(f)+']/td[2]').text
      tubo=self.driver.find_element(By.XPATH,'//*[@id="root_pagemashupcontainer-6_mashupcontainer-142_gridadvanced-4-grid-advanced"]/div[2]/table/tbody/tr['+str(f)+']/td[3]').text
      
      for c in range(1, columnas+1):
        equipo=self.driver.find_element(By.XPATH,'//*[@id="root_pagemashupcontainer-6_mashupcontainer-142_gridadvanced-4-grid-advanced"]/div[2]/table/tbody/tr['+str(f)+']/td['+str(c)+']')
        nombreEquipo=self.driver.find_element(By.XPATH,'//*[@id="root_pagemashupcontainer-6_mashupcontainer-142_gridadvanced-4-grid-advanced"]/div[2]/table/tbody/tr['+str(f)+']/td['+str(c)+']').text
        equipoClase=equipo.get_attribute("class")
        if equipoClase=="twdhtmlxcell cell_style2" and len(nombreEquipo)>3:
            errores+=f'El equipo {nombreEquipo} del departamento {departamento} linea: {linea} tubo: {tubo} esta fallando \n'

    assert len(errores)<5,  errores
    

if __name__=='__main__':
  pytest.main()