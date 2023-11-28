import json
import pytest
from flask import Flask
from main import app

@pytest.fixture
def client():
    return app.test_client()

def test_get_users(client):
    response = client.get('/users')
    assert response.status_code == 200

def test_add_user(client):
    user_data = {'name': 'John', 'lastname': 'Doe'}
    response = client.post('/users', json=user_data)
    assert response.status_code == 201

def test_get_user_by_id(client):
    response = client.get('/users/1')
    assert response.status_code == 200

def test_patch_user_by_id(client):
    user_data = {'name': 'Updated Name'}
    response = client.patch('/users/1', json=user_data)
    assert response.status_code == 204

def test_update_user_by_id(client):
    user_data = {'name': 'Updated Name', 'age': 30}
    response = client.put('/users/1', json=user_data)
    assert response.status_code == 204

def test_remove_user_by_id(client):
    response = client.delete('/users/1')
    assert response.status_code == 204
