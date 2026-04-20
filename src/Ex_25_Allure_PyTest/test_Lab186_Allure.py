import pytest
import allure

@allure.title("Verify the create booking is working")
@allure.description("We are going to verify the create booking is working")
@pytest.mark.positive
def test_create_booking_positive():
    print("test1")
    assert 1-1 == 2

@pytest.mark.negative
def test_create_booking_negative():
    print("test2")
    assert 1+1 == 2

@pytest.mark.negative
def test_create_booking_negative():
    print("test2")
    assert 1+1 == 2