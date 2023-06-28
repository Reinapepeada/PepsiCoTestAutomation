# Generated by Selenium IDE
import json
import os
import sys
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import math

p = os.path.abspath('..')
sys.path.insert(1, p)
from utilities.ligasPlanta import LIGAPRINCIPAL


class TestUC05_M_TC03_PC1_DP_Wastetab():
  def setup_method(self, method):
    self.driver = webdriver.Chrome('../../externalLibraries/chromedriver.exe')
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tUC04_M_TC05_PC1_DP_Wastetab(self):
    wasteBt = 'document.querySelector("#root_pagemashupcontainer-6_ContainedMashup-13_ptcstabset-237").shadowRoot.querySelector("ptcs-tabs > ptcs-tab:nth-child(9) > ptcs-label").shadowRoot.querySelector("#label")'
    # 1 | open | https://09384038:ARbg95917284.@meswebgsftmexicali.azure.intra.pepsico.com/Thingworx/Runtime/index.html#master=PepsiCo_Master&mashup=MES_Dashboard&__applyThemeName=PepsiCo%20Default%20Theme&_refreshTS=1670527225809 | 
    self.driver.get(LIGAPRINCIPAL)
    # WebDriverWait(self.driver, 100).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@id=\'root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_mashupcontainer-5_gridadvanced-109-bounding-box\']/div[3]")))
    time.sleep(30)
    # 2 click burger menu | click | id=burgerButton | 
    self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div/div[3]/div/div/div[2]/div/div[2]/div[2]").click()
    time.sleep(9)
    # 3 click en dropdown 
    self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div[3]/div/div[2]/div/div/div[2]/div/div[1]/div/div[4]/ptcs-dropdown").click()
    time.sleep(10)
    # 4 | click | papa departamento | 
    self.driver.execute_script('return document.querySelector("#root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100-external-wc").shadowRoot.querySelector("#chunker > div > div > ptcs-list-item:nth-child(4) > ptcs-div")').click()
    time.sleep(5)
    #4.1 | click | click en el boton de packging |
    self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div[3]/div/div[2]/div/div/div[2]/div/div[3]/div/div[2]/div/div/div[3]/div/div[1]/div/div[2]/div/div/div[2]/div/div[3]/div/div/ptcs-button").click()
    time.sleep(25)
    # 5 | click | click en boton de kpi`s |
    self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div/div[3]/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/div/div[3]/div/div[3]/div/div[1]/ptcs-button").click()
    time.sleep(6)
    # 6 | click | selecciono dando click en NE |
    self.driver.execute_script('return document.querySelector("#root_pagemashupcontainer-6_navigationfunction-211-popup_ptcsbutton-1")').click()
    time.sleep(10)
    # ----------------------
    # 7 | click | click en el boton del tiempo |
    self.driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div/div[3]/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/div/div[3]/div/div[3]/div/div[3]/ptcs-button').click()
    time.sleep(10)
    # 8 | click | boton last shift  |
    self.driver.execute_script('return document.querySelector("#root_pagemashupcontainer-6_navigationfunction-213-popup_ptcsbutton-120")').click()
    time.sleep(10)

    # 9 | click | click en el boton de waste |
    self.driver.execute_script(f'return {wasteBt}').click()
    
    time.sleep(25)

    # 10 | click | click en el boton CHW WASTE |
    self.driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div/div[3]/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div/ptcs-tab-set/ptcs-mb-container[9]/div/div/div/div[3]/div/div[2]/div/div/div[23]/div/div/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div[3]/table/tbody/tr/td[5]').click()
    time.sleep(90)
    
    # 11 | recorrido de la tabla CHW|
    errores='\n'
    pathTabla='/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div/div[3]/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div/ptcs-tab-set/ptcs-mb-container[9]/div/div/div/div[3]/div/div[2]/div/div/div[23]/div/div/div/div[2]/div[1]/div/div/div[1]/div/div/div/div[2]/div[4]/div/div/div/div[3]/div/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[2]/table/tbody'
    filas=self.driver.find_elements(By.XPATH,pathTabla+'/tr')
    filaslen=len(filas)
    for f in range(2,filaslen+1) :
      # Ubicando valores de cada campo de la tabla por fila 
      tuboNombre = self.driver.find_element(By.XPATH,pathTabla+'/tr['+str(f)+']/td['+str(1)+']').text
      CHW=self.driver.find_element(By.XPATH,pathTabla+'/tr['+str(f)+']/td['+str(7)+']').text
      MHW=self.driver.find_element(By.XPATH,pathTabla+'/tr['+str(f)+']/td['+str(8)+']').text
      #obteniendo el valor de la diferencia de CHW-MHW de la tabla
      chw_mhw=self.driver.find_element(By.XPATH,pathTabla+'/tr['+str(f)+']/td['+str(9)+']').text
      print(f"tubo {tuboNombre} CHW {CHW} MHW {MHW} chw_mhw {chw_mhw}")
      # Calculando la diferencia de CHW-MHW
      calculodiff=round(float(MHW)-float(CHW),2)
      # Calculando la tolerancia relativa
      toleranciaRelativa=round(float(MHW)*0.05,2)
      toleranciaMaxima=round(float(MHW)*0.1,2)
      # Validando que la diferencia de CHW-MHW sea igual a la declarada en el dashboard
      if (math.isclose(float(chw_mhw),float(calculodiff), abs_tol=toleranciaRelativa)) is False:
        errores+= f" la diferencia de CHW-MHW no es igual a la declarada en el dashboard en el tubo {tuboNombre} \n"
      # Validando que la diferencia de CHW-MHW sea menor a 100
      elif float(chw_mhw)>toleranciaMaxima:
        errores+= f" la diferencia de CHW-MHW es mayor al 10% de MHW = {toleranciaMaxima} en el tubo {tuboNombre} \n"
        print(f"toleranciaMaxima {toleranciaMaxima} chw_mhw {chw_mhw}")

    assert len(errores)<5, errores

if __name__=='__main__':
  pytest.main()