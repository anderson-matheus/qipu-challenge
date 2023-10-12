import os
from unittest import TestCase
import requests
from ais_web import AisWeb, AisWebError
from unittest.mock import Mock, patch

class TestAisWeb(TestCase):
    @patch('ais_web.requests.get')
    def test_get_data_404(self, mock_get):
        mock_response = requests.models.Response()
        mock_get.status_code = 404
        mock_get.return_value = mock_response

        ais_web = AisWeb('ASD123')
        with self.assertRaises(AisWebError):
            ais_web.get_data()


    @patch('ais_web.requests.get')    
    def test_get_data(self, mock_get):
        source = os.path.join(os.path.dirname(__file__), 'source.html')
        f = open(source, 'r')

        mock_response = Mock()
        mock_get.return_value = mock_response
        mock_response.text = f.read()

        ais_web = AisWeb('ASD123')
        result = ais_web.get_data()
        message = [
            '\nAs cartas disponíveis são: \n',
            'Nome: RNP X RWY 18 - Url: https://aisweb.decea.gov.br/download/?arquivo=e5bada5a-2c12-472b-bb5f1e9f5b3f01c1&apikey=1587263166',
            'Nome: RNP Z RWY 18 - Url: https://aisweb.decea.gov.br/download/?arquivo=231cff57-1956-4050-8e8f991fc73e4e23&apikey=1587263166',
            'Nome: RNAV ASETA 1A - KONVI 1A RWY 18 - Url: https://aisweb.decea.gov.br/download/?arquivo=4f06d32d-b737-4da0-abd68e2ee8763a99&apikey=1587263166',
            'Nome: RNAV ASETA 1B - KONVI 1B RWY 36 - Url: https://aisweb.decea.gov.br/download/?arquivo=2808c2de-dd87-4f36-97b3fb0c44a3b90a&apikey=1587263166',
            'Nome: RWY 18/36 - Url: https://aisweb.decea.gov.br/download/?arquivo=cafbd8e6-dd17-4e6f-ad5773b93fe4e759&apikey=1587263166',
            '\n',
            'Nascer do sol: 08:37',
            'Por do sol: 21:11',
            '\n',
            'Taf: 121500Z 1218/1306 17008KT 9999 BKN020 FEW045TCU TX25/1218Z TN18/1305Z TEMPO 1218/1223 15008KT 7000 TSRA BKN030 FEW040CB RMK PGQ=',
            'Metar: 122300Z VRB02KT 9999 FEW045 SCT100 27/17 Q1016=',
        ]

        f.close()
        assert result == '\n'.join(message)