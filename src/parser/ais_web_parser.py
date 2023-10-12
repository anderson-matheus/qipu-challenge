from bs4 import BeautifulSoup
from typing import List
from domain.ais_web_domain import (
    AisWebCardDomain,
    AisWebTimetableDomain,
    AisWebMetarTafDomain,
)

class AisWebParser:
    def __init__(self, html: str):
        self.html = html
        self.soup = BeautifulSoup(html, 'html.parser')

    def get_cards(self) -> List[AisWebCardDomain]:
        cards = []        
        uls = self.soup.find_all(
            'ul', {'class': 'list list-icons list-primary list-icons-style-2'})
        
        for ul in uls:
            for li in ul.find_all('li'):
                cards.append(AisWebCardDomain(
                    li.find('a').contents[0],
                    li.find('a').get('href')
                ))
        return cards
    
    def get_timetable(self) -> AisWebTimetableDomain:
        return AisWebTimetableDomain(
            self.soup.find('sunrise').text,
            self.soup.find('sunset').text
        )

    def get_metar_taf(self) -> AisWebMetarTafDomain:
        anchor = self.soup.find_all(id='met')[-1]

        metar_element = metar = anchor.find_next('h5').find_next('p')
        taf = ''
        metar = ''

        if len(metar_element.contents) > 0:
            metar = metar_element.contents[0]

        if len(metar_element.find_next('h5').find_next('p').contents) > 0:
            taf = metar_element.find_next('h5').find_next('p').contents[0]

        return AisWebMetarTafDomain(
            metar, taf
        )