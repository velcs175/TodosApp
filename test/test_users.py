from .utils import *
from routers.users import get_db, get_current_user
from fastapi import status

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


def test_return_user(test_user):
    response = client.get("/user")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() is None
    # data=response.json()
    # todo= data[0]
    # assert todo['username'] == 'vel'
    # assert response.json()["email"] == 'vel@gmail.com'
    # assert response.json()["first_name"] == 'Vel'
    # assert response.json()["last_name"] == 'Sankar'
    # assert response.json()["role"]== "admin"
    # assert response.json()["phone_number"] == '9999944444'

def test_change_password(test_user):
    response= client.put("/user/password", json= {"password": "pass123", "new_password":"pass456"})
    assert response.status_code == status.HTTP_204_NO_CONTENT

def test_change_password_invalid_current_password(test_user):
    response= client.put("/user/password", json={"password": 'wrongpass', "newpassword":"pass456"})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {'detail': 'Error on password change'}

def test_change_phone_number(test_user):
    response = client.put("/user/phonenumber/2222222222")
    assert response.status_code == status.HTTP_204_NO_CONTENT
