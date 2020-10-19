import requests


def test_get_projects_status_code_equals_200():
    response = requests.get("https://entryit-api.herokuapp.com/api/projects")
    assert response.status_code == 200


def test_get_projects_check_content_type_equals_json():
    response = requests.get("https://entryit-api.herokuapp.com/api/projects")
    assert response.headers['Content-Type'] == "application/json"


def test_check_projects_data_type():
    response = requests.get("https://entryit-api.herokuapp.com/api/projects")
    response_body = response.json()
    assert type(response_body["data"]) == list