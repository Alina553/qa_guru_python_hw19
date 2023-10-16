import requests
import jsonschema
from utils import load_schema


def test_get_single_user_status_not_ok():
    response = requests.get(url="https://reqres.in/api/users/23")

    assert (response.status_code == 404)


def test_get_list_status_ok():
    response = requests.get(url="https://reqres.in/api/unknown")

    assert (response.status_code == 200)


def test_param_get_delayed_response_status_ok():
    response = requests.get(url="https://reqres.in/api/users", params={"delay": 3})

    assert (response.status_code == 200)

def test_param_get_users_data_check():
    response = requests.get(url="https://reqres.in/api/users", params={"per_page": 2})

    assert(len(response.json()['data']) == 2)

def test_param_get_users_page_check():
    response = requests.get(url="https://reqres.in/api/users", params={"page":1})

    assert(response.json()['page']) == 1

def test_post_register_successful():
    schema = load_schema('post_register.json')

    response = requests.post(url='https://reqres.in/api/register', json={
    "email": "eve.holt@reqres.in",
    "password": "pistol"
    })

    assert response.status_code == 200
    assert response.json()['id'] == 4
    jsonschema.validate(response.json(), schema)

def test_delete_users():
    response = requests.delete(url="https://reqres.in/api/users/2")

    assert(response.status_code == 204)

def test_post_create_user_successfull():

    schema = load_schema('post_create_user.json')

    response = requests.post(url='https://reqres.in/api/users', json = {
    "name": "morpheus",
    "job": "leader"
    })

    jsonschema.validate(response.json(), schema)
    assert response.status_code == 201
    assert response.json()['job'] == 'leader'

def test_put_update_user():

    schema = load_schema('post_update_user.json')

    response = requests.put(url='https://reqres.in/api/users/2', json = {
    "name": "morpheus",
    "job": "zion resident"
    })

    jsonschema.validate(response.json(), schema)
    assert response.status_code == 200
    assert response.json()['name'] == 'morpheus'


def test_patch_update_user():

    schema = load_schema('post_update_user.json')

    response = requests.put(url='https://reqres.in/api/users/2', json = {
    "name": "morpheus",
    "job": "zion resident"
    })

    jsonschema.validate(response.json(), schema)
    assert response.status_code == 200
    assert response.json()['job'] == 'zion resident'