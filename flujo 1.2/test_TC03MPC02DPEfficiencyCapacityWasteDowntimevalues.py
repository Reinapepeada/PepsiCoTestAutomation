from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import pytest

class TestTC03MPC02DPEfficiencyCapacityWasteandDowntimevalues():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_TC03MPC02DPEfficiencyCapacityWasteDowntimevalues(self): 
    self.driver.get("https://09384038:ARbg95917284.@meswebgsftmexicali.azure.intra.pepsico.com/Thingworx/Runtime/index.html#master=PepsiCo_Master&mashup=MES_Dashboard&__applyThemeName=PepsiCo%20Default%20Theme&_refreshTS=1670527225809")
    # 2 | waitForElementPresent | xpath=//div[@id='root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_mashupcontainer-5_gridadvanced-109-bounding-box']/div[3] | 11000
    time.sleep(8)
    # 3 | click | xpath=//div[@id='root_pagemashupcontainer-6_flexcontainer-200-bounding-box']/div[2] | 
    self.driver.find_element(By.XPATH, "//div[@id=\'root_pagemashupcontainer-6_flexcontainer-200-bounding-box\']/div[2]").click()
    time.sleep(4)
    # 4 | click | xpath=//div[@id='root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100-bounding-box']/ptcs-dropdown | 
    self.driver.find_element(By.XPATH, "//div[@id=\'root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100-bounding-box\']/ptcs-dropdown").click()
    time.sleep(3)
    # 5 | click | xpath=//body[@id='runtime']/ptcs-list | 
    self.driver.find_element(By.XPATH, "//body[@id=\'runtime\']/ptcs-list").click()
    # 6 | click | xpath=//div[@id='cell_PlantModelSelectionForNavigation_RepeaterButton-12_ptcsbutton-43-bounding-box']/ptcs-button | 
    self.driver.find_element(By.XPATH, "//div[@id=\'cell_PlantModelSelectionForNavigation_RepeaterButton-12_ptcsbutton-43-bounding-box\']/ptcs-button").click()
    time.sleep(3)

    # Calculando cuantas filas y columnas tiene la tabla
    filas=len(self.driver.find_elements(By.XPATH,'//*[@id="root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_mashupcontainer-5_gridadvanced-109-grid-advanced"]/div[2]/table/tbody/tr'))
    columnas=len(self.driver.find_elements(By.XPATH,'//*[@id="root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_mashupcontainer-5_gridadvanced-109-grid-advanced"]/div[2]/table/tbody/tr[2]/td'))
    errores=''

    for f in range(2,filas+1) :
        tubo=self.driver.find_element(By.XPATH,'//*[@id="root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_mashupcontainer-5_gridadvanced-109-grid-advanced"]/div[2]/table/tbody/tr['+str(f)+']/td['+str(1)+']').text
        errores+='\n'+tubo+'\n'
        for c in range(3,columnas+1):
            # Ubicando valores de cada campo de la tabla por fila
            dato=(self.driver.find_element(By.XPATH,'//*[@id="root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_mashupcontainer-5_gridadvanced-109-grid-advanced"]/div[2]/table/tbody/tr['+str(f)+']/td['+str(c)+']').text)
            # Ubicando que fila es la actual
            print(tubo)
            # Convirtiendo el texto de la tabla en flotantes para poderlo comparar con un valor numerico
            try:
                dato=float(dato)
            except ValueError:
                dato=dato+".0"
                dato=float(dato)

            print(c," ", dato)
            # Comparando valores con los estandares para cada campo
            if c == 3:
                if dato>0:
                    errores+=f'El Set Point del tubo {tubo} esta en 0 o menos \n'
            elif c==4 :
                if dato>0:
                    errores+=f'El Name Plate del tubo {tubo} esta en 0 o menos \n'
            elif c==5 :
                if dato>0:
                    errores+=f'El NE esta del tubo {tubo} esta en 0 o menos \n'
            elif c==6 :
                if dato<20: 
                    errores+=f'El D esta del tubo {tubo} esta en 20 o mas \n'
            elif c==7 :
                if dato>0:
                    errores+=f'El T esta del tubo {tubo} esta en 0 o menos \n'
            elif c==8 :
                if dato>0 and dato<10:
                    errores+=f'El W esta del tubo {tubo} esta en 0 o mas de 10% \n'
        

    # Comprobar si hay errores
    assert len(errores)<10, '\n'+errores 

