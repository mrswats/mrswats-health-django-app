import pytest

from django.urls import reverse


@pytest.fixture
def url():
    def _(url_name, **url_kwargs):
        return reverse(url_name, kwargs=url_kwargs)

    return _
