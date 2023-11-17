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
  
  def test_tC04M01DPDowntimetimes(self):
    self.driver.get(LIGAPRINCIPAL)
    wasteBt = 'document.querySelector("#root_pagemashupcontainer-6_ContainedMashup-13_ptcstabset-237").shadowRoot.querySelector("ptcs-tabs > ptcs-tab:nth-child(9) > ptcs-label").shadowRoot.querySelector("#label")'
    #over_underBt = 'document.querySelector("#root_pagemashupcontainer-6_ContainedMashup-13_mashupcontainer-217_radiobuttonlist-146 > table > tbody > tr > td.widget-radio-button-item.button-selected > span")' #'//*[@id="root_pagemashupcontainer-6_ContainedMashup-13_mashupcontainer-217_radiobuttonlist-146"]/table/tbody/tr/td[2]/span'#'document.querySelector("#root_pagemashupcontainer-6_ContainedMashup-13_mashupcontainer-217_radiobuttonlist-146 > table > tbody > tr > td:nth-child(2) > span")'
    # espero a que la pagina cargue

    time.sleep(15)
    # WebDriverWait(self.driver, 100).until(expected_conditions.presence_of_element_located((By.ID, "root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_mashupcontainer-5_gridadvanced-109")))
    self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div/div[3]/div/div/div[2]/div/div[2]/div[2]").click()
    time.sleep(8)
    # 3 click en dropdown 
    # self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div[3]/div/div[2]/div/div/div[2]/div/div[1]/div/div[4]/ptcs-dropdown//ptcs-hbar/ptcs-list-item").click()
    self.driver.execute_script('return document.querySelector("#root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100").shadowRoot.querySelector("#select > ptcs-list-item")').click()
    time.sleep(5)
    # 4 | click | papa departamento | 
    self.driver.execute_script('return document.querySelector("#root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100-external-wc").shadowRoot.querySelector("#chunker > div > div > ptcs-list-item:nth-child(1) > ptcs-div > ptcs-label").shadowRoot.querySelector("#label")').click()
    time.sleep(5)
    # 5 | click | click en boton de packaging |
    self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div[3]/div/div[2]/div/div/div[2]/div/div[3]/div/div[2]/div/div/div[3]/div/div[1]/div/div[2]/div/div/div[2]/div/div[3]/div/div/ptcs-button").click()
    time.sleep(10)

    # WebDriverWait(driver,100).until(expected_conditions.presence_of_all_elements_located(By.XPATH, '//*[@id="root_pagemashupcontainer-6_ContainedMashup-13_mashupcontainer-217_mashupcontainer-176_ContainedMashup-62_timeserieschart-13"]/svg/rect[1]'))
    self.driver.execute_script(f'return {wasteBt}').click()
    
    time.sleep(5)

    #driver.execute_script(f'return {over_underBt}').click()
    over = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div/div[3]/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div/ptcs-tab-set/ptcs-mb-container[9]/div/div/div/div[3]/div/div[2]/div/div/div[23]/div/div/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div[3]/table/tbody/tr/td[2]')
    over.click()

    time.sleep(25)
    pathFilas='/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div/div[3]/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div/ptcs-tab-set/ptcs-mb-container[9]/div/div/div/div[3]/div/div[2]/div/div/div[23]/div/div/div/div[2]/div[1]/div/div/div[1]/div/div/div/div[2]/div[1]/div/div/div/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div[3]/div/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div/div[2]/table/tbody/tr'
    filas=len(self.driver.find_elements(By.XPATH,pathFilas)) #'//*[@id="root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-91_mashupcontainer-94_gridadvanced-111-grid-advanced"]/div[2]/table/tbody/tr'
    time.sleep(15)
    #hora estandar variable
    tubos=[]
    totalWasteList=[]
    sumList=[]
    errores='\n'
    for f in range(2,filas+1) :
      # Ubicando valores de cada campo de la tabla por fila   
      tuboNombre = self.driver.find_element(By.XPATH,pathFilas+'['+str(f)+']/td['+str(1)+']').text
      totalWaste=self.driver.find_element(By.XPATH,pathFilas+'['+str(f)+']/td['+str(7)+']').text
      airLeak=self.driver.find_element(By.XPATH,pathFilas+'['+str(f)+']/td['+str(2)+']').text
      doubleBag=self.driver.find_element(By.XPATH,pathFilas+'['+str(f)+']/td['+str(3)+']').text
      flat=self.driver.find_element(By.XPATH,pathFilas+'['+str(f)+']/td['+str(5)+']').text
      thick=self.driver.find_element(By.XPATH,pathFilas+'['+str(f)+']/td['+str(6)+']').text
      overCount=self.driver.find_element(By.XPATH,pathFilas+'['+str(f)+']/td['+str(11)+']').text
      underCount=self.driver.find_element(By.XPATH,pathFilas+'['+str(f)+']/td['+str(12)+']').text
      print(float(airLeak), float(doubleBag),float(flat),float(thick),float(overCount),float(underCount),"  "+totalWaste+"  "+tuboNombre)

      if float(airLeak)+float(doubleBag)+float(flat)+float(thick)+float(overCount)+float(underCount) != float(totalWaste):
        errores+= f" la suma de airleak,doublebag,flat,thick,over,under no es igual al totalwaste en el tubo {tuboNombre} en el dashboard de over/under \n"
      
      # tubos.append(tuboNombre)
      # totalWasteList.append(float(totalWaste))
      # sumList.append(float(airLeak)+float(doubleBag)+float(flat)+float(thick))
      # si algun valor es igual o menos que 0 avisa en el reporte
    # print(tubos)
    # print(totalWasteList)
    # print(sumList)
    # self.driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div/div[3]/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div/ptcs-tab-set/ptcs-mb-container[9]/div/div/div/div[3]/div/div[2]/div/div/div[23]/div/div/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div[3]/table/tbody/tr/td[5]').click()
    # time.sleep(15)
    # pathTabla='/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div/div[3]/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div/ptcs-tab-set/ptcs-mb-container[9]/div/div/div/div[3]/div/div[2]/div/div/div[23]/div/div/div/div[2]/div[1]/div/div/div[1]/div/div/div/div[2]/div[4]/div/div/div/div[3]/div/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[2]/table/tbody'
    # filas=len(self.driver.find_elements(By.XPATH,pathTabla+'/tr'))
    # for f in range(2,filas+1):
    #   # Ubicando valores de cada campo de la tabla por fila 
    #   tuboNombre = self.driver.find_element(By.XPATH,pathTabla+'/tr['+str(f)+']/td['+str(1)+']').text
    #   indiceTubo=tubos.index(tuboNombre)
    #   print(indiceTubo)  
    #   totalWasteCHW=self.driver.find_element(By.XPATH,pathTabla+'/tr['+str(f)+']/td['+str(6)+']').text
    #   actualTotalWaste=totalWasteList[indiceTubo]

    #   sumaTotalCHW=sumList[indiceTubo]+float(totalWasteCHW)
      
    #   print (sumaTotalCHW," ",actualTotalWaste)
    #   print(f"tubo {tuboNombre} totalwasteCHW {totalWasteCHW} totalwaste en la tabla {actualTotalWaste}")
    #   if sumaTotalCHW!=actualTotalWaste:
    #     errores+= f" la suma de airleak,doublebag,flat,thick y el chw waste no es igual al totalwaste en el tubo {tuboNombre} \n"

    # Comprobar si hay errores
    if len(errores)>5:
        name=convertTo.createWord(errores, 'TC03MPC02DPEfficiencyCapacityWasteandDowntimevalues')
        convertTo.convertToPdf(name)
        assert len(errores)<5, '\n'+errores
    else:
        assert len(errores)<5, '\n'+errores 


         

if __name__== '__main__':
  pytest.main()