from routers.todos import get_db,get_current_user
from fastapi import status
import pytest
from models import Todos
from .utils import *

app.dependency_overrides[get_db]= override_get_db
app.dependency_overrides[get_current_user]= override_get_current_user


def test_read_all_authenticated(test_todo):
    response =client.get("/todos")
    assert response.status_code == status.HTTP_200_OK
    # assert response.json() == [{'title':'Practise to code', 'description':'Learn', 'priority':5,'complete':False, 'owner_id':3}]
    data=response.json()
    todo= data[0]
    assert todo['title'] == 'Practise to code'
    assert todo['description'] == 'Learn'
    assert todo['priority'] == 5
    assert todo['complete'] is False
    assert todo['owner_id'] == 3

def test_read_todo_authenticated(test_todo):
    response =client.get("/todos/todo/1")
    assert response.status_code == status.HTTP_200_OK
    # assert response.json() == [{'title':'Practise to code', 'description':'Learn', 'priority':5,'complete':False, 'owner_id':3}]
    todo=response.json()
    # todo= data[0]
    assert todo['title'] == 'Practise to code'
    assert todo['description'] == 'Learn'
    assert todo['priority'] == 5
    assert todo['complete'] is False
    assert todo['owner_id'] == 3

def test_read_todo_not_found():
    response=client.get("/todos/todo/99")
    assert response.status_code == 404
    assert response.json() == { 'detail': 'Todo not found'}

def test_create_todo(test_todo):
    request_data= {
        'title': 'New todo',
        'description': 'New todo item',
        'priority': 5,
        'complete': False
    }
    response = client.post("/todos/todo", json=request_data)
    assert response.status_code == 201

    db =TestingSessionLocal()
    model= db.query(Todos).filter(Todos.id == 2).first()
    assert model.title== request_data.get('title')
    assert model.description== request_data.get('description')
    assert model.priority== request_data.get('priority')
    assert model.complete == request_data.get('complete')

def test_update_todo(test_todo):
    request_data={
        'title': 'Change title of todo already saved',
        'description': 'Need to learn',
        'priority': 4,
        'complete': False
    }
    response = client.put("/todos/todo/1", json=request_data)
    assert response.status_code == 204
    db =TestingSessionLocal()
    model= db.query(Todos).filter(Todos.id == 1).first()
    assert model.title== request_data.get('title')

def test_update_todo_not_found(test_todo):
    request_data={
        'title': 'Change title of todo already saved',
        'description': 'Need to learn',
        'priority': 4,
        'complete': False
    }       
    response= client.put("/todos/todo/99", json=request_data)
    assert response.status_code == 404
    assert response.json() == {'detail': 'Todo not found'}    

def test_delete_todo(test_todo):
    response= client.delete("/todos/todo/1")
    assert response.status_code==204
    db =TestingSessionLocal()
    model= db.query(Todos).filter(Todos.id == 1).first()
    assert model is None

def test_delete_todo_not_found(test_todo):
    response= client.delete("/todos/todo/99")
    assert response.status_code == 404
    assert response.json() == {'detail': 'Todo not found'}