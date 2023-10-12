from parser.ais_web_parser import AisWebParser
import os
from dotenv import load_dotenv
import requests
import re
from typing import List
from domain.ais_web_domain import (
    AisWebCardDomain,
    AisWebTimetableDomain,
    AisWebMetarTafDomain,
)

load_dotenv()

class AisWebError(Exception):
    pass

class AisWeb:
    def __init__(self, aerodrome_code: str):
        self.aerodrome_code = aerodrome_code
        self.url = os.getenv('AIS_WEB_URL')
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
        }

    def get_data(self) -> str:
        html = self._get_html()
        ais_web_parser = AisWebParser(html)

        cards_domain = ais_web_parser.get_cards()
        timetable_domain = ais_web_parser.get_timetable()
        metar_taf_domain = ais_web_parser.get_metar_taf()

        return self._build_message(
            cards_domain=cards_domain,
            timetable_domain=timetable_domain,
            metar_taf_domain=metar_taf_domain,
        )
    
    def _build_message(
        self,
        cards_domain: List[AisWebCardDomain],
        timetable_domain: AisWebTimetableDomain,
        metar_taf_domain: AisWebMetarTafDomain,
    ) -> str:
        message = []
        message.append('\nAs cartas disponíveis são: \n')
        for card_domain in cards_domain:
            message.append(
                'Nome: {name} - Url: {url}'.format(
                    name=card_domain.name,
                    url=card_domain.url
                )
            )

        message.append('\n')
        message.append('Nascer do sol: {sunrise}'.format(
            sunrise=timetable_domain.sunrise
        ))
        message.append('Por do sol: {sunset}'.format(
            sunset=timetable_domain.sunset
        ))

        message.append('\n')
        message.append('Taf: {taf}'.format(
            taf=metar_taf_domain.taf
        ))
        message.append('Metar: {metar}'.format(
            metar=metar_taf_domain.metar
        ))
        return '\n'.join(message)
        
    def _get_html(self) -> str:
        url = '{url}?i=aerodromos&codigo={code}'.format(
            url=self.url,
            code=self.aerodrome_code,
        )
        try:
            r = requests.get(url, headers=self.headers)
            r.raise_for_status()
            return r.text
        except Exception as e:
            raise AisWebError(e)
