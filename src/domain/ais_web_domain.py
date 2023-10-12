class AisWebCardDomain:
    def __init__(self, name: str, url: str):
        self.name = name
        self.url = url

class AisWebTimetableDomain:
    def __init__(self, sunrise: str, sunset: str):
        self.sunrise = sunrise
        self.sunset = sunset

class AisWebMetarTafDomain:
    def __init__(self, metar: str = None, taf: str = None):
        self.metar = metar
        self.taf = taf