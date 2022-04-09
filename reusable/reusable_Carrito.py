from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput.keyboard import Key, Controller
from openpyxl import load_workbook

import XLUtils
import time
class Compras:

    def __init__(self):
        # Abrir el explorador Chrome
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        print("Inicio de clase Alta Contrato")
    def test_bloque_Compras(self, path, fila, rows):

        #Abrir el aplicativo demoblaze
        self.driver.get("https://www.demoblaze.com/")
        print("Ingreso a la pagina demoblaze")

        espera = WebDriverWait(self.driver, 6)
        espera_larga = WebDriverWait(self.driver, 30)
        espera_super = WebDriverWait(self.driver, 60)
        keyboard = Controller()

        print("\033[1;31m" + "INICIO PRUEBA CASO: ", fila-1)
        #Leer los datos
        print("------------------------------------")
        caso_id = XLUtils.readData(path, 'Data', fila, 1)
        print("Caso_id: ",caso_id)
        usuario_registrado = XLUtils.readData(path, 'Data', fila, 2)
        print("Usuario registrado: ",usuario_registrado)
        usuario = XLUtils.readData(path, 'Data', fila, 3)
        print("Usuario: ",usuario)
        password = XLUtils.readData(path, 'Data', fila, 4)
        print("Password: ",password)
        descripcion_telefono = XLUtils.readData(path, 'Data', fila, 5)
        print("Descripcion Telefono: ",descripcion_telefono)

        print("------------------------------------")
        time.sleep(1)

        #Validacion de registro
        if usuario_registrado == 'NO':
            #Registrarse
            btn_sign_up = self.driver.find_element_by_xpath("//*[@id='signin2']")
            if btn_sign_up is not None:
                btn_sign_up.click()

            #Ingresar usuario
            ingresa_usuario = espera.until(EC.element_to_be_clickable((By.XPATH,"//div[2]/form/div[1]/input[@id='sign-username']")))
            if ingresa_usuario is not None:
                ingresa_usuario.send_keys(usuario)

            #Ingresar password
            ingresa_password = self.driver.find_element_by_xpath("//*[@id='sign-password']")
            if ingresa_password is not None:
                ingresa_password.send_keys(password)

            #Registrarse
            btn_sign_up_grabar = self.driver.find_element_by_xpath("//*[@id='signInModal']/div/div/div[3]/button[2]")
            if btn_sign_up_grabar is not None:
               btn_sign_up_grabar.click()
               print("Se realizo el registro")

            #Validación de Múltiples alertas
            alerta = True
            while alerta:
               try:
                    alerta = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
                    alerta = self.driver.switch_to.alert
                    time.sleep(0.5)
                    alert_text = alerta.text
                    alerta.accept()
                    print("Alerta:", alert_text)
                    substring_1 = "successful"
                    if substring_1 in alert_text:
                        print("Ultima alerta :", alert_text)
                        break
               except:
                    print("No hay alerta")
                    alerta = False

            time.sleep(2)

            #Loguearse:
            btn_log_in = self.driver.find_element_by_xpath("//*[@id='login2']")
            if btn_log_in is not None:
                btn_log_in.click()

            #Ingresar usuario
            ingresa_usuario = espera.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='loginusername']")))
            if ingresa_usuario is not None:
                ingresa_usuario.send_keys(usuario)

            #Ingresar password
            ingresa_password = self.driver.find_element_by_xpath("//*[@id='loginpassword']")
            if ingresa_password is not None:
                ingresa_password.send_keys(password)

            #Registrarse
            btn_log_in_grabar = self.driver.find_element_by_xpath("//*[@id='logInModal']/div/div/div[3]/button[2]")
            if btn_log_in_grabar is not None:
               btn_log_in_grabar.click()
               print("Se realizo el registro")

            time.sleep(3)
            locator = f".//*[@id='tbodyid']//div/div/h4/a[contains(text(),'{descripcion_telefono}')]"
            print(locator)
            #Seleccionar un producto al carrito
            btn_producto = self.driver.find_element_by_xpath(locator)
            if btn_producto is not None:
                btn_producto.click()

            #agregar al carrito
            btn_add = espera.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='tbodyid']/div[2]/div/a")))
            if btn_add is not None:
                btn_add.click()

        if usuario_registrado == 'SI':
            #Loguearse:
            btn_log_in = self.driver.find_element_by_xpath("//*[@id='login2']")
            if btn_log_in is not None:
                btn_log_in.click()

            #Ingresar usuario
            ingresa_usuario = espera.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='loginusername']")))
            if ingresa_usuario is not None:
                ingresa_usuario.send_keys(usuario)

            #Ingresar password
            ingresa_password = self.driver.find_element_by_xpath("//*[@id='loginpassword']")
            if ingresa_password is not None:
                ingresa_password.send_keys(password)

            #Registrarse
            btn_log_in_grabar = self.driver.find_element_by_xpath("//*[@id='logInModal']/div/div/div[3]/button[2]")
            if btn_log_in_grabar is not None:
               btn_log_in_grabar.click()
               print("Se realizo el registro")

            time.sleep(3)
            locator = f".//*[@id='tbodyid']//div/div/h4/a[contains(text(),'{descripcion_telefono}')]"
            print(locator)
            #Seleccionar un producto al carrito
            btn_producto = self.driver.find_element_by_xpath(locator)
            if btn_producto is not None:
                btn_producto.click()

            #agregar al carrito
            btn_add = espera.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='tbodyid']/div[2]/div/a")))
            if btn_add is not None:
                btn_add.click()

        #Validación de Múltiples alertas
        alerta = True
        while alerta:
           try:
                alerta = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
                alerta = self.driver.switch_to.alert
                time.sleep(0.5)
                alert_text = alerta.text
                alerta.accept()
                print("Alerta:", alert_text)
                substring_1 = "Product added"
                if substring_1 in alert_text:
                    print("Ultima alerta :", alert_text)
                    break
           except:
                print("No hay alerta")
                alerta = False

        #Cerrar
        self.driver.quit()





