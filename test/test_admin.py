from .utils import *
from routers.admin import get_db, get_current_user
from fastapi import status

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_admin_read_all_authenticated(test_todo):
    response = client.get("/admin/todo")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [{'complete':False, 'title':'Practise to code', 'description':'Learn', 'id':1,
                                'priority': 5, 'owner_id':3}]

def test_admin_Delete_todo(test_todo):
    response = client.delete("/admin/todo/1")
    assert response.status_code == 204

    db = TestingSessionLocal()
    model= db.query(Todos).filter(Todos.id==1).first()
    assert model is None

def test_delete_todo_not_found(test_todo):
    response = client.delete("admin/todo/99")
    assert response.status_code == 404
    assert response.json() == {'detail': 'Todo not found'}