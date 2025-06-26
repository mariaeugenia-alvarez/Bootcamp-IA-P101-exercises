from zoo_hof.invoice import generate_invoice
from zoo_hof.price_theater import generate_get_price_theater
from zoo_hof.price_zoo import generate_get_price_zoo


def test_solution():
    # Test zoo
    assert generate_invoice([4], generate_get_price_zoo) == 8

    # Test thether
    assert generate_invoice([4], generate_get_price_theater) == 4
