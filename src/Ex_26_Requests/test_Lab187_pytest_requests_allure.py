import pytest
import allure
import requests

@allure.title("TC#1- Verify the GET request.")
@allure.description("Verify that the GET request basically is successful and gives you 200, OK as a status code")
@pytest.mark.positive
def test_get_request():
    url = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url=url)
    assert response_data.status_code == 200


