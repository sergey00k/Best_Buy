import pytest
import products

def test_normal_product():
    iphone11 = products.Product("Iphone 11", price=500, quantity=1000)
    assert iphone11.name ==  "Iphone 11"

def test_invalid_details():
    try:
        iphone11 = products.Product("Iphone 11", price=-90, quantity=-900)
        assert False
    except ValueError as e:
        assert str(e) == "Price and quantity must be greater than 0."
    try:
        iphone11 = products.Product("", price=90, quantity=900)
        assert False
    except ValueError as e:
        assert str(e) == "Name must not be empty."
    try:
        iphone11 = products.Product("Iphone", price="90", quantity=900)
        assert False
    except ValueError as e:
        assert str(e) == "Invalid input type when creating new product."

def test_quantity_0():
    iphone11 = products.Product("Iphone 11", price=500, quantity=1000)
    iphone11.set_quantity(0)
    assert iphone11.is_active() == False

def test_buying():
    iphone11 = products.Product("Iphone 11", price=500, quantity=1000)
    assert iphone11.buy(10) == 5000
    assert iphone11.quantity == 990
    try:
        iphone11.buy(10000) 
        assert False
    except ValueError as e:
        assert str(e) ==  "Chosen quantity exceeds amount available in stock."


pytest.main()