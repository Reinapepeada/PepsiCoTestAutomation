import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time
import HtmlTestRunner

URL="https://09384038:ARbg95917284.@meswebgsftmexicali.azure.intra.pepsico.com/Thingworx/Runtime/index.html#master=PepsiCo_Master&mashup=MES_Dashboard&__applyThemeName=PepsiCo%20Default%20Theme&_refreshTS=1670527225809"

class suiteTest:
    def setUp(self):
        options=Options()
        options.add_experimental_option("excludeSwitches", ['enable-automation'])
        options.accept_insecure_certs=True
        options.page_load_strategy='eager'
        options.add_argument('ignore-certificate-errors')
        options.page_load_strategy='none'
        self.driver = webdriver.Chrome('/chromedriver.exe',options=options)
        self.vars = {}
        
    def test_tC01MPC01DPAccessTWXdashboard(self):
        # Test name: TC01_M_PC01_DP_Access_TWX_dashboard
        # Step # | name | target | value
        # 1 | open | https://09384038:ARbg95917284.@meswebgsftmexicali.azure.intra.pepsico.com/Thingworx/Runtime/index.html#master=PepsiCo_Master&mashup=MES_Dashboard&__applyThemeName=PepsiCo%20Default%20Theme&_refreshTS=1670527225809 | 
        self.driver.get("https://09384038:ARbg95917284.@meswebgsftmexicali.azure.intra.pepsico.com/Thingworx/Runtime/index.html#master=PepsiCo_Master&mashup=MES_Dashboard&__applyThemeName=PepsiCo%20Default%20Theme&_refreshTS=1670527225809")
        # 2 | waitForElementPresent | id=root_pagemashupcontainer-6_ContainedMashup-13_ptcstabset-237 | 10000
        WebDriverWait(self.driver, 80).until(expected_conditions.presence_of_element_located((By.ID, "root_pagemashupcontainer-6_ContainedMashup-13_ptcstabset-237")))
        # 3 | assertTitle | PepsiCo Apps - Mexicali | 
        assert self.driver.title == "PepsiCo Apps - Mexicali"

    def test_tC02MPC01DPEntitySelectionleftslider(self):
        # Test name: TC02_M_PC01_DP_Entity Selection left slider
        # Step # | name | target | value
        # 1 | open | https://09384038:ARbg95917284.@meswebgsftmexicali.azure.intra.pepsico.com/Thingworx/Runtime/index.html#master=PepsiCo_Master&mashup=MES_Dashboard&__applyThemeName=PepsiCo%20Default%20Theme&_refreshTS=1670527225809 | 
        self.driver.get("https://09384038:ARbg95917284.@meswebgsftmexicali.azure.intra.pepsico.com/Thingworx/Runtime/index.html#master=PepsiCo_Master&mashup=MES_Dashboard&__applyThemeName=PepsiCo%20Default%20Theme&_refreshTS=1670527225809")
        # 2 | waitForElementPresent | id=root_pagemashupcontainer-6_ContainedMashup-13_ptcstabset-237 | 10000
        time.sleep(6)
        # 3 | click | xpath=//div[@id='flexcontainer-103-expand-btn']/i | 
        self.driver.find_element(By.XPATH, "//div[@id=\'flexcontainer-103-expand-btn\']/i").click()
        # 4 | assertElementPresent | xpath=//div[@id='root_pagemashupcontainer-6_ContainedMashup-105_collection-106']/div | 
        elements = self.driver.find_elements(By.XPATH, "//div[@id=\'root_pagemashupcontainer-6_ContainedMashup-105_collection-106\']/div")
        assert len(elements) > 0

    def test_tC02MPC02DPEntitySelectionleftslider(self):
        # Test name: TC02_M_PC02_DP_Entity Selection left slider
        # Step # | name | target | value
        # 1 | open | https://09384038:ARbg95917284.@meswebgsftmexicali.azure.intra.pepsico.com/Thingworx/Runtime/index.html#master=PepsiCo_Master&mashup=MES_Dashboard&__applyThemeName=PepsiCo%20Default%20Theme&_refreshTS=1670527225809 | 6000
        self.driver.get("https://09384038:ARbg95917284.@meswebgsftmexicali.azure.intra.pepsico.com/Thingworx/Runtime/index.html#master=PepsiCo_Master&mashup=MES_Dashboard&__applyThemeName=PepsiCo%20Default%20Theme&_refreshTS=1670527225809")
        # 2 | waitForElementPresent | id=root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_mashupcontainer-5_gridadvanced-109 | 11000
        time.sleep(7)
        # 3 | click | id=flexcontainer-103-expand-btn | 
        self.driver.find_element(By.ID, "flexcontainer-103-expand-btn").click()
        # 4 | click | id=root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100 | 
        self.driver.find_element(By.ID, "root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100").click()
        # 5 | waitForElementPresent | id=root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100-external-wc | 3000
        WebDriverWait(self.driver, 40).until(expected_conditions.presence_of_element_located((By.ID, "root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100-external-wc")))
        # 6 | assertElementPresent | id=root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100-external-wc | 
        elements = self.driver.find_elements(By.ID, "root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100-external-wc")
        assert len(elements) > 0
    
    def test_tC02MPC03DPEntitySelectionleftslider(self):
        # Test name: TC02_M_PC03_DP_Entity Selection left slider 
        # Step # | name | target | value
        # 1 | open | https://09384038:ARbg95917284.@meswebgsftmexicali.azure.intra.pepsico.com/Thingworx/Runtime/index.html#master=PepsiCo_Master&mashup=MES_Dashboard&__applyThemeName=PepsiCo%20Default%20Theme&_refreshTS=1670527225809 | 
        self.driver.get("https://09384038:ARbg95917284.@meswebgsftmexicali.azure.intra.pepsico.com/Thingworx/Runtime/index.html#master=PepsiCo_Master&mashup=MES_Dashboard&__applyThemeName=PepsiCo%20Default%20Theme&_refreshTS=1670527225809")
        # 2 | waitForElementPresent | xpath=//div[@id='root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_mashupcontainer-5_gridadvanced-109-grid-advanced']/div/table/tbody/tr[2]/td | 11000
        time.sleep(7)
        # 3 | click | css=#flexcontainer-103-expand-btn > .tw-icon | 
        self.driver.find_element(By.CSS_SELECTOR, "#flexcontainer-103-expand-btn > .tw-icon").click()
        # 4 | click | id=root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100 | 
        self.driver.find_element(By.ID, "root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100").click()
        # 5 | click | id=root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100-external-wc | 
        self.driver.find_element(By.ID, "root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100-external-wc").click()
        # 6 | assertElementPresent | id=root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100 | 
        elements = self.driver.find_elements(By.ID, "root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100")
        assert len(elements) > 0
    
    def test_tC02MPC04DPEntitySelectionleftslider(self):
        # Test name: TC02_M_PC04_DP_Entity Selection left slider
        # Step # | name | target | value
        # 1 | open | https://09384038:ARbg95917284.@meswebgsftmexicali.azure.intra.pepsico.com/Thingworx/Runtime/index.html#master=PepsiCo_Master&mashup=MES_Dashboard&__applyThemeName=PepsiCo%20Default%20Theme&_refreshTS=1670527225809 | 3000
        self.driver.get("https://09384038:ARbg95917284.@meswebgsftmexicali.azure.intra.pepsico.com/Thingworx/Runtime/index.html#master=PepsiCo_Master&mashup=MES_Dashboard&__applyThemeName=PepsiCo%20Default%20Theme&_refreshTS=1670527225809")
        # 2 | waitForElementPresent | xpath=//div[@id='root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_mashupcontainer-5_tabsv2-93']/div[2] | 11000
        time.sleep(7)
        # 3 | click | xpath=//div[@id='root_pagemashupcontainer-6_flexcontainer-200-bounding-box']/div[2] | 
        self.driver.find_element(By.XPATH, "//div[@id=\'root_pagemashupcontainer-6_flexcontainer-200-bounding-box\']/div[2]").click()
        # 4 | waitForElementPresent | xpath=//div[@id='root_pagemashupcontainer-6_ContainedMashup-105_flexcontainer-94-bounding-box']/div | 6000
        WebDriverWait(self.driver, 80).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@id=\'root_pagemashupcontainer-6_ContainedMashup-105_flexcontainer-94-bounding-box\']/div")))
        # 5 | click | xpath=//div[@id='root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100-bounding-box']/ptcs-dropdown | 
        self.driver.find_element(By.XPATH, "//div[@id=\'root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100-bounding-box\']/ptcs-dropdown").click()
        # 6 | click | xpath=//body[@id='runtime']/ptcs-list | 
        self.driver.find_element(By.XPATH, "//body[@id=\'runtime\']/ptcs-list").click()
        # 7 | assertText | xpath=//div[@id='root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100-bounding-box']/ptcs-dropdown | Potato Chips
        assert self.driver.find_element(By.XPATH, "//div[@id=\'root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100-bounding-box\']/ptcs-dropdown").text == "Potato Chips"
        # 8 | click | xpath=//div[@id='cell_PlantModelSelectionForNavigation_RepeaterButton-12_ptcsbutton-43-bounding-box']/ptcs-button | 
        self.driver.find_element(By.XPATH, "//div[@id=\'cell_PlantModelSelectionForNavigation_RepeaterButton-12_ptcsbutton-43-bounding-box\']/ptcs-button").click()
        # 9 | waitForElementPresent | xpath=//div[@id='root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_flexcontainer-4-bounding-box']/div | 6000
        WebDriverWait(self.driver, 80).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@id=\'root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_flexcontainer-4-bounding-box\']/div")))
        # 10 | assertElementPresent | xpath=//div[@id='root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_flexcontainer-4-bounding-box']/div | 
        elements = self.driver.find_elements(By.XPATH, "//div[@id=\'root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_flexcontainer-4-bounding-box\']/div")
        assert len(elements) > 0
    
    def test_tC03MPC01DPEfficiencyCapacityWasteandDowntimevalues(self):
        # Test name: TC03_M_PC01_DP_Efficiency, Capacity, Waste and Downtime values
        # Step # | name | target | value
        # 1 | open | https://09384038:ARbg95917284.@meswebgsftmexicali.azure.intra.pepsico.com/Thingworx/Runtime/index.html#master=PepsiCo_Master&mashup=MES_Dashboard&__applyThemeName=PepsiCo%20Default%20Theme&_refreshTS=1670527225809 | 11000
        self.driver.get("https://09384038:ARbg95917284.@meswebgsftmexicali.azure.intra.pepsico.com/Thingworx/Runtime/index.html#master=PepsiCo_Master&mashup=MES_Dashboard&__applyThemeName=PepsiCo%20Default%20Theme&_refreshTS=1670527225809")
        # 2 | waitForElementPresent | xpath=//div[@id='root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_mashupcontainer-5_gridadvanced-109-bounding-box']/div[3] | 11000
        time.sleep(8)
        # 3 | click | xpath=//div[@id='root_pagemashupcontainer-6_flexcontainer-200-bounding-box']/div[2] | 
        self.driver.find_element(By.XPATH, "//div[@id=\'root_pagemashupcontainer-6_flexcontainer-200-bounding-box\']/div[2]").click()
        # 4 | click | xpath=//div[@id='root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100-bounding-box']/ptcs-dropdown | 
        self.driver.find_element(By.XPATH, "//div[@id=\'root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100-bounding-box\']/ptcs-dropdown").click()
        # 5 | click | xpath=//body[@id='runtime']/ptcs-list | 
        self.driver.find_element(By.XPATH, "//body[@id=\'runtime\']/ptcs-list").click()
        # 6 | click | xpath=//div[@id='cell_PlantModelSelectionForNavigation_RepeaterButton-12_ptcsbutton-43-bounding-box']/ptcs-button | 
        self.driver.find_element(By.XPATH, "//div[@id=\'cell_PlantModelSelectionForNavigation_RepeaterButton-12_ptcsbutton-43-bounding-box\']/ptcs-button").click()
        # 7 | waitForElementPresent | css=.tab-container-background-wrapper | 6000
        WebDriverWait(self.driver, 80).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".tab-container-background-wrapper")))
    

    def test_TC03MPC02DPEfficiencyCapacityWasteDowntimevalues(self): 
        self.driver.get(URL)
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
    pytest.main() 
    # testRunner=HtmlTestRunner.HTMLTestRunner(output='Reporte')
