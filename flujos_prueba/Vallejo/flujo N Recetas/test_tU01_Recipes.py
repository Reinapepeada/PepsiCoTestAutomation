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
import sys, os

p = os.path.abspath("../..")
sys.path.insert(1, p)
from externalLibraries import convertTo

p = os.path.abspath("..")
sys.path.insert(1, p)
from utilities.ligasPlanta import LIGAPRINCIPAL, PLANTA


class TestTC01Recipes:
    def setup_method(self, method):
        ChromeoOptions = webdriver.ChromeOptions()
        ChromeoOptions.add_argument("--ignore-certificate-errors")
        ChromeoOptions.add_argument("--ignore-ssl-errors")
        ChromeoOptions.add_argument("--start-maximized")
        ChromeoOptions.add_argument("--disable-extensions")
        ChromeoOptions.add_argument("--disable-gpu")
        ChromeoOptions.add_argument("--disable-dev-shm-usage")
        ChromeoOptions.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(options=ChromeoOptions)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_tC01Recipes(self):
        # Test name: TC02_M_PC04_DP_Entity Selection left slider
        # 1 | open | https://09384038:ARbg95917284.@meswebgsftmexicali.azure.intra.pepsico.com/Thingworx/Runtime/index.html#master=PepsiCo_Master&mashup=MES_Dashboard&__applyThemeName=PepsiCo%20Default%20Theme&_refreshTS=1670527225809 |
        self.driver.get(LIGAPRINCIPAL)
        # 2 | waitForElementPresent | xpath=//div[@id='root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_mashupcontainer-5_gridadvanced-109-bounding-box']/div[3] | 11000
        # WebDriverWait(self.driver, 100).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@id=\'root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_mashupcontainer-5_gridadvanced-109-bounding-box\']/div[3]")))
        time.sleep(10)
        # 3 | click | xpath=//div[@id='root_pagemashupcontainer-6_flexcontainer-200-bounding-box']/div[2] |
        self.driver.find_element(
            By.XPATH,
            "//div[@id='root_pagemashupcontainer-6_flexcontainer-200-bounding-box']/div[2]",
        ).click()
        time.sleep(3)
        # 4 | click | xpath=//div[@id='root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100-bounding-box']/ptcs-dropdown |
        self.driver.find_element(
            By.XPATH,
            "/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/ptcs-dropdown[1]",
        ).click()
        time.sleep(4)
        # 5 | click | xpath=//body[@id='runtime']/ptcs-list |
        jsPathPotato = 'document.querySelector("#root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100-external-wc").shadowRoot.querySelector("#chunker > div > div > ptcs-list-item:nth-child(4) > ptcs-div")'
        self.driver.execute_script(f"return {jsPathPotato}").click()
        # 7 | assertElementPresent | id=root_pagemashupcontainer-6_ContainedMashup-105_ptcsdropdown-100 |
        time.sleep(3)
        # 6 | click | xpath=//div[@id='cell_PlantModelSelectionForNavigation_RepeaterButton-12_ptcsbutton-43-bounding-box']/ptcs-button |
        self.driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div[3]/div/div[2]/div/div/div[2]/div/div[3]/div/div[2]/div/div/div[3]/div/div[1]/div/div[2]/div/div/div[2]/div/div[3]/div/div/ptcs-button",
        ).click()
        time.sleep(5)
        # 10 | assertElementPresent | xpath=//div[@id='root_pagemashupcontainer-6_ContainedMashup-13_ContainedMashup-75_flexcontainer-4-bounding-box']/div |
        # click en el dropdown de reportes
        self.driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/ul/li[2]/table/tbody/tr/td/div/a",
        ).click()
        time.sleep(2)
        # ----------------------
        # 11 click en Recetas incompletas li
        self.driver.find_element(
            By.XPATH, "/html/body/ul[2]/li[7]/table/tbody/tr/td/div/a/span"
        ).click()
        time.sleep(6)
        # reporte de recetas = [] con enunciados
        reporteRecetas = [
            [
                "SKU",
                "Description",
                "Name Plate",
                "Bag Nominal W",
                "Seasoning Level",
                "Bags Case",
                "Sleeves Case",
                "Sleeves Bags",
                "Fryer Asignment",
                "UOM",
                "Oil Level",
                "Familia",
            ]
        ]

        # 12 obtengo el numero de elementos
        itemPath = 'document.querySelector("#root_pagemashupcontainer-6_ptcsdropdown-49-external-wc").shadowRoot.querySelector("#chunker > div > div > ptcs-list-item:nth-child'
        # selecciono item:
        for i in range(1, 20):
            try:
                # 13 busco cuantos elementos tengo el el drop down de recetas por su js path
                jsDropdown = 'document.querySelector("#root_pagemashupcontainer-6_ptcsdropdown-49").shadowRoot.querySelector("#select")'
                # 14 hago click en el dropdown
                self.driver.execute_script(f"return {jsDropdown}").click()
                time.sleep(3)
                familia = self.driver.execute_script(
                    f'return document.querySelector("#root_pagemashupcontainer-6_ptcsdropdown-49-external-wc").shadowRoot.querySelector("#chunker > div > div > ptcs-list-item:nth-child({i}) > ptcs-div > ptcs-label").shadowRoot.querySelector("#label")'
                ).text
                # 15 hago click en el item
                self.driver.execute_script(
                    f'return {itemPath}({i}) > ptcs-div")'
                ).click()
                time.sleep(5)
                # 16 analizo la tabla
                tablePath = "/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div/div[3]/div/div/div[2]/div/div[3]/div/div/div[3]/div[2]/div[2]/table/tbody"
                # 17 obtengo el numero de filas
                fila = len(self.driver.find_elements(By.XPATH, f"{tablePath}/tr"))
                # 18 recorro las filas si es que hay
                if fila > 1:
                    for f in range(2, fila + 1):
                        sku = self.driver.find_element(
                            By.XPATH, f"{tablePath}/tr[{f}]/td[1]"
                        ).text
                        description = self.driver.find_element(
                            By.XPATH, f"{tablePath}/tr[{f}]/td[2]"
                        ).text
                        namePlate = self.driver.find_element(
                            By.XPATH, f"{tablePath}/tr[{f}]/td[3]"
                        ).text
                        bagNominalW = self.driver.find_element(
                            By.XPATH, f"{tablePath}/tr[{f}]/td[4]"
                        ).text
                        seasoningLevel = self.driver.find_element(
                            By.XPATH, f"{tablePath}/tr[{f}]/td[5]"
                        ).text
                        bagsCase = self.driver.find_element(
                            By.XPATH, f"{tablePath}/tr[{f}]/td[6]"
                        ).text
                        sleevesCase = self.driver.find_element(
                            By.XPATH, f"{tablePath}/tr[{f}]/td[7]"
                        ).text
                        sleevesBags = self.driver.find_element(
                            By.XPATH, f"{tablePath}/tr[{f}]/td[8]"
                        ).text
                        fryerAsignment = self.driver.find_element(
                            By.XPATH, f"{tablePath}/tr[{f}]/td[9]"
                        ).text
                        uom = self.driver.find_element(
                            By.XPATH, f"{tablePath}/tr[{f}]/td[10]"
                        ).text
                        oilLevel = self.driver.find_element(
                            By.XPATH, f"{tablePath}/tr[{f}]/td[11]"
                        ).text

                        # 19 agrego los datos a la lista
                        reporteRecetas.append(
                            [
                                sku,
                                description,
                                namePlate,
                                bagNominalW,
                                seasoningLevel,
                                bagsCase,
                                sleevesCase,
                                sleevesBags,
                                fryerAsignment,
                                uom,
                                oilLevel,
                                familia,
                            ]
                        )
            except:
                break

        # 20 hago click en administrador drop down que esta en el nav
        self.driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/ul/li[3]/table/tbody/tr/td/div/a/span",
        ).click()
        time.sleep(2)
        # 21 hago click en el boton de products maintenance
        self.driver.find_element(
            By.XPATH, "/html/body/ul[2]/li[2]/table/tbody/tr/td/div/a/span"
        ).click()
        time.sleep(20)
        # 22 declaro el path de la tabal de la cual voy a sacar el total de productos de la planta
        tablePath = "/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div/div[3]/div/div/div[2]/div/div[3]/div/div[1]/div/div[2]/div/div[1]/div/div/div[3]/div[2]/div[2]/table/tbody"

        # 23 obtengo el numero de filas
        fila = len(self.driver.find_elements(By.XPATH, f"{tablePath}/tr"))
        # 24 declaro la lista de productos
        productos = [["ID_Producto", "Descripcion", "Familia"]]
        # 25 recorro las filas si es que hay
        if fila > 1:
            for f in range(2, fila + 1):
                # 26 obtengo el nombre del producto
                productoID = self.driver.find_element(
                    By.XPATH, f"{tablePath}/tr[{f}]/td[1]"
                ).text
                productoDescripcion = self.driver.find_element(
                    By.XPATH, f"{tablePath}/tr[{f}]/td[2]"
                ).text
                familiaProducto = self.driver.find_element(
                    By.XPATH, f"{tablePath}/tr[{f}]/td[3]"
                ).text
                
                print(productoID)
                # si el id del producto es el mismo que la descripcion o es unknown o Unknown no lo agrego a la lista
                if '300' in productoID and productoID != productoDescripcion and productoID.isdigit():
                    print(productoID)
                    productos.append([productoID, productoDescripcion, familiaProducto])
                
                


        # depuracion de datos de recetas incompletas (si no esta en el tota de productos se trata de un error y lo sacamos de la lista)
        for i in range(len(reporteRecetas) - 1, 0, -1):
            if reporteRecetas[i][0] not in [x[0] for x in productos[1:]]:
                reporteRecetas.pop(i)

        # Comprobar si hay errores
        # name=convertTo.createWord(errores, 'TC03MPC02DPEfficiencyCapacityWasteandDowntimevalues',equiposNoFuncionando,equiposFuncionando)
        # convertTo.convertToPdf(name)
        # buscar el path de la carpeta donde se encuentra el archivo

        pathOG = os.path.dirname(os.path.abspath(__file__))

        # creo el path del archivo para el power bi

        path = pathOG + "/tables/recetas_" + PLANTA + ".xlsx"
        path2 = (
            pathOG + "/tables/totalProductos_" + PLANTA + ".xlsx"
        )  # creo el path reporte de excel con fecha y hora
        variable = time.strftime("%Y-%m-%d_%H-%M-%S")

        pathExcel = (
            pathOG + "/reportOutput/ReporteIncompletasRecetas" + str(variable) + ".xlsx"
        )
        pathExcel2 = pathOG + "/reportOutput/ReporteProductos" + str(variable) + ".xlsx"

        # creo el archivo de excel
        convertTo.creartablaExcel(reporteRecetas, path, "Recipes_" + PLANTA)
        convertTo.creartablaExcel(productos, path2, "Productos_" + PLANTA)
        convertTo.creartablaExcel(reporteRecetas, pathExcel, "Recipes_" + PLANTA)
        convertTo.creartablaExcel(productos, pathExcel2, "Productos_" + PLANTA)

        assert len(reporteRecetas) < 1, reporteRecetas


if __name__ == "__main__":
    pytest.main()
