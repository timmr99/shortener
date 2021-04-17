import pytest

import os

import requests

from shortener_app.utils import *

@pytest.fixture
def flask_url():
    return 'http://127.0.0.1:5000/'

@pytest.fixture
def file_location():
    return 'shortened.json'

def test_default_url(flask_url):
    response = requests.get(flask_url)
    assert response.status_code == 200
    assert response.text == 'Good'


def test_version_url(flask_url):
    ver_url = flask_url + 'version'
    response = requests.get(ver_url)
    assert response.status_code == 200
    assert response.text == '0.0.1'


def test_encode_url(flask_url):
    test_url = flask_url + '/url=http://google.com'
    response = requests.post(test_url)
    expected = flask_url + 'AEY3dXZNHm76Sbzu6oENjw'
    assert expected == response.text


def test_encode_url2(flask_url):
    test_url = flask_url + '/url=http://yahoo.com'
    response = requests.post(test_url)
    expected = flask_url + 'UoMypncGznJxe6tWUvUASE'
    assert expected == response.text


def test_decode_url(flask_url):
    test_url = flask_url + 'AEY3dXZNHm76Sbzu6oENjw'
    response = requests.get(test_url)
    expected = 'http://google.com'
    assert expected == response.text


# run this test after one of the encode tests have run
def test_for_file(file_location):
    assert os.path.isfile(file_location)

