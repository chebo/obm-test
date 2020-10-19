import requests


def test_get_locations_for_us_90210_check_status_code_equals_200():
    response = requests.get("http://api.zippopotam.us/us/90210")
    assert response.status_code == 200


def test_get_locations_for_us_90210_check_content_type_equals_json():
    response = requests.get("http://api.zippopotam.us/us/90210")
    assert response.headers['Content-Type'] == "application/json"


def test_get_locations_for_us_90210_check_country_equals_united_states():
    response = requests.get("http://api.zippopotam.us/us/90210")
    response_body = response.json()
    assert response_body["country"] == "United States"