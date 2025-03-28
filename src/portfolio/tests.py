from http import HTTPStatus

import pytest


@pytest.mark.django_db
def test_index_view(client):
    """Testa se a página index está retornando o status code 200.

    Args:
        client (Client): Instância do Django test client
            usada para simular requisições HTTP
    """
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
