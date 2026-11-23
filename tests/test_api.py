
import requests
import pytest_check as check


def test_obtener_usuario( base_url,  headers):
    url = f"{ base_url}/users/3"

    response = requests.get(url, headers)
    print(response)
    
    # NIVEL 1: STATUS CODE
    codigo = response.status_code
    assert codigo == 200

    # NIVEL 2: HEADERS
    assert "application/json" in response.headers["Content-Type"]

    # NIVEL 3: ESTRUCTURA
    data = response.json()

    assert isinstance(data,dict) # Validar que el contenido sea un diccionario
    assert "data" in data
    assert isinstance(data["data"],dict)

    assert "id" in data["data"]
    assert "email" in data["data"]
    assert "first_name" in data["data"]
    assert "last_name" in data["data"]

    # NIVEL 4: CONTENIDO
    assert data["data"]["id"] == 3
    assert data["data"]["email"] == "emma.wong@reqres.in"

    # NIVEL 5: TIEMPO DE RESPUESTA
    assert response.elapsed.total_seconds() < 5


def test_crear_usuario( base_url,  headers):
    url = f"{ base_url}/users/"

    usuario = {
        "email":"jdmdtg@gmail.com",
        "first_name":"Jose Gilberto",
        "last_name":"Medina",
        "job":"Desarrollador"
    }

    response = requests.post(url,headers= headers,json=usuario)

    # NIVEL 1
    assert response.status_code == 201

    # NIVEL 2
    assert "application/json" in response.headers["Content-Type"]

    # NIVEL 3
    data = response.json()
    check.is_in("email",data) #assert "email" in data
    check.is_in("first_name",data) #assert "first_name" in data
    check.is_in("last_name",data) #assert "last_name" in data
    check.is_in("id",data) #assert "id" in data

    # NIVEL 4
    check.equal(data["email"],usuario["email"]) # assert data["email"] == usuario["email"]
    check.equal(data["first_name"],usuario["first_name"]) # assert data["first_name"] == usuario["first_name"]

    # NIVEL 5: TIEMPO DE RESPUESTA
    assert response.elapsed.total_seconds() < 5

def test_eliminar_usuario( base_url, headers):
    url = f"{ base_url}/users/3"
    
    response = requests.delete(url,headers= headers)
    
    # NIVEL 1: STATUS CODE
    assert response.status_code == 204
    
    # NIVEL 2: HEADERS
    assert "Content-Type" not in response.headers
    
    # NIVEL 3 Y 4: ESTRUCTURA Y CONTENIDO
    assert len(response.content) == 0
    
    # NIVEL 5: TIEMPO DE RESPUESTA
    assert response.elapsed.total_seconds() < 5
    
