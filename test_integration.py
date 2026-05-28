import pytest
from app import app, db


@pytest.fixture(scope='module')
def client():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    with app.test_client() as client:
        yield client


def test_homepage_loads(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'TempConverter' in response.data


def test_conversion_stored_and_displayed(client):
    response = client.post('/', data={'celsius': '100'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'212' in response.data


def test_negative_conversion(client):
    response = client.post('/', data={'celsius': '-40'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'-40' in response.data


def test_empty_input_rejected(client):
    response = client.post('/', data={'celsius': ''}, follow_redirects=True)
    assert response.status_code == 200
