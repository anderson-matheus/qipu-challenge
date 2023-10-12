from unittest import TestCase
from ais_web_app import main
from unittest.mock import patch
from _pytest.monkeypatch import MonkeyPatch


class TestAisWebApp(TestCase):
    def setUp(self):
     self.monkeypatch = MonkeyPatch()

    def test_without_aerodrome_code(self):
        self.monkeypatch.setattr('builtins.input', lambda _: None)
        result = main()
        assert result == '\nCódigo não informado, tente novamente\n'

    @patch('ais_web.AisWeb.get_data')
    def test_not_found_data(self, mock_get_data):
        mock_get_data.side_effect = Exception('error')
        self.monkeypatch.setattr('builtins.input', lambda _: 'ASD123')
        result = main()
        
        assert result == '\nNão foi possível coletar os dados, tente novamente\n'

    @patch('ais_web.AisWeb.get_data')
    def test_with_aerodrome_code(self, mock_get_data):
        message = '\n'.join([
            'As cartas disponíveis',
            'Os horários de nascer e pôr do sol de hoje',
            'A informação de TAF e METAR disponíveis',
        ])
        mock_get_data.return_value = message
        self.monkeypatch.setattr('builtins.input', lambda _: 'SBJD')
        result = main()
        assert result == message