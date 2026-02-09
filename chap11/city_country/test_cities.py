from city_functions import city_country
def test_city_country():
    santiago_chile = city_country('santigo', 'chile')
    assert santiago_chile == 'santigo, chile'

def test_city_country_population():
    santiago_chile = city_country('santiago', 'chile', 5_000_000)
    assert santiago_chile == 'santiago, chile, - population 5000000'