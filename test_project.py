import pytest
from project import app


@pytest.fixture
def client():
    return app.test_client()

def test_main(client):
    resp = client.get('/')
    assert resp.status_code == 200

def test_mood(client):
    resp = client.get('/mood')
    assert resp.status_code == 200

def test_genre(client):
    resp = client.get('/genre')
    assert resp.status_code == 200

def test_favorite(client):
    resp = client.get('/favorite')
    assert resp.status_code == 200

def test_laugh(client):
    resp = client.post('/laugh')
    assert resp.status_code == 200

def test_nostalgic(client):
    resp = client.post('/nostalgic')
    assert resp.status_code == 200

def test_thrilled(client):
    resp = client.post('/thrilled')
    assert resp.status_code == 200

def test_learn(client):
    resp = client.post('/learn')
    assert resp.status_code == 200

def test_showgenre(client):
    resp = client.post('/showgenre')
    assert resp.status_code == 200

def test_similar(client):
    resp = client.post('/similar')
    assert resp.status_code == 200
