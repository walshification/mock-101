from dataclasses import dataclass
from typing import List


SOIL_SAMPLE = "radiation levels nominal"
PERSON_NAME = "Bob"
PERSON_AGE = 38
PERSON_HOBBIES = ["sportsball"]

ACQUAINTANCE_NAME = "Louie"
ACQUAINTANCE_AGE = 44
ACQUAINTANCE_HOBBIES = ["meteorology"]
ACQUAINTANCE_LOGIN = "louie_in_the_clouds"
ACQUAINTANCE_PASSWORD = "2Louie2cloudz"


def simple_chat(person, acquaintance):
    """A friendly encounter?"""
    chit_chat = person.get_chit_chat()
    banter = acquaintance.respond(chit_chat) or ""

    if "rain" in banter:
        return person.poncho_villa_joke()
    elif "sunny" in banter:
        return person.sports_ball_anecdote()
    else:
        raise BackAwaySlowly("I need an adult.")


@dataclass
class BackyardLab:

    login: str
    password: str

    def get_barometric_pressure(self):
        ...

    def track_barometric_pressure(self, pressure):
        ...

    def chart(self, trend):
        ...


@dataclass
class DopplerRadar:

    login: str
    password: str

    def map_sky(self):
        ...


@dataclass
class RadiationSoilTester:

    login: str
    password: str

    def sample(self, soil_sample):
        ...


@dataclass
class FancyWeatherAlgorithm:

    login: str
    password: str

    def assess_possible_weather(self, trend, sky_quality, soil_test):
        ...


class BackAwaySlowly(Exception):
    ...


@dataclass
class Person:

    name: str
    age: int
    hobbies: List[str]

    def get_chit_chat(self):
        return "Hey, how about that weather?"

    def poncho_villa_joke(self):
        return "Call me Villa cuz I'm grabbing my poncho!"

    def sports_ball_anecdote(self):
        return "Sunny day like this reminds me of sportsball ..."


@dataclass
class Acquaintance:

    name: str
    age: int
    hobbies: List[str]
    login: str
    password: str

    def get_lab_results(self):
        lab = BackyardLab(login=self.username, password=self.password)
        barometric_pressure = lab.get_barometric_pressure()
        trend = lab.track_barometric_pressure(barometric_pressure)
        lab.chart(trend)
        return trend

    def get_sky_quality(self):
        radar = DopplerRadar(
            login=self.username, password=self.password
        )
        return radar.map_sky()

    def get_soil_test(self, soil_sample):
        radiation_tester = RadiationSoilTester(
            login=self.username,
            password=self.password
        )
        return radiation_tester.test(soil_sample)  # <-- where did he GET that?

    def calculate_possible_weather(self):
        weather_algo = FancyWeatherAlgorithm(
            login=self.username,
            password=self.password,
        )
        return weather_algo.assess_possible_weather(
            self.get_lab_results(),
            self.get_sky_quality(),
            self.get_soil_test(self.soil_sample),
        )

    def respond(self, chit_chat):
        if "weather" in chit_chat:
            return self.calculate_possible_weather()
        return None
