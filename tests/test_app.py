from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root_deve_retornar_ola_mundo():
    """
    Esse teste tem 3 etapas (AA)
    - A: Arranje - Arranjo
    - A: Act     - Executa (o SUT)
    - A: Assert  - Garante que A é A
    """
    # Arranje
    client = TestClient(app)

    # Act
    response = client.get('/')

    # Assert
    assert response.status_coe == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}
