import json
import pytest
from unittest.mock import mock_open, patch
from definitions import get_data,find_first_free_id,insert_user, remove_user,patch_user,check_data
import flask



def test_get_data(mocker):
    mock_file_open = mocker.patch("builtins.open", mock_open(read_data='[{"id": 1,"name":"John","lastname":"doe"}]'))

    mocker.patch("json.load", return_value=[{"id": 1,"name":"John","lastname":"doe"}])

    result = get_data()

    mock_file_open.assert_called_once_with('data.json', 'r')

    assert result == [{"id": 1,"name":"John","lastname":"doe"}]

def test_get_data_with_id(mocker):
    mock_file_open = mocker.patch("builtins.open", mock_open(read_data='[{"id": 1,"name":"John","lastname":"doe"},{"id": 2,"name":"Pomidor","lastname":"Lama"}]'))

    mocker.patch("json.load", return_value=[{"id": 1,"name":"John","lastname":"doe"},{"id": 2,"name":"Pomidor","lastname":"Lama"}])

    result = get_data(2)

    mock_file_open.assert_called_once_with('data.json', 'r')


    assert result == {"id": 2,"name":"Pomidor","lastname":"Lama"}

def test_find_first_free_id(mocker):
    mock_file_open = mocker.patch("builtins.open", mock_open(read_data='[{"id": 1,"name":"John","lastname":"doe"},{"id": 3,"name":"Pomidor","lastname":"Lama"}]'))

    mocker.patch("json.load", return_value=[{"id": 1,"name":"John","lastname":"doe"},{"id": 3,"name":"Pomidor","lastname":"Lama"}])

    result = find_first_free_id()

    mock_file_open.assert_called_once_with('data.json', 'r')


    assert result == 2

def test_insert_user(mocker):
    mock_file_open = mocker.patch("builtins.open", mock_open(read_data='[{"id": 1,"name":"John","lastname":"doe"},{"id": 3,"name":"Pomidor","lastname":"Lama"}]'))

    mocker.patch("json.load", return_value=[{"id": 1,"name":"John","lastname":"doe"},{"id": 3,"name":"Pomidor","lastname":"Lama"}])

    insert_user({"name":"AAAAAAA","lastname":"BBBBB"})

    f = open('data.json','r')
    d = json.load(f)
    f.close()
    assert d==[{"id": 1,"name":"John","lastname":"doe"},{"id": 3,"name":"Pomidor","lastname":"Lama"},{"id": 2,"name":"AAAAAAA","lastname":"BBBBB"}]


def test_insert_user_with_id(mocker):
    mock_file_open = mocker.patch("builtins.open", mock_open(read_data='[{"id": 1,"name":"John","lastname":"doe"},{"id": 3,"name":"Pomidor","lastname":"Lama"}]'))

    mocker.patch("json.load", return_value=[{"id": 1,"name":"John","lastname":"doe"},{"id": 3,"name":"Pomidor","lastname":"Lama"}])

    insert_user({"name":"AAAAAAA","lastname":"BBBBB"},20)

    f = open('data.json','r')
    d = json.load(f)
    f.close()
    assert d==[{"id": 1,"name":"John","lastname":"doe"},{"id": 3,"name":"Pomidor","lastname":"Lama"},{"id": 20,"name":"AAAAAAA","lastname":"BBBBB"}]

def test_remove_user(mocker):
    mock_file_open = mocker.patch("builtins.open", mock_open(read_data='[{"id": 1,"name":"John","lastname":"doe"},{"id": 3,"name":"Pomidor","lastname":"Lama"}]'))

    mocker.patch("json.load", return_value=[{"id": 1,"name":"John","lastname":"doe"},{"id": 3,"name":"Pomidor","lastname":"Lama"}])

    remove_user(1)

    f = open('data.json','r')
    d = json.load(f)
    f.close()
    assert d==[{"id": 3,"name":"Pomidor","lastname":"Lama"}]


def test_patch_user(mocker):
    mock_file_open = mocker.patch("builtins.open", mock_open(read_data='[{"id": 1,"name":"John","lastname":"doe"},{"id": 3,"name":"Pomidor","lastname":"Lama"}]'))

    mocker.patch("json.load", return_value=[{"id": 1,"name":"John","lastname":"doe"},{"id": 3,"name":"Pomidor","lastname":"Lama"}])

    patch_user(1,{"name":"pomidor"})

    f = open('data.json','r')
    d = json.load(f)
    f.close()
    assert d==[{"id": 1,"name":"pomidor","lastname":"doe"},{"id": 3,"name":"Pomidor","lastname":"Lama"}]
