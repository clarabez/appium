import pytest
from pages.vergleich import Vergleich
from pages.tarife import Tarife
import time


@pytest.mark.usefixtures('test_setup')
class TestVerivox(object):
    def test_scenario_one(self, test_setup):
        vergleich = Vergleich(test_setup)
        vergleich.reach_()
        tarife = Tarife(test_setup)
        number_of_tariffs = tarife.how_many_tariffs()
        assert number_of_tariffs >= 5, 'Did not find more than 5 tariffs'

    def test_scenario_two(self, test_setup):
        # vergleich = Vergleich(test_setup)
        # vergleich.reach_()
        pass

    def test_scenario_three(self, test_setup):
        # vergleich = Vergleich(test_setup)
        # vergleich.reach_()
        pass
