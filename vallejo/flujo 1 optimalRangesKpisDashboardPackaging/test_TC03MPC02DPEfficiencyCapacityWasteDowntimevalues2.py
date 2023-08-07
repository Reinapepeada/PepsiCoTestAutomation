import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import comtypes.client
from docxtpl import DocxTemplate, InlineImage
import os,sys
import win32com.client

# Agregando librerias para poder importar modulos de otros directorios
p = os.path.abspath('../..')
sys.path.insert(1, p)
from externalLibraries import convertTo
import sys,os
p = os.path.abspath('..')
sys.path.insert(1, p)
from utilities.ligasPlanta import LIGAPRINCIPAL
 

class TestTC03MPC02DPEfficiencyCapacityWasteandDowntimevalues():
  def setup_method(self, method):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-logging")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--disable-popup-blocking")
    #Mantiene abierta la ventana
    chrome_options.add_experimental_option("detach", True)
    #Oculta mensaje "Chrome is being controlled by automated software” de la ventana
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--allow-running-insecure-content')
    chrome_options.add_argument('--disable-web-security')
    chrome_options.add_argument('--disable-desktop-notifications')
    chrome_options.add_argument("--disable-extensions")

    self.driver = webdriver.Chrome(options=chrome_options)
    self.vars = {}

  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_TC03MPC02DPEfficiencyCapacityWasteDowntimevalues(self):
    failedTubes=0
    goodTubes=0
    self.driver.get(LIGAPRINCIPAL)
    # 2 | waitForElementPresent | xpath=//div[@id='root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_mashupcontainer-5_gridadvanced-109-bounding-box']/div[3] | 11000
    time.sleep(45)
    # 3 | click | xpath=//div[@id='root_pagemashupcontainer-6_flexcontainer-200-bounding-box']/div[2] | 
    self.driver.find_element(By.XPATH, "//div[@id=\'root_pagemashupcontainer-6_flexcontainer-200-bounding-box\']/div[2]").click()
    time.sleep(15)
    # 4 | click | xpath=//div[@id='root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100-bounding-box']/ptcs-dropdown | 
    jsDropdown='document.querySelector("#root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100").shadowRoot.querySelector("#select")'
    self.driver.execute_script(f"return {jsDropdown}").click()
    time.sleep(5)
    # 5 | click | xpath=//body[@id='runtime']/ptcs-list | 
    jsPathPotato='document.querySelector("#root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100-external-wc").shadowRoot.querySelector("#chunker > div > div > ptcs-list-item:nth-child(4) > ptcs-div")'
    self.driver.execute_script(f"return {jsPathPotato}").click()
    time.sleep(5)
    # 6 | click | xpath=//div[@id='cell_PlantModelSelectionForNavigation_RepeaterButton-12_ptcsbutton-43-bounding-box']/ptcs-button | 
    self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/ptcs-button[1]").click()
    time.sleep(15)

    # Calculando cuantas filas y columnas tiene la tabla
    filas=len(self.driver.find_elements(By.XPATH,'//*[@id="root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_mashupcontainer-5_gridadvanced-109-grid-advanced"]/div[2]/table/tbody/tr'))
    columnas=len(self.driver.find_elements(By.XPATH,'//*[@id="root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_mashupcontainer-5_gridadvanced-109-grid-advanced"]/div[2]/table/tbody/tr[2]/td'))
    errores=[['Packaging Tube','Condition','Value','Status']]

    for f in range(2,filas+1) :
        tubo=self.driver.find_element(By.XPATH,'//*[@id="root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_mashupcontainer-5_gridadvanced-109-grid-advanced"]/div[2]/table/tbody/tr['+str(f)+']/td['+str(1)+']').text
        bandera=False
        # errores+='\n'+tubo+'\n'
        for c in range(3,columnas-1):
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
            print(dato)
            # Comparando valores con los estandares para cada campo
            if c == 3:
                if dato<=0:
                    # agrega los datos recolectados a la lista de errores para poder ser exportados a un documento
                    # errores+=f'El Set Point del tubo {tubo} esta en 0 o menos \n VALOR ACTUAL: {dato} \n'
                    errores.append([str(tubo),'SP >= 0  ',str(dato),'Failed'])
                    bandera=True
                else:
                    errores.append([str(tubo),'SP >= 0  ',str(dato),'OK'])
            elif c==4 :
                if dato<=0:
                    # errores+=f'El Name Plate del tubo {tubo} esta en 0 o menos \n VALOR ACTUAL: {dato} \n'
                    errores.append([str(tubo),'NP >= 0  ',str(dato),'Failed'])
                    bandera=True
                else:
                    errores.append([str(tubo),'NP >= 0  ',str(dato),'OK'])
            elif c==5 :
                if dato<=0:
                    # errores+=f'El NE esta del tubo {tubo} esta en 0 o menos  \n VALOR ACTUAL: {dato} \n '
                    errores.append([str(tubo),'NE >= 0  ',str(dato),'Failed'])
                    bandera=True
                else:
                    errores.append([str(tubo),'NE >= 0  ',str(dato),'OK'])
            elif c==6 :
                if dato>20: 
                    # errores+=f'El D esta del tubo {tubo} esta en 20 o mas \n VALOR ACTUAL: {dato} \n'
                    errores.append([str(tubo),'D <= 20\t  ',str(dato),'Failed'])
                    bandera=True
                else:
                    errores.append([str(tubo),'D <= 20\t  ',str(dato),'OK'])
            elif c==7 :
                if dato<=0:
                    # errores+=f'El T esta del tubo {tubo} esta en 0 o menos \n VALOR ACTUAL: {dato} \n'
                    errores.append([str(tubo),'T >= 0\t  ',str(dato),'Fail'])
                    bandera=True
                else:
                    errores.append([str(tubo),'T >= 0\t  ',str(dato),'OK'])

            elif c==8 :
                if dato<=0 and dato<10:
                    # errores+=f'El W esta del tubo {tubo} esta en 0 o mas de 10% \n VALOR ACTUAL: {dato} \n'
                    errores.append([str(tubo),'W>=0 W<10%',str(dato),'Fail'])
                    bandera=True
                else:
                    errores.append([str(tubo),'W>=0 W<10%',str(dato),'OK'])
        
        # evalua si el tubo es bueno o malo y lo agrega al contador
        if bandera is True:
            failedTubes+=1
        else:
            goodTubes+=1
            

    # expando la pantalla para poder ver la tabla completa
    self.driver.maximize_window()
    time.sleep(5)


    # Comprobar si hay errores
    if len(errores)>0:
        # obtengo el nombre de mi documento
        print(errores)        
        documentName=documentName=obtener_nombre_archivo_actual()
      
        convertTo.createWord(errores,documentName, failedTubes, goodTubes)
        convertTo.convertToPdf(documentName)
        # hago una captura de pantalla para poder registrar el error
        self.driver.save_screenshot('reportPDF/EfficiencyCapacityWasteandDowntimevalues.png')
        
    assert len(errores)<1, errores
   
def obtener_nombre_archivo_actual():
    documentName=os.path.basename(__file__) if "__file__" in globals() else None
    documentName=documentName.replace(".py","")
    documentName=documentName.replace("_"," ")
    documentName=documentName.upper()
    documentName=documentName.replace("TEST","TEST ")
    documentName=documentName.replace("TC","TC ")
    return documentName

