from dataclasses import dataclass
from typing import List


SOIL_SAMPLE = "radiation levels nominal"
PERSON_NAME = "Bob"
PERSON_AGE = 38
PERSON_HOBBIES = ["sportsball"]

ACQUAINTANCE_NAME = "Louie"
ACQUAINTANCE_AGE = 44
ACQUAINTANCE_HOBBIES = ["meteorology"]
ACQUAINTANCE_USERNAME = "louie_in_the_clouds"
ACQUAINTANCE_PASSWORD = "2Louie2cloudz"


def simple_chat():
    """A friendly encounter?"""
    banter = []

    person = Person(
        name=PERSON_NAME,
        age=PERSON_AGE,
        hobbies=PERSON_HOBBIES,
    )
    acquaintance = Acquaintance(
        name=ACQUAINTANCE_NAME,
        age=ACQUAINTANCE_AGE,
        hobbies=ACQUAINTANCE_HOBBIES,
        username=ACQUAINTANCE_USERNAME,
        password=ACQUAINTANCE_PASSWORD,
    )

    chit_chat = person.get_chit_chat()

    if "weather" in chit_chat:
        lab = BackyardLab(login=acquaintance.username, password=acquaintance.password)
        barometric_pressure = lab.get_barometric_pressure()
        trend = lab.track_barometric_pressure(barometric_pressure)
        lab.chart(trend)

        radar = DopplerRadar(
            login=acquaintance.username, password=acquaintance.password
        )
        sky_quality = radar.map_sky()

        radiation_tester = RadiationSoilTester(
            login=acquaintance.username,
            password=acquaintance.password
        )
        soil_test = radiation_tester.sample(SOIL_SAMPLE)  # <-- where did he GET that?

        weather_algo = FancyWeatherAlgorithm(
            login=acquaintance.username,
            password=acquaintance.password,
        )
        possible_weather = weather_algo.assess_possible_weather(
            trend,
            sky_quality,
            soil_test,
        )

        banter = acquaintance.respond(possible_weather)

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
    username: str
    password: str

    def respond(self, possible_weather):
        """
        LOTS OF COMPLICATED CALCULATIONS.
        """
        if possible_weather == "sunny":
            return "This sunny day is here to stay!"
        else:
            return "Looks like rain!"
