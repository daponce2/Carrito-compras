from selenium import webdriver
import unittest
import XLUtils
import time
from reusable.reusable_Carrito import Compras

class Carrito_Compras (unittest.TestCase):

    def setUp(self):
        print("Inicio de clase Carrito_Compras")
    def test_Carrito(self):

        # Acceso al TestData Excel
        path = "data/Data_Credicorp.xlsx"
        rows = XLUtils.getRowCount(path, 'Data')

        lista = []
        cantidad_errores = 0

        #Optener datos
        fila = 2
        while fila < rows+1:
            try:
                menu = Compras()
                menu.test_bloque_Compras(path, fila, rows)
                fila += 1
            except Exception as e:
                print(e)
                cantidad_errores += 1
                lista.append(fila)
                fila += 1

        #Salto Linea
        print("\n")
        print("------------------------------------")
        print("RESULTADOS DE LA EJECUCION")
        print("------------------------------------")
        print("Total de Casos Exitosos:", (rows-1) - cantidad_errores)
        print("Total de Casos Fallidos:", cantidad_errores)
        print("\n")
        print("LISTA DE CASOS FALLIDOS")
        print("------------------------------------")
        if lista is not None:
            for elemento in lista:
                print("Caso:", elemento - 1)
        else :
            print("No hay casos fallidos")

    def tearDown(self):
        time.sleep(1)
        #driver.quit()

if __name__ == "__main__":
    unittest.main()
