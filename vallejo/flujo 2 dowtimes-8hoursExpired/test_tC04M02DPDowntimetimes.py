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

class TestTC04M02DPDowntimetimes():
  def setup_method(self, method):
    self.driver = webdriver.Chrome('../../externalLibraries/chromedriver.exe')
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tC04M02DPDowntimetimes(self):
   
    driver=self.driver
    driver.get(LIGAPRINCIPAL)

    downTimeBt = 'document.querySelector("#root_pagemashupcontainer-6_ContainedMashup-13_ptcstabset-237").shadowRoot.querySelector("ptcs-tabs > ptcs-tab:nth-child(5) > ptcs-label").shadowRoot.querySelector("#label")'
    #variable para show all data
    showAlldata='document.querySelector("#root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-91_mashupcontainer-94_ptcsdropdown-85-external-wc").shadowRoot.querySelector("#chunker > div > div > ptcs-list-item:nth-child(1)")'
    #variable de las filas
    pathFilas = '//*[@id="root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-91_mashupcontainer-94_gridadvanced-111-grid-advanced"]/div[2]/table/tbody/tr'
    time.sleep(15)
    # 1 | click | id=root_pagemashupcontainer-6_ContainedMashup-13_ptcstabset-237 | 
    driver.execute_script(f'return {downTimeBt}').click()
    # 2 | waitForElementPresent | xpath=//div[@id='root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-91_radiobuttonlist-99']/table/tbody/tr/td[3]/span | 50000
    time.sleep(7)
    # 3 | click | css=#root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-91_radiobuttonlist-99 .widget-radio-button-item:nth-child(3) > .radio-button-state-name | 
    driver.find_element(By.CSS_SELECTOR, "#root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-91_radiobuttonlist-99 .widget-radio-button-item:nth-child(3) > .radio-button-state-name").click()
    # 4 | waitForElementPresent | id=root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-91_mashupcontainer-94_ptcsdropdown-85 | 50000
    time.sleep(60)
    driver.find_element(By.ID, "root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-91_mashupcontainer-94_ptcsdropdown-85").click()
    # 7 | click | xpath=//*[@id="chunker"]/div/div/ptcs-list-item[1]/ptcs-div | 
    time.sleep(15)
    driver.execute_script(f'return {showAlldata}').click()
    time.sleep(15)
    # 8 | click | id=root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-91_mashupcontainer-94_ptcsbutton-14 | 
    driver.find_element(By.ID, "root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-91_mashupcontainer-94_ptcsbutton-14").click()
    time.sleep(10)
    filas=len(driver.find_elements(By.XPATH,pathFilas)) #'//*[@id="root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-91_mashupcontainer-94_gridadvanced-111-grid-advanced"]/div[2]/table/tbody/tr'
    time.sleep(9)
    #hora estandar variable
    errores=''
    for f in range(2,filas+1):
        # Ubicando valores de cada campo de la tabla por fila   
        endTime=driver.find_element(By.XPATH,pathFilas+'['+str(f)+']/td['+str(3)+']').text
        print(endTime)
        if len(endTime)<5:
            print('entro a la condicion no tiene endTime')
            #ubicancdo fila actual
            tuboNombre = driver.find_element(By.XPATH,'//*[@id="root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-91_mashupcontainer-94_gridadvanced-111-grid-advanced"]/div[2]/table/tbody/tr['+str(f)+']/td['+str(1)+']').text
            #tomando los valores de la duracion
            duration = driver.find_element(By.XPATH,'//body[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/ptcs-tab-set[1]/ptcs-mb-container[5]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[2]/table[1]/tbody[1]/tr['+str(f)+']/td['+str(4)+']').text
            print(duration)
            if len(duration)>1:    
                hora=duration[:1]
                print(hora)
                if int(hora)>8:
                    errores+= f"El tubo {tuboNombre} tiene un reporte de downtime de mas de 8 horas \n"
        
    
    # Comprobar si hay errores
    if len(errores)>8:
        name=convertTo.createWord(errores, 'TC03MPC02DPEfficiencyCapacityWasteandDowntimevalues')
        convertTo.convertToPdf(name)
        assert len(errores)<10, '\n'+errores
    else:
        assert len(errores)<8, '\n'+errores 
    

if __name__== '__main__':
  pytest.main()