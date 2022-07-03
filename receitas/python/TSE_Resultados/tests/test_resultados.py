import pytest

from pages.home import Home
from pages.welcome import Initial


@pytest.mark.usefixtures('test_setup')
class TestResultados(object):
    def test_fluxo_inicial(self, test_setup):
        initial = Initial(test_setup)
        initial.realizar_fluxo_inicial()
        # is_in_home = initial.is_is_home_screen()
        # assert is_in_home, 'Não alcançou home'

    def test_one(self):
        pass

    def test_two(self):
        pass