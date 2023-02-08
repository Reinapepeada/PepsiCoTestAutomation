import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time
import HtmlTestRunner

URL="https://09384038:ARbg95917284.@meswebgsftmexicali.azure.intra.pepsico.com/Thingworx/Runtime/index.html#master=PepsiCo_Master&mashup=MES_Dashboard&__applyThemeName=PepsiCo%20Default%20Theme&_refreshTS=1670527225809"

class suite(unittest.TestCase):
    def setUp(self):
        chrome_options=webdriver.ChromeOptions()
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        chrome_options.accept_insecure_certs=True
        chrome_options.add_argument('ignore-certificate-errors')
        self.driver = webdriver.Chrome('/chromedriver.exe',chrome_options=chrome_options)
        self.vars = {}
        
    def test_tC01MPC01DPAccessTWXdashboard(self):
        # Test name: TC01_M_PC01_DP_Access TWX dashboard
        # Step # | name | target | value
        # 1 | open | URL
        self.driver.get(URL)
        # 3 | waitForElementPresent | id=root_pagemashupcontainer-6_ContainedMashup-12_mashup-root | 30000
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.ID, "root_pagemashupcontainer-6_ContainedMashup-12_mashup-root")))
        # 4 | assertTitle | PepsiCo Apps - Mexicali | 
        # has entrado en el dashboard con éxito
        assert self.driver.title == "PepsiCo Apps - Mexicali"

    def test_tC02MPC01DPEntitySelectionleftslider(self):
        # Test name: TC02_M_PC01_DP_Entity Selection left slider
        # Step # | name | target | value
        # 1 | open | https://09384038:ARbg95917284.@meswebgsftmexicali.azure.intra.pepsico.com/Thingworx/Runtime/index.html#master=PepsiCo_Master&mashup=MES_Dashboard&__applyThemeName=PepsiCo%20Default%20Theme&_refreshTS=1670527225809 | 
        self.driver.get(URL)
        time.sleep(6)
        # 2 | waitForElementVisible | id=root_pagemashupcontainer-6_ContainedMashup-13_ptcstabset-237 | 5000
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.ID, "root_pagemashupcontainer-6_ContainedMashup-13_ptcstabset-237")))
        time.sleep(2)
        # 3 | click | css=#flexcontainer-103-expand-btn > .tw-icon | 
        self.driver.find_element(By.CSS_SELECTOR, "#flexcontainer-103-expand-btn > .tw-icon").click()
        # 4 | assertElementPresent | id=root_pagemashupcontainer-6_ContainedMashup-105_mashup-root | 
        # se muestra el menu de areas y lineas de produccion
        time.sleep(2)
        elements = self.driver.find_elements(By.ID, "root_pagemashupcontainer-6_ContainedMashup-105_mashup-root")
        assert len(elements) > 0
  
    def test_tC02MPC02DPEntitySelectionleftslider(self):
        self.driver.get(URL)
        WebDriverWait(self.driver, 50).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_gridadvanced-109-grid-advanced > .objbox")))
        
        self.driver.find_element(By.ID, "flexcontainer-103-expand-btn").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100").click()
        time.sleep(3)
        print("El menu dropdown funciona!")
    
    # def test_tC02MPC03DPEntitySelectionleftslider(self):
    #     # Test name: TC02_M_PC03_DP_Entity Selection left slider
    #     # Step # | name | target | value
    #     # 1 | open | https://09384038:ARbg95917284.@meswebgsftmexicali.azure.intra.pepsico.com/Thingworx/Runtime/index.html#master=PepsiCo_Master&mashup=MES_Dashboard&__applyThemeName=PepsiCo%20Default%20Theme&_refreshTS=1670527225809 | 
    #     self.driver.get(URL)
    #     # 2 | waitForElementPresent | xpath=//ptcs-label[@id='root_pagemashupcontainer-6_ContainedMashup-12_ContainedMashup-134_ptcslabel-21'] | 30
    #     WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//ptcs-label[@id=\'root_pagemashupcontainer-6_ContainedMashup-12_ContainedMashup-134_ptcslabel-21\']")))
    #     # 3 | click | id=flexcontainer-103-expand-btn | 
    #     time.sleep(4)
    #     self.driver.find_element(By.ID, "flexcontainer-103-expand-btn").click()
    #     time.sleep(4)
    #     # 4 | click | id=root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100 | 
    #     self.driver.find_element(By.XPATH, "//div[@id='root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100-bounding-box']/ptcs-dropdown").click()
    #     time.sleep(4)
    #     # 5 | click | id=root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100-external-wc | 
    #     self.driver.find_element(By.XPATH, "//body[@id='runtime']/ptcs-list").click()
    #     time.sleep(4)
    #     # 6 | assertText | id=root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100 | Potato Chips
    #     # assert self.driver.find_element(By.ID, "root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100").text == "Potato Chips"
    #     # 7 | echo | Se ha seleccionado el area de potatos | 
    #     print("Se ha seleccionado el area de potatos")

    # def test_tC02MPC04DPEntitySelectionleftslider(self):
    #     # Test name: TC02_M_PC04_DP_Entity Selection left slider
    #     # Step # | name | target | value
    #     # 1 | open | https://09384038:ARbg95917284.@meswebgsftmexicali.azure.intra.pepsico.com/Thingworx/Runtime/index.html#master=PepsiCo_Master&mashup=MES_Dashboard&__applyThemeName=PepsiCo%20Default%20Theme&_refreshTS=1670527225809 | 
    #     self.driver.get(URL)
    #     # 2 | waitForElementPresent | id=root_pagemashupcontainer-6_ContainedMashup-12_ContainedMashup-141_flexcontainer-79 | 30
    #     WebDriverWait(self.driver, 40).until(expected_conditions.presence_of_element_located((By.ID, "root_pagemashupcontainer-6_ContainedMashup-12_ContainedMashup-141_flexcontainer-79")))
    #     time.sleep(4)
    #     # 3 | click | xpath=//div[@id='flexcontainer-103-expand-btn']/i | 
    #     self.driver.find_element(By.XPATH, "//div[@id=\'flexcontainer-103-expand-btn\']/i").click()
    #     time.sleep(4)
    #     # 4 | click | xpath=//ptcs-dropdown[@id='root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100'] | 
    #     self.driver.find_element(By.XPATH, "//ptcs-list[@id='root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100-external-wc']").click()
    #     time.sleep(4)
    #     # 5 | click | xpath=//ptcs-list[@id='root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100-external-wc'] | 
    #     self.driver.find_element(By.XPATH, "//*[@id='chunker']/div/div/ptcs-list-item[1]/ptcs-div").click()
    #     time.sleep(4)
    #     # 6 | click | xpath=//ptcs-button[@id='cell_PlantModelSelectionForNavigation_RepeaterButton-9_ptcsbutton-43'] | 
    #     self.driver.find_element(By.XPATH, "//div[3]/div/div[2]/div/div/div[3]/div/div/div/div[2]/div/div/div[2]/div/div[3]/div/div/ptcs-button").click()
    #     # 8 | echo | Se ha seleccionado la linea | 
    #     print("Se ha seleccionado la linea")
  
    def test_tC03MPC01DPEfficiencyCapacityWasteandDowntimevalues(self):
        # Test name: TC03_M_PC01_DP_Efficiency, Capacity, Waste and Downtime values
        # Step # | name | target | value
        # 1 | open | https://09384038:ARbg95917284.@meswebgsftmexicali.azure.intra.pepsico.com/Thingworx/Runtime/index.html#master=PepsiCo_Master&mashup=MES_Dashboard&__applyThemeName=PepsiCo%20Default%20Theme&_refreshTS=1670527225809 | 
        self.driver.get(URL)
        # 2 | waitForElementPresent | css=#root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_gridadvanced-109-grid-advanced > .objbox | 30000
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "#root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_gridadvanced-109-grid-advanced > .objbox")))
        # 3 | assertElementPresent | xpath=//*[@id="root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_gridadvanced-109-grid-advanced"]/div[2]/table/tbody/tr[2] | 
        time.sleep(3)
        elements = self.driver.find_elements(By.XPATH, "//*[@id=\"root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_gridadvanced-109-grid-advanced\"]/div[2]/table/tbody/tr[2]")
        assert len(elements) > 0
        # 4 | assertElementPresent | xpath=//*[@id="root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_gridadvanced-109-grid-advanced"]/div[2]/table/tbody/tr[3] | 
        elements = self.driver.find_elements(By.XPATH, "//*[@id=\"root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_gridadvanced-109-grid-advanced\"]/div[2]/table/tbody/tr[3]")
        assert len(elements) > 0
        # 5 | assertElementPresent | xpath=//*[@id="root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_gridadvanced-109-grid-advanced"]/div[2]/table/tbody/tr[4] | 
        elements = self.driver.find_elements(By.XPATH, "//*[@id=\"root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_gridadvanced-109-grid-advanced\"]/div[2]/table/tbody/tr[4]")
        assert len(elements) > 0
        # 6 | assertElementPresent | xpath=//*[@id="root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_gridadvanced-109-grid-advanced"]/div[2]/table/tbody/tr[5] | 
        elements = self.driver.find_elements(By.XPATH, "//*[@id=\"root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_gridadvanced-109-grid-advanced\"]/div[2]/table/tbody/tr[5]")
        assert len(elements) > 0
        # 7 | assertElementPresent | xpath=//*[@id="root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_gridadvanced-109-grid-advanced"]/div[2]/table/tbody/tr[6] | 
        elements = self.driver.find_elements(By.XPATH, "//*[@id=\"root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_gridadvanced-109-grid-advanced\"]/div[2]/table/tbody/tr[6]")
        assert len(elements) > 0
        # 8 | assertElementPresent | xpath=//*[@id="root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_gridadvanced-109-grid-advanced"]/div[2]/table/tbody/tr[7] | 
        elements = self.driver.find_elements(By.XPATH, "//*[@id=\"root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_gridadvanced-109-grid-advanced\"]/div[2]/table/tbody/tr[7]")
        assert len(elements) > 0
        # 9 | echo | ¡¡¡¡Todas las lineas se visualizan en pantalla!!!! | 
        print("¡¡¡¡Todas las lineas se visualizan en pantalla!!!!")

    def test_TC03MPC02DPEfficiencyCapacityWasteDowntimevalues(self): 
        self.driver.get(URL)
        WebDriverWait(self.driver, 60).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_gridadvanced-109-grid-advanced"]/div[2]/table')))
        time.sleep(5)
        driver=self.driver 
        # Calculando cuantas filas y columnas tiene la tabla
        filas=len(driver.find_elements(By.XPATH,'//*[@id="root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_gridadvanced-109-grid-advanced"]/div[2]/table/tbody/tr'))
        columnas=len(driver.find_elements(By.XPATH,'//*[@id="root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_gridadvanced-109-grid-advanced"]/div[2]/table/tbody/tr[1]/th'))


        for f in range(2,filas+1) :
            for c in range(3,columnas+1):
                # Ubicando valores de cada campo de la tabla por fila
                dato=(driver.find_element(By.XPATH,'//*[@id="root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_gridadvanced-109-grid-advanced"]/div[2]/table/tbody/tr['+str(f)+']/td['+str(c)+']').text)
                # Ubicando que fila es la actual
                tubo=driver.find_element(By.XPATH,'//*[@id="root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_gridadvanced-109-grid-advanced"]/div[2]/table/tbody/tr['+str(f)+']/td['+str(1)+']').text
                # Convirtiendo el texto de la tabla en flotantes para poderlo comparar con un valor numerico
                try:
                    dato=float(dato)
                except ValueError:
                    dato=dato+".0"
                    dato=float(dato)

                print(c," ", dato)
                # Comparando valores con los estandares para cada campo
                if c == 3:
                    assert dato>0, f'El Set Point esta de la tubo {tubo} esta en 0 o menos'
                elif c==4 :
                    assert dato>0, f'El Name Plate esta de la tubo {tubo} esta en 0 o menos'
                elif c==5 :
                    assert dato>0, f'El NE esta de la tubo {tubo} esta en 0 o menos'
                elif c==6 :
                    assert dato<20, f'El D esta de la tubo {tubo} esta en 100 o mas'
                elif c==7 :
                    assert dato>0, f'El T esta de la tubo {tubo} esta en 0 o menos'
                elif c==8 :
                    assert dato>0 and dato<10, f'El W esta de la tubo {tubo} esta en 0 o menos'   

    def teardown(self):
        self.driver.quit()
    
if __name__ == '__main__':
    unittest.main() 
    # testRunner=HtmlTestRunner.HTMLTestRunner(output='Reporte')
