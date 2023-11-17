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

p = os.path.abspath('../..')
sys.path.insert(1, p)
from externalLibraries import convertTo
import sys,os
p = os.path.abspath('..')
sys.path.insert(1, p)
from utilities.ligasPlanta import LIGAPRINCIPAL,PLANTA


class TestTC02MPC04DPEntitySelectionleftslider():
  def setup_method(self, method):
    ChromeoOptions = webdriver.ChromeOptions()
    ChromeoOptions.add_argument('--ignore-certificate-errors')
    ChromeoOptions.add_argument('--ignore-ssl-errors')
    ChromeoOptions.add_argument("--start-maximized")
    ChromeoOptions.add_argument("--disable-extensions")
    ChromeoOptions.add_argument("--disable-gpu")
    ChromeoOptions.add_argument("--disable-dev-shm-usage")
    ChromeoOptions.add_argument("--no-sandbox")
    self.driver = webdriver.Chrome(options=ChromeoOptions)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tC02MPC04DPEntitySelectionleftslider(self):
    # Test name: TC02_M_PC04_DP_Entity Selection left slider
    # 1 | open | https://09384038:ARbg95917284.@meswebgsftmexicali.azure.intra.pepsico.com/Thingworx/Runtime/index.html#master=PepsiCo_Master&mashup=MES_Dashboard&__applyThemeName=PepsiCo%20Default%20Theme&_refreshTS=1670527225809 | 
    self.driver.get(LIGAPRINCIPAL)
    # 2 | waitForElementPresent | xpath=//div[@id='root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_mashupcontainer-5_gridadvanced-109-bounding-box']/div[3] | 11000
    # WebDriverWait(self.driver, 100).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@id=\'root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_mashupcontainer-5_gridadvanced-109-bounding-box\']/div[3]")))
    time.sleep(20)
    # 3 | click | xpath=//div[@id='root_pagemashupcontainer-6_flexcontainer-200-bounding-box']/div[2] | 
    self.driver.find_element(By.XPATH, "//div[@id=\'root_pagemashupcontainer-6_flexcontainer-200-bounding-box\']/div[2]").click()
    time.sleep(7)
    # 4 | click | xpath=//div[@id='root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100-bounding-box']/ptcs-dropdown | 
    self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/ptcs-dropdown[1]").click()
    time.sleep(7)
    # 5 | click | xpath=//body[@id='runtime']/ptcs-list | 
    jsPathPotato='document.querySelector("#root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100-external-wc").shadowRoot.querySelector("#chunker > div > div > ptcs-list-item:nth-child(1) > ptcs-div")'
    self.driver.execute_script(f"return {jsPathPotato}").click()
    # 7 | assertElementPresent | id=root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100 | 
    time.sleep(8)
        # 6 | click | xpath=//div[@id='cell_PlantModelSelectionForNavigation_RepeaterButton-12_ptcsbutton-43-bounding-box']/ptcs-button | 
    self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div[3]/div/div[2]/div/div/div[2]/div/div[3]/div/div[2]/div/div/div[3]/div/div[1]/div/div[2]/div/div/div[2]/div/div[3]/div/div/ptcs-button").click()
    time.sleep(15)
    # 10 | assertElementPresent | xpath=//div[@id='root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_flexcontainer-4-bounding-box']/div | 
    # click en el dropdown de dash boards del navbar
    self.driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/ul/li[4]/table/tbody/tr/td/div/a/span').click()
    time.sleep(4)
    # ----------------------
    # 11 click en equipment status li
    self.driver.find_element(By.XPATH,'/html/body/ul[2]/li[2]/table/tbody/tr/td/div/a/span').click()
    time.sleep(35)
    

    # 12 defino matriz de errores
    errores=[["Linea","Tubo","Equipo"]]

    # 13 recorro la tabla en busca del equipo que no esta en funcionamiento (ROJO)
    TABLEPATH="/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div/div[3]/div/div/div[2]/div/div[2]/div[1]/div/div[3]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[2]/div[2]/table/tbody"
    filas=self.driver.find_elements(By.XPATH,TABLEPATH+'/tr')
    columnas=self.driver.find_elements(By.XPATH,TABLEPATH+'/tr[2]/td')
    print(filas)
    filas=len(filas)
    columnas=len(columnas)
    print(filas,columnas)
    # matriz de equipos funcionando y no funcionando
    equiposM=[['Equipos Funcionando','Equipos No Funcionando', 'Total de Equipos'],[0,0,0]]
  
    # Declaro la matriz de tipos de equipos
    tiposEquipo=[["Equipo","Conectados","Desconectados"],["Weigher",0,0],["BagMaker",0,0],["Inspector",0,0],["CheckWeigher",0,0],["CasePacker",0,0]]
    
    # recorro las filas de la tabla
    for f in range(2,filas+1):
      #bandera que indica si el equipo no esta en funcionamiento
      equipoNoFuncionando=False
      # obtengo los datos de la fila
      departamento=self.driver.find_element(By.XPATH,TABLEPATH+'/tr['+str(f)+']/td[1]').text
      linea=self.driver.find_element(By.XPATH,TABLEPATH+'/tr['+str(f)+']/td[2]').text
      tubo=self.driver.find_element(By.XPATH,TABLEPATH+'/tr['+str(f)+']/td[3]').text
      # recorro las columnas de la fila
      print("departamento: "+departamento+" linea: "+linea+" tubo: "+tubo)
      for c in range(20, columnas+1):
        # obtengo el nombre del equipo y su clase
        equipo=self.driver.find_element(By.XPATH,TABLEPATH+'/tr['+str(f)+']/td['+str(c)+']')
        nombreEquipo=self.driver.find_element(By.XPATH,TABLEPATH+'/tr['+str(f)+']/td['+str(c)+']').text
        equipoClase=equipo.get_attribute("class")
        # evalua cual es la clase del css para determinar de que color es la celda del equipo, si es rojo es porque no esta funcionando
        # esta establecido que ese nombre e clase es el de los equipos que no estan funcionando
        # OJO hay celdas fantasmas que estan en rojo pero que no corresponden a nada y no tienen texto por eso la comprobacion de que si tienen un len>3
        if "twdhtmlxcell cell_style1" in equipoClase and len(nombreEquipo)>3:
          equipoNoFuncionando=True
          errores.append([linea,tubo,nombreEquipo])
        
        if len(nombreEquipo)>3:
          # si el equipo no esta funcionando aumento el contador de equipos que no funcionan      
          if equipoNoFuncionando:
            equiposM[1][1]+=1  
          else:
            # si el equipo esta funcionando aumento el contador de equipos que funcionan
            equiposM[1][0]+=1
          
          #contar los equipos conectados y desconectados por tipo de equipo
          # Aumentando el contador de Weigher
          if equipoNoFuncionando and c==21:
            tiposEquipo[1][2]+=1
          elif c==21:
            tiposEquipo[1][1]+=1
          
          # Aumentando el contador de BagMaker
          if equipoNoFuncionando and c==22:
            tiposEquipo[2][2]+=1
          elif c==22:
            tiposEquipo[2][1]+=1
          
          # Aumentando el contador de Inspector
          if equipoNoFuncionando and c==23:
            tiposEquipo[3][2]+=1
          elif c==23:
            tiposEquipo[3][1]+=1
          
          # Aumentando el contador de CheckWeigher
          if equipoNoFuncionando and c==24:
            tiposEquipo[4][2]+=1
          elif c==24:
            tiposEquipo[4][1]+=1
          
          # Aumentando el contador de CasePacker
          if equipoNoFuncionando and c==25:
            tiposEquipo[5][2]+=1
          elif c==25:
            tiposEquipo[5][1]+=1
            

    # sumo los equipos
    equiposM[1][2]=equiposM[1][0]+equiposM[1][1]


    # Comprobar si hay errores
    if len(errores)>5:
        

        pathOG = os.path.dirname(os.path.abspath(__file__))

        # creo el path del archivo para el power bi

        path = pathOG + "/tables/totalEquipos_"+PLANTA+".xlsx"
        path2 = pathOG + "/tables/equiposDesconectados_"+PLANTA+".xlsx"
        path3 = pathOG + "/tables/tiposEquipos_"+PLANTA+".xlsx" 
        # creo el path reporte de excel con fecha y hora
        variable = time.strftime("%Y-%m-%d_%H-%M-%S") 

        pathExcel = pathOG + "/reportOutput/totalEquipos"+str(variable)+".xlsx"
        pathExcel2 = pathOG + "/reportOutput/equiposDesconectados"+str(variable)+".xlsx"
        pathExcel3 = pathOG + "/reportOutput/ReporteTiposEquipos"+str(variable)+".xlsx"
        # creo el archivo de excel
        convertTo.creartablaExcel(equiposM,path,'totalEquipos_'+PLANTA)
        convertTo.creartablaExcel(errores,path2,'equiposDesconectados_'+PLANTA)
        convertTo.creartablaExcel(tiposEquipo,path3,'reporteTiposEquipos_'+PLANTA)
        convertTo.creartablaExcel(equiposM,pathExcel,'totalEquipos_'+PLANTA)
        convertTo.creartablaExcel(errores,pathExcel2,'equiposDesconectados_'+PLANTA)
        convertTo.creartablaExcel(tiposEquipo,pathExcel3,'reporteTiposEquipos_'+PLANTA)
        assert len(errores)<1, errores
    


if __name__=='__main__':
  pytest.main()