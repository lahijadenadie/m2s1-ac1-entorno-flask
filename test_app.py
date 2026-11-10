import unittest
from app import app

class PruebasApp(unittest.TestCase):

    def setUp(self):
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['TESTING'] = True
        self.cliente = app.test_client()

    def test_pagina_principal(self):
        respuesta = self.cliente.get("/")
        self.assertEqual(respuesta.status_code, 302)

    def test_pagina_inexistente(self):
        respuesta = self.cliente.get("/no‑existe")
        self.assertEqual(respuesta.status_code, 404)

    def test_cargar_login(self):
        respuesta = self.cliente.get("/login")
        self.assertEqual(respuesta.status_code, 200)

    def test_login_vacio(self):
        respuesta = self.cliente.post("/login", data={})
        self.assertEqual(respuesta.status_code, 200)

    def test_login_datos_malos(self):
        datos = {"correo": "prueba@mal", "contraseña": "123"}
        respuesta = self.cliente.post("/login", data=datos)
        self.assertEqual(respuesta.status_code, 200)

if __name__ == "__main__":
    unittest.main()