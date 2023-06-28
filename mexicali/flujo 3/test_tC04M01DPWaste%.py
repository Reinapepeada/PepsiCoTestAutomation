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

class TestTC04M01DPDowntimetimes():
  def setup_method(self, method):
    self.driver = webdriver.Chrome('../../externalLibraries/chromedriver.exe')
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tC04M01DPDowntimetimes(self):
    self.driver.get(LIGAPRINCIPAL)
    wasteBt = 'document.querySelector("#root_pagemashupcontainer-6_ContainedMashup-13_ptcstabset-237").shadowRoot.querySelector("ptcs-tabs > ptcs-tab:nth-child(9) > ptcs-label").shadowRoot.querySelector("#label")'
    #over_underBt = 'document.querySelector("#root_pagemashupcontainer-6_ContainedMashup-13_mashupcontainer-217_radiobuttonlist-146 > table > tbody > tr > td.widget-radio-button-item.button-selected > span")' #'//*[@id="root_pagemashupcontainer-6_ContainedMashup-13_mashupcontainer-217_radiobuttonlist-146"]/table/tbody/tr/td[2]/span'#'document.querySelector("#root_pagemashupcontainer-6_ContainedMashup-13_mashupcontainer-217_radiobuttonlist-146 > table > tbody > tr > td:nth-child(2) > span")'
    # espero a que la pagina cargue

    time.sleep(15)
    # WebDriverWait(self.driver, 100).until(expected_conditions.presence_of_element_located((By.ID, "root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_mashupcontainer-5_gridadvanced-109")))
    

    # WebDriverWait(driver,100).until(expected_conditions.presence_of_all_elements_located(By.XPATH, '//*[@id="root_pagemashupcontainer-6_ContainedMashup-13_mashupcontainer-217_mashupcontainer-176_ContainedMashup-62_timeserieschart-13"]/svg/rect[1]'))
    self.driver.execute_script(f'return {wasteBt}').click()
    
    time.sleep(10)

    #driver.execute_script(f'return {over_underBt}').click()
    over = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div/div[3]/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div/ptcs-tab-set/ptcs-mb-container[9]/div/div/div/div[3]/div/div[2]/div/div/div[23]/div/div/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div[3]/table/tbody/tr/td[2]/span')
    over.click()

    time.sleep(10)
    pathFilas='/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div/div[3]/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div/ptcs-tab-set/ptcs-mb-container[9]/div/div/div/div[3]/div/div[2]/div/div/div[23]/div/div/div/div[2]/div[1]/div/div/div[1]/div/div/div/div[2]/div[1]/div/div/div/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div[3]/div/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div/div[2]/table/tbody/tr'
    filas=len(self.driver.find_elements(By.XPATH,pathFilas)) #'//*[@id="root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-91_mashupcontainer-94_gridadvanced-111-grid-advanced"]/div[2]/table/tbody/tr'
    time.sleep(12)
    errores='\n'
    for f in range(2,filas+1) :
      # Ubicando valores de cada campo de la tabla por fila   
      goodbags=self.driver.find_element(By.XPATH,pathFilas+'['+str(f)+']/td['+str(7)+']').text
      tuboNombre = self.driver.find_element(By.XPATH,pathFilas+'['+str(f)+']/td['+str(1)+']').text
      totalWaste=self.driver.find_element(By.XPATH,pathFilas+'['+str(f)+']/td['+str(6)+']').text
      porcentWaste=0
      #si algun valor es igual o menos que 0 avisa en el reporte
      if float(goodbags)<=0:
        errores+= f" No hay good Bags en el tubo {tuboNombre} \n"
      
      elif float(goodbags)>0 and float(totalWaste)>0:
        #si esta positivo calcula los porcentajes 
        porcentWaste=float(totalWaste)*100//float(goodbags)
        
      #evalua los porcentajes
      if porcentWaste>10 and porcentWaste!=0:
        errores+= f" El porcentaje de Waste respecto a las good Bags es mas de 10% en el tubo {tuboNombre} \n"
    assert len(errores)<5, errores

         

if __name__== '__main__':
  pytest.main()