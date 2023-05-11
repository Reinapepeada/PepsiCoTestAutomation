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
from utilities.ligasPlanta import LIGASSRS

class TestTC02MPC04DPEntitySelectionleftslider():
  def setup_method(self, method):
    self.driver = webdriver.Chrome('chromedriver.exe')
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tC02MPC04DPEntitySelectionleftslider(self):
    # Test name: TC02_M_PC04_DP_Entity Selection left slider
    # 1 abrir pagina en la que se va a testear
    self.driver.get(LIGASSRS)
    
    # 2 espero a que cargue
    time.sleep(8)
    
    # 3 click en By date
    self.driver.find_element(By.XPATH, '//body[1]/form[1]/table[1]/tbody[1]/tr[1]/td[1]/div[2]/div[1]/table[1]/tbody[1]/tr[5]/td[3]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[2]/td[3]/table[1]/tbody[1]/tr[5]/td[2]/div[1]/a[1]/div[1]').click()
    time.sleep(8)

    # 4 click en dropdown department
    self.driver.find_element(By.XPATH,'//body[1]/form[1]/table[1]/tbody[1]/tr[1]/td[1]/div[2]/div[1]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[2]/td[2]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/input[1]').click()
    time.sleep(4)

    # 5 click en tortillas department
    self.driver.find_element(By.XPATH, '//body[1]/form[1]/table[1]/tbody[1]/tr[1]/td[1]/div[2]/div[1]/table[1]/tbody[1]/tr[2]/td[1]/div[2]/span[1]/table[1]/tbody[1]/tr[3]/td[1]/span[1]/input[1]').click()
    time.sleep(3)

    # 6 salir del dropdown department
    self.driver.find_element(By.XPATH, '//body[1]/form[1]/table[1]/tbody[1]/tr[1]/td[1]/div[2]/div[1]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[2]/td[2]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/button[1]').click()
    time.sleep(5)

    # 7 leer el csv para saber el periodo y la semana pepsi
    with open('tables/dashboardPepsiWeek.csv') as csv_file:
      ## meto las lineas en un array
      line = csv_file.readlines()
      for l in range(0,2):
        #spliteo el enunciado del dato
        enun,dato = line[l].split(';')
        # si el enunciado pertenece a periodo o semana entonces guardalo
        if enun == 'Periodo de la Pepsi Week':
          periodo = dato
        elif enun == 'Nombre de la Pepsi Week':
          semana = dato
    
    # 8 printear el periodo y la semana pepsi
    print('Periodo de la Pepsi Week: ' + periodo)
    print('Nombre de la Pepsi Week: ' + semana)
    # semana=int(semana)-1
    # 11 click en el dropdown pepsiPeriod
    self.driver.find_element(By.XPATH,'//body[1]/form[1]/table[1]/tbody[1]/tr[1]/td[1]/div[2]/div[1]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[4]/td[5]/div[1]/select[1]').click()
    time.sleep(3)
    # 12 click en pepsiPeriod Selected
    self.driver.find_element(By.XPATH,f'//body[1]/form[1]/table[1]/tbody[1]/tr[1]/td[1]/div[2]/div[1]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[4]/td[5]/div[1]/select[1]/option[{periodo}]').click()
    time.sleep(4)
    # 9 click en el dropdown start week
    self.driver.find_element(By.XPATH,'//body[1]/form[1]/table[1]/tbody[1]/tr[1]/td[1]/div[2]/div[1]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[5]/td[2]/div[1]/select[1]').click()
    time.sleep(3)
    # 10 click on week selected
    self.driver.find_element(By.XPATH,f'//body[1]/form[1]/table[1]/tbody[1]/tr[1]/td[1]/div[2]/div[1]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[5]/td[2]/div[1]/select[1]/option[{semana}]').click()
    time.sleep(2)
    # 13 click en el dropdown end week
    self.driver.find_element(By.XPATH,'//body[1]/form[1]/table[1]/tbody[1]/tr[1]/td[1]/div[2]/div[1]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[5]/td[5]/div[1]/select[1]').click()
    time.sleep(2)
    #14 click on end week
    self.driver.find_element(By.XPATH,f'//body[1]/form[1]/table[1]/tbody[1]/tr[1]/td[1]/div[2]/div[1]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[5]/td[5]/div[1]/select[1]/option[{semana}]').click()
    time.sleep(9)
    # 15 click en view report
    self.driver.find_element(By.XPATH,'//body[1]/form[1]/table[1]/tbody[1]/tr[1]/td[1]/div[2]/div[1]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[3]/input[1]').click()
    time.sleep(10)
    # 16 click en el + mexicali
    self.driver.find_element(By.XPATH,'//body[1]/form[1]/table[1]/tbody[1]/tr[1]/td[1]/div[2]/div[1]/table[1]/tbody[1]/tr[5]/td[3]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[4]/td[3]/table[1]/tbody[1]/tr[3]/td[1]/div[1]/div[1]/a[1]').click()
    time.sleep(8)
    # 17 click en el + tortilla chips
    self.driver.find_element(By.XPATH,'//body[1]/form[1]/table[1]/tbody[1]/tr[1]/td[1]/div[2]/div[1]/table[1]/tbody[1]/tr[5]/td[3]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[4]/td[3]/table[1]/tbody[1]/tr[4]/td[2]/div[1]/div[1]/a[1]').click()
    time.sleep(10)
    # 18 click en el + TC1
    self.driver.find_element(By.XPATH,'//body[1]/form[1]/table[1]/tbody[1]/tr[1]/td[1]/div[2]/div[1]/table[1]/tbody[1]/tr[5]/td[3]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[4]/td[3]/table[1]/tbody[1]/tr[5]/td[3]/div[1]/div[1]/a[1]').click()
    time.sleep(8)
    # 19 extraigo datos de la tabla y escribo en csv

    ## 19.1 creo el archivo csv
    with open('tables/pepsiWeekSRSS.csv', 'wt') as file:
      pass
    ## 19.2 escribo los enunciados de las columnas
    with open('tables/pepsiWeekSRSS.csv', 'at') as file:
      file.write('Packaging Unit;'+';'+';'+'Downtime;'+';'+'Throughput;'+';'+'Waste;'+';'+'Efficency'+'\n')
    ## 19.3 extraigo los datos de la tabla
    fCounts=len(self.driver.find_elements(By.XPATH,'//body[1]/form[1]/table[1]/tbody[1]/tr[1]/td[1]/div[2]/div[1]/table[1]/tbody[1]/tr[5]/td[3]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[4]/td[3]/table[1]/tbody[1]/tr'))
    cCounts=len(self.driver.find_elements(By.XPATH,'//body[1]/form[1]/table[1]/tbody[1]/tr[1]/td[1]/div[2]/div[1]/table[1]/tbody[1]/tr[5]/td[3]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[4]/td[3]/table[1]/tbody[1]/tr[6]/td'))
    with open('tables/pepsiWeekSRSS.csv', 'at') as file:
      for f in range(6,fCounts+1):
        mensaje=''
        for c in range(4,cCounts+1):
          try:
            data=self.driver.find_element(By.XPATH,f'//body[1]/form[1]/table[1]/tbody[1]/tr[1]/td[1]/div[2]/div[1]/table[1]/tbody[1]/tr[5]/td[3]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[4]/td[3]/table[1]/tbody[1]/tr[{f}]/td[{c}]')
          except:
            pass
          else:
            mensaje=mensaje+data.text+';'
        file.write(mensaje+'\n')
    time.sleep(2)
