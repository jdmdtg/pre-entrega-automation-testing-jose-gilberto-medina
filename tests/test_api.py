
import requests
import pytest_check as check
from utils.logger import logger

def test_obtener_usuario( base_url,  headers):
    url = f"{ base_url}/users/3"

    response = requests.get(url, headers)
    print(response)
    
    # VALIDAMOS STATUS CODE
    codigo = response.status_code
    assert codigo == 200

    # PREPARAMOS LA CANBECERA
    assert "application/json" in response.headers["Content-Type"]

    # ESTRUCTURA
    data = response.json()
    
    # Validar que el contenido sea un diccionario
    assert isinstance(data,dict) 
    assert "data" in data
    assert isinstance(data["data"],dict)

    assert "id" in data["data"]
    assert "email" in data["data"]
    assert "first_name" in data["data"]
    assert "last_name" in data["data"]

    # CONTENIDO
    assert data["data"]["id"] == 3
    assert data["data"]["email"] == "emma.wong@reqres.in"

    # Espera
    assert response.elapsed.total_seconds() < 5


def test_crear_usuario( base_url,  headers):
    try:
        
        url = f"{ base_url}/users/"

        usuario = {
            "email":"jdmdtg@gmail.com",
            "first_name":"Jose Gilberto",
            "last_name":"Medina",
            "job":"Desarrollador"
        }

        response = requests.post(url,headers= headers,json=usuario)

        # VALIDAMOS EL CODIGO DE RESPUESTA.
        assert response.status_code == 201

        # VALIDAMOS
        assert "application/json" in response.headers["Content-Type"]

        # OBTENEMOS EL OBJ DE RESPUESTA
        data = response.json()
        check.is_in("email",data) 
        check.is_in("first_name",data) 
        check.is_in("last_name",data)
        check.is_in("id",data) 

        # NIVEL 4
        check.equal(data["email"],usuario["email"]) 
        check.equal(data["first_name"],usuario["first_name"]) 

        # NIVEL 5: TIEMPO DE RESPUESTA
        assert response.elapsed.total_seconds() < 5
    except Exception:
        logger.exception("Error durante la prueba de Inventario.")
        raise
        
def test_eliminar_usuario( base_url, headers):
    try:
        url = f"{ base_url}/users/2"
        
        response = requests.delete(url,headers= headers)
        
        # NIVEL 1: STATUS CODE
        assert response.status_code == 204
        
        # NIVEL 2: HEADERS
        assert "Content-Type" not in response.headers
        
        # NIVEL 3 Y 4: ESTRUCTURA Y CONTENIDO
        assert len(response.content) == 0
        
        # NIVEL 5: TIEMPO DE RESPUESTA
        assert response.elapsed.total_seconds() < 2
    except Exception:
        logger.exception("Error durante la prueba de Inventario.")
        raise
