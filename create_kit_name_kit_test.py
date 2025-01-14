import sender_stand_request
import data
from sender_stand_request import auth_token


def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

def positive_assert(name):
    kit_body = get_kit_body(name)
    user = sender_stand_request.post_new_user(data.user_body)
    auth_token = user.json()["authToken"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body,auth_token)
    assert kit_response.status_code == 201
    assert kit_response.json().get("name") == name

def negative_assert(name):
    kit_body = get_kit_body(name)
    user = sender_stand_request.post_new_user(data.user_body)
    auth_token = user.json()["authToken"]
    response = sender_stand_request.post_new_client_kit(kit_body,auth_token)
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "El nombre que ingresaste es incorrecto. " \
                                         "Los nombres deben tener al menos 1 caracter y no más de 512 caracteres"

def negative_assert_no_name(kit_body):
    name = kit_body.get('name', '')
    user = sender_stand_request.post_new_user(data.user_body)
    auth_token = user.json()["authToken"]
    response = sender_stand_request.post_new_client_kit(name,auth_token)
    assert name == "", f"Expected 'name' to be an empty string, but got: {name}"
    assert response.status_code == 400

#Prueba 1 Nombre con una letra
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")

#Prueba 2 Nombre con 511 letras
def test_create_kit_511_letters_in_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

#Prueba 3 Nombre con 0 letras
def test_create_kit_0_letters_in_name_get_error_response():
    negative_assert("")

#Prueba 4 Nombre con 512 letras
def test_create_kit_512_letters_in_name_get_error_response():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

#Prueba 5 Nombre con caracteres especiales
def test_create_kit_special_letters_in_name_get_success_response():
    positive_assert("№%@")


#Prueba 6 Nombre con espacios
def test_create_kit_spaces_in_name_get_success_response():
    positive_assert(" A Aaa" )


#Prueba 7 Nombre con números
def test_create_kit_numbers_in_name_get_success_response():
    positive_assert("123")

#Prueba 8 Nombre vacío con cuerpo ya definido
def test_create_kit_empty_name_get_error_response():
    kit_body = get_kit_body("")
    negative_assert_no_name(kit_body)

#Prueba 9 Nombre numérico
def test_create_kit_number_type_name_get_error_response():
    kit_body = get_kit_body(123)
