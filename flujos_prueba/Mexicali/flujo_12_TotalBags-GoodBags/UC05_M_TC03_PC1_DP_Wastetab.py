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
    chrome_options=webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-logging")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--disable-popup-blocking")
    #desactiva certificados de seguridad
    chrome_options.add_argument('--ignore-certificate-errors')

    self.driver = webdriver.Chrome( options=chrome_options)
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tUC04_M_TC05_PC1_DP_Wastetab(self):
    outputBt = 'document.querySelector("#root_pagemashupcontainer-6_ContainedMashup-13_ptcstabset-237").shadowRoot.querySelector("ptcs-tabs > ptcs-tab:nth-child(4) > ptcs-label")'
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
    

    # 10 | click | click en el boton overUnder |
    self.driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div/div[3]/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div/ptcs-tab-set/ptcs-mb-container[9]/div/div/div/div[3]/div/div[2]/div/div/div[23]/div/div/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div[3]/table/tbody/tr/td[2]').click()
    time.sleep(65)
    
    
    # 10 | defino las listas donde se van agregar los valores de goodbags para despues compararlos en la pestaña de weight |
    tuboNombress=[]
    goodBagsTubo=[]

    # 11 | recorrido de la tabla CHW|

    errores='\n'
    pathTabla='/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div/div[3]/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div/ptcs-tab-set/ptcs-mb-container[9]/div/div/div/div[3]/div/div[2]/div/div/div[23]/div/div/div/div[2]/div[1]/div/div/div[1]/div/div/div/div[2]/div[1]/div/div/div/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div[3]/div/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div/div[2]/table/tbody'
    filas=self.driver.find_elements(By.XPATH,pathTabla+'/tr')
    filaslen=len(filas)
    for f in range(2,filaslen+1) :
      # Ubicando valores de cada campo de la tabla por fila 
      tuboNombre = self.driver.find_element(By.XPATH,pathTabla+'/tr['+str(f)+']/td['+str(1)+']').text
      #obteniendo el valor de good bags de la tabla para compararlos con weight
      goodBags=self.driver.find_element(By.XPATH,pathTabla+'/tr['+str(f)+']/td['+str(8)+']').text
      print(f"tubo {tuboNombre} goodBags {goodBags}")
      goodBagsTubo.append(float(goodBags))
      tuboNombress.append(tuboNombre)
    
    print(f"tuboNombress {tuboNombress}")
    print(f"goodBagsTubo {goodBagsTubo}")
    # 9 | click | click en el boton de output |
    self.driver.execute_script(f'return {outputBt}').click()
    
    time.sleep(25)

    # 10 | click | click en el boton Weigher |
    self.driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div/div[3]/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div/ptcs-tab-set/ptcs-mb-container[4]/div/div/div/div[3]/div/div[2]/div/div/div[2]/div/div[4]/div/div[1]/div[3]/table/tbody/tr/td[4]').click()
    time.sleep(20)
    
    # 11 | recorrido de la tabla weight|
    errores='\n'
    pathTabla='/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div/div[3]/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div/ptcs-tab-set/ptcs-mb-container[4]/div/div/div/div[3]/div/div[2]/div/div/div[2]/div/div[3]/div/div/div/div[2]/div[4]/div/div/div/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div[3]/div[2]/div[2]/table/tbody'
    filas=self.driver.find_elements(By.XPATH,pathTabla+'/tr')
    filaslen=len(filas)
    for f in range(2,filaslen+1) :
      # Ubicando valores de totalBags de la tabla por fila 
      tuboNombre = self.driver.find_element(By.XPATH,pathTabla+'/tr['+str(f)+']/td['+str(1)+']').text
      totalBags=self.driver.find_element(By.XPATH,pathTabla+'/tr['+str(f)+']/td['+str(4)+']').text
      
      print(f"tubo {tuboNombre} totalBags {totalBags} goodBags {goodBagsTubo[f-2]}")
      # Validando que si totalBags es igual a las goosbags de la linea de weight
      if float(totalBags)==goodBagsTubo[f-2] : 
        errores+= f"Las goodbags{goodBagsTubo[f-2]} de {tuboNombre} coinciden con las totalBags{totalBags} de la tabla de weight\n"
      

    # Comprobar si hay errores
    if len(errores)>5:
        name=convertTo.createWord(errores, 'TC03MPC02DPEfficiencyCapacityWasteandDowntimevalues')
        convertTo.convertToPdf(name)
        assert len(errores)<5, '\n'+errores
    else:
        assert len(errores)<5, '\n'+errores 


if __name__=='__main__':
  pytest.main()