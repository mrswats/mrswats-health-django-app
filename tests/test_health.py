from http import HTTPStatus

import pytest


@pytest.fixture
def health_url(url):
    return url("health")


@pytest.fixture
def get_health(client, health_url):
    def _():
        return client.get(health_url)

    return _


def test_health_url(health_url):
    assert health_url == "/_health/"


@pytest.mark.django_db
def test_health_endpoint_status_code(get_health):
    response = get_health()
    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_health_endpoint_data(get_health):
    response = get_health()
    assert response.json() == {"health": "ok"}
